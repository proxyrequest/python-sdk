# ruff: noqa: E501,PERF401
from __future__ import annotations

import argparse
import ast
import copy
import json
import re
import shutil
import subprocess
import tempfile
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from sdk_schema import sdk_schema

ROOT = Path(__file__).resolve().parents[1]
HTTP_METHODS = {"get", "post", "put", "patch", "delete"}
ERROR_MODEL = re.compile(r"(?:Response|Error)[45]\d\d")


@dataclass(frozen=True)
class Operation:
    operation_id: str
    method_name: str
    resource_tag: str
    resource_attribute: str
    resource_class: str
    http_method: str
    path: str
    summary: str
    return_type: str
    idempotent: bool


def has_header_parameter(
    contract: dict[str, Any], path_item: dict[str, Any], operation: dict[str, Any], name: str
) -> bool:
    parameters = [*path_item.get("parameters", []), *operation.get("parameters", [])]
    for parameter in parameters:
        if "$ref" in parameter:
            parameter = (
                contract.get("components", {})
                .get("parameters", {})
                .get(parameter["$ref"].rsplit("/", 1)[-1], {})
            )
        if parameter.get("in") == "header" and parameter.get("name") == name:
            return True
    return False


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate the ProxyRequest Python SDK surface.")
    parser.add_argument("--output-root", type=Path, default=ROOT)
    return parser.parse_args()


def load_yaml(path: Path) -> dict[str, Any]:
    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict):
        raise SystemExit(f"Expected a mapping in {path}")
    return document


def model_class_name(schema_name: str, generator_config: dict[str, Any]) -> str:
    override = generator_config.get("class_overrides", {}).get(schema_name, {})
    return str(override.get("class_name", schema_name))


def response_type(
    operation: dict[str, Any], generator_config: dict[str, Any], contract: dict[str, Any]
) -> str:
    def schema_type(schema: dict[str, Any]) -> str:
        if "$ref" in schema:
            name = schema["$ref"].rsplit("/", 1)[-1]
            target = contract.get("components", {}).get("schemas", {}).get(name, {})
            if "anyOf" in target or "oneOf" in target:
                return schema_type(target)
            return model_class_name(name, generator_config)
        variants = schema.get("anyOf", schema.get("oneOf"))
        if variants:
            return " | ".join(dict.fromkeys(schema_type(item) for item in variants))
        if schema.get("type") == "array":
            return f"list[{schema_type(schema.get('items', {}))}]"
        return {
            "boolean": "bool",
            "integer": "int",
            "number": "float",
            "string": "str",
            "null": "None",
        }.get(schema.get("type"), "object")

    types: list[str] = []
    responses = operation.get("responses", {})
    for status, response in sorted(responses.items(), key=lambda item: str(item[0])):
        if not str(status).startswith("2"):
            continue
        content = response.get("content", {})
        if not content:
            types.append("None")
            continue
        content_type, media = next(iter(content.items()))
        schema = media.get("schema", {})
        types.append("FileDownload" if content_type == "application/pdf" else schema_type(schema))
    if types:
        return " | ".join(dict.fromkeys(types))
    raise SystemExit(f"Operation {operation.get('operationId')} has no successful response.")


def contract_operations() -> tuple[list[Operation], dict[str, Any], dict[str, Any]]:
    contract = sdk_schema(load_yaml(ROOT / "openapi/openapi.yaml"))
    mapping = load_yaml(ROOT / "openapi/operations.yaml")
    generator_config = load_yaml(ROOT / "openapi/generator.yaml")
    aliases = mapping.get("operations", {})
    resources = mapping.get("resources", {})
    found_ids: set[str] = set()
    operations: list[Operation] = []

    for path, path_item in contract.get("paths", {}).items():
        for http_method, operation in path_item.items():
            if http_method not in HTTP_METHODS:
                continue
            operation_id = operation["operationId"]
            found_ids.add(operation_id)
            tags = operation.get("tags", [])
            if len(tags) != 1 or tags[0] not in resources:
                raise SystemExit(f"Operation {operation_id} has an unmapped resource tag: {tags}")
            if operation_id not in aliases:
                raise SystemExit(f"Operation {operation_id} has no public method mapping.")
            resource = resources[tags[0]]
            operations.append(
                Operation(
                    operation_id=operation_id,
                    method_name=aliases[operation_id],
                    resource_tag=tags[0],
                    resource_attribute=resource["attribute"],
                    resource_class=resource["class_name"],
                    http_method=http_method.upper(),
                    path=path,
                    summary=" ".join(str(operation.get("summary", operation_id)).split()),
                    return_type=response_type(operation, generator_config, contract),
                    idempotent=has_header_parameter(
                        contract, path_item, operation, "Idempotency-Key"
                    ),
                )
            )

    extra = set(aliases) - found_ids
    if extra:
        raise SystemExit(f"Mappings exist for unknown operations: {sorted(extra)}")
    return operations, resources, generator_config


def run_generator(destination: Path) -> None:
    document = sdk_schema(load_yaml(ROOT / "openapi/openapi.yaml"))
    for path_item in document.get("paths", {}).values():
        for http_method, operation in path_item.items():
            if http_method not in HTTP_METHODS:
                continue
            content = operation.get("requestBody", {}).get("content", {})
            if "application/json" in content:
                operation["requestBody"]["content"] = {
                    "application/json": content["application/json"]
                }
    generator_schema = destination.parent / "generator-openapi.yaml"
    generator_schema.write_text(
        yaml.safe_dump(document, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    subprocess.run(
        [
            "openapi-python-client",
            "generate",
            "--path",
            str(generator_schema),
            "--config",
            str(ROOT / "openapi/generator.yaml"),
            "--meta",
            "none",
            "--output-path",
            str(destination),
            "--fail-on-warning",
        ],
        check=True,
    )


def make_enums_forward_compatible(source: str) -> str:
    marker = "(str, Enum):\n"
    if marker not in source or "def _missing_(" in source:
        return source
    method = (
        "(str, Enum):\n"
        "    @classmethod\n"
        "    def _missing_(cls, value: object):\n"
        "        if not isinstance(value, str):\n"
        "            return None\n"
        "        member = str.__new__(cls, value)\n"
        '        member._name_ = f"UNKNOWN_{value}"\n'
        "        member._value_ = value\n"
        "        return member\n\n"
    )
    return source.replace(marker, method, 1)


def postprocess_generated(generated: Path) -> None:
    for path in generated.rglob("*.py"):
        source = path.read_text(encoding="utf-8")
        source = re.sub(
            r"(accept_language:\s*str\s*\|\s*Unset\s*=\s*)[\"']en[\"']",
            r"\1UNSET",
            source,
        )
        source = source.replace("Default: 'en'.", "Defaults to the client language.")
        source = make_enums_forward_compatible(source)
        if path.parent.parent.name == "api" and "def _build_response(" in source:
            source = source.replace(
                "import httpx\n", "import httpx\n\nfrom ...._response import parse_response\n", 1
            )
            source = source.replace(
                "    return Response(\n",
                "    parsed = parse_response(_parse_response, client=client, response=response)\n    return Response(\n",
                1,
            ).replace("parsed=_parse_response(client=client, response=response)", "parsed=parsed")
        path.write_text(source, encoding="utf-8")
    subprocess.run(["ruff", "format", str(generated)], check=True)


def find_endpoint(generated: Path, operation_id: str) -> Path:
    matches = list((generated / "api").glob(f"*/{operation_id}.py"))
    if len(matches) != 1:
        raise SystemExit(f"Expected one generated module for {operation_id}, found {len(matches)}")
    return matches[0]


def public_arguments(
    endpoint: Path, renames: dict[str, str] | None = None
) -> tuple[str, list[tuple[str, str]], set[str]]:
    tree = ast.parse(endpoint.read_text(encoding="utf-8"))
    function = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "sync_detailed"
    )
    arguments = copy.deepcopy(function.args)

    positional = arguments.posonlyargs + arguments.args
    renames = renames or {}
    names = [
        (argument.arg, renames.get(argument.arg, argument.arg))
        for argument in positional
        if argument.arg != "client"
    ]
    names.extend(
        (argument.arg, renames.get(argument.arg, argument.arg))
        for argument in arguments.kwonlyargs
        if argument.arg != "client"
    )

    if any(argument.arg == "client" for argument in arguments.args):
        index = next(i for i, argument in enumerate(arguments.args) if argument.arg == "client")
        default_offset = len(arguments.args) - len(arguments.defaults)
        arguments.args.pop(index)
        if index >= default_offset:
            arguments.defaults.pop(index - default_offset)
    if any(argument.arg == "client" for argument in arguments.kwonlyargs):
        index = next(
            i for i, argument in enumerate(arguments.kwonlyargs) if argument.arg == "client"
        )
        arguments.kwonlyargs.pop(index)
        arguments.kw_defaults.pop(index)

    def simplify_union(annotation: ast.expr | None) -> ast.expr | None:
        if annotation is None:
            return None

        members: list[ast.expr] = []

        def flatten(node: ast.expr) -> None:
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
                flatten(node.left)
                flatten(node.right)
            else:
                members.append(node)

        flatten(annotation)
        unique: list[ast.expr] = []
        seen: set[str] = set()
        for member in members:
            rendered_member = ast.unparse(member)
            if rendered_member not in seen:
                unique.append(member)
                seen.add(rendered_member)
        result = unique[0]
        for member in unique[1:]:
            result = ast.BinOp(left=result, op=ast.BitOr(), right=member)
        return result

    for argument in [*arguments.posonlyargs, *arguments.args, *arguments.kwonlyargs]:
        argument.annotation = simplify_union(argument.annotation)
        argument.arg = renames.get(argument.arg, argument.arg)

    type_names: set[str] = set()
    nodes: list[ast.AST] = [
        *(argument.annotation for argument in arguments.posonlyargs if argument.annotation),
        *(argument.annotation for argument in arguments.args if argument.annotation),
        *(argument.annotation for argument in arguments.kwonlyargs if argument.annotation),
        *arguments.defaults,
        *(default for default in arguments.kw_defaults if default is not None),
    ]
    for node in nodes:
        type_names.update(child.id for child in ast.walk(node) if isinstance(child, ast.Name))

    placeholder = ast.FunctionDef(
        name="placeholder",
        args=arguments,
        body=[ast.Pass()],
        decorator_list=[],
        returns=None,
        type_comment=None,
    )
    ast.fix_missing_locations(placeholder)
    rendered = ast.unparse(placeholder).split(":\n", 1)[0].removeprefix("def placeholder")
    rendered = "(self)" if rendered == "()" else rendered.replace("(", "(self, ", 1)
    return rendered, names, type_names


def render_resource(
    operations: list[Operation],
    generated: Path,
    resource_class: str,
    model_modules: dict[str, str],
) -> str:
    imports: list[str] = []
    methods: list[str] = []
    async_methods: list[str] = []
    type_names: set[str] = set()
    needs_builtins = False

    for operation in sorted(operations, key=lambda item: item.method_name):
        endpoint = find_endpoint(generated, operation.operation_id)
        tag_module = endpoint.parent.name
        imports.append(
            f"from .._generated.api.{tag_module} import {operation.operation_id} as _{operation.operation_id}"
        )
        arguments, names, argument_type_names = public_arguments(endpoint, {})
        type_names.update(argument_type_names)
        type_names.update(
            node.id
            for node in ast.walk(ast.parse(operation.return_type, mode="eval"))
            if isinstance(node, ast.Name)
        )
        passed = ", ".join(f"{original}={public}" for original, public in names)
        comma = ", " if passed else ""
        call_name = "_download" if operation.return_type == "FileDownload" else "_call"
        response_call_name = (
            "_download_with_response"
            if operation.return_type == "FileDownload"
            else "_call_with_response"
        )
        idempotency_argument = ", _idempotent=True" if operation.idempotent else ""
        return_statement = (
            f"return cast({operation.return_type}, self._client.{call_name}(_{operation.operation_id}.sync_detailed{idempotency_argument}{comma}{passed}))"
            if operation.return_type != "None"
            else f"self._client.{call_name}(_{operation.operation_id}.sync_detailed{idempotency_argument}{comma}{passed})\n        return None"
        )
        async_return = (
            f"return cast({operation.return_type}, await self._client.{call_name}(_{operation.operation_id}.asyncio_detailed{idempotency_argument}{comma}{passed}))"
            if operation.return_type != "None"
            else f"await self._client.{call_name}(_{operation.operation_id}.asyncio_detailed{idempotency_argument}{comma}{passed})\n        return None"
        )
        response_type = operation.return_type
        if response_type.startswith("list["):
            response_type = f"builtins.{response_type}"
            needs_builtins = True
        response_return = f"return cast(ApiResponse[{response_type}], self._client.{response_call_name}(_{operation.operation_id}.sync_detailed{idempotency_argument}{comma}{passed}))"
        async_response_return = f"return cast(ApiResponse[{response_type}], await self._client.{response_call_name}(_{operation.operation_id}.asyncio_detailed{idempotency_argument}{comma}{passed}))"
        methods.append(
            f'''    def {operation.method_name}{arguments} -> {operation.return_type}:
        """{operation.summary}"""
        {return_statement}

    def {operation.method_name}_with_response{arguments} -> ApiResponse[{response_type}]:
        """{operation.summary}; include response metadata."""
        {response_return}
'''
        )
        async_methods.append(
            f'''    async def {operation.method_name}{arguments} -> {operation.return_type}:
        """{operation.summary}"""
        {async_return}

    async def {operation.method_name}_with_response{arguments} -> ApiResponse[{response_type}]:
        """{operation.summary}; include response metadata."""
        {async_response_return}
'''
        )

    builtins = {
        "Any",
        "ApiResponse",
        "FileDownload",
        "None",
        "bool",
        "dict",
        "float",
        "int",
        "list",
        "object",
        "str",
    }
    special_imports: list[str] = []
    for name in sorted(type_names - builtins):
        if name in model_modules:
            special_imports.append(f"from .._generated.models.{model_modules[name]} import {name}")
        elif name in {"UNSET", "Unset"}:
            special_imports.append(f"from .._generated.types import {name}")
        elif name == "UUID":
            special_imports.append("from uuid import UUID")
        elif name == "datetime":
            special_imports.append("import datetime")
        else:
            raise SystemExit(f"Unable to import annotation name {name} for {resource_class}.")

    return "\n".join(
        [
            "# Generated by scripts/generate.py; do not edit.",
            "from __future__ import annotations",
            "",
            *(["import builtins", ""] if needs_builtins else []),
            "from typing import Any, cast",
            "",
            "from ..files import FileDownload",
            "from ..response import ApiResponse",
            *special_imports,
            *imports,
            "",
            f"class {resource_class}:",
            "    def __init__(self, client: Any) -> None:",
            "        self._client = client",
            "",
            *methods,
            f"class Async{resource_class}:",
            "    def __init__(self, client: Any) -> None:",
            "        self._client = client",
            "",
            *async_methods,
        ]
    )


def generate_resources(operations: list[Operation], generated: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    # This resource was explicitly removed from the supported SDK surface.
    (destination / "sessions.py").unlink(missing_ok=True)
    exports: list[tuple[str, str]] = []
    grouped: dict[str, list[Operation]] = {}
    model_source = (generated / "models/__init__.py").read_text(encoding="utf-8")
    model_modules = {
        class_name: module_name
        for module_name, class_name in re.findall(r"from \.([\w_]+) import (\w+)", model_source)
    }
    for operation in operations:
        grouped.setdefault(operation.resource_class, []).append(operation)

    for class_name, resource_operations in sorted(grouped.items()):
        module_name = resource_operations[0].resource_attribute
        (destination / f"{module_name}.py").write_text(
            render_resource(resource_operations, generated, class_name, model_modules),
            encoding="utf-8",
        )
        exports.extend([(module_name, class_name), (module_name, f"Async{class_name}")])

    lines = ["# Generated by scripts/generate.py; do not edit."]
    for module_name, class_name in exports:
        lines.append(f"from .{module_name} import {class_name}")
    lines.extend(["", "__all__ = ["])
    lines.extend(f'    "{class_name}",' for _, class_name in exports)
    lines.extend(["]", ""])
    (destination / "__init__.py").write_text("\n".join(lines), encoding="utf-8")
    subprocess.run(["ruff", "format", str(destination)], check=True)


def generate_public_models(generated: Path, destination: Path) -> None:
    source = (generated / "models/__init__.py").read_text(encoding="utf-8")
    imports: list[str] = []
    names: list[str] = []
    pattern = re.compile(r"from \.([\w_]+) import (\w+)")
    for module_name, class_name in pattern.findall(source):
        if ERROR_MODEL.search(class_name):
            continue
        imports.append(f"from .._generated.models.{module_name} import {class_name}")
        names.append(class_name)
    destination.mkdir(parents=True, exist_ok=True)
    lines = ["# Generated by scripts/generate.py; do not edit.", *imports, "", "__all__ = ["]
    lines.extend(f'    "{name}",' for name in names)
    lines.extend(["]", ""])
    (destination / "__init__.py").write_text("\n".join(lines), encoding="utf-8")
    subprocess.run(["ruff", "format", str(destination)], check=True)


def generate_reference(
    operations: list[Operation], contract: dict[str, Any], generated: Path, destination: Path
) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    api_lines = [
        "# API resource reference",
        "",
        "All methods exist on both `Client` and `AsyncClient`; async calls must be awaited.",
        "",
    ]
    grouped: dict[str, list[Operation]] = {}
    for operation in operations:
        grouped.setdefault(operation.resource_attribute, []).append(operation)
    for attribute, resource_operations in sorted(grouped.items()):
        api_lines.extend(
            [f"## `{attribute}`", "", "| Method | HTTP endpoint | Returns |", "| --- | --- | --- |"]
        )
        for operation in sorted(resource_operations, key=lambda item: item.method_name):
            api_lines.append(
                f"| `{operation.method_name}()` | `{operation.http_method} {operation.path}` | `{operation.return_type}` |"
            )
        api_lines.append("")
    (destination / "api.md").write_text("\n".join(api_lines), encoding="utf-8")

    model_lines = [
        "# Model reference",
        "",
        "Models use snake_case attributes and provide `to_dict()` / `from_dict()` helpers.",
        "",
    ]
    for name, schema in sorted(contract.get("components", {}).get("schemas", {}).items()):
        description = " ".join(str(schema.get("description", "")).split())
        model_lines.append(f"- `{name}`" + (f" — {description}" if description else ""))
    model_lines.append("")
    (destination / "models.md").write_text("\n".join(model_lines), encoding="utf-8")

    mapping = load_yaml(ROOT / "openapi/operations.yaml")
    source = json.loads((ROOT / "openapi/source.json").read_text(encoding="utf-8"))
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]

    def clean(value: Any) -> str:
        return " ".join(str(value or "").split())

    def dereference(value: dict[str, Any] | None, section: str) -> dict[str, Any]:
        if not value:
            return {}
        reference = value.get("$ref")
        prefix = f"#/components/{section}/"
        if isinstance(reference, str) and reference.startswith(prefix):
            return (
                contract.get("components", {}).get(section, {}).get(reference[len(prefix) :], value)
            )
        return value

    def type_of(value: dict[str, Any] | None) -> str:
        if not value:
            return "Any"
        if "$ref" in value:
            return str(value["$ref"]).rsplit("/", 1)[-1]
        variants = value.get("oneOf", value.get("anyOf", value.get("allOf")))
        if variants:
            return " | ".join(dict.fromkeys(type_of(item) for item in variants))
        if value.get("type") == "array":
            return f"list[{type_of(value.get('items', {}))}]"
        if value.get("type") == "object" or value.get("properties"):
            return "dict[str, Any]"
        return {
            "boolean": "bool",
            "integer": "int",
            "number": "float",
            "null": "None",
            "string": "str",
        }.get(value.get("type"), "Any")

    def placeholder(name: str, value: dict[str, Any]) -> Any:
        if "example" in value:
            return value["example"]
        if "default" in value:
            return value["default"]
        if value.get("enum"):
            return value["enum"][0]
        lower = name.lower()
        if value.get("format") == "uuid" or lower == "id" or lower.endswith("_id"):
            return "550e8400-e29b-41d4-a716-446655440000"
        if value.get("format") == "date-time" or "date" in lower:
            return "2026-09-21T12:00:00Z"
        if value.get("format") == "email" or "email" in lower:
            return "developer@example.com"
        if "password" in lower:
            return "Correct-Horse-Battery-Staple-42"
        if "language" in lower:
            return "en"
        if lower == "data" or lower.endswith("_bytes"):
            return 1073741824
        if value.get("type") in {"integer", "number"}:
            return value.get("minimum", 1)
        if value.get("type") == "boolean":
            return False
        if value.get("type") == "array":
            return []
        return f"{{{name}}}"

    def example_of(value: dict[str, Any], name: str = "value", seen: set[str] | None = None) -> Any:
        seen = set() if seen is None else seen
        if "example" in value:
            return value["example"]
        if "default" in value:
            return value["default"]
        if "$ref" in value:
            model = str(value["$ref"]).rsplit("/", 1)[-1]
            if model in seen:
                return f"{{{model}}}"
            return example_of(
                contract.get("components", {}).get("schemas", {}).get(model, {}),
                model,
                seen | {model},
            )
        variants = value.get("oneOf", value.get("anyOf"))
        if variants:
            return example_of(
                next((item for item in variants if item.get("type") != "null"), variants[0]),
                name,
                seen,
            )
        if value.get("type") == "array":
            return [example_of(value.get("items", {}), name.removesuffix("s"), seen)]
        if value.get("type") == "object" or value.get("properties"):
            required = set(value.get("required", []))
            properties = value.get("properties", {})
            return {
                key: example_of(field, key, seen)
                for key, field in properties.items()
                if key in required or (not required and ("example" in field or "default" in field))
            }
        return placeholder(name, value)

    error_kinds = {
        "400": (
            "ErrorKind.VALIDATION",
            "The request arguments or business rules are invalid.",
        ),
        "401": (
            "ErrorKind.AUTHENTICATION",
            "Authentication credentials are missing, expired, or invalid.",
        ),
        "403": (
            "ErrorKind.PERMISSION",
            "The authenticated account cannot perform this operation.",
        ),
        "404": ("ErrorKind.NOT_FOUND", "The requested resource does not exist."),
        "409": (
            "ErrorKind.CONFLICT",
            "The operation conflicts with the current resource or idempotency state.",
        ),
        "412": (
            "ErrorKind.PRECONDITION",
            "A required resource precondition is no longer satisfied.",
        ),
        "429": (
            "ErrorKind.RATE_LIMIT",
            "The request was limited and can be retried later.",
        ),
    }

    def throws_for(operation: dict[str, Any]) -> list[dict[str, Any]]:
        conditions: dict[str, str] = {}
        for status in operation.get("responses", {}):
            status = str(status)
            if status.startswith("2"):
                continue
            kind, description = error_kinds.get(
                status,
                (
                    ("ErrorKind.SERVER", "ProxyRequest could not complete the operation.")
                    if status.isdigit() and int(status) >= 500
                    else ("ErrorKind.UNEXPECTED", "The API returned an unexpected failure.")
                ),
            )
            conditions[kind] = description
        conditions["ErrorKind.NETWORK"] = "The request could not reach ProxyRequest."
        conditions["ErrorKind.UNEXPECTED"] = (
            "The response could not be decoded or did not match the SDK contract."
        )
        return [
            {
                "type": "ApiError",
                "description": "Normalized API, transport, and response processing failure.",
                "conditions": [
                    {"kind": kind, "description": description}
                    for kind, description in conditions.items()
                ],
            }
        ]

    raw_by_id: dict[str, tuple[str, str, dict[str, Any], dict[str, Any]]] = {}
    for path, path_item in contract.get("paths", {}).items():
        for verb in HTTP_METHODS:
            if verb in path_item:
                raw = path_item[verb]
                raw_by_id[raw["operationId"]] = (path, verb, path_item, raw)

    resource_values: list[dict[str, Any]] = []
    resources_by_attribute: dict[str, dict[str, Any]] = {}
    for tag, value in mapping["resources"].items():
        resource = {
            "tag": tag,
            "accessor": value["attribute"],
            "className": value["class_name"],
            "description": clean(
                next(
                    (
                        entry.get("description")
                        for entry in contract.get("tags", [])
                        if entry.get("name") == tag
                    ),
                    "",
                )
            ),
            "methods": [],
        }
        resource_values.append(resource)
        resources_by_attribute[value["attribute"]] = resource

    for operation in operations:
        path, verb, path_item, raw = raw_by_id[operation.operation_id]
        endpoint = find_endpoint(generated, operation.operation_id)
        arguments, _, _ = public_arguments(endpoint, {})
        display_arguments = arguments.replace("(self, ", "(", 1) if arguments != "(self)" else "()"
        raw_parameters = [
            dereference(parameter, "parameters")
            for parameter in [*path_item.get("parameters", []), *raw.get("parameters", [])]
        ]
        bases = [
            re.sub(r"[^a-zA-Z0-9]+", "_", parameter["name"]).strip("_").lower()
            for parameter in raw_parameters
        ]
        public_names = [
            f"{base}_{raw_parameters[index]['in']}" if bases.count(base) > 1 else base
            for index, base in enumerate(bases)
        ]
        parameters = [
            {
                "name": public_names[index],
                "wireName": parameter["name"],
                "in": parameter["in"],
                "required": parameter.get("required") is True or parameter["in"] == "path",
                "type": type_of(parameter.get("schema", {})),
                "default": parameter.get("schema", {}).get("default"),
                "description": clean(parameter.get("description")),
                "example": placeholder(parameter["name"], parameter.get("schema", {})),
            }
            for index, parameter in enumerate(raw_parameters)
        ]
        body_raw = dereference(raw.get("requestBody"), "requestBodies")
        media = body_raw.get("content", {}).get("application/json") or next(
            iter(body_raw.get("content", {}).values()), {}
        )
        body_schema = media.get("schema", {})
        body_type = type_of(body_schema)
        body = (
            None
            if not raw.get("requestBody")
            else {
                "name": "body",
                "required": body_raw.get("required") is True,
                "type": body_type,
                "description": clean(body_raw.get("description")),
            }
        )
        call_arguments = [
            f"{parameter['name']}={placeholder(parameter['wireName'], raw_parameters[index].get('schema', {}))!r}"
            for index, parameter in enumerate(parameters)
            if parameter["required"]
        ]
        if body is not None:
            body_value = example_of(body_schema, body_type)
            call_arguments.append(f"body=models.{body_type}.from_dict({body_value!r})")
        if call_arguments:
            joined = ",\n        ".join(call_arguments)
            sync_call = f"(\n        {joined},\n    )"
            async_call = sync_call
        else:
            sync_call = async_call = "()"

        success = {"type": operation.return_type, "description": ""}
        failures: list[dict[str, str]] = []
        for status, response_value in raw.get("responses", {}).items():
            response_value = dereference(response_value, "responses")
            if str(status).startswith("2") and not success["description"]:
                success["description"] = clean(response_value.get("description"))
            elif not str(status).startswith("2"):
                failures.append(
                    {"status": str(status), "description": clean(response_value.get("description"))}
                )

        resource = resources_by_attribute[operation.resource_attribute]
        resource["methods"].append(
            {
                "operationId": operation.operation_id,
                "name": operation.method_name,
                "summary": operation.summary,
                "description": clean(raw.get("description")),
                "httpMethod": verb.upper(),
                "path": path,
                "signatures": [
                    {
                        "label": "Sync",
                        "signature": f"client.{operation.resource_attribute}.{operation.method_name}{display_arguments} -> {operation.return_type}",
                    },
                    {
                        "label": "Async",
                        "signature": f"await async_client.{operation.resource_attribute}.{operation.method_name}{display_arguments} -> {operation.return_type}",
                    },
                ],
                "variants": [
                    {
                        "name": f"{operation.method_name}_with_response",
                        "signature": f"client.{operation.resource_attribute}.{operation.method_name}_with_response{display_arguments} -> ApiResponse[{operation.return_type}]",
                        "description": "Returns response status, headers, ETag and idempotency metadata with the decoded data.",
                    }
                ],
                "parameters": parameters,
                "body": body,
                "returns": success,
                "errors": failures,
                "throws": throws_for(raw),
                "example": {
                    "language": "python",
                    "code": f"result = client.{operation.resource_attribute}.{operation.method_name}{sync_call}",
                },
                "asyncExample": {
                    "language": "python",
                    "code": f"result = await async_client.{operation.resource_attribute}.{operation.method_name}{async_call}",
                },
            }
        )

    public_model_source = (
        destination.parents[1] / "src/proxyrequest_sdk/models/__init__.py"
    ).read_text(encoding="utf-8")
    public_model_names = re.findall(r'^\s+"([A-Za-z0-9_]+)",$', public_model_source, re.MULTILINE)
    public_model_tree = ast.parse(public_model_source)
    public_model_modules = {
        alias.asname or alias.name: node.module.rsplit(".", 1)[-1]
        for node in public_model_tree.body
        if isinstance(node, ast.ImportFrom) and node.module and "_generated.models." in node.module
        for alias in node.names
    }

    def field_default(value: ast.expr | None) -> Any:
        if value is None or (isinstance(value, ast.Name) and value.id == "UNSET"):
            return None
        try:
            return ast.literal_eval(value)
        except (ValueError, TypeError):
            return ast.unparse(value)

    def public_type(annotation: ast.expr) -> tuple[str, bool]:
        rendered = ast.unparse(annotation)
        parts = [part.strip() for part in rendered.split("|")]
        optional = "Unset" in parts
        rendered = " | ".join(part for part in parts if part != "Unset") or "Any"
        if len(rendered) >= 2 and rendered[0] == rendered[-1] and rendered[0] in {'"', "'"}:
            rendered = rendered[1:-1]
        return rendered, optional

    model_values = []
    for name in sorted(public_model_names):
        module = public_model_modules.get(name)
        if module is None:
            continue
        model_tree = ast.parse((generated / "models" / f"{module}.py").read_text(encoding="utf-8"))
        model_class = next(
            node for node in model_tree.body if isinstance(node, ast.ClassDef) and node.name == name
        )
        is_enum = any(
            (isinstance(base, ast.Name) and base.id == "Enum")
            or (isinstance(base, ast.Attribute) and base.attr == "Enum")
            for base in model_class.bases
        )
        fields = []
        if not is_enum:
            for index, node in enumerate(model_class.body):
                if not isinstance(node, ast.AnnAssign) or not isinstance(node.target, ast.Name):
                    continue
                if node.target.id == "additional_properties":
                    continue
                field_type, optional = public_type(node.annotation)
                description = ""
                if index + 1 < len(model_class.body):
                    following = model_class.body[index + 1]
                    if (
                        isinstance(following, ast.Expr)
                        and isinstance(following.value, ast.Constant)
                        and isinstance(following.value.value, str)
                    ):
                        description = clean(following.value.value)
                fields.append(
                    {
                        "name": node.target.id,
                        "type": field_type,
                        "required": not optional and node.value is None,
                        "default": field_default(node.value),
                        "description": description,
                        "enum": None,
                    }
                )
        model_values.append(
            {
                "name": name,
                "kind": "enum" if is_enum else "class",
                "description": clean(ast.get_docstring(model_class)),
                "fields": fields,
            }
        )

    model_names = {model["name"] for model in model_values}

    def model_refs(type_name: str) -> list[str]:
        return list(
            dict.fromkeys(
                token
                for token in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", type_name)
                if token in model_names
            )
        )

    for model in model_values:
        for field in model["fields"]:
            field["modelRefs"] = model_refs(field["type"])
    for resource in resource_values:
        for method in resource["methods"]:
            for parameter in method["parameters"]:
                parameter["modelRefs"] = model_refs(parameter["type"])
            if method["body"] is not None:
                method["body"]["modelRefs"] = model_refs(method["body"]["type"])
            method["returns"]["modelRefs"] = model_refs(method["returns"]["type"])

    manifest = {
        "schemaVersion": 3,
        "sdk": {
            "id": "python",
            "label": "Python",
            "language": "Python",
            "version": project["version"],
            "package": project["name"],
            "runtime": "Python 3.11 or later",
            "install": "python -m pip install proxyrequest-sdk",
            "openapi": source,
        },
        "setup": [
            {
                "id": "sync",
                "label": "Sync",
                "language": "python",
                "code": 'from proxyrequest_sdk import Client\nfrom proxyrequest_sdk import models\n\nclient = Client.with_api_key(\n    "{api_key}", base_url="https://{api_host}/api/v1"\n)',
            },
            {
                "id": "async",
                "label": "Async",
                "language": "python",
                "code": 'from proxyrequest_sdk import AsyncClient\nfrom proxyrequest_sdk import models\n\nasync_client = AsyncClient.with_api_key(\n    "{api_key}", base_url="https://{api_host}/api/v1"\n)',
            },
        ],
        "clients": [
            {
                "name": "Client",
                "kind": "class",
                "description": "Synchronous client exposing all API resources.",
                "signatures": [
                    "Client.with_api_key(api_key, *, base_url=...)",
                    "Client.with_bearer_token(token, *, base_url=...)",
                    "Client.anonymous(*, base_url=...)",
                    "client.request(method, path, ...) -> httpx.Response",
                    "client.paginate(fetch_page, ...) -> Iterator[Item]",
                    "client.download_invoice_pdf(invoice_id) -> FileDownload",
                    "client.close() -> None",
                ],
                "members": [
                    {
                        "name": resource["accessor"],
                        "signature": f"{resource['accessor']}: {resource['className']}",
                        "description": "",
                    }
                    for resource in resource_values
                ],
            },
            {
                "name": "AsyncClient",
                "kind": "class",
                "description": "Asynchronous client with the same resource surface.",
                "signatures": [
                    "AsyncClient.with_api_key(api_key, *, base_url=...)",
                    "AsyncClient.with_bearer_token(token, *, base_url=...)",
                    "AsyncClient.anonymous(*, base_url=...)",
                    "await async_client.request(method, path, ...) -> httpx.Response",
                    "async_client.paginate(fetch_page, ...) -> AsyncIterator[Item]",
                    "await async_client.download_invoice_pdf(invoice_id) -> FileDownload",
                    "await async_client.close() -> None",
                ],
                "members": [
                    {
                        "name": resource["accessor"],
                        "signature": f"{resource['accessor']}: Async{resource['className']}",
                        "description": "",
                    }
                    for resource in resource_values
                ],
            },
        ],
        "resources": resource_values,
        "models": model_values,
        "errors": [
            {
                "name": "ApiError",
                "kind": "class",
                "description": "Normalized API and network error.",
                "signatures": [],
            },
            {
                "name": "ProxyRequestError",
                "kind": "class",
                "description": "Base SDK error.",
                "signatures": [],
            },
            {
                "name": "PaginationError",
                "kind": "class",
                "description": "Pagination contract error.",
                "signatures": [],
            },
            {
                "name": "InvalidSignatureError",
                "kind": "class",
                "description": "Webhook signature verification error.",
                "signatures": [],
            },
        ],
        "helpers": [
            {
                "name": "ApiResponse",
                "kind": "class",
                "description": "Decoded data with HTTP response metadata.",
                "signatures": [],
            },
            {
                "name": "WebhookVerifier",
                "kind": "class",
                "description": "Verifies signed ProxyRequest webhooks.",
                "signatures": ["verify()", "verify_or_raise()", "decode_verified_json()"],
            },
            {
                "name": "FileDownload",
                "kind": "class",
                "description": "Binary download with filename and content type metadata.",
                "signatures": ["FileDownload.from_response()", "save(path, *, overwrite=False)"],
            },
            {
                "name": "UNSET and Unset",
                "kind": "sentinel",
                "description": "Distinguishes an omitted optional value from an explicit null value.",
                "signatures": ["UNSET", "Unset"],
            },
        ],
    }
    (destination / "sdk-reference.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def replace_tree(source: Path, destination: Path) -> None:
    if destination.exists():
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)


def main() -> None:
    args = parse_args()
    output_root = args.output_root.resolve()
    operations, _, _ = contract_operations()
    contract = sdk_schema(load_yaml(ROOT / "openapi/openapi.yaml"))

    with tempfile.TemporaryDirectory(prefix="proxyrequest-python-") as temporary:
        generated = Path(temporary) / "_generated"
        run_generator(generated)
        postprocess_generated(generated)
        package_root = output_root / "src/proxyrequest_sdk"
        replace_tree(generated, package_root / "_generated")
        generate_public_models(generated, package_root / "models")
        generate_resources(operations, generated, package_root / "resources")
        generate_reference(operations, contract, generated, output_root / "docs/reference")

    print(f"Generated {len(operations)} operations into {output_root}.")


if __name__ == "__main__":
    main()

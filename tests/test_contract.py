from __future__ import annotations

import ast
import asyncio
import hashlib
import importlib
import inspect
import json
import re
from pathlib import Path
from typing import Any

import yaml

from proxyrequest_sdk import AsyncClient, Client
from proxyrequest_sdk.models import (
    InvoiceCreateRequest,
    InvoiceCreateRequestGatewayEnum,
    InvoiceCreateRequestStatusEnum,
    ProtocolEnum,
    UserCreateRequest,
)

ROOT = Path(__file__).resolve().parents[1]
HTTP_METHODS = {"get", "post", "put", "patch", "delete"}


def documents() -> tuple[dict[str, Any], dict[str, Any]]:
    contract = yaml.safe_load((ROOT / "openapi/openapi.yaml").read_text())
    mapping = yaml.safe_load((ROOT / "openapi/operations.yaml").read_text())
    return contract, mapping


def test_pinned_contract_metadata_and_operation_map() -> None:
    contract, mapping = documents()
    operations = [
        operation
        for path_item in contract["paths"].values()
        for method, operation in path_item.items()
        if method in HTTP_METHODS
    ]
    excluded = {"sessions_list", "sessions_destroy"}
    ids = [operation["operationId"] for operation in operations]
    assert len(set(ids)) == len(ids)
    assert set(ids) - excluded == set(mapping["operations"])
    assert not excluded.intersection(mapping["operations"])
    assert "Sessions" not in mapping["resources"]

    metadata = json.loads((ROOT / "openapi/source.json").read_text())
    assert metadata["operations"] == len(operations)
    assert metadata["schemas"] == len(contract["components"]["schemas"])
    assert set(metadata["excludedOperations"]) == excluded
    digest = hashlib.sha256((ROOT / "openapi/openapi.yaml").read_bytes()).hexdigest()
    assert metadata["sha256"] == digest


def test_every_operation_has_typed_sync_and_async_facades() -> None:
    contract, mapping = documents()
    checked = 0
    for path_item in contract["paths"].values():
        for method, operation in path_item.items():
            if method not in HTTP_METHODS:
                continue
            if operation["operationId"] in {"sessions_list", "sessions_destroy"}:
                continue
            tag = operation["tags"][0]
            resource = mapping["resources"][tag]
            module = importlib.import_module(f"proxyrequest_sdk.resources.{resource['attribute']}")
            sync_class = getattr(module, resource["class_name"])
            async_class = getattr(module, f"Async{resource['class_name']}")
            method_name = mapping["operations"][operation["operationId"]]
            sync_method = getattr(sync_class, method_name)
            async_method = getattr(async_class, method_name)
            sync_response_method = getattr(sync_class, f"{method_name}_with_response")
            async_response_method = getattr(async_class, f"{method_name}_with_response")
            assert not inspect.iscoroutinefunction(sync_method)
            assert inspect.iscoroutinefunction(async_method)
            assert not inspect.iscoroutinefunction(sync_response_method)
            assert inspect.iscoroutinefunction(async_response_method)
            assert inspect.signature(sync_method).return_annotation is not inspect.Signature.empty
            assert inspect.signature(async_method).return_annotation is not inspect.Signature.empty
            assert (
                inspect.signature(sync_response_method).return_annotation
                is not inspect.Signature.empty
            )
            assert (
                inspect.signature(async_response_method).return_annotation
                is not inspect.Signature.empty
            )
            checked += 1
    assert checked == len(mapping["operations"])


def test_client_resource_surface_is_symmetric() -> None:
    _, mapping = documents()
    sync = Client.anonymous()
    async_client = AsyncClient.anonymous()
    try:
        assert not hasattr(sync, "sessions")
        assert not hasattr(async_client, "sessions")
        for resource in mapping["resources"].values():
            assert hasattr(sync, resource["attribute"])
            assert hasattr(async_client, resource["attribute"])
    finally:
        sync.close()
        asyncio.run(async_client.close())


def test_models_serialize_snake_case_and_enums_keep_unknown_values() -> None:
    model = UserCreateRequest(username="customer", password="secret", first_name="Ada")
    assert model.to_dict()["first_name"] == "Ada"
    invoice = InvoiceCreateRequest(
        gateway=InvoiceCreateRequestGatewayEnum.MANUAL,
        status=InvoiceCreateRequestStatusEnum.PAID,
    )
    assert invoice.to_dict()["status"] == "paid"
    future = ProtocolEnum("future-protocol")
    assert future.value == "future-protocol"


def test_local_documentation_links_resolve() -> None:
    documents = [ROOT / "README.md", *(ROOT / "docs").rglob("*.md")]
    missing: list[str] = []
    for document in documents:
        for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", document.read_text()):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative = target.split("#", 1)[0]
            if relative and not (document.parent / relative).resolve().exists():
                missing.append(f"{document.relative_to(ROOT)} -> {target}")
    assert missing == []


def test_generated_reference_covers_public_operations_and_examples_parse() -> None:
    manifest = json.loads((ROOT / "docs/reference/sdk-reference.json").read_text())
    methods = [method for resource in manifest["resources"] for method in resource["methods"]]
    expected = manifest["sdk"]["openapi"]["operations"] - len(
        manifest["sdk"]["openapi"]["excludedOperations"]
    )
    assert manifest["schemaVersion"] == 3
    assert manifest["sdk"]["version"] == "2.2.0"
    assert len(methods) == expected
    assert len({method["operationId"] for method in methods}) == len(methods)
    assert len(manifest["models"]) > 100
    models = {model["name"]: model for model in manifest["models"]}
    model_names = set(models)
    assert all(method["returns"]["type"] for method in methods)
    assert all(method["throws"][0]["type"] == "ApiError" for method in methods)
    assert all(len(method["throws"][0]["conditions"]) > 1 for method in methods)
    for method in methods:
        typed_values = [*method["parameters"], method["returns"]]
        if method["body"] is not None:
            typed_values.append(method["body"])
        assert all(set(value["modelRefs"]) <= model_names for value in typed_values)
    for model in models.values():
        assert all(set(field["modelRefs"]) <= model_names for field in model["fields"])
        if model["kind"] != "enum":
            assert model["fields"], f"{model['name']} must describe its shape"
    dynamic_meta = models["PatchedUserUpdateRequestMeta"]
    assert dynamic_meta["kind"] == "map"
    assert dynamic_meta["fields"] == [
        {
            "name": "[key: str]",
            "type": "Any",
            "required": False,
            "default": None,
            "description": "Arbitrary additional property.",
            "enum": None,
            "modelRefs": [],
        }
    ]
    settings_method = next(
        method for method in methods if method["operationId"] == "settings_retrieve"
    )
    assert settings_method["returns"]["modelRefs"] == ["SettingsResponse"]
    assert len(models["PaginatedAPIKeyList"]["fields"]) > 0
    assert len(models["InvoiceCreateRequest"]["fields"]) > 0
    for setup in manifest["setup"]:
        ast.parse(setup["code"])
    for method in methods:
        ast.parse(method["example"]["code"])
        ast.parse(method["asyncExample"]["code"])

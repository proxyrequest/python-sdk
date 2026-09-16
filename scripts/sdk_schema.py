from __future__ import annotations

import copy
import json
import re
from pathlib import Path
from typing import Any

EXCLUDED_OPERATIONS = frozenset({"sessions_destroy", "sessions_list"})
HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}


def sdk_schema(source: dict[str, Any]) -> dict[str, Any]:
    """Project the canonical schema without mutating the upstream snapshot."""
    document = copy.deepcopy(source)
    seen: set[str] = set()
    for path, item in list(document.get("paths", {}).items()):
        for method, operation in list(item.items()):
            if method not in HTTP_METHODS:
                continue
            operation_id = operation.get("operationId")
            if not operation_id or operation_id in seen:
                raise ValueError(f"Missing or duplicate operationId: {operation_id}")
            seen.add(operation_id)
            if operation_id in EXCLUDED_OPERATIONS:
                del item[method]
        if not HTTP_METHODS.intersection(item):
            del document["paths"][path]
    document["tags"] = [tag for tag in document.get("tags", []) if tag["name"] != "Sessions"]
    schemas = document.get("components", {}).get("schemas", {})
    # Retain the 2.0 response variants and optional legacy password selector in
    # this minor release. The vendored upstream snapshot stays authoritative.
    compatibility = json.loads(
        (Path(__file__).resolve().parents[1] / "openapi/compatibility.json").read_text()
    )["schemas"]
    for name, legacy in compatibility.items():
        if name not in schemas or name == "InvoiceRead":
            schemas[name] = legacy
        else:
            current = schemas[name]
            current["properties"] = {
                **legacy.get("properties", {}),
                **current.get("properties", {}),
            }
            current["required"] = [
                field
                for field in current.get("required", [])
                if field in legacy.get("required", [])
            ]
    for name in list(schemas):
        if re.match(r"^Sessions?(List|Delete|Destroy)", name):
            del schemas[name]
    return document

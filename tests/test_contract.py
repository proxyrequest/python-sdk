from __future__ import annotations

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
from proxyrequest_sdk.models import ProtocolEnum, UserCreateRequest

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
    assert len(operations) == 82
    assert len(contract["components"]["schemas"]) == 127
    assert {operation["operationId"] for operation in operations} == set(mapping["operations"])
    assert len(mapping["resources"]) == 19

    metadata = json.loads((ROOT / "openapi/source.json").read_text())
    assert metadata["operations"] == 82
    assert metadata["schemas"] == 127
    digest = hashlib.sha256((ROOT / "openapi/openapi.yaml").read_bytes()).hexdigest()
    assert metadata["sha256"] == digest


def test_every_operation_has_typed_sync_and_async_facades() -> None:
    contract, mapping = documents()
    checked = 0
    for path_item in contract["paths"].values():
        for method, operation in path_item.items():
            if method not in HTTP_METHODS:
                continue
            tag = operation["tags"][0]
            resource = mapping["resources"][tag]
            module = importlib.import_module(f"proxyrequest_sdk.resources.{resource['attribute']}")
            sync_class = getattr(module, resource["class_name"])
            async_class = getattr(module, f"Async{resource['class_name']}")
            method_name = mapping["operations"][operation["operationId"]]
            sync_method = getattr(sync_class, method_name)
            async_method = getattr(async_class, method_name)
            assert not inspect.iscoroutinefunction(sync_method)
            assert inspect.iscoroutinefunction(async_method)
            assert inspect.signature(sync_method).return_annotation is not inspect.Signature.empty
            assert inspect.signature(async_method).return_annotation is not inspect.Signature.empty
            checked += 1
    assert checked == 82


def test_client_resource_surface_is_symmetric() -> None:
    _, mapping = documents()
    sync = Client.anonymous()
    async_client = AsyncClient.anonymous()
    try:
        for resource in mapping["resources"].values():
            assert hasattr(sync, resource["attribute"])
            assert hasattr(async_client, resource["attribute"])
    finally:
        sync.close()
        asyncio.run(async_client.close())


def test_models_serialize_snake_case_and_enums_keep_unknown_values() -> None:
    model = UserCreateRequest(username="customer", password="secret", first_name="Ada")
    assert model.to_dict()["first_name"] == "Ada"
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

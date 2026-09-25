from __future__ import annotations

import importlib
import json
from pathlib import Path
from typing import Any

import httpx
import pytest
from test_backend_compatibility import BASE_URL, mocked_client, result

from proxyrequest_sdk import ApiError, Client

FIXTURES = json.loads((Path(__file__).parent / "fixtures/provider-balances.json").read_text())


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("metadata", [False, True])
@pytest.mark.parametrize("variant", ["fresh", "stale", "unavailable", "empty"])
async def test_provider_balances(asynchronous: bool, metadata: bool, variant: str) -> None:
    payload = FIXTURES[variant]
    async with mocked_client(asynchronous, [httpx.Response(200, json=payload)]) as (
        client,
        requests,
    ):
        method = "list_data_balances_with_response" if metadata else "list_data_balances"
        response = await result(getattr(client.providers, method)(limit=5, offset=10))
        page = response.data if metadata else response
        assert page.to_dict() == payload
        assert requests[0].url.path == "/api/v1/providers/data-balances"
        assert requests[0].url.params == httpx.QueryParams({"limit": 5, "offset": 10})
        if metadata:
            assert response.status_code == 200
        if page.results:
            assert type(page.results[0].available_bytes) is str
            assert len(page.results[0].history) == 2


@pytest.mark.parametrize("scheme", ["Static", "Bearer"])
def test_provider_authentication(scheme: str) -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json=FIXTURES["empty"])

    factory = Client.with_api_key if scheme == "Static" else Client.with_bearer_token
    with (
        httpx.Client(base_url=BASE_URL, transport=httpx.MockTransport(handler)) as http,
        factory("superuser-key", http_client=http) as client,
    ):
        client.providers.list_data_balances()
    assert requests[0].headers["Authorization"] == f"{scheme} superuser-key"


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("status", [401, 403])
async def test_provider_permission_errors(asynchronous: bool, status: int) -> None:
    async with mocked_client(
        asynchronous, [httpx.Response(status, json={"detail": "Access denied"})]
    ) as (client, _):
        with pytest.raises(ApiError) as caught:
            await result(client.providers.list_data_balances())
        assert caught.value.status_code == status


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_provider_pagination(asynchronous: bool) -> None:
    first = {
        **FIXTURES["fresh"],
        "count": 2,
        "next": "https://api.proxyrequest.com/api/v1/providers/data-balances?limit=1&offset=1",
    }
    last = {**FIXTURES["fresh"], "count": 2}
    async with mocked_client(
        asynchronous, [httpx.Response(200, json=first), httpx.Response(200, json=last)]
    ) as (client, requests):
        pages = client.paginate(client.providers.list_data_balances, limit=1)
        rows = [row async for row in pages] if asynchronous else list(pages)
        assert len(rows) == 2
        assert len(rows[0].history) == 2
        assert [request.url.params.get("offset") for request in requests] == ["0", "1"]


@pytest.mark.parametrize(
    "operation",
    [
        "cities_list",
        "countries_list",
        "regions_list",
        "cities_retrieve",
        "countries_retrieve",
        "regions_retrieve",
    ],
)
@pytest.mark.parametrize("include", [None, False, True])
def test_include_asns(operation: str, include: bool | None) -> None:
    endpoint = importlib.import_module(
        f"proxyrequest_sdk._generated.api.locations.locations_{operation}"
    )
    arguments: dict[str, Any] = {"package_id": "package"}
    if operation.endswith("retrieve"):
        arguments["id"] = "location"
    if include is not None:
        arguments["include_asns"] = include
    query = httpx.QueryParams(endpoint._get_kwargs(**arguments)["params"])
    assert query.get("include_asns") == (None if include is None else str(include).lower())

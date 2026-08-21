from __future__ import annotations

import json
from collections.abc import Iterator
from types import SimpleNamespace
from typing import Any

import httpx
import pytest

from proxyrequest_sdk import ApiError, AsyncClient, Client, ErrorKind, PaginationError
from proxyrequest_sdk.models import TelegramSessionRequest, UserCreateRequest

BASE_URL = "https://api.proxyrequest.com/api/v1"


def test_static_api_key_language_and_json_request_are_applied() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            400,
            json={"username": ["This username is already used."]},
            headers={"X-Request-ID": "request-123"},
        )

    transport = httpx.MockTransport(handler)
    http_client = httpx.Client(base_url=BASE_URL, transport=transport)
    client = Client.with_api_key("test-key", language="uk", http_client=http_client)

    with pytest.raises(ApiError) as captured:
        client.users.create(body=UserCreateRequest(username="customer", password="secret"))

    request = requests[0]
    assert request.headers["Authorization"] == "Static test-key"
    assert request.headers["Accept-Language"] == "uk"
    assert request.headers["Content-Type"].startswith("application/json")
    assert json.loads(request.content)["username"] == "customer"
    assert captured.value.kind is ErrorKind.VALIDATION
    assert captured.value.field_errors == {"username": ["This username is already used."]}
    assert captured.value.request_id == "request-123"


def test_bearer_error_contract_and_retry_after() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["Authorization"] == "Bearer access-token"
        return httpx.Response(429, json={"detail": "Slow down."}, headers={"Retry-After": "2.5"})

    http_client = httpx.Client(base_url=BASE_URL, transport=httpx.MockTransport(handler))
    client = Client.with_bearer_token("access-token", http_client=http_client)

    with pytest.raises(ApiError) as captured:
        client.users.list()

    assert captured.value.status_code == 429
    assert captured.value.kind is ErrorKind.RATE_LIMIT
    assert captured.value.detail == "Slow down."
    assert captured.value.retry_after == 2.5


def test_anonymous_and_telegram_service_auth_are_isolated() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            200,
            json={
                "access": "access-token",
                "expires_in": 3600,
                "locale": "en",
                "timezone": "UTC",
                "user": {},
            },
        )

    http_client = httpx.Client(
        base_url=BASE_URL,
        headers={"Authorization": "Bearer must-not-leak"},
        transport=httpx.MockTransport(handler),
    )
    client = Client.anonymous(http_client=http_client)
    response = client.telegram_service.create_session(
        body=TelegramSessionRequest(telegram_user_id=100, chat_id=200),
        service_secret="telegram-service-secret",
    )

    assert response.access == "access-token"
    assert "Authorization" not in requests[0].headers
    assert requests[0].headers["X-ProxyRequest-Telegram-Secret"] == "telegram-service-secret"
    assert json.loads(requests[0].content) == {"telegram_user_id": 100, "chat_id": 200}


def test_raw_escape_hatch_uses_configuration() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url == f"{BASE_URL}/future-endpoint?active=true"
        assert request.headers["Authorization"] == "Static raw-key"
        return httpx.Response(200, json={"ok": True})

    http_client = httpx.Client(base_url=BASE_URL, transport=httpx.MockTransport(handler))
    client = Client.with_api_key("raw-key", http_client=http_client)
    response = client.request("get", "/future-endpoint", params={"active": "true"})
    assert response.json() == {"ok": True}


def test_transport_failures_become_api_errors() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("connection refused", request=request)

    http_client = httpx.Client(base_url=BASE_URL, transport=httpx.MockTransport(handler))
    client = Client.with_api_key("key", http_client=http_client)
    with pytest.raises(ApiError) as captured:
        client.users.list()
    assert captured.value.kind is ErrorKind.NETWORK
    assert captured.value.status_code is None


def test_external_client_is_not_closed_and_base_url_is_validated() -> None:
    external = httpx.Client(
        base_url=BASE_URL,
        transport=httpx.MockTransport(lambda _: httpx.Response(204)),
    )
    client = Client.anonymous(http_client=external)
    client.close()
    assert not external.is_closed
    external.close()

    wrong = httpx.Client(base_url="https://example.com")
    with pytest.raises(ValueError, match="base_url"):
        Client.anonymous(http_client=wrong)
    wrong.close()


def test_lazy_pagination_follows_offsets_and_rejects_cycles() -> None:
    offsets: list[int] = []

    def fetch(*, limit: int, offset: int) -> SimpleNamespace:
        offsets.append(offset)
        if offset == 0:
            return SimpleNamespace(results=[1, 2], next_=f"{BASE_URL}/users?limit={limit}&offset=2")
        return SimpleNamespace(results=[3], next_=None)

    client = Client.anonymous()
    assert list(client.paginate(fetch, limit=2)) == [1, 2, 3]
    assert offsets == [0, 2]
    client.close()

    def cyclic(*, limit: int, offset: int) -> SimpleNamespace:
        return SimpleNamespace(results=[offset], next_=f"{BASE_URL}/users?limit={limit}&offset=0")

    with Client.anonymous() as second, pytest.raises(PaginationError, match="repeated"):
        list(second.paginate(cyclic, limit=1))


@pytest.mark.asyncio
async def test_async_client_and_pagination() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={"count": 0, "results": []})

    http_client = httpx.AsyncClient(base_url=BASE_URL, transport=httpx.MockTransport(handler))
    client = AsyncClient.with_bearer_token("async-token", http_client=http_client)
    page = await client.users.list()
    assert page.results == []
    assert requests[0].headers["Authorization"] == "Bearer async-token"

    async def fetch(*, limit: int, offset: int) -> Any:
        next_url = f"{BASE_URL}/users?limit={limit}&offset=1" if offset == 0 else None
        return SimpleNamespace(results=[offset], next_=next_url)

    values = [item async for item in client.paginate(fetch, limit=1)]
    assert values == [0, 1]
    await client.close()
    assert not http_client.is_closed
    await http_client.aclose()


def test_paginate_is_lazy() -> None:
    called = False

    def fetch(*, limit: int, offset: int) -> Any:
        nonlocal called
        called = True
        return SimpleNamespace(results=[], next_=None)

    with Client.anonymous() as client:
        iterator: Iterator[Any] = client.paginate(fetch)
        assert not called
        list(iterator)
        assert called

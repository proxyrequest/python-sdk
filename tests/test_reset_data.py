import inspect
import json
from uuid import UUID

import httpx
import pytest

from proxyrequest_sdk import AsyncClient, Client
from proxyrequest_sdk.models import ResetDataRequest


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_reset_data_sends_only_package_and_reuses_retry_key(asynchronous: bool) -> None:
    requests: list[httpx.Request] = []
    package_id = UUID("78b4ccde-49a7-4e1d-99ce-b56b875d8a11")

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if len(requests) == 1:
            raise httpx.ReadError("connection reset", request=request)
        return httpx.Response(
            202,
            json={
                "data_remaining": 0,
                "data_spent": 10,
                "data": 10,
                "is_auto_renewal": False,
                "ledgers": [],
                "package": {
                    "id": str(package_id),
                    "name": "Residential 10 GB",
                    "alias": "residential-10gb",
                    "is_unlimited_data": False,
                    "targeting_options": {
                        "package": "package",
                        "split_char": "-",
                        "value_char": "-",
                        "continent": "continent",
                        "country": "country",
                        "region": "region",
                        "city": "city",
                        "asn": "asn",
                        "isp": "isp",
                        "username": "username",
                        "pool": "pool",
                        "location": "location",
                        "location_format": "location_format",
                        "session": "session",
                        "session_mode_tag": "session_mode",
                        "session_ttl": "session_ttl",
                        "session_ttl_format": 1,
                        "os": "os",
                        "os_combined": False,
                        "os_split_char": "-",
                        "os_linux": "linux",
                        "os_windows": "windows",
                        "os_ios": "ios",
                        "os_macos": "macos",
                        "os_android": "android",
                    },
                },
                "created": "2026-09-17T00:00:00Z",
                "updated": "2026-09-17T00:00:00Z",
                "data_updated": "2026-09-17T00:00:00Z",
            },
        )

    transport = httpx.MockTransport(handler)
    base_url = "https://api.proxyrequest.com/api/v1"
    http: httpx.Client | httpx.AsyncClient
    client: Client | AsyncClient
    if asynchronous:
        http = httpx.AsyncClient(base_url=base_url, transport=transport)
        client = AsyncClient.with_api_key("secret", http_client=http)
    else:
        http = httpx.Client(base_url=base_url, transport=transport)
        client = Client.with_api_key("secret", http_client=http)
    try:
        result = client.users.reset_data_with_response(
            id=package_id, body=ResetDataRequest(package_id=package_id)
        )
        response = await result if inspect.isawaitable(result) else result
        assert response.status_code == 202
        assert response.data.data_remaining == 0
        assert len(requests) == 2
        key = requests[0].headers["Idempotency-Key"]
        assert key
        for request in requests:
            assert request.method == "POST"
            assert request.url.path == f"/api/v1/users/{package_id}/data/reset"
            assert json.loads(request.content) == {"package_id": str(package_id)}
            assert request.headers["Idempotency-Key"] == key
    finally:
        if isinstance(http, httpx.AsyncClient):
            await http.aclose()
        else:
            http.close()

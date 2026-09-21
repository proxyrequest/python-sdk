from __future__ import annotations

import importlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any

import httpx
import pytest
from test_backend_compatibility import mocked_client, result

RAW_FEED = (Path(__file__).parent / "fixtures/analytics-large-ids.json").read_bytes()
DATES = [
    "2026-07-01T00:00:00Z",
    "2026-07-01T03:04:59.123+03:00",
    "2026-07-01T00:00:00",
    "2026-07-01 00:00:00",
    "01-07-2026 00:00:00",
    "2026-07-01",
    "01-07-2026",
    "1782864000",
    "1782864000.5",
    1782864000,
    1782864000.5,
    0,
    datetime.fromisoformat("2026-07-01T03:04:59.123+03:00"),
]


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("metadata", [False, True])
async def test_feed_uint64_ids_remain_exact(asynchronous: bool, metadata: bool) -> None:
    async with mocked_client(asynchronous, [httpx.Response(200, content=RAW_FEED)]) as (client, _):
        method = "list_feed_with_response" if metadata else "list_feed"
        response = await result(getattr(client.analytics, method)(start=1782864000.5))
        page = response.data if metadata else response
        expected = [row["id"] for row in json.loads(RAW_FEED)["results"]]
        assert [row.id for row in page.results] == expected
        assert all(type(row.id) is int for row in page.results)
        assert [row["id"] for row in page.to_dict()["results"]] == expected


@pytest.mark.parametrize("operation", ["feed", "domains", "logs", "overall", "transactions"])
@pytest.mark.parametrize("value", DATES)
def test_date_formats_in_every_analytics_request(operation: str, value: Any) -> None:
    endpoint = importlib.import_module(
        f"proxyrequest_sdk._generated.api.analytics.analytics_{operation}_retrieve"
    )
    kwargs = {"start": value, "end": value, "timezone": "Europe/Kiev"}
    if operation == "transactions":
        kwargs["id"] = "customer"
    request = endpoint._get_kwargs(**kwargs)
    params = httpx.QueryParams(request["params"])
    expected = value.isoformat() if isinstance(value, datetime) else str(value)
    assert params["start"] == params["end"] == expected
    assert params["timezone"] == "Europe/Kiev"


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("value", DATES)
async def test_date_formats_through_public_client(asynchronous: bool, value: Any) -> None:
    async with mocked_client(asynchronous, [httpx.Response(200, content=RAW_FEED)]) as (
        client,
        requests,
    ):
        await result(client.analytics.list_feed(start=value, end=value))
        expected = value.isoformat() if isinstance(value, datetime) else str(value)
        assert requests[0].url.params["start"] == requests[0].url.params["end"] == expected


def test_legacy_logs_hostname_and_omitted_dates() -> None:
    from proxyrequest_sdk._generated.api.analytics import analytics_logs_retrieve

    kwargs = analytics_logs_retrieve._get_kwargs(hostname="example.com")
    assert kwargs["params"]["hostname"] == "example.com"
    assert "start" not in kwargs["params"]
    assert "end" not in kwargs["params"]


@pytest.mark.parametrize("include", [False, True])
def test_domain_filters_and_boolean_encoding(include: bool) -> None:
    from proxyrequest_sdk._generated.api.analytics import analytics_domains_retrieve

    hostname = "https://example.com:443/path,192.0.2.1,[2001:db8::1]:80"
    params = httpx.QueryParams(
        analytics_domains_retrieve._get_kwargs(
            hostname=hostname,
            include_sub_users=include,
        )["params"]
    )
    assert params["hostname"] == hostname
    assert params["include_sub_users"] == str(include).lower()

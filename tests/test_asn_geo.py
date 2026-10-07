from __future__ import annotations

from typing import Any
from uuid import UUID

import httpx
import pytest
from test_backend_compatibility import mocked_client, result

from proxyrequest_sdk.models import LocationASNRecord


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("include_geo", [None, False, True])
async def test_asn_geography_is_opt_in(asynchronous: bool, include_geo: bool | None) -> None:
    geo = [{"country": {"code": "us", "name": "United States"}}] if include_geo else []
    payload: dict[str, Any] = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{"code": "7922", "name": "Example ASN", "country_codes": ["us"], "geo": geo}],
    }
    async with mocked_client(asynchronous, [httpx.Response(200, json=payload)]) as (
        client,
        requests,
    ):
        options = {} if include_geo is None else {"include_geo": include_geo}
        page = await result(
            client.locations.list_asns(
                package_id=UUID("550e8400-e29b-41d4-a716-446655440002"), **options
            )
        )
        record = page.results[0]
        assert isinstance(record, LocationASNRecord)
        assert record.country_codes == ["us"]
        assert len(record.geo) == len(geo)
        assert record.to_dict() == payload["results"][0]
        assert requests[0].url.params.get("include_geo") == str(bool(include_geo)).lower()

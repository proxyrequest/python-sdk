from __future__ import annotations

import json
from uuid import UUID

import httpx
import pytest
from test_backend_compatibility import FIXTURES, mocked_client, result

from proxyrequest_sdk import ApiError
from proxyrequest_sdk.models import (
    InvoiceCreateRequestGatewayEnum,
    PurchaseMutationRequest,
    RenewalCheckoutRequest,
    RenewalRequestRequest,
    RenewalSelectionRequest,
    StaticCheckoutRequest,
    StaticExportRetrieveProtocol,
)

ORDER = UUID("550e8400-e29b-41d4-a716-446655440001")
TERM = UUID("550e8400-e29b-41d4-a716-446655440002")
OFFER = UUID("550e8400-e29b-41d4-a716-446655440003")
ENDPOINT = UUID("550e8400-e29b-41d4-a716-446655440004")
INVOICE = UUID("550e8400-e29b-41d4-a716-446655440005")
WALLET = InvoiceCreateRequestGatewayEnum.WALLET
DATE = "2026-11-26T11:00:00Z"
SNAPSHOT = {
    "version": 2,
    "term_id": str(TERM),
    "duration_kind": "hours",
    "duration_value": 24,
    "quantity": 1,
    "price_cents": 150,
    "currency": "USD",
    "country_code": "US",
    "allocation_mode": "dedicated",
    "network_class": "isp",
    "hold_hours": 24,
    "commission_rate": "0",
    "commission_type": "percentage",
}


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_static_rental_purchase_carries_one_header_across_lost_response(
    asynchronous: bool,
) -> None:
    purchase = {
        "id": str(ORDER),
        "order_id": str(ORDER),
        "status": "reserved",
        "snapshot": SNAPSHOT,
        "reserved_until": DATE,
        "invoice_id": None,
    }
    invoice = {**FIXTURES["invoice_full"], "id": str(INVOICE), "rental_status": "provisioning"}
    responses: list[httpx.Response | httpx.HTTPError] = [
        httpx.ReadError("Response lost after reservation"),
        httpx.Response(201, json=purchase),
        httpx.Response(200, json={"total": 150, "currency": "USD", "groups": []}),
        httpx.Response(201, json=invoice),
        httpx.Response(200, json=invoice),
        httpx.Response(
            409, json={"code": "idempotency_conflict", "non_field_errors": ["Conflict"]}
        ),
    ]
    async with mocked_client(asynchronous, responses) as (client, requests):
        reserved = await result(
            client.orders.reserve(
                body=PurchaseMutationRequest(offer_id=OFFER, idempotency_key="reserve")
            )
        )
        assert reserved.order_id == ORDER
        assert reserved.snapshot.term_id == TERM
        quote = await result(
            client.orders.quote_checkout(ORDER, body=StaticCheckoutRequest(gateway=WALLET))
        )
        checkout = StaticCheckoutRequest(gateway=WALLET, expected_total=quote.total)
        first = await result(
            client.orders.checkout_with_response(ORDER, body=checkout, idempotency_key="pay")
        )
        replay = await result(
            client.orders.checkout_with_response(ORDER, body=checkout, idempotency_key="pay")
        )
        assert (first.status_code, replay.status_code, first.data.id) == (201, 200, replay.data.id)
        with pytest.raises(ApiError) as captured:
            await result(client.orders.checkout(ORDER, body=checkout, idempotency_key="pay"))
        assert captured.value.code == "idempotency_conflict"
        assert captured.value.idempotency_key == "pay"
        assert [req.headers["Idempotency-Key"] for req in requests[:2]] == ["reserve", "reserve"]
        assert requests[0].content == requests[1].content
        assert "Idempotency-Key" not in requests[2].headers
        assert json.loads(requests[3].content)["expected_total"] == 150


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_static_rental_read_export_and_renew(asynchronous: bool) -> None:
    rental = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [
            {
                "id": str(ENDPOINT),
                "order_id": str(ORDER),
                "allowed_ips": [],
                "periods": [],
                "connections": [
                    {
                        "address_id": str(ENDPOINT),
                        "assignment_id": str(ENDPOINT),
                        "source_ip": "192.0.2.20",
                        "host": "192.0.2.20",
                        "http_port": 8080,
                        "socks_port": 1080,
                        "state": "active",
                        "asn": None,
                        "username": "synthetic-user",
                        "password": "synthetic-password",
                    }
                ],
                "max_bandwidth_mbps": None,
                "capabilities": {"suspend": True},
                "group_id": None,
                "group_size": 1,
                "renewable": True,
                "ready": True,
            }
        ],
        "groups": [],
        "order_id": str(ORDER),
        "user_id": str(ORDER),
        "package_id": str(OFFER),
        "package_name": "ISP",
        "status": "fulfilled",
        "renewable_count": 1,
        "snapshot": SNAPSHOT,
        "invoice_id": str(INVOICE),
        "reserved_until": None,
        "terms": [],
        "invoices": [],
        "credential_mode": "per_endpoint",
        "capabilities": {"suspend": True},
    }
    lines = "socks5://synthetic-user:synthetic-password@192.0.2.20:1080\n"
    responses = [
        httpx.Response(200, json=rental),
        httpx.Response(200, text=lines, headers={"Content-Type": "text/plain; charset=utf-8"}),
        httpx.Response(200, text="", headers={"Content-Type": "text/plain; charset=utf-8"}),
        httpx.Response(
            200,
            json={"total": 50, "currency": "USD", "endpoint_ids": [str(ENDPOINT)], "quantity": 1},
        ),
        httpx.Response(201, json=FIXTURES["invoice_full"]),
    ]
    async with mocked_client(asynchronous, responses) as (client, requests):
        order = await result(client.orders.get_rental(ORDER, limit=1))
        assert order.results[0].ready
        assert order.results[0].connections[0].socks_port == 1080
        exported = await result(
            client.static_proxies.export_urls_with_response(
                order_id=ORDER,
                protocol=StaticExportRetrieveProtocol.SOCKS5,
            )
        )
        assert exported.data == lines
        assert await result(client.static_proxies.export_urls(order_id=ORDER)) == ""
        billing = RenewalCheckoutRequest(gateway=WALLET)
        quote = await result(
            client.orders.quote_renewal(
                ORDER,
                body=RenewalSelectionRequest(
                    term_id=TERM, invoice=billing, endpoint_ids=[ENDPOINT]
                ),
            )
        )
        renewal = RenewalRequestRequest(
            term_id=TERM,
            invoice=billing,
            endpoint_ids=quote.endpoint_ids,
            expected_total=quote.total,
        )
        await result(client.orders.renew(ORDER, body=renewal, idempotency_key="renew"))
        assert requests[0].url.params["limit"] == "1"
        assert requests[1].url.params["order_id"] == str(ORDER)
        assert requests[1].url.params["protocol"] == "socks5"
        assert requests[4].headers["Idempotency-Key"] == "renew"
        assert json.loads(requests[4].content)["endpoint_ids"] == [str(ENDPOINT)]


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_password_rotation_preserves_order_reset_and_can_target_a_group(
    asynchronous: bool,
) -> None:
    responses = [
        httpx.Response(200, json={"message": "Password reset successfully.", "success": True}),
        httpx.Response(202, json={"message": "Password rotation queued.", "success": True}),
        httpx.Response(
            200,
            json={
                "id": str(ENDPOINT),
                "order_id": str(ORDER),
                "allowed_ips": [],
                "periods": [],
                "connections": [],
                "max_bandwidth_mbps": None,
                "capabilities": {"rotate_password": True},
                "password_rotation_status": "succeeded",
            },
        ),
        httpx.Response(400, json={"code": "unsupported_operation", "detail": "Unavailable."}),
    ]
    async with mocked_client(asynchronous, responses) as (client, requests):
        immediate = await result(client.orders.reset_proxy_password(ORDER))
        assert immediate.success
        queued = await result(
            client.orders.reset_proxy_password_with_response(ORDER, endpoint_id=ENDPOINT)
        )
        assert queued.status_code == 202 and queued.data.success
        endpoint = await result(client.static_proxies.get_endpoint(ENDPOINT))
        assert endpoint.password_rotation_status == "succeeded"
        with pytest.raises(ApiError) as captured:
            await result(client.orders.reset_proxy_password(ORDER, endpoint_id=ENDPOINT))
        assert captured.value.code == "unsupported_operation"
        assert [r.method for r in requests] == ["POST", "POST", "GET", "POST"]
        assert all(not r.content for r in requests)
        assert "endpoint_id" not in requests[0].url.params
        assert requests[1].url.params["endpoint_id"] == str(ENDPOINT)

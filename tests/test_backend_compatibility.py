from __future__ import annotations

import inspect
import json
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any
from uuid import UUID

import httpx
import pytest

from proxyrequest_sdk import ApiError, AsyncClient, Client, ErrorKind
from proxyrequest_sdk._generated.types import UNSET
from proxyrequest_sdk.models import (
    GoogleAuthRequest,
    Invoice,
    InvoiceCreateRequest,
    InvoiceCreateRequestGatewayEnum,
    InvoiceGatewayEnum,
    InvoiceShort,
    LoginRequest,
    OTPChallenge,
    TokenPairResponse,
    TwoFactorDisableRequest,
    TwoFactorSetupRequestRequest,
    VerifyOTPRequest,
)

FIXTURES = json.loads((Path(__file__).parent / "fixtures/backend-responses.json").read_text())
BASE_URL = "https://api.proxyrequest.com/api/v1"
CHALLENGE = {"status": "otp_required", "challenge": "synthetic-challenge", "expires_in": 300}
TOKENS = {"token": "synthetic-access", "refresh": "synthetic-refresh"}


@asynccontextmanager
async def mocked_client(
    asynchronous: bool, responses: list[httpx.Response]
) -> AsyncIterator[tuple[Any, list[httpx.Request]]]:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return responses.pop(0)

    if asynchronous:
        async with (
            httpx.AsyncClient(base_url=BASE_URL, transport=httpx.MockTransport(handler)) as http,
            AsyncClient.anonymous(http_client=http) as client,
        ):
            yield client, requests
    else:
        with (
            httpx.Client(base_url=BASE_URL, transport=httpx.MockTransport(handler)) as sync_http,
            Client.anonymous(http_client=sync_http) as sync_client,
        ):
            yield sync_client, requests


async def result(value: Any) -> Any:
    return await value if inspect.isawaitable(value) else value


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("google", [False, True])
async def test_login_challenge_and_verification(asynchronous: bool, google: bool) -> None:
    async with mocked_client(
        asynchronous, [httpx.Response(202, json=CHALLENGE), httpx.Response(200, json=TOKENS)]
    ) as (client, requests):
        challenge = await result(
            client.authorization.login_with_google(body=GoogleAuthRequest(credential="synthetic"))
            if google
            else client.authorization.login(
                body=LoginRequest(email="sdk@example.com", password="synthetic")
            )
        )
        assert isinstance(challenge, OTPChallenge)
        assert challenge.challenge == CHALLENGE["challenge"]
        tokens = await result(
            client.authorization.verify_otp(
                body=VerifyOTPRequest(challenge=challenge.challenge, code="123456")
            )
        )
        assert isinstance(tokens, TokenPairResponse)
        assert tokens.token == TOKENS["token"]
        assert requests[1].url.path == "/api/v1/login/otp"
        assert json.loads(requests[1].content) == {
            "challenge": CHALLENGE["challenge"],
            "code": "123456",
        }


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_mfa_primary_factor_bodies(asynchronous: bool) -> None:
    responses = [
        httpx.Response(200, json={"secret": "synthetic", "otpauth_url": "otpauth://totp/sdk"}),
        httpx.Response(200, json={"enabled": False}),
    ]
    async with mocked_client(asynchronous, responses) as (client, requests):
        await result(
            client.profile.setup_two_factor(
                body=TwoFactorSetupRequestRequest(password="synthetic", code="123456")
            )
        )
        await result(
            client.profile.disable_two_factor(
                body=TwoFactorDisableRequest(code="123456", credential="synthetic-google")
            )
        )
        assert json.loads(requests[0].content) == {"password": "synthetic", "code": "123456"}
        assert json.loads(requests[1].content) == {
            "code": "123456",
            "credential": "synthetic-google",
        }


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("mode", ["legacy", "package"])
async def test_runtime_user_variants(asynchronous: bool, mode: str) -> None:
    payload = FIXTURES[f"user_{mode}"]
    async with mocked_client(asynchronous, [httpx.Response(200, json=payload)]) as (client, _):
        user = await result(client.profile.get())
        assert user.username == payload["username"]
        assert user.orders == ([] if mode == "package" else UNSET)
        assert user.data == (UNSET if mode == "package" else 0)
        assert ("data" in user.to_dict()) == (mode == "legacy")


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_runtime_invoice_variants_and_new_payment_fields(asynchronous: bool) -> None:
    full = {
        **FIXTURES["invoice_full"],
        "gateway": "future-provider",
        "future_field": {"kept": True},
    }
    short = FIXTURES["invoice_short"]
    responses = [
        httpx.Response(201, json=full),
        httpx.Response(200, json=short),
        httpx.Response(
            200, json={"count": 2, "next": None, "previous": None, "results": [full, short]}
        ),
    ]
    async with mocked_client(asynchronous, responses) as (client, requests):
        created = await result(
            client.invoices.create(
                body=InvoiceCreateRequest(
                    gateway=InvoiceCreateRequestGatewayEnum("whitepay"),
                    amount=500,
                    payment_currency="UAH",
                )
            )
        )
        assert isinstance(created, Invoice)
        assert created.package is None and created.coupon is None and created.country is None
        assert isinstance(created.gateway, InvoiceGatewayEnum)
        assert created.gateway.value == "future-provider"
        assert created.payment_amount == 500
        assert created["future_field"] == {"kept": True}
        assert json.loads(requests[0].content)["payment_currency"] == "UAH"
        retrieved = await result(client.invoices.get(id=UUID(short["id"])))
        assert isinstance(retrieved, InvoiceShort)
        page = await result(client.invoices.list())
        assert isinstance(page.results[0], Invoice)
        assert isinstance(page.results[1], InvoiceShort)


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(
    "status,body",
    [
        (400, b"<html>bad</html>"),
        (201, b'{"id":"invalid-model"}'),
        (201, b"<html>bad</html>"),
        (502, b'{"invoice_id":"created","retryable":true}'),
    ],
)
async def test_failed_decoding_retains_http_context_and_key(
    asynchronous: bool, status: int, body: bytes
) -> None:
    async with mocked_client(
        asynchronous,
        [httpx.Response(status, content=body, headers={"X-Request-ID": "sdk-request"})],
    ) as (client, requests):
        with pytest.raises(ApiError) as captured:
            await result(
                client.invoices.create(
                    body=InvoiceCreateRequest(
                        gateway=InvoiceCreateRequestGatewayEnum.WALLET, amount=500
                    )
                )
            )
        error = captured.value
        assert error.status_code == status
        assert error.raw_body == body
        assert error.request_id == "sdk-request"
        assert error.idempotency_key == requests[0].headers["Idempotency-Key"]
        assert error.kind == (
            ErrorKind.UNEXPECTED
            if status == 201
            else ErrorKind.VALIDATION
            if status == 400
            else ErrorKind.SERVER
        )
        assert len(requests) == 1

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.kyc_sessions_create_response_400 import KycSessionsCreateResponse400
from ...models.kyc_sessions_create_response_401 import KycSessionsCreateResponse401
from ...models.kyc_sessions_create_response_403 import KycSessionsCreateResponse403
from ...models.session_input_request import SessionInputRequest
from ...models.session_output import SessionOutput
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: SessionInputRequest,
    idempotency_key: str,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/kyc/sessions/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    KycSessionsCreateResponse400
    | KycSessionsCreateResponse401
    | KycSessionsCreateResponse403
    | SessionOutput
    | None
):
    if response.status_code == 200:
        response_200 = SessionOutput.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = KycSessionsCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = KycSessionsCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = KycSessionsCreateResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    KycSessionsCreateResponse400
    | KycSessionsCreateResponse401
    | KycSessionsCreateResponse403
    | SessionOutput
]:
    parsed = parse_response(_parse_response, client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SessionInputRequest,
    idempotency_key: str,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    KycSessionsCreateResponse400
    | KycSessionsCreateResponse401
    | KycSessionsCreateResponse403
    | SessionOutput
]:
    """Start identity verification

     Create or resume a provider-hosted verification session for the authenticated account. Supply a
    stable Idempotency-Key; the server selects the user and environment.

    Args:
        idempotency_key (str):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (SessionInputRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KycSessionsCreateResponse400 | KycSessionsCreateResponse401 | KycSessionsCreateResponse403 | SessionOutput]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SessionInputRequest,
    idempotency_key: str,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    KycSessionsCreateResponse400
    | KycSessionsCreateResponse401
    | KycSessionsCreateResponse403
    | SessionOutput
    | None
):
    """Start identity verification

     Create or resume a provider-hosted verification session for the authenticated account. Supply a
    stable Idempotency-Key; the server selects the user and environment.

    Args:
        idempotency_key (str):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (SessionInputRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KycSessionsCreateResponse400 | KycSessionsCreateResponse401 | KycSessionsCreateResponse403 | SessionOutput
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SessionInputRequest,
    idempotency_key: str,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    KycSessionsCreateResponse400
    | KycSessionsCreateResponse401
    | KycSessionsCreateResponse403
    | SessionOutput
]:
    """Start identity verification

     Create or resume a provider-hosted verification session for the authenticated account. Supply a
    stable Idempotency-Key; the server selects the user and environment.

    Args:
        idempotency_key (str):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (SessionInputRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KycSessionsCreateResponse400 | KycSessionsCreateResponse401 | KycSessionsCreateResponse403 | SessionOutput]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SessionInputRequest,
    idempotency_key: str,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    KycSessionsCreateResponse400
    | KycSessionsCreateResponse401
    | KycSessionsCreateResponse403
    | SessionOutput
    | None
):
    """Start identity verification

     Create or resume a provider-hosted verification session for the authenticated account. Supply a
    stable Idempotency-Key; the server selects the user and environment.

    Args:
        idempotency_key (str):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (SessionInputRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KycSessionsCreateResponse400 | KycSessionsCreateResponse401 | KycSessionsCreateResponse403 | SessionOutput
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.enabled_response import EnabledResponse
from ...models.mfa_error import MFAError
from ...models.two_factor_confirm_request import TwoFactorConfirmRequest
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: TwoFactorConfirmRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/profile/2fa/confirm",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EnabledResponse | MFAError | None:
    if response.status_code == 200:
        response_200 = EnabledResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = MFAError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = MFAError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = MFAError.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = MFAError.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = MFAError.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EnabledResponse | MFAError]:
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
    body: TwoFactorConfirmRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[EnabledResponse | MFAError]:
    """Manage two-factor authentication

     Prepare or confirm an authenticator, disable it, or replace recovery codes. Changes revoke previous
    authentication proofs. Setup returns an SVG QR code and recovery codes are returned once.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (TwoFactorConfirmRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnabledResponse | MFAError]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: TwoFactorConfirmRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> EnabledResponse | MFAError | None:
    """Manage two-factor authentication

     Prepare or confirm an authenticator, disable it, or replace recovery codes. Changes revoke previous
    authentication proofs. Setup returns an SVG QR code and recovery codes are returned once.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (TwoFactorConfirmRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnabledResponse | MFAError
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TwoFactorConfirmRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[EnabledResponse | MFAError]:
    """Manage two-factor authentication

     Prepare or confirm an authenticator, disable it, or replace recovery codes. Changes revoke previous
    authentication proofs. Setup returns an SVG QR code and recovery codes are returned once.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (TwoFactorConfirmRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnabledResponse | MFAError]
    """

    kwargs = _get_kwargs(
        body=body,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: TwoFactorConfirmRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> EnabledResponse | MFAError | None:
    """Manage two-factor authentication

     Prepare or confirm an authenticator, disable it, or replace recovery codes. Changes revoke previous
    authentication proofs. Setup returns an SVG QR code and recovery codes are returned once.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (TwoFactorConfirmRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnabledResponse | MFAError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

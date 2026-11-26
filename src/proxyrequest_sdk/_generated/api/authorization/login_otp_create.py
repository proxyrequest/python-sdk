from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mfa_error import MFAError
from ...models.token_pair_response import TokenPairResponse
from ...models.verify_otp_request import VerifyOTPRequest
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: VerifyOTPRequest,
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
        "url": "/login/otp",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MFAError | TokenPairResponse | None:
    if response.status_code == 200:
        response_200 = TokenPairResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = MFAError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = MFAError.from_dict(response.json())

        return response_401

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
) -> Response[MFAError | TokenPairResponse]:
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
    body: VerifyOTPRequest,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[MFAError | TokenPairResponse]:
    """Complete two-factor sign-in

     Exchange a single-use sign-in challenge and authenticator or recovery code for access and refresh
    tokens.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (VerifyOTPRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MFAError | TokenPairResponse]
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
    body: VerifyOTPRequest,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> MFAError | TokenPairResponse | None:
    """Complete two-factor sign-in

     Exchange a single-use sign-in challenge and authenticator or recovery code for access and refresh
    tokens.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (VerifyOTPRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MFAError | TokenPairResponse
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
    body: VerifyOTPRequest,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[MFAError | TokenPairResponse]:
    """Complete two-factor sign-in

     Exchange a single-use sign-in challenge and authenticator or recovery code for access and refresh
    tokens.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (VerifyOTPRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MFAError | TokenPairResponse]
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
    body: VerifyOTPRequest,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> MFAError | TokenPairResponse | None:
    """Complete two-factor sign-in

     Exchange a single-use sign-in challenge and authenticator or recovery code for access and refresh
    tokens.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (VerifyOTPRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MFAError | TokenPairResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

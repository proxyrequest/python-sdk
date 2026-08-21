from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.google_auth_request import GoogleAuthRequest
from ...models.login_google_create_response_400 import LoginGoogleCreateResponse400
from ...models.login_google_create_response_403 import LoginGoogleCreateResponse403
from ...models.token_pair_response import TokenPairResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: GoogleAuthRequest,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/login/google",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoginGoogleCreateResponse400 | LoginGoogleCreateResponse403 | TokenPairResponse | None:
    if response.status_code == 200:
        response_200 = TokenPairResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LoginGoogleCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = LoginGoogleCreateResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoginGoogleCreateResponse400 | LoginGoogleCreateResponse403 | TokenPairResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GoogleAuthRequest,
    accept_language: str | Unset = UNSET,
) -> Response[LoginGoogleCreateResponse400 | LoginGoogleCreateResponse403 | TokenPairResponse]:
    """Sign in with Google

     Verifies a Google ID token, creates or links the matching customer account when needed, and returns
    an API token pair.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (GoogleAuthRequest): Enhanced Google OAuth authentication with comprehensive security
            validation and user management.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoginGoogleCreateResponse400 | LoginGoogleCreateResponse403 | TokenPairResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: GoogleAuthRequest,
    accept_language: str | Unset = UNSET,
) -> LoginGoogleCreateResponse400 | LoginGoogleCreateResponse403 | TokenPairResponse | None:
    """Sign in with Google

     Verifies a Google ID token, creates or links the matching customer account when needed, and returns
    an API token pair.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (GoogleAuthRequest): Enhanced Google OAuth authentication with comprehensive security
            validation and user management.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoginGoogleCreateResponse400 | LoginGoogleCreateResponse403 | TokenPairResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GoogleAuthRequest,
    accept_language: str | Unset = UNSET,
) -> Response[LoginGoogleCreateResponse400 | LoginGoogleCreateResponse403 | TokenPairResponse]:
    """Sign in with Google

     Verifies a Google ID token, creates or links the matching customer account when needed, and returns
    an API token pair.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (GoogleAuthRequest): Enhanced Google OAuth authentication with comprehensive security
            validation and user management.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoginGoogleCreateResponse400 | LoginGoogleCreateResponse403 | TokenPairResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GoogleAuthRequest,
    accept_language: str | Unset = UNSET,
) -> LoginGoogleCreateResponse400 | LoginGoogleCreateResponse403 | TokenPairResponse | None:
    """Sign in with Google

     Verifies a Google ID token, creates or links the matching customer account when needed, and returns
    an API token pair.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (GoogleAuthRequest): Enhanced Google OAuth authentication with comprehensive security
            validation and user management.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoginGoogleCreateResponse400 | LoginGoogleCreateResponse403 | TokenPairResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed

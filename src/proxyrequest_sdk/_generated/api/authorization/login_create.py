from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.login_create_response_400 import LoginCreateResponse400
from ...models.login_request import LoginRequest
from ...models.token_pair_response import TokenPairResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: LoginRequest,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/login",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LoginCreateResponse400 | TokenPairResponse | None:
    if response.status_code == 200:
        response_200 = TokenPairResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LoginCreateResponse400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LoginCreateResponse400 | TokenPairResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LoginRequest,
    accept_language: str | Unset = UNSET,
) -> Response[LoginCreateResponse400 | TokenPairResponse]:
    """Sign in with email or username

     Checks account credentials and returns an access token plus a refresh token. Send the access token
    as `Authorization: Bearer `.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (LoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoginCreateResponse400 | TokenPairResponse]
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
    body: LoginRequest,
    accept_language: str | Unset = UNSET,
) -> LoginCreateResponse400 | TokenPairResponse | None:
    """Sign in with email or username

     Checks account credentials and returns an access token plus a refresh token. Send the access token
    as `Authorization: Bearer `.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (LoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoginCreateResponse400 | TokenPairResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LoginRequest,
    accept_language: str | Unset = UNSET,
) -> Response[LoginCreateResponse400 | TokenPairResponse]:
    """Sign in with email or username

     Checks account credentials and returns an access token plus a refresh token. Send the access token
    as `Authorization: Bearer `.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (LoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoginCreateResponse400 | TokenPairResponse]
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
    body: LoginRequest,
    accept_language: str | Unset = UNSET,
) -> LoginCreateResponse400 | TokenPairResponse | None:
    """Sign in with email or username

     Checks account credentials and returns an access token plus a refresh token. Send the access token
    as `Authorization: Bearer `.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (LoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoginCreateResponse400 | TokenPairResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed

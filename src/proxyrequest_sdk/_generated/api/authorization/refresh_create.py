from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.refresh_create_response_400 import RefreshCreateResponse400
from ...models.refresh_create_response_401 import RefreshCreateResponse401
from ...models.token_refresh_request import TokenRefreshRequest
from ...models.token_refresh_response import TokenRefreshResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: TokenRefreshRequest,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/refresh",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RefreshCreateResponse400 | RefreshCreateResponse401 | TokenRefreshResponse | None:
    if response.status_code == 200:
        response_200 = TokenRefreshResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RefreshCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RefreshCreateResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RefreshCreateResponse400 | RefreshCreateResponse401 | TokenRefreshResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TokenRefreshRequest,
    accept_language: str | Unset = UNSET,
) -> Response[RefreshCreateResponse400 | RefreshCreateResponse401 | TokenRefreshResponse]:
    """Refresh an access token

     Uses a valid refresh token to issue a new short-lived access token for the same account session.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (TokenRefreshRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefreshCreateResponse400 | RefreshCreateResponse401 | TokenRefreshResponse]
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
    client: AuthenticatedClient | Client,
    body: TokenRefreshRequest,
    accept_language: str | Unset = UNSET,
) -> RefreshCreateResponse400 | RefreshCreateResponse401 | TokenRefreshResponse | None:
    """Refresh an access token

     Uses a valid refresh token to issue a new short-lived access token for the same account session.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (TokenRefreshRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefreshCreateResponse400 | RefreshCreateResponse401 | TokenRefreshResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TokenRefreshRequest,
    accept_language: str | Unset = UNSET,
) -> Response[RefreshCreateResponse400 | RefreshCreateResponse401 | TokenRefreshResponse]:
    """Refresh an access token

     Uses a valid refresh token to issue a new short-lived access token for the same account session.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (TokenRefreshRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefreshCreateResponse400 | RefreshCreateResponse401 | TokenRefreshResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TokenRefreshRequest,
    accept_language: str | Unset = UNSET,
) -> RefreshCreateResponse400 | RefreshCreateResponse401 | TokenRefreshResponse | None:
    """Refresh an access token

     Uses a valid refresh token to issue a new short-lived access token for the same account session.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (TokenRefreshRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefreshCreateResponse400 | RefreshCreateResponse401 | TokenRefreshResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed

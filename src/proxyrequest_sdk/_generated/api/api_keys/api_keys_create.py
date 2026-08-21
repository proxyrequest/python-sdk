from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_key_create import APIKeyCreate
from ...models.api_key_create_request import APIKeyCreateRequest
from ...models.api_keys_create_response_400 import ApiKeysCreateResponse400
from ...models.api_keys_create_response_401 import ApiKeysCreateResponse401
from ...models.api_keys_create_response_403 import ApiKeysCreateResponse403
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: APIKeyCreateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api-keys",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    APIKeyCreate
    | ApiKeysCreateResponse400
    | ApiKeysCreateResponse401
    | ApiKeysCreateResponse403
    | None
):
    if response.status_code == 201:
        response_201 = APIKeyCreate.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ApiKeysCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiKeysCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiKeysCreateResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    APIKeyCreate | ApiKeysCreateResponse400 | ApiKeysCreateResponse401 | ApiKeysCreateResponse403
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: APIKeyCreateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    APIKeyCreate | ApiKeysCreateResponse400 | ApiKeysCreateResponse401 | ApiKeysCreateResponse403
]:
    """Create an API key

     Creates an API key for server-to-server access. allowed_ips can restrict the key to trusted IPv4 or
    IPv6 addresses.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (APIKeyCreateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIKeyCreate | ApiKeysCreateResponse400 | ApiKeysCreateResponse401 | ApiKeysCreateResponse403]
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
    body: APIKeyCreateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    APIKeyCreate
    | ApiKeysCreateResponse400
    | ApiKeysCreateResponse401
    | ApiKeysCreateResponse403
    | None
):
    """Create an API key

     Creates an API key for server-to-server access. allowed_ips can restrict the key to trusted IPv4 or
    IPv6 addresses.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (APIKeyCreateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIKeyCreate | ApiKeysCreateResponse400 | ApiKeysCreateResponse401 | ApiKeysCreateResponse403
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: APIKeyCreateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    APIKeyCreate | ApiKeysCreateResponse400 | ApiKeysCreateResponse401 | ApiKeysCreateResponse403
]:
    """Create an API key

     Creates an API key for server-to-server access. allowed_ips can restrict the key to trusted IPv4 or
    IPv6 addresses.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (APIKeyCreateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIKeyCreate | ApiKeysCreateResponse400 | ApiKeysCreateResponse401 | ApiKeysCreateResponse403]
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
    body: APIKeyCreateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    APIKeyCreate
    | ApiKeysCreateResponse400
    | ApiKeysCreateResponse401
    | ApiKeysCreateResponse403
    | None
):
    """Create an API key

     Creates an API key for server-to-server access. allowed_ips can restrict the key to trusted IPv4 or
    IPv6 addresses.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (APIKeyCreateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIKeyCreate | ApiKeysCreateResponse400 | ApiKeysCreateResponse401 | ApiKeysCreateResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed

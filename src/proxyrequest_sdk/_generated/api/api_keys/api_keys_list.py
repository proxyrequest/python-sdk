from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_keys_list_response_400 import ApiKeysListResponse400
from ...models.api_keys_list_response_401 import ApiKeysListResponse401
from ...models.api_keys_list_response_403 import ApiKeysListResponse403
from ...models.paginated_api_key_list import PaginatedAPIKeyList
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api-keys",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiKeysListResponse400
    | ApiKeysListResponse401
    | ApiKeysListResponse403
    | PaginatedAPIKeyList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedAPIKeyList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiKeysListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiKeysListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiKeysListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ApiKeysListResponse400 | ApiKeysListResponse401 | ApiKeysListResponse403 | PaginatedAPIKeyList
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    ApiKeysListResponse400 | ApiKeysListResponse401 | ApiKeysListResponse403 | PaginatedAPIKeyList
]:
    """List API keys

     Returns API keys created by the authenticated account. Secret key values are returned only where the
    underlying account policy permits it.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeysListResponse400 | ApiKeysListResponse401 | ApiKeysListResponse403 | PaginatedAPIKeyList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    ApiKeysListResponse400
    | ApiKeysListResponse401
    | ApiKeysListResponse403
    | PaginatedAPIKeyList
    | None
):
    """List API keys

     Returns API keys created by the authenticated account. Secret key values are returned only where the
    underlying account policy permits it.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeysListResponse400 | ApiKeysListResponse401 | ApiKeysListResponse403 | PaginatedAPIKeyList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    ApiKeysListResponse400 | ApiKeysListResponse401 | ApiKeysListResponse403 | PaginatedAPIKeyList
]:
    """List API keys

     Returns API keys created by the authenticated account. Secret key values are returned only where the
    underlying account policy permits it.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeysListResponse400 | ApiKeysListResponse401 | ApiKeysListResponse403 | PaginatedAPIKeyList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    ApiKeysListResponse400
    | ApiKeysListResponse401
    | ApiKeysListResponse403
    | PaginatedAPIKeyList
    | None
):
    """List API keys

     Returns API keys created by the authenticated account. Secret key values are returned only where the
    underlying account policy permits it.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeysListResponse400 | ApiKeysListResponse401 | ApiKeysListResponse403 | PaginatedAPIKeyList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            accept_language=accept_language,
        )
    ).parsed

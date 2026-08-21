from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.news_list_response_400 import NewsListResponse400
from ...models.news_list_response_401 import NewsListResponse401
from ...models.news_list_response_403 import NewsListResponse403
from ...models.paginated_news_list import PaginatedNewsList
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/news",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> NewsListResponse400 | NewsListResponse401 | NewsListResponse403 | PaginatedNewsList | None:
    if response.status_code == 200:
        response_200 = PaginatedNewsList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = NewsListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = NewsListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = NewsListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[NewsListResponse400 | NewsListResponse401 | NewsListResponse403 | PaginatedNewsList]:
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
    ordering: str | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[NewsListResponse400 | NewsListResponse401 | NewsListResponse403 | PaginatedNewsList]:
    """List product announcements

     Returns the latest customer-facing service announcements and product updates, ordered from newest to
    oldest.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NewsListResponse400 | NewsListResponse401 | NewsListResponse403 | PaginatedNewsList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        ordering=ordering,
        search=search,
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
    ordering: str | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> NewsListResponse400 | NewsListResponse401 | NewsListResponse403 | PaginatedNewsList | None:
    """List product announcements

     Returns the latest customer-facing service announcements and product updates, ordered from newest to
    oldest.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NewsListResponse400 | NewsListResponse401 | NewsListResponse403 | PaginatedNewsList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        ordering=ordering,
        search=search,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[NewsListResponse400 | NewsListResponse401 | NewsListResponse403 | PaginatedNewsList]:
    """List product announcements

     Returns the latest customer-facing service announcements and product updates, ordered from newest to
    oldest.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NewsListResponse400 | NewsListResponse401 | NewsListResponse403 | PaginatedNewsList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        ordering=ordering,
        search=search,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> NewsListResponse400 | NewsListResponse401 | NewsListResponse403 | PaginatedNewsList | None:
    """List product announcements

     Returns the latest customer-facing service announcements and product updates, ordered from newest to
    oldest.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NewsListResponse400 | NewsListResponse401 | NewsListResponse403 | PaginatedNewsList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            ordering=ordering,
            search=search,
            accept_language=accept_language,
        )
    ).parsed

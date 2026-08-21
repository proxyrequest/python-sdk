from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_order_list import PaginatedOrderList
from ...models.users_orders_list_response_400 import UsersOrdersListResponse400
from ...models.users_orders_list_response_401 import UsersOrdersListResponse401
from ...models.users_orders_list_response_403 import UsersOrdersListResponse403
from ...models.users_orders_list_response_404 import UsersOrdersListResponse404
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id_path: UUID,
    *,
    email: str | Unset = UNSET,
    id_query: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    username: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["email"] = email

    json_id_query: str | Unset = UNSET
    if not isinstance(id_query, Unset):
        json_id_query = str(id_query)
    params["id"] = json_id_query

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/{id_path}/orders".format(
            id_path=quote(str(id_path), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PaginatedOrderList
    | UsersOrdersListResponse400
    | UsersOrdersListResponse401
    | UsersOrdersListResponse403
    | UsersOrdersListResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedOrderList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UsersOrdersListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UsersOrdersListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsersOrdersListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UsersOrdersListResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PaginatedOrderList
    | UsersOrdersListResponse400
    | UsersOrdersListResponse401
    | UsersOrdersListResponse403
    | UsersOrdersListResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id_path: UUID,
    *,
    client: AuthenticatedClient,
    email: str | Unset = UNSET,
    id_query: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    username: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    PaginatedOrderList
    | UsersOrdersListResponse400
    | UsersOrdersListResponse401
    | UsersOrdersListResponse403
    | UsersOrdersListResponse404
]:
    """List a sub-user's orders

     Returns active package orders allocated to the selected sub-user. This operation is available when
    package-based authentication is enabled.

    Args:
        id_path (UUID):
        email (str | Unset):
        id_query (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        username (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrderList | UsersOrdersListResponse400 | UsersOrdersListResponse401 | UsersOrdersListResponse403 | UsersOrdersListResponse404]
    """

    kwargs = _get_kwargs(
        id_path=id_path,
        email=email,
        id_query=id_query,
        limit=limit,
        offset=offset,
        ordering=ordering,
        username=username,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id_path: UUID,
    *,
    client: AuthenticatedClient,
    email: str | Unset = UNSET,
    id_query: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    username: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    PaginatedOrderList
    | UsersOrdersListResponse400
    | UsersOrdersListResponse401
    | UsersOrdersListResponse403
    | UsersOrdersListResponse404
    | None
):
    """List a sub-user's orders

     Returns active package orders allocated to the selected sub-user. This operation is available when
    package-based authentication is enabled.

    Args:
        id_path (UUID):
        email (str | Unset):
        id_query (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        username (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOrderList | UsersOrdersListResponse400 | UsersOrdersListResponse401 | UsersOrdersListResponse403 | UsersOrdersListResponse404
    """

    return sync_detailed(
        id_path=id_path,
        client=client,
        email=email,
        id_query=id_query,
        limit=limit,
        offset=offset,
        ordering=ordering,
        username=username,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id_path: UUID,
    *,
    client: AuthenticatedClient,
    email: str | Unset = UNSET,
    id_query: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    username: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    PaginatedOrderList
    | UsersOrdersListResponse400
    | UsersOrdersListResponse401
    | UsersOrdersListResponse403
    | UsersOrdersListResponse404
]:
    """List a sub-user's orders

     Returns active package orders allocated to the selected sub-user. This operation is available when
    package-based authentication is enabled.

    Args:
        id_path (UUID):
        email (str | Unset):
        id_query (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        username (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrderList | UsersOrdersListResponse400 | UsersOrdersListResponse401 | UsersOrdersListResponse403 | UsersOrdersListResponse404]
    """

    kwargs = _get_kwargs(
        id_path=id_path,
        email=email,
        id_query=id_query,
        limit=limit,
        offset=offset,
        ordering=ordering,
        username=username,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id_path: UUID,
    *,
    client: AuthenticatedClient,
    email: str | Unset = UNSET,
    id_query: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    username: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    PaginatedOrderList
    | UsersOrdersListResponse400
    | UsersOrdersListResponse401
    | UsersOrdersListResponse403
    | UsersOrdersListResponse404
    | None
):
    """List a sub-user's orders

     Returns active package orders allocated to the selected sub-user. This operation is available when
    package-based authentication is enabled.

    Args:
        id_path (UUID):
        email (str | Unset):
        id_query (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        username (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOrderList | UsersOrdersListResponse400 | UsersOrdersListResponse401 | UsersOrdersListResponse403 | UsersOrdersListResponse404
    """

    return (
        await asyncio_detailed(
            id_path=id_path,
            client=client,
            email=email,
            id_query=id_query,
            limit=limit,
            offset=offset,
            ordering=ordering,
            username=username,
            accept_language=accept_language,
        )
    ).parsed

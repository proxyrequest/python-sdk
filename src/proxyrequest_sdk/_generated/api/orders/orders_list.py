from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.orders_list_package_type import OrdersListPackageType
from ...models.orders_list_response_400 import OrdersListResponse400
from ...models.orders_list_response_401 import OrdersListResponse401
from ...models.orders_list_response_403 import OrdersListResponse403
from ...models.paginated_order_list import PaginatedOrderList
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_alias: str | Unset = UNSET,
    package_id: str | Unset = UNSET,
    package_type: OrdersListPackageType | Unset = UNSET,
    search: str | Unset = UNSET,
    user_email: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params["package__alias"] = package_alias

    params["package__id"] = package_id

    json_package_type: str | Unset = UNSET
    if not isinstance(package_type, Unset):
        json_package_type = package_type.value

    params["package__type"] = json_package_type

    params["search"] = search

    params["user__email"] = user_email

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["user__id"] = json_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/orders",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    OrdersListResponse400
    | OrdersListResponse401
    | OrdersListResponse403
    | PaginatedOrderList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedOrderList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OrdersListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrdersListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrdersListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    OrdersListResponse400 | OrdersListResponse401 | OrdersListResponse403 | PaginatedOrderList
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
    ordering: str | Unset = UNSET,
    package_alias: str | Unset = UNSET,
    package_id: str | Unset = UNSET,
    package_type: OrdersListPackageType | Unset = UNSET,
    search: str | Unset = UNSET,
    user_email: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    OrdersListResponse400 | OrdersListResponse401 | OrdersListResponse403 | PaginatedOrderList
]:
    """List active orders

     Returns active package orders owned by the authenticated account. Filters can narrow the result by
    package or user.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_alias (str | Unset):
        package_id (str | Unset):
        package_type (OrdersListPackageType | Unset):
        search (str | Unset):
        user_email (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersListResponse400 | OrdersListResponse401 | OrdersListResponse403 | PaginatedOrderList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        ordering=ordering,
        package_alias=package_alias,
        package_id=package_id,
        package_type=package_type,
        search=search,
        user_email=user_email,
        user_id=user_id,
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
    package_alias: str | Unset = UNSET,
    package_id: str | Unset = UNSET,
    package_type: OrdersListPackageType | Unset = UNSET,
    search: str | Unset = UNSET,
    user_email: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    OrdersListResponse400
    | OrdersListResponse401
    | OrdersListResponse403
    | PaginatedOrderList
    | None
):
    """List active orders

     Returns active package orders owned by the authenticated account. Filters can narrow the result by
    package or user.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_alias (str | Unset):
        package_id (str | Unset):
        package_type (OrdersListPackageType | Unset):
        search (str | Unset):
        user_email (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersListResponse400 | OrdersListResponse401 | OrdersListResponse403 | PaginatedOrderList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        ordering=ordering,
        package_alias=package_alias,
        package_id=package_id,
        package_type=package_type,
        search=search,
        user_email=user_email,
        user_id=user_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_alias: str | Unset = UNSET,
    package_id: str | Unset = UNSET,
    package_type: OrdersListPackageType | Unset = UNSET,
    search: str | Unset = UNSET,
    user_email: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    OrdersListResponse400 | OrdersListResponse401 | OrdersListResponse403 | PaginatedOrderList
]:
    """List active orders

     Returns active package orders owned by the authenticated account. Filters can narrow the result by
    package or user.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_alias (str | Unset):
        package_id (str | Unset):
        package_type (OrdersListPackageType | Unset):
        search (str | Unset):
        user_email (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersListResponse400 | OrdersListResponse401 | OrdersListResponse403 | PaginatedOrderList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        ordering=ordering,
        package_alias=package_alias,
        package_id=package_id,
        package_type=package_type,
        search=search,
        user_email=user_email,
        user_id=user_id,
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
    package_alias: str | Unset = UNSET,
    package_id: str | Unset = UNSET,
    package_type: OrdersListPackageType | Unset = UNSET,
    search: str | Unset = UNSET,
    user_email: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    OrdersListResponse400
    | OrdersListResponse401
    | OrdersListResponse403
    | PaginatedOrderList
    | None
):
    """List active orders

     Returns active package orders owned by the authenticated account. Filters can narrow the result by
    package or user.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_alias (str | Unset):
        package_id (str | Unset):
        package_type (OrdersListPackageType | Unset):
        search (str | Unset):
        user_email (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersListResponse400 | OrdersListResponse401 | OrdersListResponse403 | PaginatedOrderList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            ordering=ordering,
            package_alias=package_alias,
            package_id=package_id,
            package_type=package_type,
            search=search,
            user_email=user_email,
            user_id=user_id,
            accept_language=accept_language,
        )
    ).parsed

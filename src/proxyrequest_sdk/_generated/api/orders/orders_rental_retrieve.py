from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.orders_rental_retrieve_response_400 import OrdersRentalRetrieveResponse400
from ...models.orders_rental_retrieve_response_401 import OrdersRentalRetrieveResponse401
from ...models.orders_rental_retrieve_response_403 import OrdersRentalRetrieveResponse403
from ...models.orders_rental_retrieve_response_404 import OrdersRentalRetrieveResponse404
from ...models.rental_detail import RentalDetail
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/orders/{id}/rental".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    OrdersRentalRetrieveResponse400
    | OrdersRentalRetrieveResponse401
    | OrdersRentalRetrieveResponse403
    | OrdersRentalRetrieveResponse404
    | RentalDetail
    | None
):
    if response.status_code == 200:
        response_200 = RentalDetail.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OrdersRentalRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrdersRentalRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrdersRentalRetrieveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = OrdersRentalRetrieveResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    OrdersRentalRetrieveResponse400
    | OrdersRentalRetrieveResponse401
    | OrdersRentalRetrieveResponse403
    | OrdersRentalRetrieveResponse404
    | RentalDetail
]:
    parsed = parse_response(_parse_response, client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    OrdersRentalRetrieveResponse400
    | OrdersRentalRetrieveResponse401
    | OrdersRentalRetrieveResponse403
    | OrdersRentalRetrieveResponse404
    | RentalDetail
]:
    """Read order rental

     Read owned IPs, paid rental periods and invoice history. Pagination applies to IPs. Integration keys
    must also have the credentials scope to receive secrets.

    Args:
        id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersRentalRetrieveResponse400 | OrdersRentalRetrieveResponse401 | OrdersRentalRetrieveResponse403 | OrdersRentalRetrieveResponse404 | RentalDetail]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    OrdersRentalRetrieveResponse400
    | OrdersRentalRetrieveResponse401
    | OrdersRentalRetrieveResponse403
    | OrdersRentalRetrieveResponse404
    | RentalDetail
    | None
):
    """Read order rental

     Read owned IPs, paid rental periods and invoice history. Pagination applies to IPs. Integration keys
    must also have the credentials scope to receive secrets.

    Args:
        id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersRentalRetrieveResponse400 | OrdersRentalRetrieveResponse401 | OrdersRentalRetrieveResponse403 | OrdersRentalRetrieveResponse404 | RentalDetail
    """

    return sync_detailed(
        id=id,
        client=client,
        limit=limit,
        offset=offset,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    OrdersRentalRetrieveResponse400
    | OrdersRentalRetrieveResponse401
    | OrdersRentalRetrieveResponse403
    | OrdersRentalRetrieveResponse404
    | RentalDetail
]:
    """Read order rental

     Read owned IPs, paid rental periods and invoice history. Pagination applies to IPs. Integration keys
    must also have the credentials scope to receive secrets.

    Args:
        id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersRentalRetrieveResponse400 | OrdersRentalRetrieveResponse401 | OrdersRentalRetrieveResponse403 | OrdersRentalRetrieveResponse404 | RentalDetail]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    OrdersRentalRetrieveResponse400
    | OrdersRentalRetrieveResponse401
    | OrdersRentalRetrieveResponse403
    | OrdersRentalRetrieveResponse404
    | RentalDetail
    | None
):
    """Read order rental

     Read owned IPs, paid rental periods and invoice history. Pagination applies to IPs. Integration keys
    must also have the credentials scope to receive secrets.

    Args:
        id (UUID):
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersRentalRetrieveResponse400 | OrdersRentalRetrieveResponse401 | OrdersRentalRetrieveResponse403 | OrdersRentalRetrieveResponse404 | RentalDetail
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            limit=limit,
            offset=offset,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

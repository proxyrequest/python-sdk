from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.coupons_list_response_400 import CouponsListResponse400
from ...models.coupons_list_response_401 import CouponsListResponse401
from ...models.coupons_list_response_403 import CouponsListResponse403
from ...models.coupons_list_type import CouponsListType
from ...models.paginated_coupon_short_list import PaginatedCouponShortList
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    search: str | Unset = UNSET,
    type_: CouponsListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["code"] = code

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params["search"] = search

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/coupons",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CouponsListResponse400
    | CouponsListResponse401
    | CouponsListResponse403
    | PaginatedCouponShortList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedCouponShortList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CouponsListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CouponsListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CouponsListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CouponsListResponse400
    | CouponsListResponse401
    | CouponsListResponse403
    | PaginatedCouponShortList
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
    code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    search: str | Unset = UNSET,
    type_: CouponsListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    CouponsListResponse400
    | CouponsListResponse401
    | CouponsListResponse403
    | PaginatedCouponShortList
]:
    """List available coupons

     Returns coupons visible to the authenticated account. Staff accounts receive administrative fields;
    customers receive the public coupon view.

    Args:
        code (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        search (str | Unset):
        type_ (CouponsListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CouponsListResponse400 | CouponsListResponse401 | CouponsListResponse403 | PaginatedCouponShortList]
    """

    kwargs = _get_kwargs(
        code=code,
        limit=limit,
        offset=offset,
        ordering=ordering,
        search=search,
        type_=type_,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    search: str | Unset = UNSET,
    type_: CouponsListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    CouponsListResponse400
    | CouponsListResponse401
    | CouponsListResponse403
    | PaginatedCouponShortList
    | None
):
    """List available coupons

     Returns coupons visible to the authenticated account. Staff accounts receive administrative fields;
    customers receive the public coupon view.

    Args:
        code (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        search (str | Unset):
        type_ (CouponsListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CouponsListResponse400 | CouponsListResponse401 | CouponsListResponse403 | PaginatedCouponShortList
    """

    return sync_detailed(
        client=client,
        code=code,
        limit=limit,
        offset=offset,
        ordering=ordering,
        search=search,
        type_=type_,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    search: str | Unset = UNSET,
    type_: CouponsListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    CouponsListResponse400
    | CouponsListResponse401
    | CouponsListResponse403
    | PaginatedCouponShortList
]:
    """List available coupons

     Returns coupons visible to the authenticated account. Staff accounts receive administrative fields;
    customers receive the public coupon view.

    Args:
        code (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        search (str | Unset):
        type_ (CouponsListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CouponsListResponse400 | CouponsListResponse401 | CouponsListResponse403 | PaginatedCouponShortList]
    """

    kwargs = _get_kwargs(
        code=code,
        limit=limit,
        offset=offset,
        ordering=ordering,
        search=search,
        type_=type_,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    search: str | Unset = UNSET,
    type_: CouponsListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    CouponsListResponse400
    | CouponsListResponse401
    | CouponsListResponse403
    | PaginatedCouponShortList
    | None
):
    """List available coupons

     Returns coupons visible to the authenticated account. Staff accounts receive administrative fields;
    customers receive the public coupon view.

    Args:
        code (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        search (str | Unset):
        type_ (CouponsListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CouponsListResponse400 | CouponsListResponse401 | CouponsListResponse403 | PaginatedCouponShortList
    """

    return (
        await asyncio_detailed(
            client=client,
            code=code,
            limit=limit,
            offset=offset,
            ordering=ordering,
            search=search,
            type_=type_,
            accept_language=accept_language,
        )
    ).parsed

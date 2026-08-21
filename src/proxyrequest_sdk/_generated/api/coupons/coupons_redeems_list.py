from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.coupons_redeems_list_response_400 import CouponsRedeemsListResponse400
from ...models.coupons_redeems_list_response_401 import CouponsRedeemsListResponse401
from ...models.coupons_redeems_list_response_403 import CouponsRedeemsListResponse403
from ...models.coupons_redeems_list_response_404 import CouponsRedeemsListResponse404
from ...models.coupons_redeems_list_type import CouponsRedeemsListType
from ...models.paginated_coupon_redeem_list import PaginatedCouponRedeemList
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    id: str,
    *,
    code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    type_: CouponsRedeemsListType | Unset = UNSET,
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

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/coupons/{id}/redeems".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CouponsRedeemsListResponse400
    | CouponsRedeemsListResponse401
    | CouponsRedeemsListResponse403
    | CouponsRedeemsListResponse404
    | PaginatedCouponRedeemList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedCouponRedeemList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CouponsRedeemsListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CouponsRedeemsListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CouponsRedeemsListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CouponsRedeemsListResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CouponsRedeemsListResponse400
    | CouponsRedeemsListResponse401
    | CouponsRedeemsListResponse403
    | CouponsRedeemsListResponse404
    | PaginatedCouponRedeemList
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    type_: CouponsRedeemsListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    CouponsRedeemsListResponse400
    | CouponsRedeemsListResponse401
    | CouponsRedeemsListResponse403
    | CouponsRedeemsListResponse404
    | PaginatedCouponRedeemList
]:
    """List coupon redemptions

     Returns accounts and invoices that redeemed the selected coupon.

    Args:
        id (str):
        code (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        type_ (CouponsRedeemsListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CouponsRedeemsListResponse400 | CouponsRedeemsListResponse401 | CouponsRedeemsListResponse403 | CouponsRedeemsListResponse404 | PaginatedCouponRedeemList]
    """

    kwargs = _get_kwargs(
        id=id,
        code=code,
        limit=limit,
        offset=offset,
        ordering=ordering,
        type_=type_,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    type_: CouponsRedeemsListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    CouponsRedeemsListResponse400
    | CouponsRedeemsListResponse401
    | CouponsRedeemsListResponse403
    | CouponsRedeemsListResponse404
    | PaginatedCouponRedeemList
    | None
):
    """List coupon redemptions

     Returns accounts and invoices that redeemed the selected coupon.

    Args:
        id (str):
        code (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        type_ (CouponsRedeemsListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CouponsRedeemsListResponse400 | CouponsRedeemsListResponse401 | CouponsRedeemsListResponse403 | CouponsRedeemsListResponse404 | PaginatedCouponRedeemList
    """

    return sync_detailed(
        id=id,
        client=client,
        code=code,
        limit=limit,
        offset=offset,
        ordering=ordering,
        type_=type_,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    type_: CouponsRedeemsListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    CouponsRedeemsListResponse400
    | CouponsRedeemsListResponse401
    | CouponsRedeemsListResponse403
    | CouponsRedeemsListResponse404
    | PaginatedCouponRedeemList
]:
    """List coupon redemptions

     Returns accounts and invoices that redeemed the selected coupon.

    Args:
        id (str):
        code (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        type_ (CouponsRedeemsListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CouponsRedeemsListResponse400 | CouponsRedeemsListResponse401 | CouponsRedeemsListResponse403 | CouponsRedeemsListResponse404 | PaginatedCouponRedeemList]
    """

    kwargs = _get_kwargs(
        id=id,
        code=code,
        limit=limit,
        offset=offset,
        ordering=ordering,
        type_=type_,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    type_: CouponsRedeemsListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    CouponsRedeemsListResponse400
    | CouponsRedeemsListResponse401
    | CouponsRedeemsListResponse403
    | CouponsRedeemsListResponse404
    | PaginatedCouponRedeemList
    | None
):
    """List coupon redemptions

     Returns accounts and invoices that redeemed the selected coupon.

    Args:
        id (str):
        code (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        type_ (CouponsRedeemsListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CouponsRedeemsListResponse400 | CouponsRedeemsListResponse401 | CouponsRedeemsListResponse403 | CouponsRedeemsListResponse404 | PaginatedCouponRedeemList
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            code=code,
            limit=limit,
            offset=offset,
            ordering=ordering,
            type_=type_,
            accept_language=accept_language,
        )
    ).parsed

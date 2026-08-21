from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.coupon import Coupon
from ...models.coupons_partial_update_response_400 import CouponsPartialUpdateResponse400
from ...models.coupons_partial_update_response_401 import CouponsPartialUpdateResponse401
from ...models.coupons_partial_update_response_403 import CouponsPartialUpdateResponse403
from ...models.coupons_partial_update_response_404 import CouponsPartialUpdateResponse404
from ...models.patched_coupon_update_request import PatchedCouponUpdateRequest
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    id: str,
    *,
    body: PatchedCouponUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/coupons/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Coupon
    | CouponsPartialUpdateResponse400
    | CouponsPartialUpdateResponse401
    | CouponsPartialUpdateResponse403
    | CouponsPartialUpdateResponse404
    | None
):
    if response.status_code == 200:
        response_200 = Coupon.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CouponsPartialUpdateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CouponsPartialUpdateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CouponsPartialUpdateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CouponsPartialUpdateResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Coupon
    | CouponsPartialUpdateResponse400
    | CouponsPartialUpdateResponse401
    | CouponsPartialUpdateResponse403
    | CouponsPartialUpdateResponse404
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
    body: PatchedCouponUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Coupon
    | CouponsPartialUpdateResponse400
    | CouponsPartialUpdateResponse401
    | CouponsPartialUpdateResponse403
    | CouponsPartialUpdateResponse404
]:
    """Update a coupon

     Updates selected coupon fields. Staff access is required.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedCouponUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Coupon | CouponsPartialUpdateResponse400 | CouponsPartialUpdateResponse401 | CouponsPartialUpdateResponse403 | CouponsPartialUpdateResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
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
    body: PatchedCouponUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Coupon
    | CouponsPartialUpdateResponse400
    | CouponsPartialUpdateResponse401
    | CouponsPartialUpdateResponse403
    | CouponsPartialUpdateResponse404
    | None
):
    """Update a coupon

     Updates selected coupon fields. Staff access is required.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedCouponUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Coupon | CouponsPartialUpdateResponse400 | CouponsPartialUpdateResponse401 | CouponsPartialUpdateResponse403 | CouponsPartialUpdateResponse404
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedCouponUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Coupon
    | CouponsPartialUpdateResponse400
    | CouponsPartialUpdateResponse401
    | CouponsPartialUpdateResponse403
    | CouponsPartialUpdateResponse404
]:
    """Update a coupon

     Updates selected coupon fields. Staff access is required.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedCouponUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Coupon | CouponsPartialUpdateResponse400 | CouponsPartialUpdateResponse401 | CouponsPartialUpdateResponse403 | CouponsPartialUpdateResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedCouponUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Coupon
    | CouponsPartialUpdateResponse400
    | CouponsPartialUpdateResponse401
    | CouponsPartialUpdateResponse403
    | CouponsPartialUpdateResponse404
    | None
):
    """Update a coupon

     Updates selected coupon fields. Staff access is required.

    Args:
        id (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedCouponUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Coupon | CouponsPartialUpdateResponse400 | CouponsPartialUpdateResponse401 | CouponsPartialUpdateResponse403 | CouponsPartialUpdateResponse404
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed

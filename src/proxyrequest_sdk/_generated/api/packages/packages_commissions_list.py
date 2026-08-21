from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.packages_commissions_list_pricing_unit import PackagesCommissionsListPricingUnit
from ...models.packages_commissions_list_response_400 import PackagesCommissionsListResponse400
from ...models.packages_commissions_list_response_401 import PackagesCommissionsListResponse401
from ...models.packages_commissions_list_response_403 import PackagesCommissionsListResponse403
from ...models.packages_commissions_list_type import PackagesCommissionsListType
from ...models.paginated_package_commission_list import PaginatedPackageCommissionList
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    alias: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    pricing_unit: PackagesCommissionsListPricingUnit | Unset = UNSET,
    type_: PackagesCommissionsListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["alias"] = alias

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    json_pricing_unit: str | Unset = UNSET
    if not isinstance(pricing_unit, Unset):
        json_pricing_unit = pricing_unit.value

    params["pricing_unit"] = json_pricing_unit

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/packages/commissions",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PackagesCommissionsListResponse400
    | PackagesCommissionsListResponse401
    | PackagesCommissionsListResponse403
    | PaginatedPackageCommissionList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedPackageCommissionList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PackagesCommissionsListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PackagesCommissionsListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PackagesCommissionsListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PackagesCommissionsListResponse400
    | PackagesCommissionsListResponse401
    | PackagesCommissionsListResponse403
    | PaginatedPackageCommissionList
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
    alias: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    pricing_unit: PackagesCommissionsListPricingUnit | Unset = UNSET,
    type_: PackagesCommissionsListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    PackagesCommissionsListResponse400
    | PackagesCommissionsListResponse401
    | PackagesCommissionsListResponse403
    | PaginatedPackageCommissionList
]:
    """List affiliate package commissions

     Returns commission rates, paid earnings, pending earnings, and referred order totals for each
    package visible to an approved marketer.

    Args:
        alias (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        pricing_unit (PackagesCommissionsListPricingUnit | Unset):
        type_ (PackagesCommissionsListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PackagesCommissionsListResponse400 | PackagesCommissionsListResponse401 | PackagesCommissionsListResponse403 | PaginatedPackageCommissionList]
    """

    kwargs = _get_kwargs(
        alias=alias,
        limit=limit,
        offset=offset,
        ordering=ordering,
        pricing_unit=pricing_unit,
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
    alias: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    pricing_unit: PackagesCommissionsListPricingUnit | Unset = UNSET,
    type_: PackagesCommissionsListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    PackagesCommissionsListResponse400
    | PackagesCommissionsListResponse401
    | PackagesCommissionsListResponse403
    | PaginatedPackageCommissionList
    | None
):
    """List affiliate package commissions

     Returns commission rates, paid earnings, pending earnings, and referred order totals for each
    package visible to an approved marketer.

    Args:
        alias (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        pricing_unit (PackagesCommissionsListPricingUnit | Unset):
        type_ (PackagesCommissionsListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PackagesCommissionsListResponse400 | PackagesCommissionsListResponse401 | PackagesCommissionsListResponse403 | PaginatedPackageCommissionList
    """

    return sync_detailed(
        client=client,
        alias=alias,
        limit=limit,
        offset=offset,
        ordering=ordering,
        pricing_unit=pricing_unit,
        type_=type_,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    alias: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    pricing_unit: PackagesCommissionsListPricingUnit | Unset = UNSET,
    type_: PackagesCommissionsListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    PackagesCommissionsListResponse400
    | PackagesCommissionsListResponse401
    | PackagesCommissionsListResponse403
    | PaginatedPackageCommissionList
]:
    """List affiliate package commissions

     Returns commission rates, paid earnings, pending earnings, and referred order totals for each
    package visible to an approved marketer.

    Args:
        alias (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        pricing_unit (PackagesCommissionsListPricingUnit | Unset):
        type_ (PackagesCommissionsListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PackagesCommissionsListResponse400 | PackagesCommissionsListResponse401 | PackagesCommissionsListResponse403 | PaginatedPackageCommissionList]
    """

    kwargs = _get_kwargs(
        alias=alias,
        limit=limit,
        offset=offset,
        ordering=ordering,
        pricing_unit=pricing_unit,
        type_=type_,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    alias: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    pricing_unit: PackagesCommissionsListPricingUnit | Unset = UNSET,
    type_: PackagesCommissionsListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    PackagesCommissionsListResponse400
    | PackagesCommissionsListResponse401
    | PackagesCommissionsListResponse403
    | PaginatedPackageCommissionList
    | None
):
    """List affiliate package commissions

     Returns commission rates, paid earnings, pending earnings, and referred order totals for each
    package visible to an approved marketer.

    Args:
        alias (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        pricing_unit (PackagesCommissionsListPricingUnit | Unset):
        type_ (PackagesCommissionsListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PackagesCommissionsListResponse400 | PackagesCommissionsListResponse401 | PackagesCommissionsListResponse403 | PaginatedPackageCommissionList
    """

    return (
        await asyncio_detailed(
            client=client,
            alias=alias,
            limit=limit,
            offset=offset,
            ordering=ordering,
            pricing_unit=pricing_unit,
            type_=type_,
            accept_language=accept_language,
        )
    ).parsed

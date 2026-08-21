from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.packages_list_pricing_unit import PackagesListPricingUnit
from ...models.packages_list_response_400 import PackagesListResponse400
from ...models.packages_list_response_401 import PackagesListResponse401
from ...models.packages_list_response_403 import PackagesListResponse403
from ...models.packages_list_type import PackagesListType
from ...models.paginated_package_list import PaginatedPackageList
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    alias: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    pricing_unit: PackagesListPricingUnit | Unset = UNSET,
    search: str | Unset = UNSET,
    type_: PackagesListType | Unset = UNSET,
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

    params["search"] = search

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/packages",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PackagesListResponse400
    | PackagesListResponse401
    | PackagesListResponse403
    | PaginatedPackageList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedPackageList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PackagesListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PackagesListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PackagesListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PackagesListResponse400
    | PackagesListResponse401
    | PackagesListResponse403
    | PaginatedPackageList
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
    pricing_unit: PackagesListPricingUnit | Unset = UNSET,
    search: str | Unset = UNSET,
    type_: PackagesListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    PackagesListResponse400
    | PackagesListResponse401
    | PackagesListResponse403
    | PaginatedPackageList
]:
    """List available proxy packages

     Returns public packages and private packages already assigned to the authenticated account,
    including pricing and targeting capabilities.

    Args:
        alias (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        pricing_unit (PackagesListPricingUnit | Unset):
        search (str | Unset):
        type_ (PackagesListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PackagesListResponse400 | PackagesListResponse401 | PackagesListResponse403 | PaginatedPackageList]
    """

    kwargs = _get_kwargs(
        alias=alias,
        limit=limit,
        offset=offset,
        ordering=ordering,
        pricing_unit=pricing_unit,
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
    alias: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    pricing_unit: PackagesListPricingUnit | Unset = UNSET,
    search: str | Unset = UNSET,
    type_: PackagesListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    PackagesListResponse400
    | PackagesListResponse401
    | PackagesListResponse403
    | PaginatedPackageList
    | None
):
    """List available proxy packages

     Returns public packages and private packages already assigned to the authenticated account,
    including pricing and targeting capabilities.

    Args:
        alias (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        pricing_unit (PackagesListPricingUnit | Unset):
        search (str | Unset):
        type_ (PackagesListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PackagesListResponse400 | PackagesListResponse401 | PackagesListResponse403 | PaginatedPackageList
    """

    return sync_detailed(
        client=client,
        alias=alias,
        limit=limit,
        offset=offset,
        ordering=ordering,
        pricing_unit=pricing_unit,
        search=search,
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
    pricing_unit: PackagesListPricingUnit | Unset = UNSET,
    search: str | Unset = UNSET,
    type_: PackagesListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    PackagesListResponse400
    | PackagesListResponse401
    | PackagesListResponse403
    | PaginatedPackageList
]:
    """List available proxy packages

     Returns public packages and private packages already assigned to the authenticated account,
    including pricing and targeting capabilities.

    Args:
        alias (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        pricing_unit (PackagesListPricingUnit | Unset):
        search (str | Unset):
        type_ (PackagesListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PackagesListResponse400 | PackagesListResponse401 | PackagesListResponse403 | PaginatedPackageList]
    """

    kwargs = _get_kwargs(
        alias=alias,
        limit=limit,
        offset=offset,
        ordering=ordering,
        pricing_unit=pricing_unit,
        search=search,
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
    pricing_unit: PackagesListPricingUnit | Unset = UNSET,
    search: str | Unset = UNSET,
    type_: PackagesListType | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    PackagesListResponse400
    | PackagesListResponse401
    | PackagesListResponse403
    | PaginatedPackageList
    | None
):
    """List available proxy packages

     Returns public packages and private packages already assigned to the authenticated account,
    including pricing and targeting capabilities.

    Args:
        alias (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        pricing_unit (PackagesListPricingUnit | Unset):
        search (str | Unset):
        type_ (PackagesListType | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PackagesListResponse400 | PackagesListResponse401 | PackagesListResponse403 | PaginatedPackageList
    """

    return (
        await asyncio_detailed(
            client=client,
            alias=alias,
            limit=limit,
            offset=offset,
            ordering=ordering,
            pricing_unit=pricing_unit,
            search=search,
            type_=type_,
            accept_language=accept_language,
        )
    ).parsed

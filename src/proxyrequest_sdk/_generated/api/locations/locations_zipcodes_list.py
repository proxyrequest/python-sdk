from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.locations_zipcodes_list_response_400 import LocationsZipcodesListResponse400
from ...models.locations_zipcodes_list_response_401 import LocationsZipcodesListResponse401
from ...models.locations_zipcodes_list_response_403 import LocationsZipcodesListResponse403
from ...models.locations_zipcodes_list_response_503 import LocationsZipcodesListResponse503
from ...models.paginated_postal_list import PaginatedPostalList
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    *,
    asn_code: str | Unset = UNSET,
    city_code: str | Unset = UNSET,
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    isp_code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    max_count: int | Unset = UNSET,
    min_count: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID,
    region_code: str | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    params: dict[str, Any] = {}

    params["asn__code"] = asn_code

    params["city__code"] = city_code

    params["code"] = code

    params["country__code"] = country_code

    params["isp__code"] = isp_code

    params["limit"] = limit

    params["max_count"] = max_count

    params["min_count"] = min_count

    params["offset"] = offset

    params["ordering"] = ordering

    json_package_id = str(package_id)
    params["package_id"] = json_package_id

    params["region__code"] = region_code

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/locations/zipcodes",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LocationsZipcodesListResponse400
    | LocationsZipcodesListResponse401
    | LocationsZipcodesListResponse403
    | LocationsZipcodesListResponse503
    | PaginatedPostalList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedPostalList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LocationsZipcodesListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = LocationsZipcodesListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = LocationsZipcodesListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 503:
        response_503 = LocationsZipcodesListResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LocationsZipcodesListResponse400
    | LocationsZipcodesListResponse401
    | LocationsZipcodesListResponse403
    | LocationsZipcodesListResponse503
    | PaginatedPostalList
]:
    parsed = parse_response(_parse_response, client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    asn_code: str | Unset = UNSET,
    city_code: str | Unset = UNSET,
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    isp_code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    max_count: int | Unset = UNSET,
    min_count: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID,
    region_code: str | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    LocationsZipcodesListResponse400
    | LocationsZipcodesListResponse401
    | LocationsZipcodesListResponse403
    | LocationsZipcodesListResponse503
    | PaginatedPostalList
]:
    """List available ZIP codes

     Returns active ZIP codes observed in the selected package provider dictionaries. All geographic and
    network filters intersect actual provider combinations. Counts are dictionary node counts, not live
    health.

    Args:
        asn_code (str | Unset):
        city_code (str | Unset):
        code (str | Unset):
        country_code (str | Unset):
        isp_code (str | Unset):
        limit (int | Unset):
        max_count (int | Unset):
        min_count (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID):
        region_code (str | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LocationsZipcodesListResponse400 | LocationsZipcodesListResponse401 | LocationsZipcodesListResponse403 | LocationsZipcodesListResponse503 | PaginatedPostalList]
    """

    kwargs = _get_kwargs(
        asn_code=asn_code,
        city_code=city_code,
        code=code,
        country_code=country_code,
        isp_code=isp_code,
        limit=limit,
        max_count=max_count,
        min_count=min_count,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        region_code=region_code,
        search=search,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    asn_code: str | Unset = UNSET,
    city_code: str | Unset = UNSET,
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    isp_code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    max_count: int | Unset = UNSET,
    min_count: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID,
    region_code: str | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    LocationsZipcodesListResponse400
    | LocationsZipcodesListResponse401
    | LocationsZipcodesListResponse403
    | LocationsZipcodesListResponse503
    | PaginatedPostalList
    | None
):
    """List available ZIP codes

     Returns active ZIP codes observed in the selected package provider dictionaries. All geographic and
    network filters intersect actual provider combinations. Counts are dictionary node counts, not live
    health.

    Args:
        asn_code (str | Unset):
        city_code (str | Unset):
        code (str | Unset):
        country_code (str | Unset):
        isp_code (str | Unset):
        limit (int | Unset):
        max_count (int | Unset):
        min_count (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID):
        region_code (str | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LocationsZipcodesListResponse400 | LocationsZipcodesListResponse401 | LocationsZipcodesListResponse403 | LocationsZipcodesListResponse503 | PaginatedPostalList
    """

    return sync_detailed(
        client=client,
        asn_code=asn_code,
        city_code=city_code,
        code=code,
        country_code=country_code,
        isp_code=isp_code,
        limit=limit,
        max_count=max_count,
        min_count=min_count,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        region_code=region_code,
        search=search,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    asn_code: str | Unset = UNSET,
    city_code: str | Unset = UNSET,
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    isp_code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    max_count: int | Unset = UNSET,
    min_count: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID,
    region_code: str | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    LocationsZipcodesListResponse400
    | LocationsZipcodesListResponse401
    | LocationsZipcodesListResponse403
    | LocationsZipcodesListResponse503
    | PaginatedPostalList
]:
    """List available ZIP codes

     Returns active ZIP codes observed in the selected package provider dictionaries. All geographic and
    network filters intersect actual provider combinations. Counts are dictionary node counts, not live
    health.

    Args:
        asn_code (str | Unset):
        city_code (str | Unset):
        code (str | Unset):
        country_code (str | Unset):
        isp_code (str | Unset):
        limit (int | Unset):
        max_count (int | Unset):
        min_count (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID):
        region_code (str | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LocationsZipcodesListResponse400 | LocationsZipcodesListResponse401 | LocationsZipcodesListResponse403 | LocationsZipcodesListResponse503 | PaginatedPostalList]
    """

    kwargs = _get_kwargs(
        asn_code=asn_code,
        city_code=city_code,
        code=code,
        country_code=country_code,
        isp_code=isp_code,
        limit=limit,
        max_count=max_count,
        min_count=min_count,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        region_code=region_code,
        search=search,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    asn_code: str | Unset = UNSET,
    city_code: str | Unset = UNSET,
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    isp_code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    max_count: int | Unset = UNSET,
    min_count: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID,
    region_code: str | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    LocationsZipcodesListResponse400
    | LocationsZipcodesListResponse401
    | LocationsZipcodesListResponse403
    | LocationsZipcodesListResponse503
    | PaginatedPostalList
    | None
):
    """List available ZIP codes

     Returns active ZIP codes observed in the selected package provider dictionaries. All geographic and
    network filters intersect actual provider combinations. Counts are dictionary node counts, not live
    health.

    Args:
        asn_code (str | Unset):
        city_code (str | Unset):
        code (str | Unset):
        country_code (str | Unset):
        isp_code (str | Unset):
        limit (int | Unset):
        max_count (int | Unset):
        min_count (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID):
        region_code (str | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LocationsZipcodesListResponse400 | LocationsZipcodesListResponse401 | LocationsZipcodesListResponse403 | LocationsZipcodesListResponse503 | PaginatedPostalList
    """

    return (
        await asyncio_detailed(
            client=client,
            asn_code=asn_code,
            city_code=city_code,
            code=code,
            country_code=country_code,
            isp_code=isp_code,
            limit=limit,
            max_count=max_count,
            min_count=min_count,
            offset=offset,
            ordering=ordering,
            package_id=package_id,
            region_code=region_code,
            search=search,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

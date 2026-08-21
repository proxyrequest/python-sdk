from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.locations_cities_list_response_400 import LocationsCitiesListResponse400
from ...models.locations_cities_list_response_401 import LocationsCitiesListResponse401
from ...models.locations_cities_list_response_403 import LocationsCitiesListResponse403
from ...models.paginated_city_list import PaginatedCityList
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    *,
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    region_code: str | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["code"] = code

    params["country__code"] = country_code

    params["limit"] = limit

    params["name"] = name

    params["offset"] = offset

    params["ordering"] = ordering

    json_package_id: str | Unset = UNSET
    if not isinstance(package_id, Unset):
        json_package_id = str(package_id)
    params["package_id"] = json_package_id

    params["region__code"] = region_code

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/locations/cities",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LocationsCitiesListResponse400
    | LocationsCitiesListResponse401
    | LocationsCitiesListResponse403
    | PaginatedCityList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedCityList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LocationsCitiesListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = LocationsCitiesListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = LocationsCitiesListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LocationsCitiesListResponse400
    | LocationsCitiesListResponse401
    | LocationsCitiesListResponse403
    | PaginatedCityList
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
    country_code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    region_code: str | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    LocationsCitiesListResponse400
    | LocationsCitiesListResponse401
    | LocationsCitiesListResponse403
    | PaginatedCityList
]:
    """List available cities

     Returns cities supported by the selected package, country, and region, including targetable ISPs and
    autonomous system numbers.

    Args:
        code (str | Unset):
        country_code (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID | Unset):
        region_code (str | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LocationsCitiesListResponse400 | LocationsCitiesListResponse401 | LocationsCitiesListResponse403 | PaginatedCityList]
    """

    kwargs = _get_kwargs(
        code=code,
        country_code=country_code,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        region_code=region_code,
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
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    region_code: str | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    LocationsCitiesListResponse400
    | LocationsCitiesListResponse401
    | LocationsCitiesListResponse403
    | PaginatedCityList
    | None
):
    """List available cities

     Returns cities supported by the selected package, country, and region, including targetable ISPs and
    autonomous system numbers.

    Args:
        code (str | Unset):
        country_code (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID | Unset):
        region_code (str | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LocationsCitiesListResponse400 | LocationsCitiesListResponse401 | LocationsCitiesListResponse403 | PaginatedCityList
    """

    return sync_detailed(
        client=client,
        code=code,
        country_code=country_code,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        region_code=region_code,
        search=search,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    region_code: str | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    LocationsCitiesListResponse400
    | LocationsCitiesListResponse401
    | LocationsCitiesListResponse403
    | PaginatedCityList
]:
    """List available cities

     Returns cities supported by the selected package, country, and region, including targetable ISPs and
    autonomous system numbers.

    Args:
        code (str | Unset):
        country_code (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID | Unset):
        region_code (str | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LocationsCitiesListResponse400 | LocationsCitiesListResponse401 | LocationsCitiesListResponse403 | PaginatedCityList]
    """

    kwargs = _get_kwargs(
        code=code,
        country_code=country_code,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        region_code=region_code,
        search=search,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    region_code: str | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    LocationsCitiesListResponse400
    | LocationsCitiesListResponse401
    | LocationsCitiesListResponse403
    | PaginatedCityList
    | None
):
    """List available cities

     Returns cities supported by the selected package, country, and region, including targetable ISPs and
    autonomous system numbers.

    Args:
        code (str | Unset):
        country_code (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID | Unset):
        region_code (str | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LocationsCitiesListResponse400 | LocationsCitiesListResponse401 | LocationsCitiesListResponse403 | PaginatedCityList
    """

    return (
        await asyncio_detailed(
            client=client,
            code=code,
            country_code=country_code,
            limit=limit,
            name=name,
            offset=offset,
            ordering=ordering,
            package_id=package_id,
            region_code=region_code,
            search=search,
            accept_language=accept_language,
        )
    ).parsed

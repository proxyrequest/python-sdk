from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.locations_asn_list_response_400 import LocationsAsnListResponse400
from ...models.locations_asn_list_response_401 import LocationsAsnListResponse401
from ...models.locations_asn_list_response_403 import LocationsAsnListResponse403
from ...models.paginated_location_asn_record_list import PaginatedLocationASNRecordList
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    *,
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    global_: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["code"] = code

    params["country__code"] = country_code

    params["global"] = global_

    params["limit"] = limit

    params["name"] = name

    params["offset"] = offset

    params["ordering"] = ordering

    json_package_id: str | Unset = UNSET
    if not isinstance(package_id, Unset):
        json_package_id = str(package_id)
    params["package_id"] = json_package_id

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/locations/asn",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LocationsAsnListResponse400
    | LocationsAsnListResponse401
    | LocationsAsnListResponse403
    | PaginatedLocationASNRecordList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedLocationASNRecordList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LocationsAsnListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = LocationsAsnListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = LocationsAsnListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LocationsAsnListResponse400
    | LocationsAsnListResponse401
    | LocationsAsnListResponse403
    | PaginatedLocationASNRecordList
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
    global_: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    LocationsAsnListResponse400
    | LocationsAsnListResponse401
    | LocationsAsnListResponse403
    | PaginatedLocationASNRecordList
]:
    """List available autonomous systems

     Returns targetable ASNs for the selected package. Geo-scoped records include the country, region, or
    city where the ASN can be selected.

    Args:
        code (str | Unset):
        country_code (str | Unset):
        global_ (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LocationsAsnListResponse400 | LocationsAsnListResponse401 | LocationsAsnListResponse403 | PaginatedLocationASNRecordList]
    """

    kwargs = _get_kwargs(
        code=code,
        country_code=country_code,
        global_=global_,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
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
    global_: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    LocationsAsnListResponse400
    | LocationsAsnListResponse401
    | LocationsAsnListResponse403
    | PaginatedLocationASNRecordList
    | None
):
    """List available autonomous systems

     Returns targetable ASNs for the selected package. Geo-scoped records include the country, region, or
    city where the ASN can be selected.

    Args:
        code (str | Unset):
        country_code (str | Unset):
        global_ (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LocationsAsnListResponse400 | LocationsAsnListResponse401 | LocationsAsnListResponse403 | PaginatedLocationASNRecordList
    """

    return sync_detailed(
        client=client,
        code=code,
        country_code=country_code,
        global_=global_,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        search=search,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    global_: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    LocationsAsnListResponse400
    | LocationsAsnListResponse401
    | LocationsAsnListResponse403
    | PaginatedLocationASNRecordList
]:
    """List available autonomous systems

     Returns targetable ASNs for the selected package. Geo-scoped records include the country, region, or
    city where the ASN can be selected.

    Args:
        code (str | Unset):
        country_code (str | Unset):
        global_ (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LocationsAsnListResponse400 | LocationsAsnListResponse401 | LocationsAsnListResponse403 | PaginatedLocationASNRecordList]
    """

    kwargs = _get_kwargs(
        code=code,
        country_code=country_code,
        global_=global_,
        limit=limit,
        name=name,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
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
    global_: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    LocationsAsnListResponse400
    | LocationsAsnListResponse401
    | LocationsAsnListResponse403
    | PaginatedLocationASNRecordList
    | None
):
    """List available autonomous systems

     Returns targetable ASNs for the selected package. Geo-scoped records include the country, region, or
    city where the ASN can be selected.

    Args:
        code (str | Unset):
        country_code (str | Unset):
        global_ (bool | Unset):
        limit (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID | Unset):
        search (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LocationsAsnListResponse400 | LocationsAsnListResponse401 | LocationsAsnListResponse403 | PaginatedLocationASNRecordList
    """

    return (
        await asyncio_detailed(
            client=client,
            code=code,
            country_code=country_code,
            global_=global_,
            limit=limit,
            name=name,
            offset=offset,
            ordering=ordering,
            package_id=package_id,
            search=search,
            accept_language=accept_language,
        )
    ).parsed

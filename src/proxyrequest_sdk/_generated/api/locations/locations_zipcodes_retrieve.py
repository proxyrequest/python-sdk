from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.locations_zipcodes_retrieve_response_400 import LocationsZipcodesRetrieveResponse400
from ...models.locations_zipcodes_retrieve_response_401 import LocationsZipcodesRetrieveResponse401
from ...models.locations_zipcodes_retrieve_response_403 import LocationsZipcodesRetrieveResponse403
from ...models.locations_zipcodes_retrieve_response_404 import LocationsZipcodesRetrieveResponse404
from ...models.locations_zipcodes_retrieve_response_503 import LocationsZipcodesRetrieveResponse503
from ...models.postal import Postal
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: str,
    *,
    asn_code: str | Unset = UNSET,
    city_code: str | Unset = UNSET,
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    isp_code: str | Unset = UNSET,
    max_count: int | Unset = UNSET,
    min_count: int | Unset = UNSET,
    package_id: UUID,
    region_code: str | Unset = UNSET,
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

    params["max_count"] = max_count

    params["min_count"] = min_count

    json_package_id = str(package_id)
    params["package_id"] = json_package_id

    params["region__code"] = region_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/locations/zipcodes/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LocationsZipcodesRetrieveResponse400
    | LocationsZipcodesRetrieveResponse401
    | LocationsZipcodesRetrieveResponse403
    | LocationsZipcodesRetrieveResponse404
    | LocationsZipcodesRetrieveResponse503
    | Postal
    | None
):
    if response.status_code == 200:
        response_200 = Postal.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LocationsZipcodesRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = LocationsZipcodesRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = LocationsZipcodesRetrieveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = LocationsZipcodesRetrieveResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 503:
        response_503 = LocationsZipcodesRetrieveResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LocationsZipcodesRetrieveResponse400
    | LocationsZipcodesRetrieveResponse401
    | LocationsZipcodesRetrieveResponse403
    | LocationsZipcodesRetrieveResponse404
    | LocationsZipcodesRetrieveResponse503
    | Postal
]:
    parsed = parse_response(_parse_response, client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    asn_code: str | Unset = UNSET,
    city_code: str | Unset = UNSET,
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    isp_code: str | Unset = UNSET,
    max_count: int | Unset = UNSET,
    min_count: int | Unset = UNSET,
    package_id: UUID,
    region_code: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    LocationsZipcodesRetrieveResponse400
    | LocationsZipcodesRetrieveResponse401
    | LocationsZipcodesRetrieveResponse403
    | LocationsZipcodesRetrieveResponse404
    | LocationsZipcodesRetrieveResponse503
    | Postal
]:
    """Get an available ZIP code

     Returns a ZIP code from the selected package coverage. Unavailable or excluded ZIP codes return 404.

    Args:
        id (str):
        asn_code (str | Unset):
        city_code (str | Unset):
        code (str | Unset):
        country_code (str | Unset):
        isp_code (str | Unset):
        max_count (int | Unset):
        min_count (int | Unset):
        package_id (UUID):
        region_code (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LocationsZipcodesRetrieveResponse400 | LocationsZipcodesRetrieveResponse401 | LocationsZipcodesRetrieveResponse403 | LocationsZipcodesRetrieveResponse404 | LocationsZipcodesRetrieveResponse503 | Postal]
    """

    kwargs = _get_kwargs(
        id=id,
        asn_code=asn_code,
        city_code=city_code,
        code=code,
        country_code=country_code,
        isp_code=isp_code,
        max_count=max_count,
        min_count=min_count,
        package_id=package_id,
        region_code=region_code,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    asn_code: str | Unset = UNSET,
    city_code: str | Unset = UNSET,
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    isp_code: str | Unset = UNSET,
    max_count: int | Unset = UNSET,
    min_count: int | Unset = UNSET,
    package_id: UUID,
    region_code: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    LocationsZipcodesRetrieveResponse400
    | LocationsZipcodesRetrieveResponse401
    | LocationsZipcodesRetrieveResponse403
    | LocationsZipcodesRetrieveResponse404
    | LocationsZipcodesRetrieveResponse503
    | Postal
    | None
):
    """Get an available ZIP code

     Returns a ZIP code from the selected package coverage. Unavailable or excluded ZIP codes return 404.

    Args:
        id (str):
        asn_code (str | Unset):
        city_code (str | Unset):
        code (str | Unset):
        country_code (str | Unset):
        isp_code (str | Unset):
        max_count (int | Unset):
        min_count (int | Unset):
        package_id (UUID):
        region_code (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LocationsZipcodesRetrieveResponse400 | LocationsZipcodesRetrieveResponse401 | LocationsZipcodesRetrieveResponse403 | LocationsZipcodesRetrieveResponse404 | LocationsZipcodesRetrieveResponse503 | Postal
    """

    return sync_detailed(
        id=id,
        client=client,
        asn_code=asn_code,
        city_code=city_code,
        code=code,
        country_code=country_code,
        isp_code=isp_code,
        max_count=max_count,
        min_count=min_count,
        package_id=package_id,
        region_code=region_code,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    asn_code: str | Unset = UNSET,
    city_code: str | Unset = UNSET,
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    isp_code: str | Unset = UNSET,
    max_count: int | Unset = UNSET,
    min_count: int | Unset = UNSET,
    package_id: UUID,
    region_code: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    LocationsZipcodesRetrieveResponse400
    | LocationsZipcodesRetrieveResponse401
    | LocationsZipcodesRetrieveResponse403
    | LocationsZipcodesRetrieveResponse404
    | LocationsZipcodesRetrieveResponse503
    | Postal
]:
    """Get an available ZIP code

     Returns a ZIP code from the selected package coverage. Unavailable or excluded ZIP codes return 404.

    Args:
        id (str):
        asn_code (str | Unset):
        city_code (str | Unset):
        code (str | Unset):
        country_code (str | Unset):
        isp_code (str | Unset):
        max_count (int | Unset):
        min_count (int | Unset):
        package_id (UUID):
        region_code (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LocationsZipcodesRetrieveResponse400 | LocationsZipcodesRetrieveResponse401 | LocationsZipcodesRetrieveResponse403 | LocationsZipcodesRetrieveResponse404 | LocationsZipcodesRetrieveResponse503 | Postal]
    """

    kwargs = _get_kwargs(
        id=id,
        asn_code=asn_code,
        city_code=city_code,
        code=code,
        country_code=country_code,
        isp_code=isp_code,
        max_count=max_count,
        min_count=min_count,
        package_id=package_id,
        region_code=region_code,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    asn_code: str | Unset = UNSET,
    city_code: str | Unset = UNSET,
    code: str | Unset = UNSET,
    country_code: str | Unset = UNSET,
    isp_code: str | Unset = UNSET,
    max_count: int | Unset = UNSET,
    min_count: int | Unset = UNSET,
    package_id: UUID,
    region_code: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    LocationsZipcodesRetrieveResponse400
    | LocationsZipcodesRetrieveResponse401
    | LocationsZipcodesRetrieveResponse403
    | LocationsZipcodesRetrieveResponse404
    | LocationsZipcodesRetrieveResponse503
    | Postal
    | None
):
    """Get an available ZIP code

     Returns a ZIP code from the selected package coverage. Unavailable or excluded ZIP codes return 404.

    Args:
        id (str):
        asn_code (str | Unset):
        city_code (str | Unset):
        code (str | Unset):
        country_code (str | Unset):
        isp_code (str | Unset):
        max_count (int | Unset):
        min_count (int | Unset):
        package_id (UUID):
        region_code (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LocationsZipcodesRetrieveResponse400 | LocationsZipcodesRetrieveResponse401 | LocationsZipcodesRetrieveResponse403 | LocationsZipcodesRetrieveResponse404 | LocationsZipcodesRetrieveResponse503 | Postal
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            asn_code=asn_code,
            city_code=city_code,
            code=code,
            country_code=country_code,
            isp_code=isp_code,
            max_count=max_count,
            min_count=min_count,
            package_id=package_id,
            region_code=region_code,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

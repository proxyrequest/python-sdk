from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.city import City
from ...models.locations_cities_retrieve_response_400 import LocationsCitiesRetrieveResponse400
from ...models.locations_cities_retrieve_response_401 import LocationsCitiesRetrieveResponse401
from ...models.locations_cities_retrieve_response_403 import LocationsCitiesRetrieveResponse403
from ...models.locations_cities_retrieve_response_404 import LocationsCitiesRetrieveResponse404
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: str,
    *,
    include_asns: bool | Unset = UNSET,
    package_id: UUID,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["include_asns"] = include_asns

    json_package_id = str(package_id)
    params["package_id"] = json_package_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/locations/cities/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    City
    | LocationsCitiesRetrieveResponse400
    | LocationsCitiesRetrieveResponse401
    | LocationsCitiesRetrieveResponse403
    | LocationsCitiesRetrieveResponse404
    | None
):
    if response.status_code == 200:
        response_200 = City.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LocationsCitiesRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = LocationsCitiesRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = LocationsCitiesRetrieveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = LocationsCitiesRetrieveResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    City
    | LocationsCitiesRetrieveResponse400
    | LocationsCitiesRetrieveResponse401
    | LocationsCitiesRetrieveResponse403
    | LocationsCitiesRetrieveResponse404
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
    include_asns: bool | Unset = UNSET,
    package_id: UUID,
    accept_language: str | Unset = UNSET,
) -> Response[
    City
    | LocationsCitiesRetrieveResponse400
    | LocationsCitiesRetrieveResponse401
    | LocationsCitiesRetrieveResponse403
    | LocationsCitiesRetrieveResponse404
]:
    """Get a city

     Returns one city and its available network targeting options. The asns field is always present and
    defaults to an empty array. Pass include_asns=true to include available autonomous system numbers.
    This option does not affect the standalone /locations/asn endpoint or the compact proxy-node
    response format.

    Args:
        id (str):
        include_asns (bool | Unset):  Default: False.
        package_id (UUID):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[City | LocationsCitiesRetrieveResponse400 | LocationsCitiesRetrieveResponse401 | LocationsCitiesRetrieveResponse403 | LocationsCitiesRetrieveResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        include_asns=include_asns,
        package_id=package_id,
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
    include_asns: bool | Unset = UNSET,
    package_id: UUID,
    accept_language: str | Unset = UNSET,
) -> (
    City
    | LocationsCitiesRetrieveResponse400
    | LocationsCitiesRetrieveResponse401
    | LocationsCitiesRetrieveResponse403
    | LocationsCitiesRetrieveResponse404
    | None
):
    """Get a city

     Returns one city and its available network targeting options. The asns field is always present and
    defaults to an empty array. Pass include_asns=true to include available autonomous system numbers.
    This option does not affect the standalone /locations/asn endpoint or the compact proxy-node
    response format.

    Args:
        id (str):
        include_asns (bool | Unset):  Default: False.
        package_id (UUID):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        City | LocationsCitiesRetrieveResponse400 | LocationsCitiesRetrieveResponse401 | LocationsCitiesRetrieveResponse403 | LocationsCitiesRetrieveResponse404
    """

    return sync_detailed(
        id=id,
        client=client,
        include_asns=include_asns,
        package_id=package_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    include_asns: bool | Unset = UNSET,
    package_id: UUID,
    accept_language: str | Unset = UNSET,
) -> Response[
    City
    | LocationsCitiesRetrieveResponse400
    | LocationsCitiesRetrieveResponse401
    | LocationsCitiesRetrieveResponse403
    | LocationsCitiesRetrieveResponse404
]:
    """Get a city

     Returns one city and its available network targeting options. The asns field is always present and
    defaults to an empty array. Pass include_asns=true to include available autonomous system numbers.
    This option does not affect the standalone /locations/asn endpoint or the compact proxy-node
    response format.

    Args:
        id (str):
        include_asns (bool | Unset):  Default: False.
        package_id (UUID):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[City | LocationsCitiesRetrieveResponse400 | LocationsCitiesRetrieveResponse401 | LocationsCitiesRetrieveResponse403 | LocationsCitiesRetrieveResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        include_asns=include_asns,
        package_id=package_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    include_asns: bool | Unset = UNSET,
    package_id: UUID,
    accept_language: str | Unset = UNSET,
) -> (
    City
    | LocationsCitiesRetrieveResponse400
    | LocationsCitiesRetrieveResponse401
    | LocationsCitiesRetrieveResponse403
    | LocationsCitiesRetrieveResponse404
    | None
):
    """Get a city

     Returns one city and its available network targeting options. The asns field is always present and
    defaults to an empty array. Pass include_asns=true to include available autonomous system numbers.
    This option does not affect the standalone /locations/asn endpoint or the compact proxy-node
    response format.

    Args:
        id (str):
        include_asns (bool | Unset):  Default: False.
        package_id (UUID):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        City | LocationsCitiesRetrieveResponse400 | LocationsCitiesRetrieveResponse401 | LocationsCitiesRetrieveResponse403 | LocationsCitiesRetrieveResponse404
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include_asns=include_asns,
            package_id=package_id,
            accept_language=accept_language,
        )
    ).parsed

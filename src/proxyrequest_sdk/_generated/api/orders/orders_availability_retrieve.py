from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.availability_response import AvailabilityResponse
from ...models.orders_availability_retrieve_allocation_mode import (
    OrdersAvailabilityRetrieveAllocationMode,
)
from ...models.orders_availability_retrieve_network_class import (
    OrdersAvailabilityRetrieveNetworkClass,
)
from ...models.orders_availability_retrieve_response_400 import (
    OrdersAvailabilityRetrieveResponse400,
)
from ...models.orders_availability_retrieve_response_401 import (
    OrdersAvailabilityRetrieveResponse401,
)
from ...models.orders_availability_retrieve_response_403 import (
    OrdersAvailabilityRetrieveResponse403,
)
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    *,
    allocation_mode: OrdersAvailabilityRetrieveAllocationMode | Unset = UNSET,
    city_id: UUID | Unset = UNSET,
    country_code: str | Unset = UNSET,
    network_class: OrdersAvailabilityRetrieveNetworkClass | Unset = UNSET,
    operator: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    region_id: UUID | Unset = UNSET,
    term_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    params: dict[str, Any] = {}

    json_allocation_mode: str | Unset = UNSET
    if not isinstance(allocation_mode, Unset):
        json_allocation_mode = allocation_mode.value

    params["allocation_mode"] = json_allocation_mode

    json_city_id: str | Unset = UNSET
    if not isinstance(city_id, Unset):
        json_city_id = str(city_id)
    params["city_id"] = json_city_id

    params["country_code"] = country_code

    json_network_class: str | Unset = UNSET
    if not isinstance(network_class, Unset):
        json_network_class = network_class.value

    params["network_class"] = json_network_class

    params["operator"] = operator

    json_package_id: str | Unset = UNSET
    if not isinstance(package_id, Unset):
        json_package_id = str(package_id)
    params["package_id"] = json_package_id

    json_region_id: str | Unset = UNSET
    if not isinstance(region_id, Unset):
        json_region_id = str(region_id)
    params["region_id"] = json_region_id

    json_term_id: str | Unset = UNSET
    if not isinstance(term_id, Unset):
        json_term_id = str(term_id)
    params["term_id"] = json_term_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/orders/availability",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AvailabilityResponse
    | OrdersAvailabilityRetrieveResponse400
    | OrdersAvailabilityRetrieveResponse401
    | OrdersAvailabilityRetrieveResponse403
    | None
):
    if response.status_code == 200:
        response_200 = AvailabilityResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OrdersAvailabilityRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrdersAvailabilityRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrdersAvailabilityRetrieveResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AvailabilityResponse
    | OrdersAvailabilityRetrieveResponse400
    | OrdersAvailabilityRetrieveResponse401
    | OrdersAvailabilityRetrieveResponse403
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
    allocation_mode: OrdersAvailabilityRetrieveAllocationMode | Unset = UNSET,
    city_id: UUID | Unset = UNSET,
    country_code: str | Unset = UNSET,
    network_class: OrdersAvailabilityRetrieveNetworkClass | Unset = UNSET,
    operator: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    region_id: UUID | Unset = UNSET,
    term_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    AvailabilityResponse
    | OrdersAvailabilityRetrieveResponse400
    | OrdersAvailabilityRetrieveResponse401
    | OrdersAvailabilityRetrieveResponse403
]:
    """Available static rental locations

     List visible purchasable packages, rental terms, countries, regions, cities and Mobile operators.
    Filter by package_id and network_class (isp, dc or mobile). Counts deduplicate endpoints and include
    capacity and port constraints; checkout rechecks inventory atomically.

    Args:
        allocation_mode (OrdersAvailabilityRetrieveAllocationMode | Unset):
        city_id (UUID | Unset):
        country_code (str | Unset):
        network_class (OrdersAvailabilityRetrieveNetworkClass | Unset):
        operator (str | Unset):
        package_id (UUID | Unset):
        region_id (UUID | Unset):
        term_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailabilityResponse | OrdersAvailabilityRetrieveResponse400 | OrdersAvailabilityRetrieveResponse401 | OrdersAvailabilityRetrieveResponse403]
    """

    kwargs = _get_kwargs(
        allocation_mode=allocation_mode,
        city_id=city_id,
        country_code=country_code,
        network_class=network_class,
        operator=operator,
        package_id=package_id,
        region_id=region_id,
        term_id=term_id,
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
    allocation_mode: OrdersAvailabilityRetrieveAllocationMode | Unset = UNSET,
    city_id: UUID | Unset = UNSET,
    country_code: str | Unset = UNSET,
    network_class: OrdersAvailabilityRetrieveNetworkClass | Unset = UNSET,
    operator: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    region_id: UUID | Unset = UNSET,
    term_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    AvailabilityResponse
    | OrdersAvailabilityRetrieveResponse400
    | OrdersAvailabilityRetrieveResponse401
    | OrdersAvailabilityRetrieveResponse403
    | None
):
    """Available static rental locations

     List visible purchasable packages, rental terms, countries, regions, cities and Mobile operators.
    Filter by package_id and network_class (isp, dc or mobile). Counts deduplicate endpoints and include
    capacity and port constraints; checkout rechecks inventory atomically.

    Args:
        allocation_mode (OrdersAvailabilityRetrieveAllocationMode | Unset):
        city_id (UUID | Unset):
        country_code (str | Unset):
        network_class (OrdersAvailabilityRetrieveNetworkClass | Unset):
        operator (str | Unset):
        package_id (UUID | Unset):
        region_id (UUID | Unset):
        term_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailabilityResponse | OrdersAvailabilityRetrieveResponse400 | OrdersAvailabilityRetrieveResponse401 | OrdersAvailabilityRetrieveResponse403
    """

    return sync_detailed(
        client=client,
        allocation_mode=allocation_mode,
        city_id=city_id,
        country_code=country_code,
        network_class=network_class,
        operator=operator,
        package_id=package_id,
        region_id=region_id,
        term_id=term_id,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    allocation_mode: OrdersAvailabilityRetrieveAllocationMode | Unset = UNSET,
    city_id: UUID | Unset = UNSET,
    country_code: str | Unset = UNSET,
    network_class: OrdersAvailabilityRetrieveNetworkClass | Unset = UNSET,
    operator: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    region_id: UUID | Unset = UNSET,
    term_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    AvailabilityResponse
    | OrdersAvailabilityRetrieveResponse400
    | OrdersAvailabilityRetrieveResponse401
    | OrdersAvailabilityRetrieveResponse403
]:
    """Available static rental locations

     List visible purchasable packages, rental terms, countries, regions, cities and Mobile operators.
    Filter by package_id and network_class (isp, dc or mobile). Counts deduplicate endpoints and include
    capacity and port constraints; checkout rechecks inventory atomically.

    Args:
        allocation_mode (OrdersAvailabilityRetrieveAllocationMode | Unset):
        city_id (UUID | Unset):
        country_code (str | Unset):
        network_class (OrdersAvailabilityRetrieveNetworkClass | Unset):
        operator (str | Unset):
        package_id (UUID | Unset):
        region_id (UUID | Unset):
        term_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailabilityResponse | OrdersAvailabilityRetrieveResponse400 | OrdersAvailabilityRetrieveResponse401 | OrdersAvailabilityRetrieveResponse403]
    """

    kwargs = _get_kwargs(
        allocation_mode=allocation_mode,
        city_id=city_id,
        country_code=country_code,
        network_class=network_class,
        operator=operator,
        package_id=package_id,
        region_id=region_id,
        term_id=term_id,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    allocation_mode: OrdersAvailabilityRetrieveAllocationMode | Unset = UNSET,
    city_id: UUID | Unset = UNSET,
    country_code: str | Unset = UNSET,
    network_class: OrdersAvailabilityRetrieveNetworkClass | Unset = UNSET,
    operator: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    region_id: UUID | Unset = UNSET,
    term_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    AvailabilityResponse
    | OrdersAvailabilityRetrieveResponse400
    | OrdersAvailabilityRetrieveResponse401
    | OrdersAvailabilityRetrieveResponse403
    | None
):
    """Available static rental locations

     List visible purchasable packages, rental terms, countries, regions, cities and Mobile operators.
    Filter by package_id and network_class (isp, dc or mobile). Counts deduplicate endpoints and include
    capacity and port constraints; checkout rechecks inventory atomically.

    Args:
        allocation_mode (OrdersAvailabilityRetrieveAllocationMode | Unset):
        city_id (UUID | Unset):
        country_code (str | Unset):
        network_class (OrdersAvailabilityRetrieveNetworkClass | Unset):
        operator (str | Unset):
        package_id (UUID | Unset):
        region_id (UUID | Unset):
        term_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailabilityResponse | OrdersAvailabilityRetrieveResponse400 | OrdersAvailabilityRetrieveResponse401 | OrdersAvailabilityRetrieveResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            allocation_mode=allocation_mode,
            city_id=city_id,
            country_code=country_code,
            network_class=network_class,
            operator=operator,
            package_id=package_id,
            region_id=region_id,
            term_id=term_id,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.static_endpoints_throughput_retrieve_response_400 import (
    StaticEndpointsThroughputRetrieveResponse400,
)
from ...models.static_endpoints_throughput_retrieve_response_401 import (
    StaticEndpointsThroughputRetrieveResponse401,
)
from ...models.static_endpoints_throughput_retrieve_response_403 import (
    StaticEndpointsThroughputRetrieveResponse403,
)
from ...models.static_endpoints_throughput_retrieve_response_404 import (
    StaticEndpointsThroughputRetrieveResponse404,
)
from ...models.throughput import Throughput
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/static/endpoints/{id}/throughput".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    StaticEndpointsThroughputRetrieveResponse400
    | StaticEndpointsThroughputRetrieveResponse401
    | StaticEndpointsThroughputRetrieveResponse403
    | StaticEndpointsThroughputRetrieveResponse404
    | Throughput
    | None
):
    if response.status_code == 200:
        response_200 = Throughput.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StaticEndpointsThroughputRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StaticEndpointsThroughputRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = StaticEndpointsThroughputRetrieveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = StaticEndpointsThroughputRetrieveResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    StaticEndpointsThroughputRetrieveResponse400
    | StaticEndpointsThroughputRetrieveResponse401
    | StaticEndpointsThroughputRetrieveResponse403
    | StaticEndpointsThroughputRetrieveResponse404
    | Throughput
]:
    parsed = parse_response(_parse_response, client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    StaticEndpointsThroughputRetrieveResponse400
    | StaticEndpointsThroughputRetrieveResponse401
    | StaticEndpointsThroughputRetrieveResponse403
    | StaticEndpointsThroughputRetrieveResponse404
    | Throughput
]:
    """Read current rental speed

     Read combined live upload/download speed from the short-lived accounting projection. Missing or
    expired observations return available=false and null values; no historical usage quota is tracked.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StaticEndpointsThroughputRetrieveResponse400 | StaticEndpointsThroughputRetrieveResponse401 | StaticEndpointsThroughputRetrieveResponse403 | StaticEndpointsThroughputRetrieveResponse404 | Throughput]
    """

    kwargs = _get_kwargs(
        id=id,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    StaticEndpointsThroughputRetrieveResponse400
    | StaticEndpointsThroughputRetrieveResponse401
    | StaticEndpointsThroughputRetrieveResponse403
    | StaticEndpointsThroughputRetrieveResponse404
    | Throughput
    | None
):
    """Read current rental speed

     Read combined live upload/download speed from the short-lived accounting projection. Missing or
    expired observations return available=false and null values; no historical usage quota is tracked.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StaticEndpointsThroughputRetrieveResponse400 | StaticEndpointsThroughputRetrieveResponse401 | StaticEndpointsThroughputRetrieveResponse403 | StaticEndpointsThroughputRetrieveResponse404 | Throughput
    """

    return sync_detailed(
        id=id,
        client=client,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    StaticEndpointsThroughputRetrieveResponse400
    | StaticEndpointsThroughputRetrieveResponse401
    | StaticEndpointsThroughputRetrieveResponse403
    | StaticEndpointsThroughputRetrieveResponse404
    | Throughput
]:
    """Read current rental speed

     Read combined live upload/download speed from the short-lived accounting projection. Missing or
    expired observations return available=false and null values; no historical usage quota is tracked.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StaticEndpointsThroughputRetrieveResponse400 | StaticEndpointsThroughputRetrieveResponse401 | StaticEndpointsThroughputRetrieveResponse403 | StaticEndpointsThroughputRetrieveResponse404 | Throughput]
    """

    kwargs = _get_kwargs(
        id=id,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    StaticEndpointsThroughputRetrieveResponse400
    | StaticEndpointsThroughputRetrieveResponse401
    | StaticEndpointsThroughputRetrieveResponse403
    | StaticEndpointsThroughputRetrieveResponse404
    | Throughput
    | None
):
    """Read current rental speed

     Read combined live upload/download speed from the short-lived accounting projection. Missing or
    expired observations return available=false and null values; no historical usage quota is tracked.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StaticEndpointsThroughputRetrieveResponse400 | StaticEndpointsThroughputRetrieveResponse401 | StaticEndpointsThroughputRetrieveResponse403 | StaticEndpointsThroughputRetrieveResponse404 | Throughput
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.analytics_connections_retrieve_response_400 import (
    AnalyticsConnectionsRetrieveResponse400,
)
from ...models.analytics_connections_retrieve_response_401 import (
    AnalyticsConnectionsRetrieveResponse401,
)
from ...models.analytics_connections_retrieve_response_403 import (
    AnalyticsConnectionsRetrieveResponse403,
)
from ...models.analytics_connections_retrieve_response_500 import (
    AnalyticsConnectionsRetrieveResponse500,
)
from ...models.connections_response import ConnectionsResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_package_id: str | Unset = UNSET
    if not isinstance(package_id, Unset):
        json_package_id = str(package_id)
    params["package_id"] = json_package_id

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["user_id"] = json_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/connections",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AnalyticsConnectionsRetrieveResponse400
    | AnalyticsConnectionsRetrieveResponse401
    | AnalyticsConnectionsRetrieveResponse403
    | AnalyticsConnectionsRetrieveResponse500
    | ConnectionsResponse
    | None
):
    if response.status_code == 200:
        response_200 = ConnectionsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AnalyticsConnectionsRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AnalyticsConnectionsRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AnalyticsConnectionsRetrieveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = AnalyticsConnectionsRetrieveResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AnalyticsConnectionsRetrieveResponse400
    | AnalyticsConnectionsRetrieveResponse401
    | AnalyticsConnectionsRetrieveResponse403
    | AnalyticsConnectionsRetrieveResponse500
    | ConnectionsResponse
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    AnalyticsConnectionsRetrieveResponse400
    | AnalyticsConnectionsRetrieveResponse401
    | AnalyticsConnectionsRetrieveResponse403
    | AnalyticsConnectionsRetrieveResponse500
    | ConnectionsResponse
]:
    """List active proxy connections

     Returns a paginated snapshot of active connections for the selected user and package scope.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        package_id (UUID | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsConnectionsRetrieveResponse400 | AnalyticsConnectionsRetrieveResponse401 | AnalyticsConnectionsRetrieveResponse403 | AnalyticsConnectionsRetrieveResponse500 | ConnectionsResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        package_id=package_id,
        user_id=user_id,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    AnalyticsConnectionsRetrieveResponse400
    | AnalyticsConnectionsRetrieveResponse401
    | AnalyticsConnectionsRetrieveResponse403
    | AnalyticsConnectionsRetrieveResponse500
    | ConnectionsResponse
    | None
):
    """List active proxy connections

     Returns a paginated snapshot of active connections for the selected user and package scope.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        package_id (UUID | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsConnectionsRetrieveResponse400 | AnalyticsConnectionsRetrieveResponse401 | AnalyticsConnectionsRetrieveResponse403 | AnalyticsConnectionsRetrieveResponse500 | ConnectionsResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        package_id=package_id,
        user_id=user_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    AnalyticsConnectionsRetrieveResponse400
    | AnalyticsConnectionsRetrieveResponse401
    | AnalyticsConnectionsRetrieveResponse403
    | AnalyticsConnectionsRetrieveResponse500
    | ConnectionsResponse
]:
    """List active proxy connections

     Returns a paginated snapshot of active connections for the selected user and package scope.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        package_id (UUID | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsConnectionsRetrieveResponse400 | AnalyticsConnectionsRetrieveResponse401 | AnalyticsConnectionsRetrieveResponse403 | AnalyticsConnectionsRetrieveResponse500 | ConnectionsResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        package_id=package_id,
        user_id=user_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    AnalyticsConnectionsRetrieveResponse400
    | AnalyticsConnectionsRetrieveResponse401
    | AnalyticsConnectionsRetrieveResponse403
    | AnalyticsConnectionsRetrieveResponse500
    | ConnectionsResponse
    | None
):
    """List active proxy connections

     Returns a paginated snapshot of active connections for the selected user and package scope.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        package_id (UUID | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsConnectionsRetrieveResponse400 | AnalyticsConnectionsRetrieveResponse401 | AnalyticsConnectionsRetrieveResponse403 | AnalyticsConnectionsRetrieveResponse500 | ConnectionsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            package_id=package_id,
            user_id=user_id,
            accept_language=accept_language,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.endpoint_page import EndpointPage
from ...models.static_endpoints_list_response_400 import StaticEndpointsListResponse400
from ...models.static_endpoints_list_response_401 import StaticEndpointsListResponse401
from ...models.static_endpoints_list_response_403 import StaticEndpointsListResponse403
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_order_id: str | Unset = UNSET
    if not isinstance(order_id, Unset):
        json_order_id = str(order_id)
    params["order_id"] = json_order_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/static/endpoints",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    EndpointPage
    | StaticEndpointsListResponse400
    | StaticEndpointsListResponse401
    | StaticEndpointsListResponse403
    | None
):
    if response.status_code == 200:
        response_200 = EndpointPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StaticEndpointsListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StaticEndpointsListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = StaticEndpointsListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    EndpointPage
    | StaticEndpointsListResponse400
    | StaticEndpointsListResponse401
    | StaticEndpointsListResponse403
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    EndpointPage
    | StaticEndpointsListResponse400
    | StaticEndpointsListResponse401
    | StaticEndpointsListResponse403
]:
    """List rented addresses

     List only the authenticated customer's endpoints, their connection ports and paid periods.
    Optionally filter by order_id; limit and offset control pagination.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        order_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndpointPage | StaticEndpointsListResponse400 | StaticEndpointsListResponse401 | StaticEndpointsListResponse403]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_id=order_id,
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    EndpointPage
    | StaticEndpointsListResponse400
    | StaticEndpointsListResponse401
    | StaticEndpointsListResponse403
    | None
):
    """List rented addresses

     List only the authenticated customer's endpoints, their connection ports and paid periods.
    Optionally filter by order_id; limit and offset control pagination.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        order_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndpointPage | StaticEndpointsListResponse400 | StaticEndpointsListResponse401 | StaticEndpointsListResponse403
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        order_id=order_id,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    EndpointPage
    | StaticEndpointsListResponse400
    | StaticEndpointsListResponse401
    | StaticEndpointsListResponse403
]:
    """List rented addresses

     List only the authenticated customer's endpoints, their connection ports and paid periods.
    Optionally filter by order_id; limit and offset control pagination.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        order_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndpointPage | StaticEndpointsListResponse400 | StaticEndpointsListResponse401 | StaticEndpointsListResponse403]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_id=order_id,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    order_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    EndpointPage
    | StaticEndpointsListResponse400
    | StaticEndpointsListResponse401
    | StaticEndpointsListResponse403
    | None
):
    """List rented addresses

     List only the authenticated customer's endpoints, their connection ports and paid periods.
    Optionally filter by order_id; limit and offset control pagination.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        order_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndpointPage | StaticEndpointsListResponse400 | StaticEndpointsListResponse401 | StaticEndpointsListResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            order_id=order_id,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

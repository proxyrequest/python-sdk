from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.endpoint import Endpoint
from ...models.patched_endpoint_update_request import PatchedEndpointUpdateRequest
from ...models.static_endpoints_partial_update_response_400 import (
    StaticEndpointsPartialUpdateResponse400,
)
from ...models.static_endpoints_partial_update_response_401 import (
    StaticEndpointsPartialUpdateResponse401,
)
from ...models.static_endpoints_partial_update_response_403 import (
    StaticEndpointsPartialUpdateResponse403,
)
from ...models.static_endpoints_partial_update_response_404 import (
    StaticEndpointsPartialUpdateResponse404,
)
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedEndpointUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/static/endpoints/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Endpoint
    | StaticEndpointsPartialUpdateResponse400
    | StaticEndpointsPartialUpdateResponse401
    | StaticEndpointsPartialUpdateResponse403
    | StaticEndpointsPartialUpdateResponse404
    | None
):
    if response.status_code == 200:
        response_200 = Endpoint.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StaticEndpointsPartialUpdateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StaticEndpointsPartialUpdateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = StaticEndpointsPartialUpdateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = StaticEndpointsPartialUpdateResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Endpoint
    | StaticEndpointsPartialUpdateResponse400
    | StaticEndpointsPartialUpdateResponse401
    | StaticEndpointsPartialUpdateResponse403
    | StaticEndpointsPartialUpdateResponse404
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
    body: PatchedEndpointUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    Endpoint
    | StaticEndpointsPartialUpdateResponse400
    | StaticEndpointsPartialUpdateResponse401
    | StaticEndpointsPartialUpdateResponse403
    | StaticEndpointsPartialUpdateResponse404
]:
    """Update rental access

     Change the label, active status or allowed client IP/CIDR networks. The next node configuration
    update applies the policy to new and existing connections.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (PatchedEndpointUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Endpoint | StaticEndpointsPartialUpdateResponse400 | StaticEndpointsPartialUpdateResponse401 | StaticEndpointsPartialUpdateResponse403 | StaticEndpointsPartialUpdateResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
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
    body: PatchedEndpointUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    Endpoint
    | StaticEndpointsPartialUpdateResponse400
    | StaticEndpointsPartialUpdateResponse401
    | StaticEndpointsPartialUpdateResponse403
    | StaticEndpointsPartialUpdateResponse404
    | None
):
    """Update rental access

     Change the label, active status or allowed client IP/CIDR networks. The next node configuration
    update applies the policy to new and existing connections.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (PatchedEndpointUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Endpoint | StaticEndpointsPartialUpdateResponse400 | StaticEndpointsPartialUpdateResponse401 | StaticEndpointsPartialUpdateResponse403 | StaticEndpointsPartialUpdateResponse404
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchedEndpointUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    Endpoint
    | StaticEndpointsPartialUpdateResponse400
    | StaticEndpointsPartialUpdateResponse401
    | StaticEndpointsPartialUpdateResponse403
    | StaticEndpointsPartialUpdateResponse404
]:
    """Update rental access

     Change the label, active status or allowed client IP/CIDR networks. The next node configuration
    update applies the policy to new and existing connections.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (PatchedEndpointUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Endpoint | StaticEndpointsPartialUpdateResponse400 | StaticEndpointsPartialUpdateResponse401 | StaticEndpointsPartialUpdateResponse403 | StaticEndpointsPartialUpdateResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchedEndpointUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    Endpoint
    | StaticEndpointsPartialUpdateResponse400
    | StaticEndpointsPartialUpdateResponse401
    | StaticEndpointsPartialUpdateResponse403
    | StaticEndpointsPartialUpdateResponse404
    | None
):
    """Update rental access

     Change the label, active status or allowed client IP/CIDR networks. The next node configuration
    update applies the policy to new and existing connections.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (PatchedEndpointUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Endpoint | StaticEndpointsPartialUpdateResponse400 | StaticEndpointsPartialUpdateResponse401 | StaticEndpointsPartialUpdateResponse403 | StaticEndpointsPartialUpdateResponse404
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

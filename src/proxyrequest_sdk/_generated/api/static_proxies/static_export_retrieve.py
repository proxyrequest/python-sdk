from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.static_export_retrieve_protocol import StaticExportRetrieveProtocol
from ...models.static_export_retrieve_response_400 import StaticExportRetrieveResponse400
from ...models.static_export_retrieve_response_401 import StaticExportRetrieveResponse401
from ...models.static_export_retrieve_response_403 import StaticExportRetrieveResponse403
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    *,
    order_id: UUID | Unset = UNSET,
    protocol: StaticExportRetrieveProtocol | Unset = StaticExportRetrieveProtocol.HTTP,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    params: dict[str, Any] = {}

    json_order_id: str | Unset = UNSET
    if not isinstance(order_id, Unset):
        json_order_id = str(order_id)
    params["order_id"] = json_order_id

    json_protocol: str | Unset = UNSET
    if not isinstance(protocol, Unset):
        json_protocol = protocol.value

    params["protocol"] = json_protocol

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/static/export",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    StaticExportRetrieveResponse400
    | StaticExportRetrieveResponse401
    | StaticExportRetrieveResponse403
    | str
    | None
):
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 400:
        response_400 = StaticExportRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StaticExportRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = StaticExportRetrieveResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    StaticExportRetrieveResponse400
    | StaticExportRetrieveResponse401
    | StaticExportRetrieveResponse403
    | str
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
    order_id: UUID | Unset = UNSET,
    protocol: StaticExportRetrieveProtocol | Unset = StaticExportRetrieveProtocol.HTTP,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    StaticExportRetrieveResponse400
    | StaticExportRetrieveResponse401
    | StaticExportRetrieveResponse403
    | str
]:
    """Export proxy connection URLs

     Download active HTTP or SOCKS5 connection URLs including credentials. Select protocol=http or socks5
    and optionally order_id. At most 10000 rentals can be exported at once; responses must not be
    cached.

    Args:
        order_id (UUID | Unset):
        protocol (StaticExportRetrieveProtocol | Unset):  Default:
            StaticExportRetrieveProtocol.HTTP.
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StaticExportRetrieveResponse400 | StaticExportRetrieveResponse401 | StaticExportRetrieveResponse403 | str]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        protocol=protocol,
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
    order_id: UUID | Unset = UNSET,
    protocol: StaticExportRetrieveProtocol | Unset = StaticExportRetrieveProtocol.HTTP,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    StaticExportRetrieveResponse400
    | StaticExportRetrieveResponse401
    | StaticExportRetrieveResponse403
    | str
    | None
):
    """Export proxy connection URLs

     Download active HTTP or SOCKS5 connection URLs including credentials. Select protocol=http or socks5
    and optionally order_id. At most 10000 rentals can be exported at once; responses must not be
    cached.

    Args:
        order_id (UUID | Unset):
        protocol (StaticExportRetrieveProtocol | Unset):  Default:
            StaticExportRetrieveProtocol.HTTP.
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StaticExportRetrieveResponse400 | StaticExportRetrieveResponse401 | StaticExportRetrieveResponse403 | str
    """

    return sync_detailed(
        client=client,
        order_id=order_id,
        protocol=protocol,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    order_id: UUID | Unset = UNSET,
    protocol: StaticExportRetrieveProtocol | Unset = StaticExportRetrieveProtocol.HTTP,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    StaticExportRetrieveResponse400
    | StaticExportRetrieveResponse401
    | StaticExportRetrieveResponse403
    | str
]:
    """Export proxy connection URLs

     Download active HTTP or SOCKS5 connection URLs including credentials. Select protocol=http or socks5
    and optionally order_id. At most 10000 rentals can be exported at once; responses must not be
    cached.

    Args:
        order_id (UUID | Unset):
        protocol (StaticExportRetrieveProtocol | Unset):  Default:
            StaticExportRetrieveProtocol.HTTP.
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StaticExportRetrieveResponse400 | StaticExportRetrieveResponse401 | StaticExportRetrieveResponse403 | str]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        protocol=protocol,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    order_id: UUID | Unset = UNSET,
    protocol: StaticExportRetrieveProtocol | Unset = StaticExportRetrieveProtocol.HTTP,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    StaticExportRetrieveResponse400
    | StaticExportRetrieveResponse401
    | StaticExportRetrieveResponse403
    | str
    | None
):
    """Export proxy connection URLs

     Download active HTTP or SOCKS5 connection URLs including credentials. Select protocol=http or socks5
    and optionally order_id. At most 10000 rentals can be exported at once; responses must not be
    cached.

    Args:
        order_id (UUID | Unset):
        protocol (StaticExportRetrieveProtocol | Unset):  Default:
            StaticExportRetrieveProtocol.HTTP.
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StaticExportRetrieveResponse400 | StaticExportRetrieveResponse401 | StaticExportRetrieveResponse403 | str
    """

    return (
        await asyncio_detailed(
            client=client,
            order_id=order_id,
            protocol=protocol,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

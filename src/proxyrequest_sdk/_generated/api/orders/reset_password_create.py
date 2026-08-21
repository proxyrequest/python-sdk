from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.proxy_password_reset_response import ProxyPasswordResetResponse
from ...models.reset_password_create_response_400 import ResetPasswordCreateResponse400
from ...models.reset_password_create_response_404 import ResetPasswordCreateResponse404
from ...models.reset_password_request import ResetPasswordRequest
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: ResetPasswordRequest,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/reset-password",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ProxyPasswordResetResponse
    | ResetPasswordCreateResponse400
    | ResetPasswordCreateResponse404
    | None
):
    if response.status_code == 200:
        response_200 = ProxyPasswordResetResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ResetPasswordCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ResetPasswordCreateResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ProxyPasswordResetResponse | ResetPasswordCreateResponse400 | ResetPasswordCreateResponse404
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
    body: ResetPasswordRequest,
    accept_language: str | Unset = UNSET,
) -> Response[
    ProxyPasswordResetResponse | ResetPasswordCreateResponse400 | ResetPasswordCreateResponse404
]:
    """Reset an order's proxy password

     Rotates the proxy password for the order identified by order_id. Existing proxy connection strings
    stop working after the rotation; use the updated proxy password for all new connections.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (ResetPasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProxyPasswordResetResponse | ResetPasswordCreateResponse400 | ResetPasswordCreateResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ResetPasswordRequest,
    accept_language: str | Unset = UNSET,
) -> (
    ProxyPasswordResetResponse
    | ResetPasswordCreateResponse400
    | ResetPasswordCreateResponse404
    | None
):
    """Reset an order's proxy password

     Rotates the proxy password for the order identified by order_id. Existing proxy connection strings
    stop working after the rotation; use the updated proxy password for all new connections.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (ResetPasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProxyPasswordResetResponse | ResetPasswordCreateResponse400 | ResetPasswordCreateResponse404
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ResetPasswordRequest,
    accept_language: str | Unset = UNSET,
) -> Response[
    ProxyPasswordResetResponse | ResetPasswordCreateResponse400 | ResetPasswordCreateResponse404
]:
    """Reset an order's proxy password

     Rotates the proxy password for the order identified by order_id. Existing proxy connection strings
    stop working after the rotation; use the updated proxy password for all new connections.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (ResetPasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProxyPasswordResetResponse | ResetPasswordCreateResponse400 | ResetPasswordCreateResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ResetPasswordRequest,
    accept_language: str | Unset = UNSET,
) -> (
    ProxyPasswordResetResponse
    | ResetPasswordCreateResponse400
    | ResetPasswordCreateResponse404
    | None
):
    """Reset an order's proxy password

     Rotates the proxy password for the order identified by order_id. Existing proxy connection strings
    stop working after the rotation; use the updated proxy password for all new connections.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (ResetPasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProxyPasswordResetResponse | ResetPasswordCreateResponse400 | ResetPasswordCreateResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed

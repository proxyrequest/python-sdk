from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.proxy_password_reset_request_request import ProxyPasswordResetRequestRequest
from ...models.proxy_password_reset_response import ProxyPasswordResetResponse
from ...models.reset_password_create_response_400 import ResetPasswordCreateResponse400
from ...models.reset_password_create_response_401 import ResetPasswordCreateResponse401
from ...models.reset_password_create_response_403 import ResetPasswordCreateResponse403
from ...models.reset_password_create_response_404 import ResetPasswordCreateResponse404
from ...models.reset_password_request import ResetPasswordRequest
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: ProxyPasswordResetRequestRequest | ResetPasswordRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/reset-password",
    }

    if isinstance(body, ResetPasswordRequest):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ProxyPasswordResetResponse
    | ResetPasswordCreateResponse400
    | ResetPasswordCreateResponse401
    | ResetPasswordCreateResponse403
    | ResetPasswordCreateResponse404
    | None
):
    if response.status_code == 200:
        response_200 = ProxyPasswordResetResponse.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = ProxyPasswordResetResponse.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ResetPasswordCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ResetPasswordCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ResetPasswordCreateResponse403.from_dict(response.json())

        return response_403

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
    ProxyPasswordResetResponse
    | ResetPasswordCreateResponse400
    | ResetPasswordCreateResponse401
    | ResetPasswordCreateResponse403
    | ResetPasswordCreateResponse404
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
    body: ProxyPasswordResetRequestRequest | ResetPasswordRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    ProxyPasswordResetResponse
    | ResetPasswordCreateResponse400
    | ResetPasswordCreateResponse401
    | ResetPasswordCreateResponse403
    | ResetPasswordCreateResponse404
]:
    """Confirm an account password reset or rotate an order's proxy password

     Recover a login password using a valid reset token, or send order_id with authentication to rotate a
    proxy password for an owned order. Static rental clients can use the order-scoped password reset
    operation.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (ProxyPasswordResetRequestRequest | ResetPasswordRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProxyPasswordResetResponse | ResetPasswordCreateResponse400 | ResetPasswordCreateResponse401 | ResetPasswordCreateResponse403 | ResetPasswordCreateResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: ProxyPasswordResetRequestRequest | ResetPasswordRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    ProxyPasswordResetResponse
    | ResetPasswordCreateResponse400
    | ResetPasswordCreateResponse401
    | ResetPasswordCreateResponse403
    | ResetPasswordCreateResponse404
    | None
):
    """Confirm an account password reset or rotate an order's proxy password

     Recover a login password using a valid reset token, or send order_id with authentication to rotate a
    proxy password for an owned order. Static rental clients can use the order-scoped password reset
    operation.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (ProxyPasswordResetRequestRequest | ResetPasswordRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProxyPasswordResetResponse | ResetPasswordCreateResponse400 | ResetPasswordCreateResponse401 | ResetPasswordCreateResponse403 | ResetPasswordCreateResponse404
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProxyPasswordResetRequestRequest | ResetPasswordRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    ProxyPasswordResetResponse
    | ResetPasswordCreateResponse400
    | ResetPasswordCreateResponse401
    | ResetPasswordCreateResponse403
    | ResetPasswordCreateResponse404
]:
    """Confirm an account password reset or rotate an order's proxy password

     Recover a login password using a valid reset token, or send order_id with authentication to rotate a
    proxy password for an owned order. Static rental clients can use the order-scoped password reset
    operation.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (ProxyPasswordResetRequestRequest | ResetPasswordRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProxyPasswordResetResponse | ResetPasswordCreateResponse400 | ResetPasswordCreateResponse401 | ResetPasswordCreateResponse403 | ResetPasswordCreateResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ProxyPasswordResetRequestRequest | ResetPasswordRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    ProxyPasswordResetResponse
    | ResetPasswordCreateResponse400
    | ResetPasswordCreateResponse401
    | ResetPasswordCreateResponse403
    | ResetPasswordCreateResponse404
    | None
):
    """Confirm an account password reset or rotate an order's proxy password

     Recover a login password using a valid reset token, or send order_id with authentication to rotate a
    proxy password for an owned order. Static rental clients can use the order-scoped password reset
    operation.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (ProxyPasswordResetRequestRequest | ResetPasswordRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProxyPasswordResetResponse | ResetPasswordCreateResponse400 | ResetPasswordCreateResponse401 | ResetPasswordCreateResponse403 | ResetPasswordCreateResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

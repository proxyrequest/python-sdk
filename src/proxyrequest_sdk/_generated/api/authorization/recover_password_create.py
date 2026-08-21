from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.password_recovery_response import PasswordRecoveryResponse
from ...models.recover_password_create_response_400 import RecoverPasswordCreateResponse400
from ...models.recover_password_request import RecoverPasswordRequest
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: RecoverPasswordRequest,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/recover-password",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PasswordRecoveryResponse | RecoverPasswordCreateResponse400 | None:
    if response.status_code == 200:
        response_200 = PasswordRecoveryResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RecoverPasswordCreateResponse400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PasswordRecoveryResponse | RecoverPasswordCreateResponse400]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RecoverPasswordRequest,
    accept_language: str | Unset = UNSET,
) -> Response[PasswordRecoveryResponse | RecoverPasswordCreateResponse400]:
    """Send a password recovery email

     Validates the anti-bot token and sends account recovery instructions to the supplied email address.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (RecoverPasswordRequest): Password recovery with enhanced security and comprehensive
            error handling.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PasswordRecoveryResponse | RecoverPasswordCreateResponse400]
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
    body: RecoverPasswordRequest,
    accept_language: str | Unset = UNSET,
) -> PasswordRecoveryResponse | RecoverPasswordCreateResponse400 | None:
    """Send a password recovery email

     Validates the anti-bot token and sends account recovery instructions to the supplied email address.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (RecoverPasswordRequest): Password recovery with enhanced security and comprehensive
            error handling.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PasswordRecoveryResponse | RecoverPasswordCreateResponse400
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RecoverPasswordRequest,
    accept_language: str | Unset = UNSET,
) -> Response[PasswordRecoveryResponse | RecoverPasswordCreateResponse400]:
    """Send a password recovery email

     Validates the anti-bot token and sends account recovery instructions to the supplied email address.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (RecoverPasswordRequest): Password recovery with enhanced security and comprehensive
            error handling.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PasswordRecoveryResponse | RecoverPasswordCreateResponse400]
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
    body: RecoverPasswordRequest,
    accept_language: str | Unset = UNSET,
) -> PasswordRecoveryResponse | RecoverPasswordCreateResponse400 | None:
    """Send a password recovery email

     Validates the anti-bot token and sends account recovery instructions to the supplied email address.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (RecoverPasswordRequest): Password recovery with enhanced security and comprehensive
            error handling.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PasswordRecoveryResponse | RecoverPasswordCreateResponse400
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.integrations_telegram_session_create_response_400 import (
    IntegrationsTelegramSessionCreateResponse400,
)
from ...models.telegram_session_request import TelegramSessionRequest
from ...models.telegram_session_response import TelegramSessionResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: TelegramSessionRequest,
    x_proxy_request_telegram_secret: str,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-ProxyRequest-Telegram-Secret"] = x_proxy_request_telegram_secret

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/integrations/telegram/session",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IntegrationsTelegramSessionCreateResponse400 | TelegramSessionResponse | None:
    if response.status_code == 200:
        response_200 = TelegramSessionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = IntegrationsTelegramSessionCreateResponse400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IntegrationsTelegramSessionCreateResponse400 | TelegramSessionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TelegramSessionRequest,
    x_proxy_request_telegram_secret: str,
    accept_language: str | Unset = UNSET,
) -> Response[IntegrationsTelegramSessionCreateResponse400 | TelegramSessionResponse]:
    """Create a Telegram API session

     Returns a two-minute access token for an already linked private chat.

    Args:
        x_proxy_request_telegram_secret (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (TelegramSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationsTelegramSessionCreateResponse400 | TelegramSessionResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        x_proxy_request_telegram_secret=x_proxy_request_telegram_secret,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: TelegramSessionRequest,
    x_proxy_request_telegram_secret: str,
    accept_language: str | Unset = UNSET,
) -> IntegrationsTelegramSessionCreateResponse400 | TelegramSessionResponse | None:
    """Create a Telegram API session

     Returns a two-minute access token for an already linked private chat.

    Args:
        x_proxy_request_telegram_secret (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (TelegramSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationsTelegramSessionCreateResponse400 | TelegramSessionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        x_proxy_request_telegram_secret=x_proxy_request_telegram_secret,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TelegramSessionRequest,
    x_proxy_request_telegram_secret: str,
    accept_language: str | Unset = UNSET,
) -> Response[IntegrationsTelegramSessionCreateResponse400 | TelegramSessionResponse]:
    """Create a Telegram API session

     Returns a two-minute access token for an already linked private chat.

    Args:
        x_proxy_request_telegram_secret (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (TelegramSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationsTelegramSessionCreateResponse400 | TelegramSessionResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        x_proxy_request_telegram_secret=x_proxy_request_telegram_secret,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TelegramSessionRequest,
    x_proxy_request_telegram_secret: str,
    accept_language: str | Unset = UNSET,
) -> IntegrationsTelegramSessionCreateResponse400 | TelegramSessionResponse | None:
    """Create a Telegram API session

     Returns a two-minute access token for an already linked private chat.

    Args:
        x_proxy_request_telegram_secret (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (TelegramSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationsTelegramSessionCreateResponse400 | TelegramSessionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_proxy_request_telegram_secret=x_proxy_request_telegram_secret,
            accept_language=accept_language,
        )
    ).parsed

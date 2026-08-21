from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.integrations_telegram_link_consume_create_response_400 import (
    IntegrationsTelegramLinkConsumeCreateResponse400,
)
from ...models.telegram_connection_response import TelegramConnectionResponse
from ...models.telegram_link_consume_request import TelegramLinkConsumeRequest
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: TelegramLinkConsumeRequest,
    x_proxy_request_telegram_secret: str,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-ProxyRequest-Telegram-Secret"] = x_proxy_request_telegram_secret

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/integrations/telegram/link/consume",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IntegrationsTelegramLinkConsumeCreateResponse400 | TelegramConnectionResponse | None:
    if response.status_code == 200:
        response_200 = TelegramConnectionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = IntegrationsTelegramLinkConsumeCreateResponse400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IntegrationsTelegramLinkConsumeCreateResponse400 | TelegramConnectionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TelegramLinkConsumeRequest,
    x_proxy_request_telegram_secret: str,
    accept_language: str | Unset = UNSET,
) -> Response[IntegrationsTelegramLinkConsumeCreateResponse400 | TelegramConnectionResponse]:
    """Consume a Telegram account link

     Links a private Telegram chat after validating the single-use token.

    Args:
        x_proxy_request_telegram_secret (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (TelegramLinkConsumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationsTelegramLinkConsumeCreateResponse400 | TelegramConnectionResponse]
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
    body: TelegramLinkConsumeRequest,
    x_proxy_request_telegram_secret: str,
    accept_language: str | Unset = UNSET,
) -> IntegrationsTelegramLinkConsumeCreateResponse400 | TelegramConnectionResponse | None:
    """Consume a Telegram account link

     Links a private Telegram chat after validating the single-use token.

    Args:
        x_proxy_request_telegram_secret (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (TelegramLinkConsumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationsTelegramLinkConsumeCreateResponse400 | TelegramConnectionResponse
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
    body: TelegramLinkConsumeRequest,
    x_proxy_request_telegram_secret: str,
    accept_language: str | Unset = UNSET,
) -> Response[IntegrationsTelegramLinkConsumeCreateResponse400 | TelegramConnectionResponse]:
    """Consume a Telegram account link

     Links a private Telegram chat after validating the single-use token.

    Args:
        x_proxy_request_telegram_secret (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (TelegramLinkConsumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationsTelegramLinkConsumeCreateResponse400 | TelegramConnectionResponse]
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
    body: TelegramLinkConsumeRequest,
    x_proxy_request_telegram_secret: str,
    accept_language: str | Unset = UNSET,
) -> IntegrationsTelegramLinkConsumeCreateResponse400 | TelegramConnectionResponse | None:
    """Consume a Telegram account link

     Links a private Telegram chat after validating the single-use token.

    Args:
        x_proxy_request_telegram_secret (str):
        accept_language (str | Unset):  Defaults to the client language.
        body (TelegramLinkConsumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationsTelegramLinkConsumeCreateResponse400 | TelegramConnectionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_proxy_request_telegram_secret=x_proxy_request_telegram_secret,
            accept_language=accept_language,
        )
    ).parsed

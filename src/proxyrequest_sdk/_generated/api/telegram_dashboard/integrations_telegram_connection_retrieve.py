from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.integrations_telegram_connection_retrieve_response_400 import (
    IntegrationsTelegramConnectionRetrieveResponse400,
)
from ...models.integrations_telegram_connection_retrieve_response_401 import (
    IntegrationsTelegramConnectionRetrieveResponse401,
)
from ...models.integrations_telegram_connection_retrieve_response_403 import (
    IntegrationsTelegramConnectionRetrieveResponse403,
)
from ...models.telegram_connection_response import TelegramConnectionResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/integrations/telegram/connection",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    IntegrationsTelegramConnectionRetrieveResponse400
    | IntegrationsTelegramConnectionRetrieveResponse401
    | IntegrationsTelegramConnectionRetrieveResponse403
    | TelegramConnectionResponse
    | None
):
    if response.status_code == 200:
        response_200 = TelegramConnectionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = IntegrationsTelegramConnectionRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = IntegrationsTelegramConnectionRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = IntegrationsTelegramConnectionRetrieveResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    IntegrationsTelegramConnectionRetrieveResponse400
    | IntegrationsTelegramConnectionRetrieveResponse401
    | IntegrationsTelegramConnectionRetrieveResponse403
    | TelegramConnectionResponse
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
    accept_language: str | Unset = UNSET,
) -> Response[
    IntegrationsTelegramConnectionRetrieveResponse400
    | IntegrationsTelegramConnectionRetrieveResponse401
    | IntegrationsTelegramConnectionRetrieveResponse403
    | TelegramConnectionResponse
]:
    """Get the Telegram dashboard connection

     Returns connection state and bot details for the authenticated account.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationsTelegramConnectionRetrieveResponse400 | IntegrationsTelegramConnectionRetrieveResponse401 | IntegrationsTelegramConnectionRetrieveResponse403 | TelegramConnectionResponse]
    """

    kwargs = _get_kwargs(
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
) -> (
    IntegrationsTelegramConnectionRetrieveResponse400
    | IntegrationsTelegramConnectionRetrieveResponse401
    | IntegrationsTelegramConnectionRetrieveResponse403
    | TelegramConnectionResponse
    | None
):
    """Get the Telegram dashboard connection

     Returns connection state and bot details for the authenticated account.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationsTelegramConnectionRetrieveResponse400 | IntegrationsTelegramConnectionRetrieveResponse401 | IntegrationsTelegramConnectionRetrieveResponse403 | TelegramConnectionResponse
    """

    return sync_detailed(
        client=client,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
) -> Response[
    IntegrationsTelegramConnectionRetrieveResponse400
    | IntegrationsTelegramConnectionRetrieveResponse401
    | IntegrationsTelegramConnectionRetrieveResponse403
    | TelegramConnectionResponse
]:
    """Get the Telegram dashboard connection

     Returns connection state and bot details for the authenticated account.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationsTelegramConnectionRetrieveResponse400 | IntegrationsTelegramConnectionRetrieveResponse401 | IntegrationsTelegramConnectionRetrieveResponse403 | TelegramConnectionResponse]
    """

    kwargs = _get_kwargs(
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
) -> (
    IntegrationsTelegramConnectionRetrieveResponse400
    | IntegrationsTelegramConnectionRetrieveResponse401
    | IntegrationsTelegramConnectionRetrieveResponse403
    | TelegramConnectionResponse
    | None
):
    """Get the Telegram dashboard connection

     Returns connection state and bot details for the authenticated account.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationsTelegramConnectionRetrieveResponse400 | IntegrationsTelegramConnectionRetrieveResponse401 | IntegrationsTelegramConnectionRetrieveResponse403 | TelegramConnectionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            accept_language=accept_language,
        )
    ).parsed

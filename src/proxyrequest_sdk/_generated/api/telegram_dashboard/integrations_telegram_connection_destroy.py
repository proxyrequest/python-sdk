from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.integrations_telegram_connection_destroy_response_400 import (
    IntegrationsTelegramConnectionDestroyResponse400,
)
from ...models.integrations_telegram_connection_destroy_response_401 import (
    IntegrationsTelegramConnectionDestroyResponse401,
)
from ...models.integrations_telegram_connection_destroy_response_403 import (
    IntegrationsTelegramConnectionDestroyResponse403,
)
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
        "method": "delete",
        "url": "/integrations/telegram/connection",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | IntegrationsTelegramConnectionDestroyResponse400
    | IntegrationsTelegramConnectionDestroyResponse401
    | IntegrationsTelegramConnectionDestroyResponse403
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = IntegrationsTelegramConnectionDestroyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = IntegrationsTelegramConnectionDestroyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = IntegrationsTelegramConnectionDestroyResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | IntegrationsTelegramConnectionDestroyResponse400
    | IntegrationsTelegramConnectionDestroyResponse401
    | IntegrationsTelegramConnectionDestroyResponse403
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
    Any
    | IntegrationsTelegramConnectionDestroyResponse400
    | IntegrationsTelegramConnectionDestroyResponse401
    | IntegrationsTelegramConnectionDestroyResponse403
]:
    """Disconnect the Telegram dashboard

     Revokes the Telegram identity link and all future bot sessions.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IntegrationsTelegramConnectionDestroyResponse400 | IntegrationsTelegramConnectionDestroyResponse401 | IntegrationsTelegramConnectionDestroyResponse403]
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
    Any
    | IntegrationsTelegramConnectionDestroyResponse400
    | IntegrationsTelegramConnectionDestroyResponse401
    | IntegrationsTelegramConnectionDestroyResponse403
    | None
):
    """Disconnect the Telegram dashboard

     Revokes the Telegram identity link and all future bot sessions.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IntegrationsTelegramConnectionDestroyResponse400 | IntegrationsTelegramConnectionDestroyResponse401 | IntegrationsTelegramConnectionDestroyResponse403
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
    Any
    | IntegrationsTelegramConnectionDestroyResponse400
    | IntegrationsTelegramConnectionDestroyResponse401
    | IntegrationsTelegramConnectionDestroyResponse403
]:
    """Disconnect the Telegram dashboard

     Revokes the Telegram identity link and all future bot sessions.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IntegrationsTelegramConnectionDestroyResponse400 | IntegrationsTelegramConnectionDestroyResponse401 | IntegrationsTelegramConnectionDestroyResponse403]
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
    Any
    | IntegrationsTelegramConnectionDestroyResponse400
    | IntegrationsTelegramConnectionDestroyResponse401
    | IntegrationsTelegramConnectionDestroyResponse403
    | None
):
    """Disconnect the Telegram dashboard

     Revokes the Telegram identity link and all future bot sessions.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IntegrationsTelegramConnectionDestroyResponse400 | IntegrationsTelegramConnectionDestroyResponse401 | IntegrationsTelegramConnectionDestroyResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            accept_language=accept_language,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.integrations_telegram_connection_partial_update_response_400 import (
    IntegrationsTelegramConnectionPartialUpdateResponse400,
)
from ...models.integrations_telegram_connection_partial_update_response_401 import (
    IntegrationsTelegramConnectionPartialUpdateResponse401,
)
from ...models.integrations_telegram_connection_partial_update_response_403 import (
    IntegrationsTelegramConnectionPartialUpdateResponse403,
)
from ...models.patched_telegram_connection_update_request import (
    PatchedTelegramConnectionUpdateRequest,
)
from ...models.telegram_connection_response import TelegramConnectionResponse
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: PatchedTelegramConnectionUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/integrations/telegram/connection",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    IntegrationsTelegramConnectionPartialUpdateResponse400
    | IntegrationsTelegramConnectionPartialUpdateResponse401
    | IntegrationsTelegramConnectionPartialUpdateResponse403
    | TelegramConnectionResponse
    | None
):
    if response.status_code == 200:
        response_200 = TelegramConnectionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = IntegrationsTelegramConnectionPartialUpdateResponse400.from_dict(
            response.json()
        )

        return response_400

    if response.status_code == 401:
        response_401 = IntegrationsTelegramConnectionPartialUpdateResponse401.from_dict(
            response.json()
        )

        return response_401

    if response.status_code == 403:
        response_403 = IntegrationsTelegramConnectionPartialUpdateResponse403.from_dict(
            response.json()
        )

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    IntegrationsTelegramConnectionPartialUpdateResponse400
    | IntegrationsTelegramConnectionPartialUpdateResponse401
    | IntegrationsTelegramConnectionPartialUpdateResponse403
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
    body: PatchedTelegramConnectionUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    IntegrationsTelegramConnectionPartialUpdateResponse400
    | IntegrationsTelegramConnectionPartialUpdateResponse401
    | IntegrationsTelegramConnectionPartialUpdateResponse403
    | TelegramConnectionResponse
]:
    """Update Telegram dashboard preferences

     Changes the language or timezone used by the Telegram dashboard.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedTelegramConnectionUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationsTelegramConnectionPartialUpdateResponse400 | IntegrationsTelegramConnectionPartialUpdateResponse401 | IntegrationsTelegramConnectionPartialUpdateResponse403 | TelegramConnectionResponse]
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
    body: PatchedTelegramConnectionUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    IntegrationsTelegramConnectionPartialUpdateResponse400
    | IntegrationsTelegramConnectionPartialUpdateResponse401
    | IntegrationsTelegramConnectionPartialUpdateResponse403
    | TelegramConnectionResponse
    | None
):
    """Update Telegram dashboard preferences

     Changes the language or timezone used by the Telegram dashboard.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedTelegramConnectionUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationsTelegramConnectionPartialUpdateResponse400 | IntegrationsTelegramConnectionPartialUpdateResponse401 | IntegrationsTelegramConnectionPartialUpdateResponse403 | TelegramConnectionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PatchedTelegramConnectionUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    IntegrationsTelegramConnectionPartialUpdateResponse400
    | IntegrationsTelegramConnectionPartialUpdateResponse401
    | IntegrationsTelegramConnectionPartialUpdateResponse403
    | TelegramConnectionResponse
]:
    """Update Telegram dashboard preferences

     Changes the language or timezone used by the Telegram dashboard.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedTelegramConnectionUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationsTelegramConnectionPartialUpdateResponse400 | IntegrationsTelegramConnectionPartialUpdateResponse401 | IntegrationsTelegramConnectionPartialUpdateResponse403 | TelegramConnectionResponse]
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
    body: PatchedTelegramConnectionUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    IntegrationsTelegramConnectionPartialUpdateResponse400
    | IntegrationsTelegramConnectionPartialUpdateResponse401
    | IntegrationsTelegramConnectionPartialUpdateResponse403
    | TelegramConnectionResponse
    | None
):
    """Update Telegram dashboard preferences

     Changes the language or timezone used by the Telegram dashboard.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedTelegramConnectionUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationsTelegramConnectionPartialUpdateResponse400 | IntegrationsTelegramConnectionPartialUpdateResponse401 | IntegrationsTelegramConnectionPartialUpdateResponse403 | TelegramConnectionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.integration_key import IntegrationKey
from ...models.static_integration_keys_list_response_400 import StaticIntegrationKeysListResponse400
from ...models.static_integration_keys_list_response_401 import StaticIntegrationKeysListResponse401
from ...models.static_integration_keys_list_response_403 import StaticIntegrationKeysListResponse403
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/static/integration-keys",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    StaticIntegrationKeysListResponse400
    | StaticIntegrationKeysListResponse401
    | StaticIntegrationKeysListResponse403
    | list[IntegrationKey]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IntegrationKey.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = StaticIntegrationKeysListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StaticIntegrationKeysListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = StaticIntegrationKeysListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    StaticIntegrationKeysListResponse400
    | StaticIntegrationKeysListResponse401
    | StaticIntegrationKeysListResponse403
    | list[IntegrationKey]
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
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    StaticIntegrationKeysListResponse400
    | StaticIntegrationKeysListResponse401
    | StaticIntegrationKeysListResponse403
    | list[IntegrationKey]
]:
    """List static proxy integration keys

     Read the current account's delegated key names, scopes and IP restrictions.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StaticIntegrationKeysListResponse400 | StaticIntegrationKeysListResponse401 | StaticIntegrationKeysListResponse403 | list[IntegrationKey]]
    """

    kwargs = _get_kwargs(
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
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    StaticIntegrationKeysListResponse400
    | StaticIntegrationKeysListResponse401
    | StaticIntegrationKeysListResponse403
    | list[IntegrationKey]
    | None
):
    """List static proxy integration keys

     Read the current account's delegated key names, scopes and IP restrictions.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StaticIntegrationKeysListResponse400 | StaticIntegrationKeysListResponse401 | StaticIntegrationKeysListResponse403 | list[IntegrationKey]
    """

    return sync_detailed(
        client=client,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    StaticIntegrationKeysListResponse400
    | StaticIntegrationKeysListResponse401
    | StaticIntegrationKeysListResponse403
    | list[IntegrationKey]
]:
    """List static proxy integration keys

     Read the current account's delegated key names, scopes and IP restrictions.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StaticIntegrationKeysListResponse400 | StaticIntegrationKeysListResponse401 | StaticIntegrationKeysListResponse403 | list[IntegrationKey]]
    """

    kwargs = _get_kwargs(
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    StaticIntegrationKeysListResponse400
    | StaticIntegrationKeysListResponse401
    | StaticIntegrationKeysListResponse403
    | list[IntegrationKey]
    | None
):
    """List static proxy integration keys

     Read the current account's delegated key names, scopes and IP restrictions.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StaticIntegrationKeysListResponse400 | StaticIntegrationKeysListResponse401 | StaticIntegrationKeysListResponse403 | list[IntegrationKey]
    """

    return (
        await asyncio_detailed(
            client=client,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

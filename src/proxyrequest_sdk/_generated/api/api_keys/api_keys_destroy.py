from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_keys_destroy_response_400 import ApiKeysDestroyResponse400
from ...models.api_keys_destroy_response_401 import ApiKeysDestroyResponse401
from ...models.api_keys_destroy_response_403 import ApiKeysDestroyResponse403
from ...models.api_keys_destroy_response_404 import ApiKeysDestroyResponse404
from ...models.api_keys_destroy_response_409 import ApiKeysDestroyResponse409
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    id: str,
    *,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api-keys/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ApiKeysDestroyResponse400
    | ApiKeysDestroyResponse401
    | ApiKeysDestroyResponse403
    | ApiKeysDestroyResponse404
    | ApiKeysDestroyResponse409
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ApiKeysDestroyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiKeysDestroyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiKeysDestroyResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiKeysDestroyResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ApiKeysDestroyResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | ApiKeysDestroyResponse400
    | ApiKeysDestroyResponse401
    | ApiKeysDestroyResponse403
    | ApiKeysDestroyResponse404
    | ApiKeysDestroyResponse409
]:
    parsed = parse_response(_parse_response, client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Any
    | ApiKeysDestroyResponse400
    | ApiKeysDestroyResponse401
    | ApiKeysDestroyResponse403
    | ApiKeysDestroyResponse404
    | ApiKeysDestroyResponse409
]:
    """Revoke an API key

     Permanently revokes an API key owned by the authenticated account. Requests using the revoked key
    fail immediately.

    Args:
        id (str):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiKeysDestroyResponse400 | ApiKeysDestroyResponse401 | ApiKeysDestroyResponse403 | ApiKeysDestroyResponse404 | ApiKeysDestroyResponse409]
    """

    kwargs = _get_kwargs(
        id=id,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Any
    | ApiKeysDestroyResponse400
    | ApiKeysDestroyResponse401
    | ApiKeysDestroyResponse403
    | ApiKeysDestroyResponse404
    | ApiKeysDestroyResponse409
    | None
):
    """Revoke an API key

     Permanently revokes an API key owned by the authenticated account. Requests using the revoked key
    fail immediately.

    Args:
        id (str):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiKeysDestroyResponse400 | ApiKeysDestroyResponse401 | ApiKeysDestroyResponse403 | ApiKeysDestroyResponse404 | ApiKeysDestroyResponse409
    """

    return sync_detailed(
        id=id,
        client=client,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Any
    | ApiKeysDestroyResponse400
    | ApiKeysDestroyResponse401
    | ApiKeysDestroyResponse403
    | ApiKeysDestroyResponse404
    | ApiKeysDestroyResponse409
]:
    """Revoke an API key

     Permanently revokes an API key owned by the authenticated account. Requests using the revoked key
    fail immediately.

    Args:
        id (str):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiKeysDestroyResponse400 | ApiKeysDestroyResponse401 | ApiKeysDestroyResponse403 | ApiKeysDestroyResponse404 | ApiKeysDestroyResponse409]
    """

    kwargs = _get_kwargs(
        id=id,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Any
    | ApiKeysDestroyResponse400
    | ApiKeysDestroyResponse401
    | ApiKeysDestroyResponse403
    | ApiKeysDestroyResponse404
    | ApiKeysDestroyResponse409
    | None
):
    """Revoke an API key

     Permanently revokes an API key owned by the authenticated account. Requests using the revoked key
    fail immediately.

    Args:
        id (str):
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiKeysDestroyResponse400 | ApiKeysDestroyResponse401 | ApiKeysDestroyResponse403 | ApiKeysDestroyResponse404 | ApiKeysDestroyResponse409
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            idempotency_key=idempotency_key,
            accept_language=accept_language,
        )
    ).parsed

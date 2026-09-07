from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.users_destroy_response_400 import UsersDestroyResponse400
from ...models.users_destroy_response_401 import UsersDestroyResponse401
from ...models.users_destroy_response_403 import UsersDestroyResponse403
from ...models.users_destroy_response_404 import UsersDestroyResponse404
from ...models.users_destroy_response_409 import UsersDestroyResponse409
from ...models.users_destroy_response_412 import UsersDestroyResponse412
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    idempotency_key: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/users/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | UsersDestroyResponse400
    | UsersDestroyResponse401
    | UsersDestroyResponse403
    | UsersDestroyResponse404
    | UsersDestroyResponse409
    | UsersDestroyResponse412
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = UsersDestroyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UsersDestroyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsersDestroyResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UsersDestroyResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UsersDestroyResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 412:
        response_412 = UsersDestroyResponse412.from_dict(response.json())

        return response_412

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | UsersDestroyResponse400
    | UsersDestroyResponse401
    | UsersDestroyResponse403
    | UsersDestroyResponse404
    | UsersDestroyResponse409
    | UsersDestroyResponse412
]:
    parsed = parse_response(_parse_response, client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Any
    | UsersDestroyResponse400
    | UsersDestroyResponse401
    | UsersDestroyResponse403
    | UsersDestroyResponse404
    | UsersDestroyResponse409
    | UsersDestroyResponse412
]:
    """Delete a user

     Deletes a user that the authenticated account is allowed to manage.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        if_match (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UsersDestroyResponse400 | UsersDestroyResponse401 | UsersDestroyResponse403 | UsersDestroyResponse404 | UsersDestroyResponse409 | UsersDestroyResponse412]
    """

    kwargs = _get_kwargs(
        id=id,
        idempotency_key=idempotency_key,
        if_match=if_match,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Any
    | UsersDestroyResponse400
    | UsersDestroyResponse401
    | UsersDestroyResponse403
    | UsersDestroyResponse404
    | UsersDestroyResponse409
    | UsersDestroyResponse412
    | None
):
    """Delete a user

     Deletes a user that the authenticated account is allowed to manage.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        if_match (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UsersDestroyResponse400 | UsersDestroyResponse401 | UsersDestroyResponse403 | UsersDestroyResponse404 | UsersDestroyResponse409 | UsersDestroyResponse412
    """

    return sync_detailed(
        id=id,
        client=client,
        idempotency_key=idempotency_key,
        if_match=if_match,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    Any
    | UsersDestroyResponse400
    | UsersDestroyResponse401
    | UsersDestroyResponse403
    | UsersDestroyResponse404
    | UsersDestroyResponse409
    | UsersDestroyResponse412
]:
    """Delete a user

     Deletes a user that the authenticated account is allowed to manage.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        if_match (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UsersDestroyResponse400 | UsersDestroyResponse401 | UsersDestroyResponse403 | UsersDestroyResponse404 | UsersDestroyResponse409 | UsersDestroyResponse412]
    """

    kwargs = _get_kwargs(
        id=id,
        idempotency_key=idempotency_key,
        if_match=if_match,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
    if_match: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    Any
    | UsersDestroyResponse400
    | UsersDestroyResponse401
    | UsersDestroyResponse403
    | UsersDestroyResponse404
    | UsersDestroyResponse409
    | UsersDestroyResponse412
    | None
):
    """Delete a user

     Deletes a user that the authenticated account is allowed to manage.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        if_match (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UsersDestroyResponse400 | UsersDestroyResponse401 | UsersDestroyResponse403 | UsersDestroyResponse404 | UsersDestroyResponse409 | UsersDestroyResponse412
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            idempotency_key=idempotency_key,
            if_match=if_match,
            accept_language=accept_language,
        )
    ).parsed

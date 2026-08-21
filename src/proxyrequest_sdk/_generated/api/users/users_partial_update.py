from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patched_user_update_request import PatchedUserUpdateRequest
from ...models.user import User
from ...models.users_partial_update_response_400 import UsersPartialUpdateResponse400
from ...models.users_partial_update_response_401 import UsersPartialUpdateResponse401
from ...models.users_partial_update_response_403 import UsersPartialUpdateResponse403
from ...models.users_partial_update_response_404 import UsersPartialUpdateResponse404
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedUserUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/users/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    User
    | UsersPartialUpdateResponse400
    | UsersPartialUpdateResponse401
    | UsersPartialUpdateResponse403
    | UsersPartialUpdateResponse404
    | None
):
    if response.status_code == 202:
        response_202 = User.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = UsersPartialUpdateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UsersPartialUpdateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsersPartialUpdateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UsersPartialUpdateResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    User
    | UsersPartialUpdateResponse400
    | UsersPartialUpdateResponse401
    | UsersPartialUpdateResponse403
    | UsersPartialUpdateResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchedUserUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    User
    | UsersPartialUpdateResponse400
    | UsersPartialUpdateResponse401
    | UsersPartialUpdateResponse403
    | UsersPartialUpdateResponse404
]:
    """Update a user

     Updates selected fields for a visible user and returns the latest account state.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedUserUpdateRequest | Unset): Optional fields accepted when updating part of an
            existing customer account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[User | UsersPartialUpdateResponse400 | UsersPartialUpdateResponse401 | UsersPartialUpdateResponse403 | UsersPartialUpdateResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
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
    body: PatchedUserUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    User
    | UsersPartialUpdateResponse400
    | UsersPartialUpdateResponse401
    | UsersPartialUpdateResponse403
    | UsersPartialUpdateResponse404
    | None
):
    """Update a user

     Updates selected fields for a visible user and returns the latest account state.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedUserUpdateRequest | Unset): Optional fields accepted when updating part of an
            existing customer account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        User | UsersPartialUpdateResponse400 | UsersPartialUpdateResponse401 | UsersPartialUpdateResponse403 | UsersPartialUpdateResponse404
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchedUserUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    User
    | UsersPartialUpdateResponse400
    | UsersPartialUpdateResponse401
    | UsersPartialUpdateResponse403
    | UsersPartialUpdateResponse404
]:
    """Update a user

     Updates selected fields for a visible user and returns the latest account state.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedUserUpdateRequest | Unset): Optional fields accepted when updating part of an
            existing customer account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[User | UsersPartialUpdateResponse400 | UsersPartialUpdateResponse401 | UsersPartialUpdateResponse403 | UsersPartialUpdateResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchedUserUpdateRequest | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    User
    | UsersPartialUpdateResponse400
    | UsersPartialUpdateResponse401
    | UsersPartialUpdateResponse403
    | UsersPartialUpdateResponse404
    | None
):
    """Update a user

     Updates selected fields for a visible user and returns the latest account state.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        body (PatchedUserUpdateRequest | Unset): Optional fields accepted when updating part of an
            existing customer account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        User | UsersPartialUpdateResponse400 | UsersPartialUpdateResponse401 | UsersPartialUpdateResponse403 | UsersPartialUpdateResponse404
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed

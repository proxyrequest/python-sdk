from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_user_list import PaginatedUserList
from ...models.users_list_response_400 import UsersListResponse400
from ...models.users_list_response_401 import UsersListResponse401
from ...models.users_list_response_403 import UsersListResponse403
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    *,
    email: str | Unset = UNSET,
    id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    username: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["email"] = email

    json_id: str | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = str(id)
    params["id"] = json_id

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    json_package_id: str | Unset = UNSET
    if not isinstance(package_id, Unset):
        json_package_id = str(package_id)
    params["package__id"] = json_package_id

    params["search"] = search

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedUserList | UsersListResponse400 | UsersListResponse401 | UsersListResponse403 | None:
    if response.status_code == 200:
        response_200 = PaginatedUserList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UsersListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UsersListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UsersListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PaginatedUserList | UsersListResponse400 | UsersListResponse401 | UsersListResponse403
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
    email: str | Unset = UNSET,
    id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    username: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    PaginatedUserList | UsersListResponse400 | UsersListResponse401 | UsersListResponse403
]:
    """List users in the current account

     Returns users visible to the caller. Resellers see their sub-users, regular customers see only
    themselves, and administrators can see all users.

    Args:
        email (str | Unset):
        id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID | Unset):
        search (str | Unset):
        username (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserList | UsersListResponse400 | UsersListResponse401 | UsersListResponse403]
    """

    kwargs = _get_kwargs(
        email=email,
        id=id,
        limit=limit,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        search=search,
        username=username,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    email: str | Unset = UNSET,
    id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    username: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> PaginatedUserList | UsersListResponse400 | UsersListResponse401 | UsersListResponse403 | None:
    """List users in the current account

     Returns users visible to the caller. Resellers see their sub-users, regular customers see only
    themselves, and administrators can see all users.

    Args:
        email (str | Unset):
        id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID | Unset):
        search (str | Unset):
        username (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserList | UsersListResponse400 | UsersListResponse401 | UsersListResponse403
    """

    return sync_detailed(
        client=client,
        email=email,
        id=id,
        limit=limit,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        search=search,
        username=username,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    email: str | Unset = UNSET,
    id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    username: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    PaginatedUserList | UsersListResponse400 | UsersListResponse401 | UsersListResponse403
]:
    """List users in the current account

     Returns users visible to the caller. Resellers see their sub-users, regular customers see only
    themselves, and administrators can see all users.

    Args:
        email (str | Unset):
        id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID | Unset):
        search (str | Unset):
        username (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserList | UsersListResponse400 | UsersListResponse401 | UsersListResponse403]
    """

    kwargs = _get_kwargs(
        email=email,
        id=id,
        limit=limit,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        search=search,
        username=username,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    email: str | Unset = UNSET,
    id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    username: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> PaginatedUserList | UsersListResponse400 | UsersListResponse401 | UsersListResponse403 | None:
    """List users in the current account

     Returns users visible to the caller. Resellers see their sub-users, regular customers see only
    themselves, and administrators can see all users.

    Args:
        email (str | Unset):
        id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        package_id (UUID | Unset):
        search (str | Unset):
        username (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserList | UsersListResponse400 | UsersListResponse401 | UsersListResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            email=email,
            id=id,
            limit=limit,
            offset=offset,
            ordering=ordering,
            package_id=package_id,
            search=search,
            username=username,
            accept_language=accept_language,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_login_history_list import PaginatedLoginHistoryList
from ...models.profile_login_history_response_400 import ProfileLoginHistoryResponse400
from ...models.profile_login_history_response_401 import ProfileLoginHistoryResponse401
from ...models.profile_login_history_response_403 import ProfileLoginHistoryResponse403
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/profile/login-history",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PaginatedLoginHistoryList
    | ProfileLoginHistoryResponse400
    | ProfileLoginHistoryResponse401
    | ProfileLoginHistoryResponse403
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedLoginHistoryList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProfileLoginHistoryResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProfileLoginHistoryResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProfileLoginHistoryResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PaginatedLoginHistoryList
    | ProfileLoginHistoryResponse400
    | ProfileLoginHistoryResponse401
    | ProfileLoginHistoryResponse403
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    PaginatedLoginHistoryList
    | ProfileLoginHistoryResponse400
    | ProfileLoginHistoryResponse401
    | ProfileLoginHistoryResponse403
]:
    """List your recent successful sign-ins

     Returns only the authenticated user's latest personal sign-ins, newest first. At most 50 records are
    retained per account. Refreshes, API key requests, failed attempts and impersonation are excluded.
    Client metadata is descriptive, not proof of identity; location is present only when supplied by
    trusted Cloudflare edges.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLoginHistoryList | ProfileLoginHistoryResponse400 | ProfileLoginHistoryResponse401 | ProfileLoginHistoryResponse403]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    PaginatedLoginHistoryList
    | ProfileLoginHistoryResponse400
    | ProfileLoginHistoryResponse401
    | ProfileLoginHistoryResponse403
    | None
):
    """List your recent successful sign-ins

     Returns only the authenticated user's latest personal sign-ins, newest first. At most 50 records are
    retained per account. Refreshes, API key requests, failed attempts and impersonation are excluded.
    Client metadata is descriptive, not proof of identity; location is present only when supplied by
    trusted Cloudflare edges.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLoginHistoryList | ProfileLoginHistoryResponse400 | ProfileLoginHistoryResponse401 | ProfileLoginHistoryResponse403
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    PaginatedLoginHistoryList
    | ProfileLoginHistoryResponse400
    | ProfileLoginHistoryResponse401
    | ProfileLoginHistoryResponse403
]:
    """List your recent successful sign-ins

     Returns only the authenticated user's latest personal sign-ins, newest first. At most 50 records are
    retained per account. Refreshes, API key requests, failed attempts and impersonation are excluded.
    Client metadata is descriptive, not proof of identity; location is present only when supplied by
    trusted Cloudflare edges.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLoginHistoryList | ProfileLoginHistoryResponse400 | ProfileLoginHistoryResponse401 | ProfileLoginHistoryResponse403]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    PaginatedLoginHistoryList
    | ProfileLoginHistoryResponse400
    | ProfileLoginHistoryResponse401
    | ProfileLoginHistoryResponse403
    | None
):
    """List your recent successful sign-ins

     Returns only the authenticated user's latest personal sign-ins, newest first. At most 50 records are
    retained per account. Refreshes, API key requests, failed attempts and impersonation are excluded.
    Client metadata is descriptive, not proof of identity; location is present only when supplied by
    trusted Cloudflare edges.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLoginHistoryList | ProfileLoginHistoryResponse400 | ProfileLoginHistoryResponse401 | ProfileLoginHistoryResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

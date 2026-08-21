from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_reward_list import PaginatedRewardList
from ...models.rewards_list_level import RewardsListLevel
from ...models.rewards_list_response_400 import RewardsListResponse400
from ...models.rewards_list_response_401 import RewardsListResponse401
from ...models.rewards_list_response_403 import RewardsListResponse403
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    *,
    level: RewardsListLevel | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    user_email: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    json_level: str | Unset = UNSET
    if not isinstance(level, Unset):
        json_level = level.value

    params["level"] = json_level

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params["user__email"] = user_email

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["user__id"] = json_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rewards",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PaginatedRewardList
    | RewardsListResponse400
    | RewardsListResponse401
    | RewardsListResponse403
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedRewardList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RewardsListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RewardsListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = RewardsListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PaginatedRewardList | RewardsListResponse400 | RewardsListResponse401 | RewardsListResponse403
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
    level: RewardsListLevel | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    user_email: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    PaginatedRewardList | RewardsListResponse400 | RewardsListResponse401 | RewardsListResponse403
]:
    """List account rewards

     Returns referral and campaign rewards earned by the authenticated account, ordered from newest to
    oldest.

    Args:
        level (RewardsListLevel | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        user_email (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRewardList | RewardsListResponse400 | RewardsListResponse401 | RewardsListResponse403]
    """

    kwargs = _get_kwargs(
        level=level,
        limit=limit,
        offset=offset,
        ordering=ordering,
        user_email=user_email,
        user_id=user_id,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    level: RewardsListLevel | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    user_email: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    PaginatedRewardList
    | RewardsListResponse400
    | RewardsListResponse401
    | RewardsListResponse403
    | None
):
    """List account rewards

     Returns referral and campaign rewards earned by the authenticated account, ordered from newest to
    oldest.

    Args:
        level (RewardsListLevel | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        user_email (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRewardList | RewardsListResponse400 | RewardsListResponse401 | RewardsListResponse403
    """

    return sync_detailed(
        client=client,
        level=level,
        limit=limit,
        offset=offset,
        ordering=ordering,
        user_email=user_email,
        user_id=user_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    level: RewardsListLevel | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    user_email: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    PaginatedRewardList | RewardsListResponse400 | RewardsListResponse401 | RewardsListResponse403
]:
    """List account rewards

     Returns referral and campaign rewards earned by the authenticated account, ordered from newest to
    oldest.

    Args:
        level (RewardsListLevel | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        user_email (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRewardList | RewardsListResponse400 | RewardsListResponse401 | RewardsListResponse403]
    """

    kwargs = _get_kwargs(
        level=level,
        limit=limit,
        offset=offset,
        ordering=ordering,
        user_email=user_email,
        user_id=user_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    level: RewardsListLevel | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    user_email: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    PaginatedRewardList
    | RewardsListResponse400
    | RewardsListResponse401
    | RewardsListResponse403
    | None
):
    """List account rewards

     Returns referral and campaign rewards earned by the authenticated account, ordered from newest to
    oldest.

    Args:
        level (RewardsListLevel | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        user_email (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRewardList | RewardsListResponse400 | RewardsListResponse401 | RewardsListResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            level=level,
            limit=limit,
            offset=offset,
            ordering=ordering,
            user_email=user_email,
            user_id=user_id,
            accept_language=accept_language,
        )
    ).parsed

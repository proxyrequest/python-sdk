from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.analytics_overall_retrieve_response_400 import AnalyticsOverallRetrieveResponse400
from ...models.analytics_overall_retrieve_response_401 import AnalyticsOverallRetrieveResponse401
from ...models.analytics_overall_retrieve_response_403 import AnalyticsOverallRetrieveResponse403
from ...models.analytics_overall_retrieve_response_500 import AnalyticsOverallRetrieveResponse500
from ...models.overall_response import OverallResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime


def _get_kwargs(
    *,
    end: datetime.datetime | Unset = UNSET,
    include_sub_users: bool | Unset = False,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    json_end: str | Unset = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

    params["include_sub_users"] = include_sub_users

    params["limit"] = limit

    params["offset"] = offset

    json_package_id: str | Unset = UNSET
    if not isinstance(package_id, Unset):
        json_package_id = str(package_id)
    params["package_id"] = json_package_id

    json_start: str | Unset = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    params["timezone"] = timezone

    json_user_id: str | Unset = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["user_id"] = json_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/overall",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AnalyticsOverallRetrieveResponse400
    | AnalyticsOverallRetrieveResponse401
    | AnalyticsOverallRetrieveResponse403
    | AnalyticsOverallRetrieveResponse500
    | OverallResponse
    | None
):
    if response.status_code == 200:
        response_200 = OverallResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AnalyticsOverallRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AnalyticsOverallRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AnalyticsOverallRetrieveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = AnalyticsOverallRetrieveResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AnalyticsOverallRetrieveResponse400
    | AnalyticsOverallRetrieveResponse401
    | AnalyticsOverallRetrieveResponse403
    | AnalyticsOverallRetrieveResponse500
    | OverallResponse
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
    end: datetime.datetime | Unset = UNSET,
    include_sub_users: bool | Unset = False,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    AnalyticsOverallRetrieveResponse400
    | AnalyticsOverallRetrieveResponse401
    | AnalyticsOverallRetrieveResponse403
    | AnalyticsOverallRetrieveResponse500
    | OverallResponse
]:
    """Get traffic totals over time

     Returns transferred bytes and request counts grouped into time buckets for charts and usage
    reporting.

    Args:
        end (datetime.datetime | Unset):
        include_sub_users (bool | Unset):  Default: False.
        limit (int | Unset):
        offset (int | Unset):
        package_id (UUID | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsOverallRetrieveResponse400 | AnalyticsOverallRetrieveResponse401 | AnalyticsOverallRetrieveResponse403 | AnalyticsOverallRetrieveResponse500 | OverallResponse]
    """

    kwargs = _get_kwargs(
        end=end,
        include_sub_users=include_sub_users,
        limit=limit,
        offset=offset,
        package_id=package_id,
        start=start,
        timezone=timezone,
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
    end: datetime.datetime | Unset = UNSET,
    include_sub_users: bool | Unset = False,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    AnalyticsOverallRetrieveResponse400
    | AnalyticsOverallRetrieveResponse401
    | AnalyticsOverallRetrieveResponse403
    | AnalyticsOverallRetrieveResponse500
    | OverallResponse
    | None
):
    """Get traffic totals over time

     Returns transferred bytes and request counts grouped into time buckets for charts and usage
    reporting.

    Args:
        end (datetime.datetime | Unset):
        include_sub_users (bool | Unset):  Default: False.
        limit (int | Unset):
        offset (int | Unset):
        package_id (UUID | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsOverallRetrieveResponse400 | AnalyticsOverallRetrieveResponse401 | AnalyticsOverallRetrieveResponse403 | AnalyticsOverallRetrieveResponse500 | OverallResponse
    """

    return sync_detailed(
        client=client,
        end=end,
        include_sub_users=include_sub_users,
        limit=limit,
        offset=offset,
        package_id=package_id,
        start=start,
        timezone=timezone,
        user_id=user_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    end: datetime.datetime | Unset = UNSET,
    include_sub_users: bool | Unset = False,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    AnalyticsOverallRetrieveResponse400
    | AnalyticsOverallRetrieveResponse401
    | AnalyticsOverallRetrieveResponse403
    | AnalyticsOverallRetrieveResponse500
    | OverallResponse
]:
    """Get traffic totals over time

     Returns transferred bytes and request counts grouped into time buckets for charts and usage
    reporting.

    Args:
        end (datetime.datetime | Unset):
        include_sub_users (bool | Unset):  Default: False.
        limit (int | Unset):
        offset (int | Unset):
        package_id (UUID | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsOverallRetrieveResponse400 | AnalyticsOverallRetrieveResponse401 | AnalyticsOverallRetrieveResponse403 | AnalyticsOverallRetrieveResponse500 | OverallResponse]
    """

    kwargs = _get_kwargs(
        end=end,
        include_sub_users=include_sub_users,
        limit=limit,
        offset=offset,
        package_id=package_id,
        start=start,
        timezone=timezone,
        user_id=user_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    end: datetime.datetime | Unset = UNSET,
    include_sub_users: bool | Unset = False,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    AnalyticsOverallRetrieveResponse400
    | AnalyticsOverallRetrieveResponse401
    | AnalyticsOverallRetrieveResponse403
    | AnalyticsOverallRetrieveResponse500
    | OverallResponse
    | None
):
    """Get traffic totals over time

     Returns transferred bytes and request counts grouped into time buckets for charts and usage
    reporting.

    Args:
        end (datetime.datetime | Unset):
        include_sub_users (bool | Unset):  Default: False.
        limit (int | Unset):
        offset (int | Unset):
        package_id (UUID | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsOverallRetrieveResponse400 | AnalyticsOverallRetrieveResponse401 | AnalyticsOverallRetrieveResponse403 | AnalyticsOverallRetrieveResponse500 | OverallResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            end=end,
            include_sub_users=include_sub_users,
            limit=limit,
            offset=offset,
            package_id=package_id,
            start=start,
            timezone=timezone,
            user_id=user_id,
            accept_language=accept_language,
        )
    ).parsed

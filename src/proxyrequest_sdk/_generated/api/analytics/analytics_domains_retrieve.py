from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.analytics_domains_retrieve_ordering import AnalyticsDomainsRetrieveOrdering
from ...models.analytics_domains_retrieve_response_400 import AnalyticsDomainsRetrieveResponse400
from ...models.analytics_domains_retrieve_response_401 import AnalyticsDomainsRetrieveResponse401
from ...models.analytics_domains_retrieve_response_403 import AnalyticsDomainsRetrieveResponse403
from ...models.analytics_domains_retrieve_response_500 import AnalyticsDomainsRetrieveResponse500
from ...models.domains_response import DomainsResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime


def _get_kwargs(
    *,
    end: datetime.datetime | Unset = UNSET,
    hostname: str | Unset = UNSET,
    include_sub_users: bool | Unset = False,
    ledger_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: AnalyticsDomainsRetrieveOrdering | Unset = AnalyticsDomainsRetrieveOrdering.VALUE_0,
    package_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
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

    params["hostname"] = hostname

    params["include_sub_users"] = include_sub_users

    json_ledger_id: str | Unset = UNSET
    if not isinstance(ledger_id, Unset):
        json_ledger_id = str(ledger_id)
    params["ledger_id"] = json_ledger_id

    params["limit"] = limit

    params["offset"] = offset

    json_ordering: str | Unset = UNSET
    if not isinstance(ordering, Unset):
        json_ordering = ordering.value

    params["ordering"] = json_ordering

    json_package_id: str | Unset = UNSET
    if not isinstance(package_id, Unset):
        json_package_id = str(package_id)
    params["package_id"] = json_package_id

    params["search"] = search

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
        "url": "/analytics/domains",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AnalyticsDomainsRetrieveResponse400
    | AnalyticsDomainsRetrieveResponse401
    | AnalyticsDomainsRetrieveResponse403
    | AnalyticsDomainsRetrieveResponse500
    | DomainsResponse
    | None
):
    if response.status_code == 200:
        response_200 = DomainsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AnalyticsDomainsRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AnalyticsDomainsRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AnalyticsDomainsRetrieveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = AnalyticsDomainsRetrieveResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AnalyticsDomainsRetrieveResponse400
    | AnalyticsDomainsRetrieveResponse401
    | AnalyticsDomainsRetrieveResponse403
    | AnalyticsDomainsRetrieveResponse500
    | DomainsResponse
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
    hostname: str | Unset = UNSET,
    include_sub_users: bool | Unset = False,
    ledger_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: AnalyticsDomainsRetrieveOrdering | Unset = AnalyticsDomainsRetrieveOrdering.VALUE_0,
    package_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    AnalyticsDomainsRetrieveResponse400
    | AnalyticsDomainsRetrieveResponse401
    | AnalyticsDomainsRetrieveResponse403
    | AnalyticsDomainsRetrieveResponse500
    | DomainsResponse
]:
    """List top destination domains

     Aggregates request count and transferred bytes by destination hostname for the selected reporting
    window and account scope.

    Args:
        end (datetime.datetime | Unset):
        hostname (str | Unset):
        include_sub_users (bool | Unset):  Default: False.
        ledger_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (AnalyticsDomainsRetrieveOrdering | Unset):  Default:
            AnalyticsDomainsRetrieveOrdering.VALUE_0.
        package_id (UUID | Unset):
        search (str | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsDomainsRetrieveResponse400 | AnalyticsDomainsRetrieveResponse401 | AnalyticsDomainsRetrieveResponse403 | AnalyticsDomainsRetrieveResponse500 | DomainsResponse]
    """

    kwargs = _get_kwargs(
        end=end,
        hostname=hostname,
        include_sub_users=include_sub_users,
        ledger_id=ledger_id,
        limit=limit,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        search=search,
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
    hostname: str | Unset = UNSET,
    include_sub_users: bool | Unset = False,
    ledger_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: AnalyticsDomainsRetrieveOrdering | Unset = AnalyticsDomainsRetrieveOrdering.VALUE_0,
    package_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    AnalyticsDomainsRetrieveResponse400
    | AnalyticsDomainsRetrieveResponse401
    | AnalyticsDomainsRetrieveResponse403
    | AnalyticsDomainsRetrieveResponse500
    | DomainsResponse
    | None
):
    """List top destination domains

     Aggregates request count and transferred bytes by destination hostname for the selected reporting
    window and account scope.

    Args:
        end (datetime.datetime | Unset):
        hostname (str | Unset):
        include_sub_users (bool | Unset):  Default: False.
        ledger_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (AnalyticsDomainsRetrieveOrdering | Unset):  Default:
            AnalyticsDomainsRetrieveOrdering.VALUE_0.
        package_id (UUID | Unset):
        search (str | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsDomainsRetrieveResponse400 | AnalyticsDomainsRetrieveResponse401 | AnalyticsDomainsRetrieveResponse403 | AnalyticsDomainsRetrieveResponse500 | DomainsResponse
    """

    return sync_detailed(
        client=client,
        end=end,
        hostname=hostname,
        include_sub_users=include_sub_users,
        ledger_id=ledger_id,
        limit=limit,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        search=search,
        start=start,
        timezone=timezone,
        user_id=user_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    end: datetime.datetime | Unset = UNSET,
    hostname: str | Unset = UNSET,
    include_sub_users: bool | Unset = False,
    ledger_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: AnalyticsDomainsRetrieveOrdering | Unset = AnalyticsDomainsRetrieveOrdering.VALUE_0,
    package_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    AnalyticsDomainsRetrieveResponse400
    | AnalyticsDomainsRetrieveResponse401
    | AnalyticsDomainsRetrieveResponse403
    | AnalyticsDomainsRetrieveResponse500
    | DomainsResponse
]:
    """List top destination domains

     Aggregates request count and transferred bytes by destination hostname for the selected reporting
    window and account scope.

    Args:
        end (datetime.datetime | Unset):
        hostname (str | Unset):
        include_sub_users (bool | Unset):  Default: False.
        ledger_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (AnalyticsDomainsRetrieveOrdering | Unset):  Default:
            AnalyticsDomainsRetrieveOrdering.VALUE_0.
        package_id (UUID | Unset):
        search (str | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsDomainsRetrieveResponse400 | AnalyticsDomainsRetrieveResponse401 | AnalyticsDomainsRetrieveResponse403 | AnalyticsDomainsRetrieveResponse500 | DomainsResponse]
    """

    kwargs = _get_kwargs(
        end=end,
        hostname=hostname,
        include_sub_users=include_sub_users,
        ledger_id=ledger_id,
        limit=limit,
        offset=offset,
        ordering=ordering,
        package_id=package_id,
        search=search,
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
    hostname: str | Unset = UNSET,
    include_sub_users: bool | Unset = False,
    ledger_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: AnalyticsDomainsRetrieveOrdering | Unset = AnalyticsDomainsRetrieveOrdering.VALUE_0,
    package_id: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    AnalyticsDomainsRetrieveResponse400
    | AnalyticsDomainsRetrieveResponse401
    | AnalyticsDomainsRetrieveResponse403
    | AnalyticsDomainsRetrieveResponse500
    | DomainsResponse
    | None
):
    """List top destination domains

     Aggregates request count and transferred bytes by destination hostname for the selected reporting
    window and account scope.

    Args:
        end (datetime.datetime | Unset):
        hostname (str | Unset):
        include_sub_users (bool | Unset):  Default: False.
        ledger_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        ordering (AnalyticsDomainsRetrieveOrdering | Unset):  Default:
            AnalyticsDomainsRetrieveOrdering.VALUE_0.
        package_id (UUID | Unset):
        search (str | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsDomainsRetrieveResponse400 | AnalyticsDomainsRetrieveResponse401 | AnalyticsDomainsRetrieveResponse403 | AnalyticsDomainsRetrieveResponse500 | DomainsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            end=end,
            hostname=hostname,
            include_sub_users=include_sub_users,
            ledger_id=ledger_id,
            limit=limit,
            offset=offset,
            ordering=ordering,
            package_id=package_id,
            search=search,
            start=start,
            timezone=timezone,
            user_id=user_id,
            accept_language=accept_language,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.analytics_logs_retrieve_protocol import AnalyticsLogsRetrieveProtocol
from ...models.analytics_logs_retrieve_response_400 import AnalyticsLogsRetrieveResponse400
from ...models.analytics_logs_retrieve_response_401 import AnalyticsLogsRetrieveResponse401
from ...models.analytics_logs_retrieve_response_403 import AnalyticsLogsRetrieveResponse403
from ...models.analytics_logs_retrieve_response_500 import AnalyticsLogsRetrieveResponse500
from ...models.logs_response import LogsResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime


def _get_kwargs(
    *,
    city: str | Unset = UNSET,
    country: str | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    error_code: int | Unset = UNSET,
    hostname: str | Unset = UNSET,
    ledger_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    protocol: AnalyticsLogsRetrieveProtocol | Unset = UNSET,
    region: str | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["city"] = city

    params["country"] = country

    json_end: str | Unset = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

    params["error_code"] = error_code

    params["hostname"] = hostname

    json_ledger_id: str | Unset = UNSET
    if not isinstance(ledger_id, Unset):
        json_ledger_id = str(ledger_id)
    params["ledger_id"] = json_ledger_id

    params["limit"] = limit

    params["offset"] = offset

    json_package_id: str | Unset = UNSET
    if not isinstance(package_id, Unset):
        json_package_id = str(package_id)
    params["package_id"] = json_package_id

    json_protocol: str | Unset = UNSET
    if not isinstance(protocol, Unset):
        json_protocol = protocol.value

    params["protocol"] = json_protocol

    params["region"] = region

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
        "url": "/analytics/logs",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AnalyticsLogsRetrieveResponse400
    | AnalyticsLogsRetrieveResponse401
    | AnalyticsLogsRetrieveResponse403
    | AnalyticsLogsRetrieveResponse500
    | LogsResponse
    | None
):
    if response.status_code == 200:
        response_200 = LogsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AnalyticsLogsRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AnalyticsLogsRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AnalyticsLogsRetrieveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = AnalyticsLogsRetrieveResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AnalyticsLogsRetrieveResponse400
    | AnalyticsLogsRetrieveResponse401
    | AnalyticsLogsRetrieveResponse403
    | AnalyticsLogsRetrieveResponse500
    | LogsResponse
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
    city: str | Unset = UNSET,
    country: str | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    error_code: int | Unset = UNSET,
    hostname: str | Unset = UNSET,
    ledger_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    protocol: AnalyticsLogsRetrieveProtocol | Unset = UNSET,
    region: str | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    AnalyticsLogsRetrieveResponse400
    | AnalyticsLogsRetrieveResponse401
    | AnalyticsLogsRetrieveResponse403
    | AnalyticsLogsRetrieveResponse500
    | LogsResponse
]:
    """List proxy error logs

     Returns request-level proxy errors with server, client, targeting, package, and error-code context.

    Args:
        city (str | Unset):
        country (str | Unset):
        end (datetime.datetime | Unset):
        error_code (int | Unset):
        hostname (str | Unset):
        ledger_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        package_id (UUID | Unset):
        protocol (AnalyticsLogsRetrieveProtocol | Unset):
        region (str | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsLogsRetrieveResponse400 | AnalyticsLogsRetrieveResponse401 | AnalyticsLogsRetrieveResponse403 | AnalyticsLogsRetrieveResponse500 | LogsResponse]
    """

    kwargs = _get_kwargs(
        city=city,
        country=country,
        end=end,
        error_code=error_code,
        hostname=hostname,
        ledger_id=ledger_id,
        limit=limit,
        offset=offset,
        package_id=package_id,
        protocol=protocol,
        region=region,
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
    city: str | Unset = UNSET,
    country: str | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    error_code: int | Unset = UNSET,
    hostname: str | Unset = UNSET,
    ledger_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    protocol: AnalyticsLogsRetrieveProtocol | Unset = UNSET,
    region: str | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    AnalyticsLogsRetrieveResponse400
    | AnalyticsLogsRetrieveResponse401
    | AnalyticsLogsRetrieveResponse403
    | AnalyticsLogsRetrieveResponse500
    | LogsResponse
    | None
):
    """List proxy error logs

     Returns request-level proxy errors with server, client, targeting, package, and error-code context.

    Args:
        city (str | Unset):
        country (str | Unset):
        end (datetime.datetime | Unset):
        error_code (int | Unset):
        hostname (str | Unset):
        ledger_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        package_id (UUID | Unset):
        protocol (AnalyticsLogsRetrieveProtocol | Unset):
        region (str | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsLogsRetrieveResponse400 | AnalyticsLogsRetrieveResponse401 | AnalyticsLogsRetrieveResponse403 | AnalyticsLogsRetrieveResponse500 | LogsResponse
    """

    return sync_detailed(
        client=client,
        city=city,
        country=country,
        end=end,
        error_code=error_code,
        hostname=hostname,
        ledger_id=ledger_id,
        limit=limit,
        offset=offset,
        package_id=package_id,
        protocol=protocol,
        region=region,
        start=start,
        timezone=timezone,
        user_id=user_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    city: str | Unset = UNSET,
    country: str | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    error_code: int | Unset = UNSET,
    hostname: str | Unset = UNSET,
    ledger_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    protocol: AnalyticsLogsRetrieveProtocol | Unset = UNSET,
    region: str | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    AnalyticsLogsRetrieveResponse400
    | AnalyticsLogsRetrieveResponse401
    | AnalyticsLogsRetrieveResponse403
    | AnalyticsLogsRetrieveResponse500
    | LogsResponse
]:
    """List proxy error logs

     Returns request-level proxy errors with server, client, targeting, package, and error-code context.

    Args:
        city (str | Unset):
        country (str | Unset):
        end (datetime.datetime | Unset):
        error_code (int | Unset):
        hostname (str | Unset):
        ledger_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        package_id (UUID | Unset):
        protocol (AnalyticsLogsRetrieveProtocol | Unset):
        region (str | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsLogsRetrieveResponse400 | AnalyticsLogsRetrieveResponse401 | AnalyticsLogsRetrieveResponse403 | AnalyticsLogsRetrieveResponse500 | LogsResponse]
    """

    kwargs = _get_kwargs(
        city=city,
        country=country,
        end=end,
        error_code=error_code,
        hostname=hostname,
        ledger_id=ledger_id,
        limit=limit,
        offset=offset,
        package_id=package_id,
        protocol=protocol,
        region=region,
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
    city: str | Unset = UNSET,
    country: str | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    error_code: int | Unset = UNSET,
    hostname: str | Unset = UNSET,
    ledger_id: UUID | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    package_id: UUID | Unset = UNSET,
    protocol: AnalyticsLogsRetrieveProtocol | Unset = UNSET,
    region: str | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    user_id: UUID | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    AnalyticsLogsRetrieveResponse400
    | AnalyticsLogsRetrieveResponse401
    | AnalyticsLogsRetrieveResponse403
    | AnalyticsLogsRetrieveResponse500
    | LogsResponse
    | None
):
    """List proxy error logs

     Returns request-level proxy errors with server, client, targeting, package, and error-code context.

    Args:
        city (str | Unset):
        country (str | Unset):
        end (datetime.datetime | Unset):
        error_code (int | Unset):
        hostname (str | Unset):
        ledger_id (UUID | Unset):
        limit (int | Unset):
        offset (int | Unset):
        package_id (UUID | Unset):
        protocol (AnalyticsLogsRetrieveProtocol | Unset):
        region (str | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        user_id (UUID | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsLogsRetrieveResponse400 | AnalyticsLogsRetrieveResponse401 | AnalyticsLogsRetrieveResponse403 | AnalyticsLogsRetrieveResponse500 | LogsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            city=city,
            country=country,
            end=end,
            error_code=error_code,
            hostname=hostname,
            ledger_id=ledger_id,
            limit=limit,
            offset=offset,
            package_id=package_id,
            protocol=protocol,
            region=region,
            start=start,
            timezone=timezone,
            user_id=user_id,
            accept_language=accept_language,
        )
    ).parsed

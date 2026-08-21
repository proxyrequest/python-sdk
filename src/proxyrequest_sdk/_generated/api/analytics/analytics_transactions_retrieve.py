from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.analytics_transactions_retrieve_response_400 import (
    AnalyticsTransactionsRetrieveResponse400,
)
from ...models.analytics_transactions_retrieve_response_401 import (
    AnalyticsTransactionsRetrieveResponse401,
)
from ...models.analytics_transactions_retrieve_response_403 import (
    AnalyticsTransactionsRetrieveResponse403,
)
from ...models.analytics_transactions_retrieve_response_404 import (
    AnalyticsTransactionsRetrieveResponse404,
)
from ...models.analytics_transactions_retrieve_response_500 import (
    AnalyticsTransactionsRetrieveResponse500,
)
from ...models.transactions_response import TransactionsResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime


def _get_kwargs(
    id: str,
    *,
    end: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    recipient_id: UUID | Unset = UNSET,
    sender_id: UUID | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    type_: int | Unset = UNSET,
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

    params["limit"] = limit

    params["offset"] = offset

    json_recipient_id: str | Unset = UNSET
    if not isinstance(recipient_id, Unset):
        json_recipient_id = str(recipient_id)
    params["recipient_id"] = json_recipient_id

    json_sender_id: str | Unset = UNSET
    if not isinstance(sender_id, Unset):
        json_sender_id = str(sender_id)
    params["sender_id"] = json_sender_id

    json_start: str | Unset = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    params["timezone"] = timezone

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/{id}/transactions".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AnalyticsTransactionsRetrieveResponse400
    | AnalyticsTransactionsRetrieveResponse401
    | AnalyticsTransactionsRetrieveResponse403
    | AnalyticsTransactionsRetrieveResponse404
    | AnalyticsTransactionsRetrieveResponse500
    | TransactionsResponse
    | None
):
    if response.status_code == 200:
        response_200 = TransactionsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AnalyticsTransactionsRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AnalyticsTransactionsRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AnalyticsTransactionsRetrieveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AnalyticsTransactionsRetrieveResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = AnalyticsTransactionsRetrieveResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AnalyticsTransactionsRetrieveResponse400
    | AnalyticsTransactionsRetrieveResponse401
    | AnalyticsTransactionsRetrieveResponse403
    | AnalyticsTransactionsRetrieveResponse404
    | AnalyticsTransactionsRetrieveResponse500
    | TransactionsResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    end: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    recipient_id: UUID | Unset = UNSET,
    sender_id: UUID | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    type_: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    AnalyticsTransactionsRetrieveResponse400
    | AnalyticsTransactionsRetrieveResponse401
    | AnalyticsTransactionsRetrieveResponse403
    | AnalyticsTransactionsRetrieveResponse404
    | AnalyticsTransactionsRetrieveResponse500
    | TransactionsResponse
]:
    """List data transactions

     Returns data allocation and consumption transactions visible to the caller. Sender and recipient
    filters are restricted to the caller's scope.

    Args:
        id (str):
        end (datetime.datetime | Unset):
        limit (int | Unset):
        offset (int | Unset):
        recipient_id (UUID | Unset):
        sender_id (UUID | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        type_ (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsTransactionsRetrieveResponse400 | AnalyticsTransactionsRetrieveResponse401 | AnalyticsTransactionsRetrieveResponse403 | AnalyticsTransactionsRetrieveResponse404 | AnalyticsTransactionsRetrieveResponse500 | TransactionsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        end=end,
        limit=limit,
        offset=offset,
        recipient_id=recipient_id,
        sender_id=sender_id,
        start=start,
        timezone=timezone,
        type_=type_,
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
    end: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    recipient_id: UUID | Unset = UNSET,
    sender_id: UUID | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    type_: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    AnalyticsTransactionsRetrieveResponse400
    | AnalyticsTransactionsRetrieveResponse401
    | AnalyticsTransactionsRetrieveResponse403
    | AnalyticsTransactionsRetrieveResponse404
    | AnalyticsTransactionsRetrieveResponse500
    | TransactionsResponse
    | None
):
    """List data transactions

     Returns data allocation and consumption transactions visible to the caller. Sender and recipient
    filters are restricted to the caller's scope.

    Args:
        id (str):
        end (datetime.datetime | Unset):
        limit (int | Unset):
        offset (int | Unset):
        recipient_id (UUID | Unset):
        sender_id (UUID | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        type_ (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsTransactionsRetrieveResponse400 | AnalyticsTransactionsRetrieveResponse401 | AnalyticsTransactionsRetrieveResponse403 | AnalyticsTransactionsRetrieveResponse404 | AnalyticsTransactionsRetrieveResponse500 | TransactionsResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        end=end,
        limit=limit,
        offset=offset,
        recipient_id=recipient_id,
        sender_id=sender_id,
        start=start,
        timezone=timezone,
        type_=type_,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    end: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    recipient_id: UUID | Unset = UNSET,
    sender_id: UUID | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    type_: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    AnalyticsTransactionsRetrieveResponse400
    | AnalyticsTransactionsRetrieveResponse401
    | AnalyticsTransactionsRetrieveResponse403
    | AnalyticsTransactionsRetrieveResponse404
    | AnalyticsTransactionsRetrieveResponse500
    | TransactionsResponse
]:
    """List data transactions

     Returns data allocation and consumption transactions visible to the caller. Sender and recipient
    filters are restricted to the caller's scope.

    Args:
        id (str):
        end (datetime.datetime | Unset):
        limit (int | Unset):
        offset (int | Unset):
        recipient_id (UUID | Unset):
        sender_id (UUID | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        type_ (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsTransactionsRetrieveResponse400 | AnalyticsTransactionsRetrieveResponse401 | AnalyticsTransactionsRetrieveResponse403 | AnalyticsTransactionsRetrieveResponse404 | AnalyticsTransactionsRetrieveResponse500 | TransactionsResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        end=end,
        limit=limit,
        offset=offset,
        recipient_id=recipient_id,
        sender_id=sender_id,
        start=start,
        timezone=timezone,
        type_=type_,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    end: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    recipient_id: UUID | Unset = UNSET,
    sender_id: UUID | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    timezone: str | Unset = UNSET,
    type_: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    AnalyticsTransactionsRetrieveResponse400
    | AnalyticsTransactionsRetrieveResponse401
    | AnalyticsTransactionsRetrieveResponse403
    | AnalyticsTransactionsRetrieveResponse404
    | AnalyticsTransactionsRetrieveResponse500
    | TransactionsResponse
    | None
):
    """List data transactions

     Returns data allocation and consumption transactions visible to the caller. Sender and recipient
    filters are restricted to the caller's scope.

    Args:
        id (str):
        end (datetime.datetime | Unset):
        limit (int | Unset):
        offset (int | Unset):
        recipient_id (UUID | Unset):
        sender_id (UUID | Unset):
        start (datetime.datetime | Unset):
        timezone (str | Unset):
        type_ (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsTransactionsRetrieveResponse400 | AnalyticsTransactionsRetrieveResponse401 | AnalyticsTransactionsRetrieveResponse403 | AnalyticsTransactionsRetrieveResponse404 | AnalyticsTransactionsRetrieveResponse500 | TransactionsResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            end=end,
            limit=limit,
            offset=offset,
            recipient_id=recipient_id,
            sender_id=sender_id,
            start=start,
            timezone=timezone,
            type_=type_,
            accept_language=accept_language,
        )
    ).parsed

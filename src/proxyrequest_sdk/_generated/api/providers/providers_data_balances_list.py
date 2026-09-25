from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_provider_data_balance_list import PaginatedProviderDataBalanceList
from ...models.providers_data_balances_list_response_400 import ProvidersDataBalancesListResponse400
from ...models.providers_data_balances_list_response_401 import ProvidersDataBalancesListResponse401
from ...models.providers_data_balances_list_response_403 import ProvidersDataBalancesListResponse403
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/providers/data-balances",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PaginatedProviderDataBalanceList
    | ProvidersDataBalancesListResponse400
    | ProvidersDataBalancesListResponse401
    | ProvidersDataBalancesListResponse403
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedProviderDataBalanceList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProvidersDataBalancesListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProvidersDataBalancesListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProvidersDataBalancesListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PaginatedProviderDataBalanceList
    | ProvidersDataBalancesListResponse400
    | ProvidersDataBalancesListResponse401
    | ProvidersDataBalancesListResponse403
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
) -> Response[
    PaginatedProviderDataBalanceList
    | ProvidersDataBalancesListResponse400
    | ProvidersDataBalancesListResponse401
    | ProvidersDataBalancesListResponse403
]:
    """List provider data balances

     Requires a JWT belonging to an active superuser or an API key owned by an active superuser,
    including requests using X-Impersonate-User. Returns one result per provider with recorded balances.
    The latest observation by observed_at is the baseline; available_bytes is that observation's
    balance, not a sum of purchased data. All byte amounts are decimal strings. Calculations are saved
    asynchronously; inspect freshness, error and calculated_at before using them. History is ordered by
    creation time descending and limited by PROVIDER_DATA_BALANCE_HISTORY_LIMIT (default 10). Pagination
    counts providers, not history entries.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedProviderDataBalanceList | ProvidersDataBalancesListResponse400 | ProvidersDataBalancesListResponse401 | ProvidersDataBalancesListResponse403]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        accept_language=accept_language,
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
) -> (
    PaginatedProviderDataBalanceList
    | ProvidersDataBalancesListResponse400
    | ProvidersDataBalancesListResponse401
    | ProvidersDataBalancesListResponse403
    | None
):
    """List provider data balances

     Requires a JWT belonging to an active superuser or an API key owned by an active superuser,
    including requests using X-Impersonate-User. Returns one result per provider with recorded balances.
    The latest observation by observed_at is the baseline; available_bytes is that observation's
    balance, not a sum of purchased data. All byte amounts are decimal strings. Calculations are saved
    asynchronously; inspect freshness, error and calculated_at before using them. History is ordered by
    creation time descending and limited by PROVIDER_DATA_BALANCE_HISTORY_LIMIT (default 10). Pagination
    counts providers, not history entries.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedProviderDataBalanceList | ProvidersDataBalancesListResponse400 | ProvidersDataBalancesListResponse401 | ProvidersDataBalancesListResponse403
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    PaginatedProviderDataBalanceList
    | ProvidersDataBalancesListResponse400
    | ProvidersDataBalancesListResponse401
    | ProvidersDataBalancesListResponse403
]:
    """List provider data balances

     Requires a JWT belonging to an active superuser or an API key owned by an active superuser,
    including requests using X-Impersonate-User. Returns one result per provider with recorded balances.
    The latest observation by observed_at is the baseline; available_bytes is that observation's
    balance, not a sum of purchased data. All byte amounts are decimal strings. Calculations are saved
    asynchronously; inspect freshness, error and calculated_at before using them. History is ordered by
    creation time descending and limited by PROVIDER_DATA_BALANCE_HISTORY_LIMIT (default 10). Pagination
    counts providers, not history entries.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedProviderDataBalanceList | ProvidersDataBalancesListResponse400 | ProvidersDataBalancesListResponse401 | ProvidersDataBalancesListResponse403]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> (
    PaginatedProviderDataBalanceList
    | ProvidersDataBalancesListResponse400
    | ProvidersDataBalancesListResponse401
    | ProvidersDataBalancesListResponse403
    | None
):
    """List provider data balances

     Requires a JWT belonging to an active superuser or an API key owned by an active superuser,
    including requests using X-Impersonate-User. Returns one result per provider with recorded balances.
    The latest observation by observed_at is the baseline; available_bytes is that observation's
    balance, not a sum of purchased data. All byte amounts are decimal strings. Calculations are saved
    asynchronously; inspect freshness, error and calculated_at before using them. History is ordered by
    creation time descending and limited by PROVIDER_DATA_BALANCE_HISTORY_LIMIT (default 10). Pagination
    counts providers, not history entries.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedProviderDataBalanceList | ProvidersDataBalancesListResponse400 | ProvidersDataBalancesListResponse401 | ProvidersDataBalancesListResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            accept_language=accept_language,
        )
    ).parsed

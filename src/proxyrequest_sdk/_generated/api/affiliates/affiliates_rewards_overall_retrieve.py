from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.affiliate_stats_response import AffiliateStatsResponse
from ...models.affiliates_rewards_overall_retrieve_response_400 import (
    AffiliatesRewardsOverallRetrieveResponse400,
)
from ...models.affiliates_rewards_overall_retrieve_response_401 import (
    AffiliatesRewardsOverallRetrieveResponse401,
)
from ...models.affiliates_rewards_overall_retrieve_response_403 import (
    AffiliatesRewardsOverallRetrieveResponse403,
)
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliates/rewards/overall",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AffiliateStatsResponse
    | AffiliatesRewardsOverallRetrieveResponse400
    | AffiliatesRewardsOverallRetrieveResponse401
    | AffiliatesRewardsOverallRetrieveResponse403
    | None
):
    if response.status_code == 200:
        response_200 = AffiliateStatsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AffiliatesRewardsOverallRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AffiliatesRewardsOverallRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AffiliatesRewardsOverallRetrieveResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AffiliateStatsResponse
    | AffiliatesRewardsOverallRetrieveResponse400
    | AffiliatesRewardsOverallRetrieveResponse401
    | AffiliatesRewardsOverallRetrieveResponse403
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
    accept_language: str | Unset = UNSET,
) -> Response[
    AffiliateStatsResponse
    | AffiliatesRewardsOverallRetrieveResponse400
    | AffiliatesRewardsOverallRetrieveResponse401
    | AffiliatesRewardsOverallRetrieveResponse403
]:
    """Get affiliate earnings over time

     Returns affiliate reward totals for the requested date range. start, end, and timezone use the same
    rules as analytics endpoints.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffiliateStatsResponse | AffiliatesRewardsOverallRetrieveResponse400 | AffiliatesRewardsOverallRetrieveResponse401 | AffiliatesRewardsOverallRetrieveResponse403]
    """

    kwargs = _get_kwargs(
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
) -> (
    AffiliateStatsResponse
    | AffiliatesRewardsOverallRetrieveResponse400
    | AffiliatesRewardsOverallRetrieveResponse401
    | AffiliatesRewardsOverallRetrieveResponse403
    | None
):
    """Get affiliate earnings over time

     Returns affiliate reward totals for the requested date range. start, end, and timezone use the same
    rules as analytics endpoints.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffiliateStatsResponse | AffiliatesRewardsOverallRetrieveResponse400 | AffiliatesRewardsOverallRetrieveResponse401 | AffiliatesRewardsOverallRetrieveResponse403
    """

    return sync_detailed(
        client=client,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
) -> Response[
    AffiliateStatsResponse
    | AffiliatesRewardsOverallRetrieveResponse400
    | AffiliatesRewardsOverallRetrieveResponse401
    | AffiliatesRewardsOverallRetrieveResponse403
]:
    """Get affiliate earnings over time

     Returns affiliate reward totals for the requested date range. start, end, and timezone use the same
    rules as analytics endpoints.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffiliateStatsResponse | AffiliatesRewardsOverallRetrieveResponse400 | AffiliatesRewardsOverallRetrieveResponse401 | AffiliatesRewardsOverallRetrieveResponse403]
    """

    kwargs = _get_kwargs(
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
) -> (
    AffiliateStatsResponse
    | AffiliatesRewardsOverallRetrieveResponse400
    | AffiliatesRewardsOverallRetrieveResponse401
    | AffiliatesRewardsOverallRetrieveResponse403
    | None
):
    """Get affiliate earnings over time

     Returns affiliate reward totals for the requested date range. start, end, and timezone use the same
    rules as analytics endpoints.

    Args:
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffiliateStatsResponse | AffiliatesRewardsOverallRetrieveResponse400 | AffiliatesRewardsOverallRetrieveResponse401 | AffiliatesRewardsOverallRetrieveResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            accept_language=accept_language,
        )
    ).parsed

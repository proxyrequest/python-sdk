from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.affiliates_list_response_400 import AffiliatesListResponse400
from ...models.affiliates_list_response_401 import AffiliatesListResponse401
from ...models.affiliates_list_response_403 import AffiliatesListResponse403
from ...models.paginated_affiliate_list import PaginatedAffiliateList
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
        "url": "/affiliates",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AffiliatesListResponse400
    | AffiliatesListResponse401
    | AffiliatesListResponse403
    | PaginatedAffiliateList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedAffiliateList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AffiliatesListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AffiliatesListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AffiliatesListResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AffiliatesListResponse400
    | AffiliatesListResponse401
    | AffiliatesListResponse403
    | PaginatedAffiliateList
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[
    AffiliatesListResponse400
    | AffiliatesListResponse401
    | AffiliatesListResponse403
    | PaginatedAffiliateList
]:
    """List referred customers

     Returns customers attributed to the authenticated affiliate together with the referral information
    available to that account.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffiliatesListResponse400 | AffiliatesListResponse401 | AffiliatesListResponse403 | PaginatedAffiliateList]
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
    AffiliatesListResponse400
    | AffiliatesListResponse401
    | AffiliatesListResponse403
    | PaginatedAffiliateList
    | None
):
    """List referred customers

     Returns customers attributed to the authenticated affiliate together with the referral information
    available to that account.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffiliatesListResponse400 | AffiliatesListResponse401 | AffiliatesListResponse403 | PaginatedAffiliateList
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
    AffiliatesListResponse400
    | AffiliatesListResponse401
    | AffiliatesListResponse403
    | PaginatedAffiliateList
]:
    """List referred customers

     Returns customers attributed to the authenticated affiliate together with the referral information
    available to that account.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffiliatesListResponse400 | AffiliatesListResponse401 | AffiliatesListResponse403 | PaginatedAffiliateList]
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
    AffiliatesListResponse400
    | AffiliatesListResponse401
    | AffiliatesListResponse403
    | PaginatedAffiliateList
    | None
):
    """List referred customers

     Returns customers attributed to the authenticated affiliate together with the referral information
    available to that account.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        accept_language (str | Unset):  Defaults to the client language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffiliatesListResponse400 | AffiliatesListResponse401 | AffiliatesListResponse403 | PaginatedAffiliateList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            accept_language=accept_language,
        )
    ).parsed

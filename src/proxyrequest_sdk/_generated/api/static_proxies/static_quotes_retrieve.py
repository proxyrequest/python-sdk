from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rental_quote import RentalQuote
from ...models.static_quotes_retrieve_response_400 import StaticQuotesRetrieveResponse400
from ...models.static_quotes_retrieve_response_401 import StaticQuotesRetrieveResponse401
from ...models.static_quotes_retrieve_response_403 import StaticQuotesRetrieveResponse403
from ...models.static_quotes_retrieve_response_404 import StaticQuotesRetrieveResponse404
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    offer_id: UUID,
    *,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/static/quotes/{offer_id}".format(
            offer_id=quote(str(offer_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RentalQuote
    | StaticQuotesRetrieveResponse400
    | StaticQuotesRetrieveResponse401
    | StaticQuotesRetrieveResponse403
    | StaticQuotesRetrieveResponse404
    | None
):
    if response.status_code == 200:
        response_200 = RentalQuote.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StaticQuotesRetrieveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StaticQuotesRetrieveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = StaticQuotesRetrieveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = StaticQuotesRetrieveResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RentalQuote
    | StaticQuotesRetrieveResponse400
    | StaticQuotesRetrieveResponse401
    | StaticQuotesRetrieveResponse403
    | StaticQuotesRetrieveResponse404
]:
    parsed = parse_response(_parse_response, client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )


def sync_detailed(
    offer_id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    RentalQuote
    | StaticQuotesRetrieveResponse400
    | StaticQuotesRetrieveResponse401
    | StaticQuotesRetrieveResponse403
    | StaticQuotesRetrieveResponse404
]:
    """Quote an address bundle

     Read the current rental terms and full bundle price before reserving inventory. The quote itself
    does not reserve addresses or charge the account.

    Args:
        offer_id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RentalQuote | StaticQuotesRetrieveResponse400 | StaticQuotesRetrieveResponse401 | StaticQuotesRetrieveResponse403 | StaticQuotesRetrieveResponse404]
    """

    kwargs = _get_kwargs(
        offer_id=offer_id,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    offer_id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    RentalQuote
    | StaticQuotesRetrieveResponse400
    | StaticQuotesRetrieveResponse401
    | StaticQuotesRetrieveResponse403
    | StaticQuotesRetrieveResponse404
    | None
):
    """Quote an address bundle

     Read the current rental terms and full bundle price before reserving inventory. The quote itself
    does not reserve addresses or charge the account.

    Args:
        offer_id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RentalQuote | StaticQuotesRetrieveResponse400 | StaticQuotesRetrieveResponse401 | StaticQuotesRetrieveResponse403 | StaticQuotesRetrieveResponse404
    """

    return sync_detailed(
        offer_id=offer_id,
        client=client,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    offer_id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    RentalQuote
    | StaticQuotesRetrieveResponse400
    | StaticQuotesRetrieveResponse401
    | StaticQuotesRetrieveResponse403
    | StaticQuotesRetrieveResponse404
]:
    """Quote an address bundle

     Read the current rental terms and full bundle price before reserving inventory. The quote itself
    does not reserve addresses or charge the account.

    Args:
        offer_id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RentalQuote | StaticQuotesRetrieveResponse400 | StaticQuotesRetrieveResponse401 | StaticQuotesRetrieveResponse403 | StaticQuotesRetrieveResponse404]
    """

    kwargs = _get_kwargs(
        offer_id=offer_id,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    offer_id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    RentalQuote
    | StaticQuotesRetrieveResponse400
    | StaticQuotesRetrieveResponse401
    | StaticQuotesRetrieveResponse403
    | StaticQuotesRetrieveResponse404
    | None
):
    """Quote an address bundle

     Read the current rental terms and full bundle price before reserving inventory. The quote itself
    does not reserve addresses or charge the account.

    Args:
        offer_id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RentalQuote | StaticQuotesRetrieveResponse400 | StaticQuotesRetrieveResponse401 | StaticQuotesRetrieveResponse403 | StaticQuotesRetrieveResponse404
    """

    return (
        await asyncio_detailed(
            offer_id=offer_id,
            client=client,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

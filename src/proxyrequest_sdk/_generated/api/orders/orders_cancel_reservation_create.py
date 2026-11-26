from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.orders_cancel_reservation_create_response_400 import (
    OrdersCancelReservationCreateResponse400,
)
from ...models.orders_cancel_reservation_create_response_401 import (
    OrdersCancelReservationCreateResponse401,
)
from ...models.orders_cancel_reservation_create_response_403 import (
    OrdersCancelReservationCreateResponse403,
)
from ...models.orders_cancel_reservation_create_response_404 import (
    OrdersCancelReservationCreateResponse404,
)
from ...models.reservation_cancellation import ReservationCancellation
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    id: UUID,
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
        "method": "post",
        "url": "/orders/{id}/cancel-reservation".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    OrdersCancelReservationCreateResponse400
    | OrdersCancelReservationCreateResponse401
    | OrdersCancelReservationCreateResponse403
    | OrdersCancelReservationCreateResponse404
    | ReservationCancellation
    | None
):
    if response.status_code == 200:
        response_200 = ReservationCancellation.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OrdersCancelReservationCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrdersCancelReservationCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrdersCancelReservationCreateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = OrdersCancelReservationCreateResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    OrdersCancelReservationCreateResponse400
    | OrdersCancelReservationCreateResponse401
    | OrdersCancelReservationCreateResponse403
    | OrdersCancelReservationCreateResponse404
    | ReservationCancellation
]:
    parsed = parse_response(_parse_response, client=client, response=response)
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=parsed,
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    OrdersCancelReservationCreateResponse400
    | OrdersCancelReservationCreateResponse401
    | OrdersCancelReservationCreateResponse403
    | OrdersCancelReservationCreateResponse404
    | ReservationCancellation
]:
    """Cancel an unissued reservation

     Release the authenticated customer's reservation only before an invoice is created or any assignment
    is issued. Repeated cancellation is safe.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersCancelReservationCreateResponse400 | OrdersCancelReservationCreateResponse401 | OrdersCancelReservationCreateResponse403 | OrdersCancelReservationCreateResponse404 | ReservationCancellation]
    """

    kwargs = _get_kwargs(
        id=id,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    OrdersCancelReservationCreateResponse400
    | OrdersCancelReservationCreateResponse401
    | OrdersCancelReservationCreateResponse403
    | OrdersCancelReservationCreateResponse404
    | ReservationCancellation
    | None
):
    """Cancel an unissued reservation

     Release the authenticated customer's reservation only before an invoice is created or any assignment
    is issued. Repeated cancellation is safe.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersCancelReservationCreateResponse400 | OrdersCancelReservationCreateResponse401 | OrdersCancelReservationCreateResponse403 | OrdersCancelReservationCreateResponse404 | ReservationCancellation
    """

    return sync_detailed(
        id=id,
        client=client,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    OrdersCancelReservationCreateResponse400
    | OrdersCancelReservationCreateResponse401
    | OrdersCancelReservationCreateResponse403
    | OrdersCancelReservationCreateResponse404
    | ReservationCancellation
]:
    """Cancel an unissued reservation

     Release the authenticated customer's reservation only before an invoice is created or any assignment
    is issued. Repeated cancellation is safe.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrdersCancelReservationCreateResponse400 | OrdersCancelReservationCreateResponse401 | OrdersCancelReservationCreateResponse403 | OrdersCancelReservationCreateResponse404 | ReservationCancellation]
    """

    kwargs = _get_kwargs(
        id=id,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    OrdersCancelReservationCreateResponse400
    | OrdersCancelReservationCreateResponse401
    | OrdersCancelReservationCreateResponse403
    | OrdersCancelReservationCreateResponse404
    | ReservationCancellation
    | None
):
    """Cancel an unissued reservation

     Release the authenticated customer's reservation only before an invoice is created or any assignment
    is issued. Repeated cancellation is safe.

    Args:
        id (UUID):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrdersCancelReservationCreateResponse400 | OrdersCancelReservationCreateResponse401 | OrdersCancelReservationCreateResponse403 | OrdersCancelReservationCreateResponse404 | ReservationCancellation
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

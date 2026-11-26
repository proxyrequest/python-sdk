from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...._response import parse_response

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.purchase_mutation_request import PurchaseMutationRequest
from ...models.purchase_response import PurchaseResponse
from ...models.static_mutation_error import StaticMutationError
from ...models.static_purchases_create_response_400 import StaticPurchasesCreateResponse400
from ...models.static_purchases_create_response_401 import StaticPurchasesCreateResponse401
from ...models.static_purchases_create_response_403 import StaticPurchasesCreateResponse403
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: PurchaseMutationRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_impersonate_user, Unset):
        headers["X-Impersonate-User"] = x_impersonate_user

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/static/purchases",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PurchaseResponse
    | StaticMutationError
    | StaticPurchasesCreateResponse400
    | StaticPurchasesCreateResponse401
    | StaticPurchasesCreateResponse403
    | None
):
    if response.status_code == 201:
        response_201 = PurchaseResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = StaticPurchasesCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StaticPurchasesCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = StaticPurchasesCreateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = StaticMutationError.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PurchaseResponse
    | StaticMutationError
    | StaticPurchasesCreateResponse400
    | StaticPurchasesCreateResponse401
    | StaticPurchasesCreateResponse403
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
    body: PurchaseMutationRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    PurchaseResponse
    | StaticMutationError
    | StaticPurchasesCreateResponse400
    | StaticPurchasesCreateResponse401
    | StaticPurchasesCreateResponse403
]:
    """Reserve a new Order

     Reserve one package and one common rental term in one order for 15 minutes. Checkout creates the
    invoice separately. Include Idempotency-Key or the legacy idempotency_key.

    Args:
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (PurchaseMutationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseResponse | StaticMutationError | StaticPurchasesCreateResponse400 | StaticPurchasesCreateResponse401 | StaticPurchasesCreateResponse403]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PurchaseMutationRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    PurchaseResponse
    | StaticMutationError
    | StaticPurchasesCreateResponse400
    | StaticPurchasesCreateResponse401
    | StaticPurchasesCreateResponse403
    | None
):
    """Reserve a new Order

     Reserve one package and one common rental term in one order for 15 minutes. Checkout creates the
    invoice separately. Include Idempotency-Key or the legacy idempotency_key.

    Args:
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (PurchaseMutationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseResponse | StaticMutationError | StaticPurchasesCreateResponse400 | StaticPurchasesCreateResponse401 | StaticPurchasesCreateResponse403
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PurchaseMutationRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> Response[
    PurchaseResponse
    | StaticMutationError
    | StaticPurchasesCreateResponse400
    | StaticPurchasesCreateResponse401
    | StaticPurchasesCreateResponse403
]:
    """Reserve a new Order

     Reserve one package and one common rental term in one order for 15 minutes. Checkout creates the
    invoice separately. Include Idempotency-Key or the legacy idempotency_key.

    Args:
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (PurchaseMutationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseResponse | StaticMutationError | StaticPurchasesCreateResponse400 | StaticPurchasesCreateResponse401 | StaticPurchasesCreateResponse403]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
        x_impersonate_user=x_impersonate_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PurchaseMutationRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
    x_impersonate_user: str | Unset = UNSET,
) -> (
    PurchaseResponse
    | StaticMutationError
    | StaticPurchasesCreateResponse400
    | StaticPurchasesCreateResponse401
    | StaticPurchasesCreateResponse403
    | None
):
    """Reserve a new Order

     Reserve one package and one common rental term in one order for 15 minutes. Checkout creates the
    invoice separately. Include Idempotency-Key or the legacy idempotency_key.

    Args:
        idempotency_key (str | Unset):
        accept_language (str | Unset):  Defaults to the client language.
        x_impersonate_user (str | Unset):
        body (PurchaseMutationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseResponse | StaticMutationError | StaticPurchasesCreateResponse400 | StaticPurchasesCreateResponse401 | StaticPurchasesCreateResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
            accept_language=accept_language,
            x_impersonate_user=x_impersonate_user,
        )
    ).parsed

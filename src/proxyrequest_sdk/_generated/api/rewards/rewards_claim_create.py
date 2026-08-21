from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reward_claim_request import RewardClaimRequest
from ...models.rewards_claim_create_response_400 import RewardsClaimCreateResponse400
from ...models.rewards_claim_create_response_401 import RewardsClaimCreateResponse401
from ...models.rewards_claim_create_response_403 import RewardsClaimCreateResponse403
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    body: RewardClaimRequest,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rewards/claim",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | RewardsClaimCreateResponse400
    | RewardsClaimCreateResponse401
    | RewardsClaimCreateResponse403
    | None
):
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 400:
        response_400 = RewardsClaimCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RewardsClaimCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = RewardsClaimCreateResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | RewardsClaimCreateResponse400
    | RewardsClaimCreateResponse401
    | RewardsClaimCreateResponse403
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
    body: RewardClaimRequest,
    accept_language: str | Unset = UNSET,
) -> Response[
    Any
    | RewardsClaimCreateResponse400
    | RewardsClaimCreateResponse401
    | RewardsClaimCreateResponse403
]:
    """Claim available rewards

     Moves an eligible reward balance or data reward into the customer account. Minimum claim thresholds
    and reward state are validated.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (RewardClaimRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RewardsClaimCreateResponse400 | RewardsClaimCreateResponse401 | RewardsClaimCreateResponse403]
    """

    kwargs = _get_kwargs(
        body=body,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RewardClaimRequest,
    accept_language: str | Unset = UNSET,
) -> (
    Any
    | RewardsClaimCreateResponse400
    | RewardsClaimCreateResponse401
    | RewardsClaimCreateResponse403
    | None
):
    """Claim available rewards

     Moves an eligible reward balance or data reward into the customer account. Minimum claim thresholds
    and reward state are validated.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (RewardClaimRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RewardsClaimCreateResponse400 | RewardsClaimCreateResponse401 | RewardsClaimCreateResponse403
    """

    return sync_detailed(
        client=client,
        body=body,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RewardClaimRequest,
    accept_language: str | Unset = UNSET,
) -> Response[
    Any
    | RewardsClaimCreateResponse400
    | RewardsClaimCreateResponse401
    | RewardsClaimCreateResponse403
]:
    """Claim available rewards

     Moves an eligible reward balance or data reward into the customer account. Minimum claim thresholds
    and reward state are validated.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (RewardClaimRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RewardsClaimCreateResponse400 | RewardsClaimCreateResponse401 | RewardsClaimCreateResponse403]
    """

    kwargs = _get_kwargs(
        body=body,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RewardClaimRequest,
    accept_language: str | Unset = UNSET,
) -> (
    Any
    | RewardsClaimCreateResponse400
    | RewardsClaimCreateResponse401
    | RewardsClaimCreateResponse403
    | None
):
    """Claim available rewards

     Moves an eligible reward balance or data reward into the customer account. Minimum claim thresholds
    and reward state are validated.

    Args:
        accept_language (str | Unset):  Defaults to the client language.
        body (RewardClaimRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RewardsClaimCreateResponse400 | RewardsClaimCreateResponse401 | RewardsClaimCreateResponse403
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept_language=accept_language,
        )
    ).parsed

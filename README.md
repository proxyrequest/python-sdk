# ProxyRequest Python SDK

[![CI](https://github.com/proxyrequest/python-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/proxyrequest/python-sdk/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/proxyrequest-sdk.svg?cacheSeconds=300)](https://pypi.org/project/proxyrequest-sdk/)
[![Python](https://img.shields.io/pypi/pyversions/proxyrequest-sdk.svg?cacheSeconds=300)](https://pypi.org/project/proxyrequest-sdk/)

Official synchronous and asynchronous Python client for the
[ProxyRequest](https://proxyrequest.com/) public API. It covers all 82 operations
in the current contract: users, orders, proxy generation, analytics, invoices,
packages, locations, webhooks, API keys, Telegram integration, and more.

## What is ProxyRequest?

ProxyRequest is a white-label proxy platform for operators and resellers that
already have upstream proxy supply. It provides the product and control layer
needed to turn that supply into a customer-facing service:

- managed HTTP, HTTPS, SOCKS5, and SOCKS5h gateways;
- packages, users, orders, proxy credentials, limits, and byte accounting;
- geographic and network targeting, sticky sessions, and multi-provider routing;
- customer and reseller dashboards, invoices, coupons, and payment flows;
- analytics, signed webhooks, API keys, and operational reporting.

You can use the complete managed backend and customer dashboard, or keep your
own frontend, identity, and billing while ProxyRequest handles provisioning,
routing, accounting, and analytics headlessly. You retain your brand, pricing,
customer relationships, and upstream provider contracts.

ProxyRequest is not an upstream bandwidth plan. Provider traffic and contracts
remain separate from the platform subscription. See the
[platform overview](https://proxyrequest.com/docs/) for the complete operating
boundary.

## How this SDK fits

The REST API is the control plane around proxy traffic. This SDK provisions
resources and reads their state; customer proxy requests go to the managed
gateway servers instead of passing through the SDK or REST API.

```text
Your Python backend ── HTTPS/JSON ──> ProxyRequest API
Customer traffic ───── HTTP/SOCKS ──> Managed gateways ──> Destination
```

Keep the credentials for those paths separate: API keys belong only in trusted
backend code, while generated proxy usernames and passwords are supplied only
to the customer or workload that connects to a gateway.

The most important resource relationships are:

```text
Customer purchase:
Package -> Invoice -> Paid invoice -> Order / data ledger -> Proxy credentials

Reseller provisioning:
Eligible root order -> Sub-user + child allocation -> Proxy credentials
```

Invoices describe commercial state. Orders and data ledgers describe service
entitlement. Creating an invoice or returning from checkout is therefore not
proof that proxy access is active.

## Choose an integration path

| Scenario | Recommended flow |
| --- | --- |
| Built-in customer checkout | Select a package, create an invoice, obtain its payment link, confirm payment and entitlement, then generate proxy credentials. |
| Reseller-managed customer | Create a sub-user, assign a package and byte limit from an eligible root order, then generate credentials for that user. |
| Existing headless platform | Keep your own customer and billing records, persist mappings to ProxyRequest users/packages/orders, and provision through the API. |

See [purchase a package with an invoice](https://github.com/proxyrequest/python-sdk/blob/main/docs/guides/purchase-flow.md)
and [provision a reseller customer](https://github.com/proxyrequest/python-sdk/blob/main/docs/guides/reseller-provisioning.md)
for complete Python examples.

## Installation

```bash
python -m pip install proxyrequest-sdk
```

Python 3.11 or newer is required. The package uses `httpx` and includes both
sync and async clients.

## Quick start

```python
import os

from proxyrequest_sdk import Client
from proxyrequest_sdk.models import UserCreateRequest

with Client.with_api_key(os.environ["PROXYREQUEST_API_KEY"]) as client:
    profile = client.profile.get()
    user = client.users.create(
        body=UserCreateRequest(
            username="customer-reference",
            password=os.urandom(32).hex(),
        )
    )
    print(profile.username, user.id)
```

Static API keys are sent as `Authorization: Static YOUR_API_KEY`. Never expose
them to browser code.

The asynchronous API has the same resource and method names:

```python
import os

from proxyrequest_sdk import AsyncClient


async def list_users() -> None:
    async with AsyncClient.with_api_key(os.environ["PROXYREQUEST_API_KEY"]) as client:
        page = await client.users.list(limit=100)
        for user in page.results:
            print(user.username)
```

## Resource API

`Client` and `AsyncClient` expose one object per API group:

```python
client.authorization
client.users
client.profile
client.orders
client.proxies
client.analytics
client.invoices
client.coupons
client.rewards
client.affiliates
client.packages
client.locations
client.api_keys
client.webhooks
client.telegram
client.telegram_service
client.sessions
client.settings
client.news
```

All operation parameters and return values are typed. Request and response
models live in `proxyrequest_sdk.models`, use snake_case attributes, and expose
`to_dict()` / `from_dict()` helpers. IDs follow their OpenAPI type (`UUID` or
opaque `str`), and all byte amounts are Python integers.

See the generated [API resource reference](https://github.com/proxyrequest/python-sdk/blob/main/docs/reference/api.md)
and [model reference](https://github.com/proxyrequest/python-sdk/blob/main/docs/reference/models.md).

## Pagination

List endpoints return their typed OpenAPI page. Use `paginate()` to follow all
pages lazily:

```python
with Client.with_api_key(os.environ["PROXYREQUEST_API_KEY"]) as client:
    for user in client.paginate(client.users.list, limit=100):
        print(user.username)
```

The asynchronous variant is also lazy:

```python
async with AsyncClient.with_api_key(os.environ["PROXYREQUEST_API_KEY"]) as client:
    async for user in client.paginate(client.users.list, limit=100):
        print(user.username)
```

## Errors

Every documented and undocumented HTTP failure is normalized to `ApiError`.
Network and decoding problems use the same contract:

```python
from proxyrequest_sdk import ApiError, ErrorKind

try:
    client.profile.get()
except ApiError as error:
    if error.kind is ErrorKind.AUTHENTICATION:
        # Replace the invalid API key or bearer token.
        pass
    print(error.status_code, error.request_id, error.field_errors)
```

The SDK does not automatically retry writes or refresh JWTs. Call
`client.authorization.refresh(...)` explicitly when your application owns a
token pair.

## Configuration and custom deployments

```python
import httpx

client = Client.with_api_key(
    os.environ["PROXYREQUEST_API_KEY"],
    base_url="https://customer-api.example/api/v1",
    language="uk",
    timeout=20,
    connect_timeout=5,
)
```

An existing `httpx.Client` or `httpx.AsyncClient` can be supplied through
`http_client`. It must have the same `base_url`; the SDK applies its auth,
language, and user-agent headers but leaves closing the external client to the
caller. The `request()` method is an authenticated escape hatch for endpoints
introduced before the next SDK release.

## Invoice downloads

```python
download = client.download_invoice_pdf(invoice_id)
path = download.save(f"./{download.filename}")
print(path, download.content_type)
```

`save()` does not overwrite an existing file unless `overwrite=True` is passed.

## Telegram service operations

Account-side Telegram operations use the client's API key. Bot service
operations require the service secret explicitly and never reuse the ordinary
Authorization header:

```python
from proxyrequest_sdk.models import TelegramSessionRequest

session = client.telegram_service.create_session(
    body=TelegramSessionRequest(telegram_user_id=123456789, chat_id=123456789),
    service_secret=os.environ["PROXYREQUEST_TELEGRAM_SECRET"],
)
```

## Webhook verification

Verify the exact raw body before decoding it:

```python
from proxyrequest_sdk import WebhookVerifier

payload = WebhookVerifier.decode_verified_json(
    raw_body,
    request.headers.get("X-Webhook-Signature", ""),
    os.environ["PROXYREQUEST_WEBHOOK_SECRET"],
    timestamp_header=request.headers.get("X-Webhook-Timestamp"),
)
```

## Platform documentation

- [Platform documentation](https://proxyrequest.com/docs/): capabilities,
  responsibility boundaries, deployment modes, and starting points.
- [Integration overview](https://proxyrequest.com/docs/integration/overview/):
  control-plane boundary and common API flows.
- [API fundamentals](https://proxyrequest.com/docs/integration/api-fundamentals/)
  and [API resource map](https://proxyrequest.com/docs/integration/api-resource-map/):
  authentication, errors, pagination, and resource relationships.
- [Billing and growth](https://proxyrequest.com/docs/integration/billing-and-growth/):
  invoices, payment links, coupons, and entitlement reconciliation.
- [Reseller workflow](https://proxyrequest.com/docs/integration/reseller-workflow/)
  and [users and data](https://proxyrequest.com/docs/integration/users-and-data/):
  sub-user provisioning and safe byte allocation.
- [Catalog and proxy generation](https://proxyrequest.com/docs/integration/catalog-and-proxies/):
  packages, orders, locations, and credentials.
- [Webhooks](https://proxyrequest.com/docs/integration/webhooks/) and
  [usage accounting](https://proxyrequest.com/docs/proxy/usage-accounting/):
  event handling, root ledgers, child limits, and reconciliation.
- [API reference](https://proxyrequest.com/docs/api/): exact endpoints,
  request schemas, responses, and examples.

## Development

```bash
uv sync --all-groups
make quality
make generate-check
make build
```

The vendored schema is pinned in `openapi/source.json`. Run
`make sync-openapi SOURCE=/path/to/openapi.yml`, followed by `make generate`, to
update it. Generation is pinned and CI rejects uncommitted contract changes.

## License

MIT

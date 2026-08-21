# Provision a reseller customer

Use this flow when your application is authoritative for customer identity and
billing, while ProxyRequest enforces proxy access, byte accounting, routing,
and reporting. The authenticated reseller must already own an eligible root
order for the package being assigned.

```text
Your customer + billing record
        -> ProxyRequest sub-user + child allocation
        -> generated proxy credentials
        -> webhooks + analytics reconciliation
```

This is direct provisioning, not a purchase. Use the
[invoice purchase flow](purchase-flow.md) when ProxyRequest should create the
commercial record and payment flow.

## Root entitlement and child allocation

A root order owns the physical data ledgers. A reseller-created child order
carries one managed customer's personal consumption limit while traffic still
uses the shared root ledger. Adding 10 GiB to a child does not reserve or move
10 GiB out of the root ledger, so the sum of child limits can exceed the
remaining shared pool. Monitor both values before promising capacity.

## Create and provision a sub-user

The public contract requires a unique username and account password. A headless
integration can generate opaque values server-side and omit email. When
assigning a package during user creation, pass `package_id` and `data` together.

```python
import os
import secrets
from uuid import UUID

from proxyrequest_sdk import UNSET, Client
from proxyrequest_sdk.models import GenerateProxyRequest, UserCreateRequest, UserCreateRequestMeta

client = Client.with_api_key(os.environ["PROXYREQUEST_API_KEY"])
allocation_bytes = 10 * 1024**3

package_page = client.packages.list(limit=100)
if not package_page.results or package_page.results[0].id is UNSET:
    raise RuntimeError("No eligible package is available.")
package_id = UUID(package_page.results[0].id)

user = client.users.create(
    body=UserCreateRequest(
        username="customer-01842",
        password=secrets.token_hex(32),
        package_id=package_id,
        data=allocation_bytes,
        meta=UserCreateRequestMeta.from_dict({"customer_reference": "crm-01842"}),
    )
)

# Persist the immutable local customer -> ProxyRequest user mapping now.
result = client.proxies.generate(
    body=GenerateProxyRequest(package_id=package_id, user_id=user.id, quantity=1)
)
for proxy in result.proxies:
    print("Proxy:", proxy.connection_string)
```

The optional `meta` object is suitable for non-sensitive correlation data, but
it does not replace an explicit mapping in your database. Treat both the user
password and generated proxy credentials as secrets.

## Add data to an existing child order

Use `add_data()` when an existing managed user receives an additional
allowance. Record the intended pre-operation state before sending the request.

```python
import os
from uuid import UUID

from proxyrequest_sdk import Client
from proxyrequest_sdk.models import AddDataRequest

client = Client.with_api_key(os.environ["PROXYREQUEST_API_KEY"])

user_id = UUID("replace-with-the-mapped-user-id")
package_id = UUID("replace-with-the-mapped-package-id")
additional_bytes = 5 * 1024**3

updated_order = client.users.add_data(
    user_id,
    body=AddDataRequest(package_id=package_id, data=additional_bytes),
)
print("Updated order:", updated_order.id)
```

Subtraction is a financial action as well as an access-control change. Give it
separate authorization, store the business reason, and verify the resulting
state before reporting success.

## Make provisioning recoverable

Persist these mappings and events as soon as each step succeeds:

| Local record | ProxyRequest record |
| --- | --- |
| Customer ID | User ID |
| Product/SKU | Package ID |
| Entitlement | Order ID and allocation state |
| Billing or provisioning operation | Request context, byte amount, result, and timestamp |

Generate an internal operation ID before the first write. If a user creation or
allocation request has an ambiguous timeout, read the affected state before
retrying; repeating an uncertain data-add can grant the allowance twice. Signed
webhooks are useful for prompt updates, but reconcile them with durable order
state and analytics rather than treating delivery as the only source of truth.

## Related documentation

- [Platform integration overview](https://proxyrequest.com/docs/integration/overview/)
- [Reseller workflow](https://proxyrequest.com/docs/integration/reseller-workflow/)
- [Users and data lifecycle](https://proxyrequest.com/docs/integration/users-and-data/)
- [Catalog and proxy generation](https://proxyrequest.com/docs/integration/catalog-and-proxies/)
- [Usage accounting](https://proxyrequest.com/docs/proxy/usage-accounting/)
- [Webhooks](https://proxyrequest.com/docs/integration/webhooks/)
- [Create a sub-user](https://proxyrequest.com/docs/api/operations/users_create/)
- [Add data](https://proxyrequest.com/docs/api/operations/users_data_add_create/)
- [Generate proxy credentials](https://proxyrequest.com/docs/api/operations/proxies_generate_create/)
- SDK references: [API resources](../reference/api.md) and [models](../reference/models.md)

[Back to the SDK README](../../README.md)

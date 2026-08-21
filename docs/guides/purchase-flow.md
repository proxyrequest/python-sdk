# Purchase a package with an invoice

Use this flow when ProxyRequest should calculate the current package price,
create the commercial record, and initialize the selected payment provider. A
purchase can apply to the authenticated account or to a managed sub-user.

```text
Package -> optional coupon preview -> pending invoice -> checkout
        -> paid invoice -> order / data ledger -> proxy credentials
```

An invoice is commercial state; an order and its ledger are service state. Do
not activate access because invoice creation succeeded or because the browser
returned from checkout. Confirm the paid invoice server-side and verify the
resulting entitlement.

## 1. Select a package and create the invoice

Package IDs must come from the current deployment. Byte amounts are integers;
this example uses 10 GiB. Confirm whether your product uses decimal GB or
binary GiB and perform that conversion once in your billing layer.

`user_id` is optional. Omit it to purchase for the authenticated account, or
set it to a managed sub-user UUID. Available payment gateways depend on the
deployment; this example uses Stripe.

```python
import os
from uuid import UUID

from proxyrequest_sdk import UNSET, Client
from proxyrequest_sdk.models import (
    CouponCalculatePriceRequest,
    InvoiceCreateRequest,
    InvoiceCreateRequestGatewayEnum,
)

client = Client.with_api_key(os.environ["PROXYREQUEST_API_KEY"])
data_bytes = 10 * 1024**3

package_page = client.packages.list(limit=100)
if not package_page.results or package_page.results[0].id is UNSET:
    raise RuntimeError("No package is available for this account.")
package_id = UUID(package_page.results[0].id)

managed_user_id: UUID | None = None
coupon_code: str | None = None

if coupon_code is not None:
    preview = client.coupons.calculate_price(
        body=CouponCalculatePriceRequest(
            package_id=package_id,
            coupon_code=coupon_code,
            data=data_bytes,
        )
    )
    print("Discounted total:", preview.price_discounted)

invoice_request = InvoiceCreateRequest(
    package_id=package_id,
    gateway=InvoiceCreateRequestGatewayEnum.STRIPE,
    data=data_bytes,
)
if managed_user_id is not None:
    invoice_request.user_id = managed_user_id
if coupon_code is not None:
    invoice_request.coupon_code = coupon_code

invoice = client.invoices.create(body=invoice_request)
if invoice.id is UNSET:
    raise RuntimeError("The created invoice has no ID.")

# Persist invoice.id next to your checkout record before redirecting.
payment = client.invoices.get_payment_link(invoice.id)
print("Send the customer to:", payment.payment_url)
```

The coupon preview is informational and does not create or reserve anything.
Recalculate immediately before checkout and treat the total returned by invoice
creation as authoritative.

## 2. Confirm payment and entitlement

Run confirmation from your backend after a verified payment notification, or
when the customer returns. A browser redirect alone is not proof of settlement.

```python
import os
from uuid import UUID

from proxyrequest_sdk import Client
from proxyrequest_sdk.models import GenerateProxyRequest, InvoiceStatusEnum

client = Client.with_api_key(os.environ["PROXYREQUEST_API_KEY"])

invoice_id = "replace-with-the-persisted-invoice-id"
package_id = "replace-with-the-persisted-package-id"
managed_user_id: UUID | None = None

invoice = client.invoices.get(invoice_id)
if invoice.status is not InvoiceStatusEnum.PAID:
    raise RuntimeError("The invoice is not paid; access stays inactive.")

order_filters = {"limit": 100, "package_id": package_id}
if managed_user_id is not None:
    order_filters["user_id"] = managed_user_id
orders = client.orders.list(**order_filters)
if not orders.results:
    raise RuntimeError("Payment is recorded, but the entitlement is not ready.")

request = GenerateProxyRequest(package_id=UUID(package_id), quantity=1)
if managed_user_id is not None:
    request.user_id = managed_user_id
result = client.proxies.generate(body=request)

for proxy in result.proxies:
    print("Proxy:", proxy.connection_string)
```

Treat generated connection strings as secrets. Deliver them over an
authenticated channel and do not write them to application logs.

## Recovery and reconciliation

- Persist your checkout ID, ProxyRequest invoice ID, package ID, recipient user
  ID, expected byte amount, and current local state.
- If invoice creation times out after the request was sent, inspect visible
  invoices before repeating the write. The API does not promise a universal
  idempotency key for writes.
- Keep payment, invoice, order, allocation, and credential states separate so
  a partially completed workflow can resume safely.
- Use signed webhooks for prompt reactions, then reconcile against invoices,
  durable order/ledger state, and closed analytics windows.

## Related documentation

- [Billing, coupons, and growth](https://proxyrequest.com/docs/integration/billing-and-growth/)
- [Catalog and proxy generation](https://proxyrequest.com/docs/integration/catalog-and-proxies/)
- [API resource map](https://proxyrequest.com/docs/integration/api-resource-map/)
- [Create an invoice](https://proxyrequest.com/docs/api/operations/invoices_create/)
- [Get an invoice payment link](https://proxyrequest.com/docs/api/operations/invoices_pay_retrieve/)
- [List active orders](https://proxyrequest.com/docs/api/operations/orders_list/)
- [Generate proxy credentials](https://proxyrequest.com/docs/api/operations/proxies_generate_create/)
- SDK references: [API resources](../reference/api.md) and [models](../reference/models.md)

[Back to the SDK README](../../README.md)

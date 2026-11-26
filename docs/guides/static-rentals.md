# Static ISP and datacenter rentals

Use the static rental API to read assigned endpoints, buy more addresses, or
extend selected endpoints. This guide assumes static rentals are enabled on the
API deployment and the integration can retrieve proxy credentials. Keep
credentials and exported URLs in your secret store.

## Connect to a previously purchased proxy

```python
import os
from uuid import UUID

from proxyrequest_sdk import UNSET, Client
from proxyrequest_sdk.models import StaticExportRetrieveProtocol

with Client.with_api_key(os.environ["PROXYREQUEST_API_KEY"]) as client:
    order_id = UUID(os.environ["PROXYREQUEST_STATIC_ORDER_ID"])
    rental = client.orders.get_rental(order_id, limit=100)
    for endpoint in rental.results:
        if endpoint.ready and endpoint.id is not UNSET:
            # Persist the endpoint ID so you can update the connection after a replacement.
            endpoint_reference = UUID(endpoint.id)
    urls = client.static_proxies.export_urls(
        order_id=order_id,
        protocol=StaticExportRetrieveProtocol.HTTP,
    ).splitlines()
    # Supply these URLs to the proxy configuration of your workload.
```

Check `rental.next_` and advance `offset` to read more endpoint pages. For
structured connections, use the active entries in each ready endpoint's
`connections`. Use its individual username and password when supplied. A
shared-credential order exposes `rental.username` and `rental.proxy_password`.
The export includes only endpoints usable with the selected protocol. Read the
rental again after an IP replacement to pick up the new connection for the same
endpoint ID.

## Reserve, pay, and renew

Choose the offer from `client.orders.list_catalog()`. This example uses a wallet
with sufficient balance. Store the mutation keys with the corresponding
business operation before sending the request and reuse them after a timeout.

```python
import os
from uuid import UUID

from proxyrequest_sdk import UNSET, Client
from proxyrequest_sdk.models import (
    InvoiceCreateRequestGatewayEnum,
    PurchaseMutationRequest,
    RenewalCheckoutRequest,
    RenewalRequestRequest,
    RenewalSelectionRequest,
    StaticCheckoutRequest,
)

wallet = InvoiceCreateRequestGatewayEnum.WALLET
with Client.with_api_key(os.environ["PROXYREQUEST_API_KEY"]) as client:
    offer_id = UUID(os.environ["PROXYREQUEST_STATIC_OFFER_ID"])
    operation = os.environ["YOUR_PURCHASE_OPERATION_ID"]
    reservation = client.orders.reserve(
        body=PurchaseMutationRequest(offer_id=offer_id),
        idempotency_key=f"{operation}-reserve",
    )
    order_id = reservation.id
    quote = client.orders.quote_checkout(order_id, body=StaticCheckoutRequest(gateway=wallet))
    invoice = client.orders.checkout(
        order_id,
        body=StaticCheckoutRequest(gateway=wallet, expected_total=quote.total),
        idempotency_key=f"{operation}-checkout",
    )

    # Poll this read with backoff until fulfillment is settled or your wait expires.
    # Payment status alone cannot confirm that an individual endpoint is usable.
    rental = client.orders.get_rental(order_id)
    ready = [
        UUID(endpoint.id)
        for endpoint in rental.results
        if endpoint.ready and endpoint.renewable and endpoint.id is not UNSET
    ]
    if ready:
        term = rental.snapshot.term_id
        billing = RenewalCheckoutRequest(gateway=wallet)
        preview = client.orders.quote_renewal(
            order_id,
            body=RenewalSelectionRequest(term_id=term, invoice=billing, endpoint_ids=ready),
        )
        # Call renew when your application is ready to pay for the next period.
        renewal = client.orders.renew(
            order_id,
            body=RenewalRequestRequest(
                term_id=term, invoice=billing, endpoint_ids=ready, expected_total=preview.total,
            ),
            idempotency_key=os.environ["YOUR_RENEWAL_OPERATION_ID"],
        )
```

Checkout may return `provisioning`. Poll the rental independently of the
invoice, with a bounded deadline. A partial delivery can contain ready
endpoints and failed or refunded items. Inspect the matching invoice entry
in `rental.invoices` for its result and refund amount. If an operation fails
with `ApiError.code == "price_changed"`, fetch a new quote before authorizing
a different total. An idempotency conflict requires checking the original
operation before sending another payment.

The same methods are available on `AsyncClient`. For example,
`await client.orders.get_rental(order_id)` returns the same `RentalDetail`.

# API resource reference

All methods exist on both `Client` and `AsyncClient`; async calls must be awaited.

## `affiliates`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `get_rewards_overall()` | `GET /affiliates/rewards/overall` | `AffiliateStatsResponse` |
| `list()` | `GET /affiliates` | `PaginatedAffiliateList` |
| `list_rewards()` | `GET /affiliates/rewards` | `PaginatedAffiliateRewardList` |

## `analytics`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `get_connections()` | `GET /analytics/connections` | `ConnectionsResponse` |
| `get_overall()` | `GET /analytics/overall` | `OverallResponse` |
| `get_transactions()` | `GET /analytics/{id}/transactions` | `TransactionsResponse` |
| `list_domains()` | `GET /analytics/domains` | `DomainsResponse` |
| `list_feed()` | `GET /analytics/feed` | `FeedResponse` |
| `list_logs()` | `GET /analytics/logs` | `LogsResponse` |

## `api_keys`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `create()` | `POST /api-keys` | `APIKeyCreate` |
| `delete()` | `DELETE /api-keys/{id}` | `None` |
| `list()` | `GET /api-keys` | `PaginatedAPIKeyList` |

## `authorization`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `login()` | `POST /login` | `TokenPairResponse | OTPChallenge` |
| `login_with_google()` | `POST /login/google` | `TokenPairResponse | OTPChallenge` |
| `recover_password()` | `POST /recover-password` | `PasswordRecoveryResponse` |
| `refresh()` | `POST /refresh` | `TokenRefreshResponse` |
| `signup()` | `POST /signup` | `TokenPairResponse` |
| `verify_otp()` | `POST /login/otp` | `TokenPairResponse` |

## `coupons`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `calculate_price()` | `POST /coupons/calculate-price` | `CouponPriceResponse` |
| `create()` | `POST /coupons` | `Coupon` |
| `delete()` | `DELETE /coupons/{id}` | `None` |
| `get()` | `GET /coupons/{id}` | `CouponShort` |
| `list()` | `GET /coupons` | `PaginatedCouponShortList` |
| `list_redeems()` | `GET /coupons/{id}/redeems` | `PaginatedCouponRedeemList` |
| `replace()` | `PUT /coupons/{id}` | `Coupon` |
| `update()` | `PATCH /coupons/{id}` | `Coupon` |

## `invoices`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `create()` | `POST /invoices` | `Invoice` |
| `delete()` | `DELETE /invoices/{id}` | `None` |
| `download_pdf()` | `GET /invoices/{id}/download/pdf` | `FileDownload` |
| `get()` | `GET /invoices/{id}` | `Invoice | InvoiceShort` |
| `get_payment_link()` | `GET /invoices/{id}/pay` | `PaymentLinkResponse` |
| `list()` | `GET /invoices` | `PaginatedInvoiceReadList` |
| `quote()` | `POST /invoices/quote` | `PurchaseQuoteResponse` |

## `kyc`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `create_session()` | `POST /kyc/sessions/` | `SessionOutput` |
| `get_status()` | `GET /kyc/` | `Status` |

## `locations`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `get_city()` | `GET /locations/cities/{id}` | `City` |
| `get_continent()` | `GET /locations/continents/{id}` | `Continent` |
| `get_country()` | `GET /locations/countries/{id}` | `Country` |
| `get_region()` | `GET /locations/regions/{id}` | `Region` |
| `get_zipcode()` | `GET /locations/zipcodes/{id}` | `Postal` |
| `list_asns()` | `GET /locations/asn` | `PaginatedLocationASNRecordList` |
| `list_cities()` | `GET /locations/cities` | `PaginatedCityList` |
| `list_continents()` | `GET /locations/continents` | `PaginatedContinentList` |
| `list_countries()` | `GET /locations/countries` | `PaginatedCountryList` |
| `list_isps()` | `GET /locations/isps` | `PaginatedISPList` |
| `list_regions()` | `GET /locations/regions` | `PaginatedRegionList` |
| `list_zipcodes()` | `GET /locations/zipcodes` | `PaginatedPostalList` |

## `news`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `list()` | `GET /news` | `PaginatedNewsList` |

## `orders`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `cancel_reservation()` | `POST /orders/{id}/cancel-reservation` | `ReservationCancellation` |
| `checkout()` | `POST /orders/{id}/checkout` | `Invoice` |
| `delete()` | `DELETE /orders/{id}` | `UsageClosureResponse | None` |
| `get()` | `GET /orders/{id}` | `OrderDetailed` |
| `get_availability()` | `GET /orders/availability` | `AvailabilityResponse` |
| `get_calendar_renewal()` | `GET /orders/{id}/auto-renewal` | `AutoRenewalStatus` |
| `get_rental()` | `GET /orders/{id}/rental` | `RentalDetail` |
| `list()` | `GET /orders` | `PaginatedOrderList` |
| `list_catalog()` | `GET /orders/catalog` | `CatalogPage` |
| `list_products()` | `GET /orders/products` | `Products` |
| `list_replacements()` | `GET /orders/{id}/replacement-requests` | `ReplacementPage` |
| `quote_checkout()` | `POST /orders/{id}/checkout/quote` | `CheckoutQuote` |
| `quote_purchase()` | `POST /orders/purchase/quote` | `RentalQuote` |
| `quote_renewal()` | `POST /orders/{id}/renew/quote` | `RenewalQuote` |
| `renew()` | `POST /orders/{id}/renew` | `Invoice` |
| `request_replacement()` | `POST /orders/{id}/replacement-requests` | `ReplacementResponse` |
| `reserve()` | `POST /orders/purchase` | `PurchaseResponse` |
| `reset_password()` | `POST /reset-password` | `ProxyPasswordResetResponse` |
| `reset_proxy_password()` | `POST /orders/{id}/proxy-password/reset` | `ProxyPasswordResetResponse` |
| `set_calendar_renewal()` | `PUT /orders/{id}/auto-renewal` | `AutoRenewalStatus` |
| `update_auto_renewal()` | `PATCH /orders/{id}` | `Order` |

## `packages`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `list()` | `GET /packages` | `PaginatedPackageList` |
| `list_commissions()` | `GET /packages/commissions` | `PaginatedPackageCommissionList` |

## `profile`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `change_password()` | `POST /profile/change-password` | `MessageResponse` |
| `confirm_two_factor()` | `POST /profile/2fa/confirm` | `EnabledResponse` |
| `connect_google()` | `POST /profile/social-accounts/google` | `list[SocialAccountState]` |
| `delete()` | `DELETE /profile` | `UsageClosureResponse | None` |
| `disable_two_factor()` | `POST /profile/2fa/disable` | `EnabledResponse` |
| `get()` | `GET /profile` | `User` |
| `get_two_factor_status()` | `GET /profile/2fa/status` | `EnabledResponse` |
| `list_login_history()` | `GET /profile/login-history` | `PaginatedLoginHistoryList` |
| `list_social_accounts()` | `GET /profile/social-accounts` | `list[SocialAccountState]` |
| `regenerate_two_factor_codes()` | `POST /profile/2fa/regenerate` | `MFAResponse` |
| `setup_two_factor()` | `POST /profile/2fa/setup` | `TwoFactorSetupResponse` |
| `update()` | `PATCH /profile` | `User` |

## `providers`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `list_data_balances()` | `GET /providers/data-balances` | `PaginatedProviderDataBalanceList` |

## `proxies`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `generate()` | `POST /proxies/generate` | `GenerateProxyResponse` |

## `rewards`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `claim()` | `POST /rewards/claim` | `None` |
| `list()` | `GET /rewards` | `PaginatedRewardList` |

## `settings`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `get()` | `GET /settings` | `SettingsResponse` |

## `static_proxies`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `checkout()` | `POST /static/purchases/{id}/checkout` | `Invoice` |
| `create_integration_key()` | `POST /static/integration-keys` | `IntegrationKeyCreated` |
| `export_urls()` | `GET /static/export` | `str` |
| `get_endpoint()` | `GET /static/endpoints/{id}` | `Endpoint` |
| `get_purchase()` | `GET /static/purchases/{id}` | `PurchaseResponse` |
| `get_throughput()` | `GET /static/endpoints/{id}/throughput` | `Throughput` |
| `list_catalog()` | `GET /static/catalog` | `CatalogPage` |
| `list_endpoints()` | `GET /static/endpoints` | `EndpointPage` |
| `list_integration_keys()` | `GET /static/integration-keys` | `list[IntegrationKey]` |
| `list_purchases()` | `GET /static/purchases` | `StaticPurchasePage` |
| `quote_offer()` | `GET /static/quotes/{offer_id}` | `RentalQuote` |
| `reserve()` | `POST /static/purchases` | `PurchaseResponse` |
| `revoke_integration_key()` | `DELETE /static/integration-keys/{id}` | `None` |
| `update_endpoint()` | `PATCH /static/endpoints/{id}` | `Endpoint` |

## `telegram`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `create_link()` | `POST /integrations/telegram/link` | `TelegramLinkResponse` |
| `delete_connection()` | `DELETE /integrations/telegram/connection` | `None` |
| `get_connection()` | `GET /integrations/telegram/connection` | `TelegramConnectionResponse` |
| `update_connection()` | `PATCH /integrations/telegram/connection` | `TelegramConnectionResponse` |

## `users`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `add_data()` | `POST /users/{id}/data/add` | `Order` |
| `create()` | `POST /users` | `User` |
| `delete()` | `DELETE /users/{id}` | `UsageClosureResponse | None` |
| `get()` | `GET /users/{id}` | `User` |
| `list()` | `GET /users` | `PaginatedUserList` |
| `list_orders()` | `GET /users/{id}/orders` | `PaginatedOrderList` |
| `reset_data()` | `POST /users/{id}/data/reset` | `Order` |
| `reset_password()` | `POST /users/{id}/password` | `User` |
| `set_connection_limit()` | `PATCH /users/{id}/connection-limit` | `Order` |
| `subtract_data()` | `POST /users/{id}/data/subtract` | `Order` |
| `update()` | `PATCH /users/{id}` | `User` |

## `webhooks`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `create()` | `POST /webhooks` | `WebhookCreated` |
| `delete()` | `DELETE /webhooks/{id}` | `None` |
| `get()` | `GET /webhooks/{id}` | `WebhookList` |
| `get_static_events()` | `GET /webhooks/{id}/static-events` | `StaticWebhookSubscription` |
| `list()` | `GET /webhooks` | `PaginatedWebhookList` |
| `set_static_events()` | `PATCH /webhooks/{id}/static-events` | `StaticWebhookSubscription` |

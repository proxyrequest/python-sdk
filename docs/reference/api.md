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
| `login()` | `POST /login` | `TokenPairResponse` |
| `login_with_google()` | `POST /login/google` | `TokenPairResponse` |
| `recover_password()` | `POST /recover-password` | `PasswordRecoveryResponse` |
| `refresh()` | `POST /refresh` | `TokenRefreshResponse` |
| `signup()` | `POST /signup` | `TokenPairResponse` |

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
| `get()` | `GET /invoices/{id}` | `Invoice` |
| `get_payment_link()` | `GET /invoices/{id}/pay` | `PaymentLinkResponse` |
| `list()` | `GET /invoices` | `PaginatedInvoiceList` |

## `locations`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `get_city()` | `GET /locations/cities/{id}` | `City` |
| `get_continent()` | `GET /locations/continents/{id}` | `Continent` |
| `get_country()` | `GET /locations/countries/{id}` | `Country` |
| `get_region()` | `GET /locations/regions/{id}` | `Region` |
| `list_asns()` | `GET /locations/asn` | `PaginatedLocationASNRecordList` |
| `list_cities()` | `GET /locations/cities` | `PaginatedCityList` |
| `list_continents()` | `GET /locations/continents` | `PaginatedContinentList` |
| `list_countries()` | `GET /locations/countries` | `PaginatedCountryList` |
| `list_isps()` | `GET /locations/isps` | `PaginatedISPList` |
| `list_regions()` | `GET /locations/regions` | `PaginatedRegionList` |

## `news`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `list()` | `GET /news` | `PaginatedNewsList` |

## `orders`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `delete()` | `DELETE /orders/{id}` | `None` |
| `get()` | `GET /orders/{id}` | `OrderDetailed` |
| `list()` | `GET /orders` | `PaginatedOrderList` |
| `reset_password()` | `POST /reset-password` | `ProxyPasswordResetResponse` |
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
| `delete()` | `DELETE /profile` | `None` |
| `disable_two_factor()` | `POST /profile/2fa/disable` | `EnabledResponse` |
| `get()` | `GET /profile` | `User` |
| `get_two_factor_status()` | `GET /profile/2fa/status` | `EnabledResponse` |
| `setup_two_factor()` | `POST /profile/2fa/setup` | `TwoFactorSetupResponse` |
| `update()` | `PATCH /profile` | `User` |

## `proxies`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `generate()` | `POST /proxies/generate` | `GenerateProxyResponse` |

## `rewards`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `claim()` | `POST /rewards/claim` | `None` |
| `list()` | `GET /rewards` | `PaginatedRewardList` |

## `sessions`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `delete()` | `DELETE /sessions/{id}` | `SessionDeleteResponse` |
| `list()` | `GET /sessions` | `list[SessionListResponse]` |

## `settings`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `get()` | `GET /settings` | `SettingsResponse` |

## `telegram`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `create_link()` | `POST /integrations/telegram/link` | `TelegramLinkResponse` |
| `delete_connection()` | `DELETE /integrations/telegram/connection` | `None` |
| `get_connection()` | `GET /integrations/telegram/connection` | `TelegramConnectionResponse` |
| `update_connection()` | `PATCH /integrations/telegram/connection` | `TelegramConnectionResponse` |

## `telegram_service`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `consume_link()` | `POST /integrations/telegram/link/consume` | `TelegramConnectionResponse` |
| `create_session()` | `POST /integrations/telegram/session` | `TelegramSessionResponse` |

## `users`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `add_data()` | `POST /users/{id}/data/add` | `Order` |
| `create()` | `POST /users` | `User` |
| `delete()` | `DELETE /users/{id}` | `None` |
| `get()` | `GET /users/{id}` | `User` |
| `list()` | `GET /users` | `PaginatedUserList` |
| `list_orders()` | `GET /users/{id}/orders` | `PaginatedOrderList` |
| `reset_password()` | `POST /users/{id}/password` | `User` |
| `subtract_data()` | `POST /users/{id}/data/subtract` | `Order` |
| `update()` | `PATCH /users/{id}` | `User` |

## `webhooks`

| Method | HTTP endpoint | Returns |
| --- | --- | --- |
| `create()` | `POST /webhooks` | `WebhookCreated` |
| `delete()` | `DELETE /webhooks/{id}` | `None` |
| `get()` | `GET /webhooks/{id}` | `WebhookList` |
| `list()` | `GET /webhooks` | `PaginatedWebhookList` |

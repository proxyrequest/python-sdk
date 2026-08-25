# Changelog

All notable changes to the ProxyRequest Python SDK are documented here.

## Unreleased

- Added automatic and explicit idempotency keys with bounded ambiguous-outcome
  retries.
- Added response metadata variants and explicit ETag/`If-Match` optimistic
  concurrency support.

## 1.0.0 - 2026-08-21

- Initial stable release covering all 82 public API operations.
- Added synchronous and asynchronous clients with typed attrs models.
- Added normalized errors, lazy pagination, invoice downloads, raw requests,
  and signed webhook verification.
- Added purchase and reseller provisioning guides.

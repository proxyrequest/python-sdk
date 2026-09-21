# Changelog

All notable changes to the ProxyRequest Python SDK are documented here.

## Unreleased

## 2.2.0 - 2026-09-21

- Synchronize the public OpenAPI contract from backend commit `2c4505a`.
- Accept Unix seconds and all documented date strings while preserving existing date inputs.
- Keep the legacy logs hostname argument and existing response contracts.
- Cover feed/domains pagination, nullable feed timestamps, and UInt64 IDs with regression tests.

## 2.1.0 - 2026-09-17

- Add atomic per-package data reset with typed requests, response metadata, and idempotent retries.
- Refresh the public API contract and document root balances versus child allocations.

## 2.0.0 - 2026-09-16

- Replace the incorrect webhook verifier with the actual `X-Signature`
  Base64 HMAC-SHA256 format over exact raw bytes.

- Regenerated from the public backend contract (81 operations, 130 schemas),
  excluding the two disabled sessions-management operations from generated clients.
- Added the optional `pending`/`paid` status to invoice creation requests.
- Added typed OTP verification and 200/202 login support for sync and async clients.
- Corrected MFA bodies, payment fields, nullable invoices, and both backend user modes.
- Preserved HTTP status, raw response, headers, cause, and idempotency key when
  response decoding fails; HTTP errors are classified before model decoding.
- Replaced fixed contract-size gates and added backend-serializer regression fixtures.

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

# Analytics compatibility

The SDK accepts all documented reporting-window formats for `start` and `end`:
ISO 8601 with or without an offset, `YYYY-MM-DD HH:MM:SS`, `DD-MM-YYYY HH:MM:SS`,
`YYYY-MM-DD`, `DD-MM-YYYY`, and Unix timestamps in **seconds**, including fractions.
Strings pass through unchanged; numeric timestamps are also accepted. Milliseconds
are not converted automatically. Omitted parameters retain the server defaults.

The server interprets offset-free date strings in the requested timezone, converts
explicit offsets, and truncates reporting boundaries to the minute. Date-only
values start at midnight. Missing, empty or unknown timezone names use the server's
deployment timezone (UTC by default). Prefer explicit ISO offsets when timezone
interpretation matters. Response date fields keep their existing types.

The `hostname` filter on feed and domains accepts a comma-separated mixture of
domains, IPv4/IPv6 addresses and HTTP(S) URLs. Normalization belongs to the server;
the SDK preserves the supplied string. Bracket IPv6 addresses when adding a port.
`include_sub_users` is a boolean on domains and overall. The legacy logs `hostname`
argument remains available for source compatibility, but the server ignores it.

Domain records contain `hostname`, `requests` and `data`; the SDK does not add a
`timestamp` or a page `count`. Feed timestamps can legitimately be null.

## Feed identifiers

`FeedRecord.id` remains an arbitrary-precision Python `int`, preserving the full
UInt64 range. Version 2.2 does not change response types, including datetime fields.
Regression fixtures cover the reported feed IDs and numeric boundaries.

```python
page = client.analytics.list_feed(
    start=1782864000.5,
    end="2026-07-02T00:00:00Z",
    timezone="Europe/Kiev",
)
id_value: int = page.results[0].id
```

Existing `datetime` inputs still serialize through `isoformat()`. All date formats
are supported by sync and async clients, including methods with response metadata.

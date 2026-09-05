# Canonical data

Each `*.jsonl` file is a type-homogeneous canonical stream validated against
`schemas/1.0.0/` and the semantic rules in `scripts/validate_records.py`.

Rules:

- UTF-8, one complete JSON object per line, LF terminated, no blank lines.
- Records sort by `id`; line order carries no domain meaning.
- Foreign keys use opaque typed `id` values, never names or `canonical_key`.
- `canonical_key` is a stable, grep-friendly handle and is immutable after a
  released dataset version.
- Provider-native values remain present when normalized values are added.
- Missing or negative findings use typed absence records, never overloaded
  null values.
- Research reports are evidence and ingestion queues, not canonical data.
- Synthetic structural fixtures live under `tests/fixtures/`, never here.

Current coverage is intentionally small: the first evidence-grounded bundle
encodes the report-plus-embedded-card form selected by ADR-0006. A covered
calibration subject does not imply complete provider coverage.

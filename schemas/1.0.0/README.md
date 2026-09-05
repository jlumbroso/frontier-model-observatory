# Frontier Model Observatory schema candidate 1.0.0

Draft 2020-12 schemas and JSONL fixtures for the first evidence model.

The records under `tests/fixtures/schema/` are structural examples. They use
calibration vocabulary to exercise references and invariants, but they are not
canonical research claims and must never be projected into the public corpus.

Every non-byte record has:

- an opaque typed UUID identity in `id`;
- an immutable, grep-friendly `canonical_key`, unique within `record_type`;
- source-native and normalized values where normalization occurs.

Foreign keys always use `id`, never `canonical_key`. Byte objects are addressed by
their SHA-256 digest and do not have a canonical key.

Install and validate:

```sh
python -m pip install -r requirements.txt
python scripts/validate_records.py tests/fixtures/schema \
  --exclusion-policy policy/exclusions.json
python -m unittest discover -s tests -v
```

The validator checks JSONL framing, Draft 2020-12 schemas, global ID and
canonical-key uniqueness, foreign-key types, containment and supersession
cycles, temporal ordering, redirect chains, byte hashes when materialized, and
selected family-specific invariants.

Schema identifiers are immutable URNs such as
`urn:fmo:schema:1.0.0:artifact`; local validation resolves them through an
explicit registry and never depends on network retrieval.

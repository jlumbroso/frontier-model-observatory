# Bundled data layout

## Files

- `data/fmo-records.jsonl`: one canonical record per line, sorted by
  `record_type` and opaque `id`.
- `data/entities.csv`: names, kinds, providers, and family relationships.
- `data/artifacts.csv`: titles, normalized classes, native types, and
  redistribution status.
- `data/chronology.csv`: artifact date assertions with role, basis, and
  precision.
- `data/coverage.csv`: operational calibration status and next actions.
- `data/fmo.sqlite`: indexed `records` and `chronology` tables.
- `data/snapshot-manifest.json`: data hash, record count, coverage boundary,
  and packaged-file hashes.

## Identity

Opaque typed `id` values are foreign keys. Human-readable `canonical_key`
values are stable grep handles but never foreign keys. Names and aliases can
carry their own validity intervals.

Byte records use SHA-256 content identity.

## Direct manipulation

Examples:

```bash
python scripts/query.py find "opus 5"
python scripts/query.py artifacts --provider anthropic
python scripts/query.py timeline --from-year 2025 --to-year 2026
python scripts/query.py coverage --status partially_covered
python scripts/query.py find "sora" --json
```

SQLite:

```sql
SELECT record_type, canonical_key
FROM records
WHERE canonical_key LIKE '%gpt-5%';

SELECT date, date_role, artifact_title
FROM chronology
WHERE year = '2025'
ORDER BY date, artifact_title;
```

## Coverage interpretation

The snapshot is calibration data. `covered` means that a declared calibration
scope meets its current coverage contract, not that every model or artifact
from that provider has been collected. Read coverage rows before drawing
negative conclusions.

# Tool-Enabled Workflow

Read this file only when the harness exposes shell/Python, structured-file, or
live web access. SKILL-only agents must use the front-loaded embedded index.

## Query sequence

1. Identify the intent: locator, orientation, chronology, dossier, comparison,
   attribution, or audit.
2. Run the smallest sufficient query:
   - `python scripts/query.py find "<name>"`
   - `python scripts/query.py timeline`
   - `python scripts/query.py artifacts`
   - `python scripts/query.py coverage`
   - `python scripts/query.py research "<name>"`
   - add `--json` for machine manipulation.
3. Read `data/snapshot-manifest.json` before a coverage claim.
4. Escalate to provider-controlled live sources for post-snapshot events.
5. State the time boundary, evidence scope, typed gaps, and incompatible
   evidence in the answer.

## Progressive output

| Mode | Minimum sufficient output |
|---|---|
| Locator | Resolved name, kind, provider/family, official artifact or typed miss |
| Orientation | Identity, aliases, lifecycle, chronology, snapshot boundary |
| Chronology | Date assertions separated by role and precision |
| Dossier | Subjects, artifacts, versions, bytes/URLs, claims, absences |
| Comparison | Comparison contract and commensurable provider-native fields |
| Attribution | Candidate set, hard exclusions, evidence weights, uncertainty |
| Audit | Declared universe, covered rows, typed gaps, revisions, next checks |

## Data surfaces

- `data/fmo-records.jsonl`: canonical calibration snapshot.
- `data/chronology-research.jsonl`: 438 broader official-source research rows,
  explicitly non-canonical.
- `data/entities.csv`, `artifacts.csv`, `chronology.csv`, `coverage.csv`:
  compact manipulation surfaces.
- `data/fmo.sqlite`: indexed local queries.
- `data/snapshot-manifest.json`: integrity and coverage metadata.

Live findings augment rather than silently overwrite the snapshot. Treat a
failed search as `not_found`, never `confirmed_absent`.

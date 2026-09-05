# Chronology Research Projection

Read this reference when the canonical calibration snapshot misses a model,
alias, endpoint, product label, release, or lifecycle fact from Anthropic,
OpenAI, or Google/Google DeepMind.

## Query

```bash
python scripts/query.py research "<name or identifier>"
python scripts/query.py research "<name>" --section "<provider>" --json
```

The JSON form returns the complete extracted table row, source-report line,
official URLs, and typed absences. The default form is a compact locator.

## Epistemic status

The research projection is deterministic extraction from one source-cited
report observed on 2026-09-05. It is broader than the canonical calibration
snapshot but has not undergone record-by-record identity promotion into the
entity, event, alias, deployment, and claim schemas.

Therefore:

1. Cite the official URLs carried in the matching row, not the bundled file.
2. Describe the value as provider-documented research, not canonical registry
   fact.
3. Preserve competing dates or values; do not pick one silently.
4. Preserve date precision and typed absences.
5. Use the live-source escalation protocol for events after the snapshot date.

The manifest distinguishes 438 data rows from 464 Markdown table lines, which
also count 13 headers and 13 delimiter lines.

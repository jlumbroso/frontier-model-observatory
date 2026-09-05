# Frontier Model Observatory Skill

A progressively disclosed, provenance-first skill for AI model chronology,
official disclosure artifacts, prompts, and conversation attribution.

## Included

- compact `SKILL.md` decision protocol;
- optional epistemic, attribution, query-mode, and data-layout references;
- deterministic query script;
- dated canonical JSONL/CSV/SQLite snapshot;
- integrity and coverage manifest.

Provider PDF and HTML archives are intentionally not bundled. The skill retains
their official locators and byte identities while keeping installation small.

## Use

```bash
python scripts/query.py find "model name"
python scripts/query.py timeline
python scripts/query.py artifacts --provider openai
python scripts/query.py coverage
```

The snapshot is a calibration corpus, not comprehensive frontier coverage.
Queries beyond it should escalate to current official-source research.

## Source

The canonical repository is
`https://github.com/jlumbroso/frontier-model-observatory`.

Version: 0.1.1
License: MIT

---
name: frontier-model-observatory
description: "Frontier AI model chronology, cards, prompts, release identity, and conversation attribution. Use for model timelines, unfamiliar model names, system/model cards, safety disclosures, prompt provenance, or identifying a model from a dated conversation; not for generic AI explanations without a model-history question."
license: MIT
compatibility: "Bundled snapshot queries require Python 3.10+. Live updates require web access. The snapshot is useful without either."
metadata:
  author: "Jérémie Lumbroso and GPT 5.6 Sol at Perplexity Computer"
  version: "0.1.0"
---

# Frontier Model Observatory

Use a provenance-first, temporal record of AI models, releases, artifacts, and
prompts. Separate what a provider stated from what an evaluator measured and
what the observatory inferred.

## Scope warning

The bundled snapshot is a **calibration corpus**, not comprehensive frontier
coverage. Read `data/snapshot-manifest.json` before making a coverage claim.
When a requested model, release, or date lies outside the snapshot, report a
typed miss and research current official sources instead of guessing.

## Workflow

1. **Identify the intent and time boundary.**
   - Locator: find an unfamiliar model or document.
   - Orientation: place a model in a provider and family.
   - Chronology: determine what existed or was documented by a date.
   - Dossier: assemble one subject's artifacts, versions, claims, and gaps.
   - Comparison: compare provider disclosures or evaluations.
   - Attribution: identify plausible authorship of a conversation.
   - Audit: assess coverage, revisions, missing disclosures, or stale links.
2. **Query the smallest sufficient snapshot surface.**
   - Run `python scripts/query.py find "<name>"` for unfamiliar names.
   - Run `python scripts/query.py timeline` for date questions.
   - Run `python scripts/query.py artifacts` for cards and reports.
   - Run `python scripts/query.py coverage` before claiming completeness.
   - Add `--json` when the result will be manipulated by code or another tool.
3. **Load depth only when the task requires it.**
   - Read `references/epistemic-protocol.md` for comparisons, audits, claim
     synthesis, or any consequential conclusion.
   - Read `references/query-modes.md` when choosing output depth or handling a
     compound request.
   - Read `references/attribution.md` for conversation attribution.
   - Read `references/data-layout.md` for direct JSONL/CSV/SQLite work.
4. **Escalate beyond the snapshot honestly.**
   - Search provider-controlled indexes, cards, reports, documentation, and
     release pages.
   - Prefer the original artifact and record retrieval time.
   - Preserve provider-native terminology before mapping it.
   - Treat a failed search as `not_found`, never `confirmed_absent`.
   - Keep live findings separate from bundled snapshot facts until canonical
     ingestion and validation occur.
5. **Answer at the smallest sufficient depth.**
   - State the subject, time boundary, and evidence scope.
   - Cite official URLs next to factual claims.
   - Name decisive uncertainty and incompatible evidence.
   - Offer the next deeper mode only when it could change the conclusion.

## Epistemic invariants

Never collapse:

- model family, model, checkpoint, configuration, deployment, product,
  endpoint, or alias;
- provider assertion, evaluation result, independent verification, or
  observatory inference;
- publication, revision, index, observation, retrieval, and transport dates;
- artifact, artifact version, URL, byte object, or part of a larger document;
- `not_reported`, `not_found`, `not_evaluated`, `withheld`,
  `not_applicable`, and `confirmed_absent`;
- provider-issued files and observatory-generated captures or renderings.

Do not compare scores unless subject, benchmark, metric, harness, configuration,
date, and mitigation state are sufficiently commensurable. If they are not,
present a sourced juxtaposition rather than a ranking.

## Progressive output contract

| Mode | Minimum sufficient output |
|---|---|
| Locator | Resolved name, kind, provider/family, official artifact or typed miss |
| Orientation | Identity, aliases, lifecycle, known chronology, snapshot boundary |
| Chronology | Date assertions separated by role and precision |
| Dossier | Subjects, artifacts, versions, byte/URL identity, claims, absences |
| Comparison | Comparison contract, commensurable fields, provider-native terms |
| Attribution | Candidate set, hard exclusions, evidence weights, residual uncertainty |
| Audit | Declared universe, covered rows, typed gaps, revisions, next checks |

## Hard failure behavior

- Unknown recent name: search; do not reinterpret it as a typo without evidence.
- Impossible date attribution: test both model attribution and timestamp
  corruption.
- Multiple artifacts with one title: preserve separate versions and bytes.
- One URL with changed bytes: create a new observation/version; do not overwrite.
- HTML-only disclosure: do not invent a PDF.
- Card embedded in a report: cite the part locator; do not fabricate a
  standalone document.
- Official page containing repository-excluded material: preserve only allowed
  metadata, URL, hash, and typed policy outcome.

## Examples

**Unfamiliar name**

> "What is Claude Opus 5, and could a January 2025 model know about it?"

Use Orientation, state the snapshot date, and distinguish the newer model's
release evidence from the older model's training cutoff.

**Conversation attribution**

> "This transcript is dated 2024 but attributed to a model released in 2026."

Use Attribution. Treat release incompatibility as strong evidence, consider
timestamp corruption separately, and do not infer authorship from style alone.

**Provider comparison**

> "Which provider publishes more complete safety documentation?"

Use Audit before Comparison. Define the artifact universe and dimensions;
compare documented coverage, not provider marketing vocabulary.

## Bundled resources

- `scripts/query.py`: run for deterministic snapshot lookup and filtering.
- `data/fmo-records.jsonl`: complete bundled canonical snapshot.
- `data/entities.csv`, `data/artifacts.csv`, `data/chronology.csv`,
  `data/coverage.csv`: compact manipulation surfaces.
- `data/fmo.sqlite`: indexed local queries.
- `data/snapshot-manifest.json`: coverage boundary and integrity metadata.
- `references/epistemic-protocol.md`: read for evidence synthesis.
- `references/query-modes.md`: read for progressive depth selection.
- `references/attribution.md`: read for authorship reconstruction.
- `references/data-layout.md`: read for direct data access.

The repository archive and research reports are intentionally not bundled.

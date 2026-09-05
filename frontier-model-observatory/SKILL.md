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

## What this skill does

This skill is an external historical memory for frontier AI models. Use it to:

- identify unfamiliar model, product, endpoint, and alias names;
- place them in provider, family, release, and retirement chronology;
- locate system cards, model cards, prompts, and technical reports;
- test whether a conversation attribution is chronologically possible;
- distinguish official facts, research extraction, canonical records, and gaps.

It contains useful knowledge at several capability levels. **Do not assume that
shell, Python, databases, structured files, sub-files, or web access exist.**
Silently determine the highest available level and use it. If only this file is
visible, the embedded orientation below is the data source, not merely
instructions for an unavailable tool.

Use a provenance-first, temporal record of AI models, releases, artifacts, and
prompts. Separate what a provider stated from what an evaluator measured and
what the observatory inferred.

## Capability ladder

1. **SKILL-only**: Use the embedded identity and chronology anchors below. State
   that the answer uses the embedded 2026-09-05 orientation when its boundary
   matters. Never claim to have queried files or tools.
2. **Markdown-only**: Read the smallest matching file under
   `references/chronology/`. Start with its `README.md`; no shell is needed.
3. **Structured-file access**: Search `data/chronology-research.jsonl` for broad
   chronology or `data/fmo-records.jsonl` for canonical calibration records.
4. **Executable access**: Run `python scripts/query.py ...` for deterministic
   filtering, JSON output, and typed misses.
5. **Live-source access**: Verify provider-controlled sources for events after
   2026-09-05 or unresolved gaps. Keep live findings separate until ingestion.

If a level is unavailable, step down; do not stop merely because a higher level
is missing. If only SKILL.md is visible and an identity is not embedded, say
exactly that the compact fallback cannot resolve it, preserve `not_found`, and
request web access or a relevant Markdown sub-file. **Do not infer identity from
naming resemblance, memory snippets, role names, or writing style.**

## Embedded orientation for SKILL-only harnesses

These are dated anchor facts, not comprehensive coverage:

- **Claude Fable 5 is not Claude Opus 5.** Fable 5 is a distinct Anthropic
  model with API ID `claude-fable-5`, released **2026-06-09**, with a
  January 2026 knowledge cutoff. Access was suspended 2026-06-12 and restored
  2026-07-01. It is the predecessor of Fable 5.1
  ([Anthropic release notes](https://platform.claude.com/docs/en/release-notes/overview),
  [Transparency Hub](https://www.anthropic.com/transparency)).
- **Claude Opus 5** is a separate Anthropic model, released **2026-07-24**,
  with API ID `claude-opus-5` and a May 2026 knowledge cutoff
  ([Anthropic model overview](https://docs.claude.com/en/docs/about-claude/models/overview)).
- **Claude Sonnet 4.5** was released **2025-09-29** with a January 2025
  knowledge cutoff. A model trained in January 2025 cannot know this release
  from core training
  ([Anthropic announcement](https://www.anthropic.com/news/claude-sonnet-4-5)).
- **Claude Fable 5.1** and **Claude Mythos 5.1** were released
  **2026-09-01**. Anthropic describes them as the same model with different
  safeguard levels; Mythos is an invite-only configuration, not an alias for
  Opus
  ([Anthropic announcement](https://www.anthropic.com/claude-fable-and-mythos-5-1)).
- **GPT-5.6 Sol** was released **2026-07-09**; `gpt-5.6` routed to
  `gpt-5.6-sol`. Its documented knowledge cutoff is 2026-02-16
  ([OpenAI changelog](https://platform.openai.com/docs/changelog)).
- **GPT-6 Astra** was released **2026-09-03** with limited rollout rather than
  general availability and a documented 2026-04-30 knowledge cutoff
  ([OpenAI model page](https://platform.openai.com/docs/models/gpt-6-astra)).
- **Gemini 3.8 Flash** became generally available **2026-09-02**. Its card
  gives a dual-valued cutoff: March 2026 generally, with some domains limited
  to January 2025
  ([Google model card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-8-Flash-Model-Card.pdf)).

For a SKILL-only answer to “Who is Fable 5?”, answer the first two bullets
directly. Do not reinterpret Fable as a personal nickname, infer it is Opus,
or invent an identifier, release, takedown, or government action.

## Scope warning

The bundled canonical snapshot is a **calibration corpus**, not comprehensive
frontier coverage. A separate official-source chronology research projection
covers the three core providers more broadly but is explicitly non-canonical.
Read `data/snapshot-manifest.json` before making a coverage claim. When a
requested model, release, or date lies outside both bundled surfaces, report a
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
   - With only SKILL.md, use the embedded orientation and stop before any
     unsupported detail.
   - With Markdown sub-files, read `references/chronology/README.md`, then one
     provider or task view.
   - Run `python scripts/query.py find "<name>"` for unfamiliar names.
   - Run `python scripts/query.py timeline` for date questions.
   - Run `python scripts/query.py artifacts` for cards and reports.
   - Run `python scripts/query.py coverage` before claiming completeness.
   - Run `python scripts/query.py research "<name>"` when the canonical
     calibration snapshot misses a core-provider model or historical label.
   - Add `--json` when the result will be manipulated by code or another tool.
3. **Load depth only when the task requires it.**
   - Read `references/epistemic-protocol.md` for comparisons, audits, claim
     synthesis, or any consequential conclusion.
   - Read `references/query-modes.md` when choosing output depth or handling a
     compound request.
   - Read `references/attribution.md` for conversation attribution.
   - Read `references/data-layout.md` for direct JSONL/CSV/SQLite work.
   - Read `references/chronology-research.md` before using non-canonical
     chronology rows in an answer or attribution analysis.
   - Read `references/chronology/README.md` when files are readable but code
     execution is unavailable.
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
- `data/chronology-research.jsonl`: 438 official-source research rows; search
  on demand and never present them as canonical records.
- `data/chronology-research-manifest.json`: source hash, counts, and semantic
  status for the research projection.
- `references/epistemic-protocol.md`: read for evidence synthesis.
- `references/query-modes.md`: read for progressive depth selection.
- `references/attribution.md`: read for authorship reconstruction.
- `references/data-layout.md`: read for direct data access.
- `references/chronology-research.md`: read before using comprehensive
  research rows.
- `references/chronology/`: generated provider- and task-specific Markdown
  chronology for no-shell environments.

The repository archive, full report, and extracted texts are not bundled.

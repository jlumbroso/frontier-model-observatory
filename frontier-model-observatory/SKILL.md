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

> **NO SHELL OR FILE ACCESS? START HERE.** Stay in “No-tools orientation”
> below. It is your complete data source. Do not attempt Python, claim to read
> sub-files, or conclude that the skill is useless.

## No-tools orientation

This skill is an external historical memory for frontier AI models. It
identifies model names, release order, aliases, cards, knowledge cutoffs, and
chronological impossibilities. The embedded snapshot below was observed
**2026-09-05**. It is useful but not exhaustive.

Use only capabilities explicitly exposed by the harness. If you have no file
reader, shell, or web tool, assume **SKILL-only** immediately. Do not “test” an
unavailable capability by proposing or imagining a command.

### Embedded release index

Sorted newest first within this compact snapshot:

| Date | Provider | Model or configuration | Key status |
|---|---|---|---|
| 2026-09-03 | OpenAI | GPT-6 Astra | Released; limited rollout, not yet GA |
| 2026-09-03 | Google | Lyria 3.5 | Music model endpoint released |
| 2026-09-02 | Google | Gemini 3.8 Flash | Stable and generally available |
| 2026-09-01 | Anthropic | Claude Fable 5.1 / Mythos 5.1 | Same model, different safeguard configurations |
| 2026-07-24 | Anthropic | Claude Opus 5 | Separate Opus model |
| 2026-07-09 | OpenAI | GPT-5.6 Sol | `gpt-5.6` routed to `gpt-5.6-sol` |
| 2026-06-30 | Anthropic | Claude Sonnet 5 | Released |
| 2026-06-09 | Anthropic | Claude Fable 5 | Distinct from Opus 5 |
| 2026-05-19 | Google | Gemini 3.5 Flash | Released |
| 2026-04-24 | OpenAI | GPT-5.5 | Released |
| 2025-09-29 | Anthropic | Claude Sonnet 4.5 | January 2025 knowledge cutoff |

Index dates come from the
[Anthropic release notes](https://platform.claude.com/docs/en/release-notes/overview),
[OpenAI changelog](https://platform.openai.com/docs/changelog), and
[Google model lifecycle table](https://ai.google.dev/gemini-api/docs/deprecations).

For “latest” questions, say **latest in this embedded snapshot**, name the
provider and modality boundary, and do not imply exhaustive coverage. Here,
the latest embedded OpenAI model is GPT-6 Astra; the latest embedded Anthropic
release is Fable 5.1 / Mythos 5.1; and the latest embedded Google release is
Lyria 3.5, with Gemini 3.8 Flash the latest embedded general multimodal model.

## What this skill does

This skill is an external historical memory for frontier AI models. Use it to:

- identify unfamiliar model, product, endpoint, and alias names;
- place them in provider, family, release, and retirement chronology;
- locate system cards, model cards, prompts, and technical reports;
- test whether a conversation attribution is chronologically possible;
- distinguish official facts, research extraction, canonical records, and gaps.

Use a provenance-first, temporal record of AI models, releases, artifacts, and
prompts. Separate what a provider stated from what an evaluator measured and
what the observatory inferred.

## Capability upgrades

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

Do not probe capabilities by attempting `python --version`. Inspect only the
tools and resources the harness explicitly exposes. If a level is unavailable,
step down. If an identity is not embedded, say the compact snapshot cannot
resolve it, preserve `not_found`, and request live research or one relevant
Markdown file. **Do not infer identity from naming resemblance, memory
snippets, role names, or writing style.**

## Embedded identity details

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
When a requested model, release, or date lies outside the embedded snapshot,
report a typed miss and request a higher capability instead of guessing.

## When more access exists

- **Markdown reader**: Read `references/chronology/README.md`, then exactly one
  provider or task file.
- **Structured-file reader**: Use `data/chronology-research.jsonl` for broad
  chronology and `data/fmo-records.jsonl` for canonical calibration records.
- **Shell/Python**: Read `references/tool-enabled-workflow.md`, then use
  `scripts/query.py`.
- **Live web**: Verify events after 2026-09-05 from provider-controlled sources.
- **Attribution or comparison**: Read only the matching optional protocol.

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

## Optional resource map

- Markdown-only chronology: `references/chronology/README.md`
- Tool-enabled procedure: `references/tool-enabled-workflow.md`
- Evidence synthesis: `references/epistemic-protocol.md`
- Conversation attribution: `references/attribution.md`
- Structured data: `references/data-layout.md`

Do not read these when only SKILL.md is available. The repository archive,
full report, and extracted texts are not bundled.

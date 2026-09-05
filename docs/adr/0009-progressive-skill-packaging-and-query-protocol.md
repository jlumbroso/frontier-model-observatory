<!-- adr template version: "adr 3.10.0" -->

# Progressive Skill Packaging and Query Protocol

- **Date**: 2026-09-05
- **Iteration**: 4
- **Status**: Partially Implemented
- **Deciders**: GPT 5.6 Sol at Perplexity Computer, under the continuing agency grant

**TL;DR**: Package a thin progressive skill with a validated canonical snapshot and deterministic query tool, while keeping archival binaries and deep research reports in the repository.

---

## Originating Context

**Source**: Founding conversation and implemented architecture in ADR-0003, ADR-0006, ADR-0007, and ADR-0008.

The human requires a broad-ranging skill usable by models with stale training, redundant access paths for context loading and manipulation, and downloadable skill artifacts on releases. The repository now has 146 canonical calibration records and a comprehensive 438-row official-source chronology research projection.

An operational test in a Companion harness exposed a false assumption: that a
loaded skill can necessarily execute Python or read bundled sub-files. The
harness loaded only `SKILL.md`. Asked “Do you know who Fable 5 is?”, the model
first conflated Fable 5 with Opus 5, then invented an identifier, release date,
and government takedown. After being directed to the skill, it discovered that
it could neither run `query.py` nor read the referenced data and concluded the
skill was architecturally incompatible. See
`docs/vignettes/2026-09-05-skill-only-fable-5-failure.md`.

**Agency Grant**: Build the best model-usable skill and release surface without waiting for another blocking question.

---

## Explicitation

**What I understand**:

1. The skill should teach an agent how to reason from the observatory, not load every card into context.
2. A model without repository access still needs a compact dated snapshot for chronology, identity, artifact, and coverage questions.
3. Progressive disclosure should deepen from lookup to dossier, comparison, attribution, and corpus audit only when the user’s decision requires it.
4. Archived binaries belong in the repository’s evidence layer, not the default skill context.

**Assumptions**:

- The first skill release is an honest calibration release, not a claim of comprehensive provider coverage.
- A standard-library query script is more reliable than asking every host model to reinvent JSONL filtering.
- Packaged data is generated from canonical records and is never edited inside the skill.

**Confirm**: Self-check against founding requirements and accepted ADRs.

---

## Decision

### Skill hub

Keep `SKILL.md` compact. It defines:

- trigger and non-trigger boundaries;
- intent detection;
- source and evidence hierarchy;
- progressive output modes;
- epistemic invariants;
- required typed-absence and temporal behavior;
- exact conditions for reading references or running the query script.

### Progressive modes

Support:

1. **Locator**: identify a model or official artifact.
2. **Orientation**: place a model in provider, family, release, and alias context.
3. **Chronology**: answer date and historical-availability questions.
4. **Dossier**: assemble one subject’s artifacts, versions, prompts, claims, and gaps.
5. **Comparison**: compare only commensurable, explicitly scoped evidence.
6. **Attribution**: rule conversation candidates in or out using hard temporal and deployment constraints before weak stylistic evidence.
7. **Audit**: evaluate disclosure coverage, revision history, typed absences, and corpus freshness.

The model should produce the smallest sufficient mode and deepen only when compression would erase a decisive distinction.

### Runtime capability ladder

The package must remain useful at five independently testable levels:

1. **SKILL-only**: `SKILL.md` explains the capability and embeds a small,
   source-linked identity and chronology spine for load-bearing recent models.
2. **Markdown-only**: generated provider and task views under
   `references/chronology/` expose the comprehensive research corpus without
   requiring code or structured-file access.
3. **Structured-file access**: JSONL, JSON, CSV, and SQLite support direct
   manipulation.
4. **Executable access**: `query.py` supplies deterministic filtering and typed
   misses.
5. **Live-source access**: provider-controlled sources update or extend the
   dated snapshot.

Agents step down when a capability is absent; they do not stop at an
unavailable higher level. The hub must never direct a SKILL-only agent to an
unavailable tool as its sole answer path. Naming resemblance, conversation
snippets, and role names are not identity evidence.

### Packaged resources

Bundle:

- the complete current canonical JSONL snapshot;
- the comprehensive core-provider chronology research JSONL and its manifest,
  explicitly marked `research_projection_not_canonical`;
- compact CSV indexes for entities, artifacts, chronology, and coverage;
- a standard-library query script;
- references for epistemic protocol, query modes, data layout, and attribution;
- snapshot manifest with schema version, coverage boundary, hashes, and source revision.

Do not bundle provider PDF/HTML bytes, quarantine material, full extracted texts, or the full research reports. Records preserve official URLs and hashes; repository users can inspect the archive and release users can download the separate extracted-text package.

### Query interface

The packaged script supports model/name lookup, artifact lookup, provider and family filtering, timeline/as-of queries, coverage inspection, raw ID resolution, and on-demand search over comprehensive chronology research. Output is deterministic Markdown or JSON and states whether results are canonical or research projections.

### Release contract

Build a deterministic ZIP named with skill version, include SHA-256 checksums and a manifest, validate the complete skill tree, and make release workflows attach the ZIP directly to GitHub Releases.

**Why**: This separates frequently needed orientation from optional documentary depth, preserves model context, and makes the same evidence manipulable by both language models and conventional tools.

**Trade-offs accepted**: An installed snapshot can become stale. Every answer must expose its snapshot date and trigger live official-source research for questions beyond coverage or requiring current truth.

---

## Consequences

- Skill installation works without cloning the archive.
- Loading only `SKILL.md` still explains the skill and resolves its embedded
  anchor identities without pretending to access unavailable resources.
- Markdown-readable harnesses can browse comprehensive provider chronology
  without shell or Python.
- Packaged data remains inspectable and grep-friendly.
- The skill cannot imply that current calibration coverage is comprehensive.
- Comprehensive research rows remain usable without being silently promoted to canonical identity claims.
- Live research augments rather than silently overwrites snapshot evidence.
- Release packaging and skill validation become part of `just verify-complete`.

---

## Action Items

- [x] Author and validate `SKILL.md` plus progressive references.
- [x] Implement and test the packaged query tool.
- [x] Generate snapshot data and manifest from canonical records.
- [x] Implement deterministic ZIP, checksum, and release manifest generation.
- [x] Register skill freshness, validation, and packaging with `just verify`.
- [x] Bundle and query the comprehensive chronology behind an explicit non-canonical boundary.
- [x] Add and test SKILL-only and Markdown-only graceful-degradation paths.

---

## Validation

- [x] Architecture distinguishes skill context from archival evidence.
- [x] Agent Skills validator passes the complete 19-file tree.
- [x] Query tests cover lookup, chronology, as-of, coverage, typed misses, and non-canonical research lookup.
- [x] SKILL-only regression test requires the explicit statement that Claude
  Fable 5 is not Claude Opus 5 and forbids identity inference from naming.
- [x] Markdown generation tests require non-empty Anthropic, OpenAI, and Google
  partitions and known anchor identities.
- [x] A rebuilt skill tree matches committed generated resources.
- [x] Release package is deterministic and checksum-bound.

---

## Iterations

### Iteration 1 (2026-09-05)
- Trigger: Canonical data and redundant projections became available.
- Contributors: GPT 5.6 Sol at Perplexity Computer.
- Changes: Defined progressive modes, package boundary, query interface, and release contract.
- Outcome: Accepted.

### Iteration 2 (2026-09-05)
- Trigger: Skill protocol, snapshot, query CLI, validation, and packaging implemented.
- Contributors: GPT 5.6 Sol at Perplexity Computer.
- Changes: Built a 16-file progressively disclosed skill with a queryable 132-record snapshot and a deterministic 65,525-byte ZIP plus complete release bundle.
- Outcome: Accepted → Partially Implemented; hosted release publication and broader-than-calibration coverage remain.

### Iteration 3 (2026-09-05)
- Trigger: Comprehensive official-source chronology became available before semantic record-by-record canonical promotion.
- Contributors: GPT 5.6 Sol at Perplexity Computer.
- Changes: Added a 438-row chronology JSONL and manifest, an on-demand `research` query mode, a required epistemic reference, and explicit canonical-versus-research output status. The deterministic skill ZIP is now 138,192 bytes across 19 files.
- Outcome: Broader-than-calibration chronology is immediately usable by models without weakening canonical identity constraints; semantic promotion and hosted publication remain.

### Iteration 4 (2026-09-05)
- Trigger: Companion-harness test loaded only `SKILL.md`, misidentified Fable 5 as Opus 5, fabricated chronology, and could not access referenced files or Python.
- Contributors: Jérémie Lumbroso; Claude Sonnet 4.5 as test subject; GPT 5.6 Sol at Perplexity Computer.
- Changes: Added an explicit five-level capability ladder, a source-linked SKILL-only orientation spine, a hard Fable-versus-Opus identity invariant, eight generated Markdown chronology views, and regression tests for constrained harnesses.
- Outcome: The skill now degrades from live research through executable, structured-file, Markdown-only, and SKILL-only operation instead of collapsing when tools are unavailable.

---

## Links

- Related ADRs: `0003-epistemic-records-and-generated-views.md`, `0004-artifact-archive-and-prompt-provenance.md`, `0007-legible-continuous-integration-and-release-artifacts.md`, `0008-canonical-schema-package-identifiers-and-validation-layers.md`
- Related code: `frontier-model-observatory/`, skill builder and package scripts
- Supersedes: none

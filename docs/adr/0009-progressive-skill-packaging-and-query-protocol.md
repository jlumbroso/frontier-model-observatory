<!-- adr template version: "adr 3.10.0" -->

# Progressive Skill Packaging and Query Protocol

- **Date**: 2026-09-05
- **Iteration**: 3
- **Status**: Partially Implemented
- **Deciders**: GPT 5.6 Sol at Perplexity Computer, under the continuing agency grant

**TL;DR**: Package a thin progressive skill with a validated canonical snapshot and deterministic query tool, while keeping archival binaries and deep research reports in the repository.

---

## Originating Context

**Source**: Founding conversation and implemented architecture in ADR-0003, ADR-0006, ADR-0007, and ADR-0008.

The human requires a broad-ranging skill usable by models with stale training, redundant access paths for context loading and manipulation, and downloadable skill artifacts on releases. The repository now has 146 canonical calibration records and a comprehensive 438-row official-source chronology research projection.

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

---

## Validation

- [x] Architecture distinguishes skill context from archival evidence.
- [x] Agent Skills validator passes the complete 19-file tree.
- [x] Query tests cover lookup, chronology, as-of, coverage, typed misses, and non-canonical research lookup.
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

---

## Links

- Related ADRs: `0003-epistemic-records-and-generated-views.md`, `0004-artifact-archive-and-prompt-provenance.md`, `0007-legible-continuous-integration-and-release-artifacts.md`, `0008-canonical-schema-package-identifiers-and-validation-layers.md`
- Related code: `frontier-model-observatory/`, skill builder and package scripts
- Supersedes: none

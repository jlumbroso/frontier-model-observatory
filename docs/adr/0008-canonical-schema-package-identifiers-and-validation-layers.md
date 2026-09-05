<!-- adr template version: "adr 3.10.0" -->

# Canonical Schema Package, Identifiers, and Validation Layers

- **Date**: 2026-09-05
- **Iteration**: 1
- **Status**: Accepted
- **Deciders**: GPT 5.6 Sol at Perplexity Computer, under the continuing agency grant

**TL;DR**: Use versioned JSON Schema 2020-12, type-homogeneous JSONL streams, opaque typed IDs plus human-readable canonical keys, and layered semantic validation beyond schema shape.

---

## Originating Context

**Source**:

- [Evidence Schema Recommendation](../research/2026-09-05-evidence-schema-recommendation.md)
- [Primary-Source Calibration Corpus](../research/2026-09-05-primary-source-calibration-corpus.md)
- ADR-0003 and ADR-0006

The calibration report demonstrated that artifact, version, bytes, URLs, retrievals, parts, claims, and subject identities change on different timescales. The schema review converted those observations into an implementation-ready package and found no blocking design question.

**Agency Grant**: Make reversible implementation choices and continue without human interruption unless no safe progress remains.

---

## Explicitation

**What I understand**:

1. JSON Schema should validate record shape, but cannot establish referential, temporal, graph, byte-integrity, or epistemic correctness alone.
2. Canonical JSONL streams should be homogeneous so models and tools can load one record family without filtering a universal event soup.
3. Identities must survive corrected names and boundaries, while humans and models still need grep-friendly handles.
4. Provider-native terms and dates must survive every normalized projection.

**Assumptions**:

- Schema version `1.0.0` is pre-release until all twelve calibration bundles validate.
- Identifier flavor is not meaningful to consumers beyond the documented typed grammar.
- Controlled vocabularies must have explicit `other` escape hatches and preserve native values.

**Confirm**: Self-check against the two research reports and accepted architecture.

---

## Decision

### Schema package

Use JSON Schema Draft 2020-12 under `schemas/1.0.0/`, with immutable absolute `$id` values and a common definitions schema.

Use separate canonical JSONL streams for:

- entities;
- events;
- artifacts;
- artifact versions;
- byte objects;
- URL aliases;
- redirect observations;
- artifact parts;
- artifact relationships;
- claims;
- retrieval events;
- typed absences;
- coverage-ledger entries.

Provide a union schema for mixed-record validation, not a mixed canonical stream.

### Shared and separate concepts

Use one discriminated entity schema for organizations, model families, models, checkpoints, configurations, products, deployments, endpoints, and aliases. “Provider” is an organization role.

Use one claim schema for ordinary and evaluation claims because they share evidence, attribution, epistemic status, bitemporality, and correction semantics. Evaluation claims add strict conditional fields.

Keep artifacts, versions, byte objects, URL aliases, redirect observations, parts, relationships, retrievals, absences, and coverage entries separate because each has distinct identity, lifecycle, and validation rules.

### Identifiers and model-usable handles

Every non-byte canonical record has:

- an opaque, typed, immutable identifier such as `fmo:artifact:<uuid>`;
- a required `canonical_key`, unique within record type, human-readable, grep-friendly, and immutable after schema release;
- time-scoped names and aliases that may change without rewriting foreign keys.

Foreign keys use opaque IDs, never canonical keys or names. Generated views may expose canonical keys prominently.

Byte objects are content-addressed by lowercase SHA-256 and use `fmo:sha256:<digest>`.

This dual system intentionally differs from the schema review’s opaque-only recommendation. Opaque IDs preserve referential stability; canonical keys preserve model experience and inspectability.

### Time and uncertainty

Preserve valid time and observed time as independent axes. Time values carry lexical precision (`instant`, `day`, `month`, or `year`), source-native rendering, qualifier, basis, and evidence where applicable. Never synthesize a day from month-only evidence.

Keep publication, revision, cover, index, platform, effective, and transport dates as typed assertions rather than one overloaded date.

Typed absences are records, not null values. `not_found` requires a bounded search scope and normally a recheck date. `confirmed_absent` requires authoritative or provably exhaustive evidence.

### Validation layers

Run validation in this order:

1. JSONL framing and duplicate-key checks.
2. JSON Schema.
3. ID uniqueness, prefix/type agreement, and references.
4. Graph invariants and cycle checks.
5. Temporal and as-of semantics.
6. Byte hashes, lengths, media detection, and storage.
7. Retrieval and redirect continuity.
8. Evidence-locator resolution.
9. Epistemic and correction rules.
10. archive, quarantine, and redistribution policy.
11. coverage-ledger consistency.
12. repository exclusion policy.
13. deterministic projection regeneration.

Each implemented layer registers a real check and summary metrics with `just verify`.

**Why**: This decomposition follows the independent change rates observed in the twelve calibration subjects while providing stable intermediate forms for implementation and model use.

**Trade-offs accepted**: The schema family is larger than a single relational table. Its explicit boundaries reduce hidden coupling, and homogeneous streams allow consumers to load only what they need.

---

## Consequences

- Natural names can be corrected without cascading foreign-key rewrites.
- Canonical keys are convenience handles, not identity.
- A schema-valid record may still fail semantic validation.
- Evaluation corrections become linked claims rather than overwritten numbers.
- URLs and transport headers remain observations, not artifact identity or editorial facts.
- A missing standalone file cannot be fabricated for a disclosure embedded in a report.

---

## Action Items

- [ ] Implement and meta-validate the complete schema package.
- [ ] Implement JSONL framing, schema, registry, and integrity validators.
- [ ] Add one non-contrived fixture bundle per calibration subject.
- [ ] Register schema and canonical-record checks with the summary engine.
- [ ] Revisit artifact-version scope overrides only after all twelve bundles are encoded.

---

## Validation

- [x] Schema recommendation covers all documentary-variation dimensions.
- [x] No blocking design question remains.
- [ ] All schema files pass Draft 2020-12 meta-validation.
- [ ] All twelve fixture bundles pass layered validation.
- [ ] Optional calibration subjects require no field overloading.

---

## Iterations

### Iteration 1 (2026-09-05)
- Trigger: Completion of the evidence-schema design review.
- Contributors: Schema-design subagent; GPT 5.6 Sol at Perplexity Computer.
- Changes: Adopted package boundaries, homogeneous streams, layered validation, and dual opaque/readable identifiers.
- Outcome: Accepted.

---

## Links

- Related ADRs: `0003-epistemic-records-and-generated-views.md`, `0004-artifact-archive-and-prompt-provenance.md`, `0006-calibration-corpus-and-documentary-variation-stopping-rule.md`, `0007-legible-continuous-integration-and-release-artifacts.md`
- Related research: `docs/research/2026-09-05-evidence-schema-recommendation.md`
- Related code: `schemas/1.0.0/`, `data/`, schema validator
- Supersedes: none

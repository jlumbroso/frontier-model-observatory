<!-- adr template version: "adr 3.10.0" -->

# Epistemic Records and Generated Views

- **Date**: 2026-09-05
- **Iteration**: 4
- **Status**: Partially Implemented
- **Deciders**: Jérémie Lumbroso; GPT 5.6 Sol at Perplexity Computer

**TL;DR**: Keep canonical, versioned evidence records in the repository and generate many redundant path-oriented views for humans, models, grep, and data tools.

---

## Originating Context

**Source**: Founding conversation, 2026-09-05.

The human asked for the same body of knowledge to be reachable by provider, year, family, and other filters, as well as Markdown, JSON, CSV, and JSONL. The reason is not cosmetic duplication: models often load only a subpath or context slice, while scripts need formats they can grep, stream, join, and validate.

Human answer, preserved:

> "I think the canonical representation should probably be on our repo and rendered and projected in several different formats but also like like suborganizations because models can load like sub paths one at a time ... reorganizing the same information [through] very different paths can I think be helpful."

**Agency Grant**: Choose a coherent canonical representation and derive redundant access structures.

---

## Explicitation

**What I understand**:

1. The Git repository is the durable system of record.
2. Redundant organization is a usability feature when views are generated from common records.
3. Models need small, semantically coherent context packs rather than one universal corpus dump.
4. Human-readable projections and machine-readable datasets must not become independent truth-maintenance surfaces.

**Assumptions**:

- Canonical means authoritatively edited and reviewed, not necessarily one physical file.
- Generated outputs may be committed when doing so improves availability, diffability, or use without a build environment.
- Every projection will declare the dataset/schema version and generation provenance.

**Confirm**: Jérémie should confirm the proposed canonical record families and historical correction semantics.

---

## Epistemic invariants

Every load-bearing assertion should be representable as an evidence-bearing claim with:

- subject identity and subject type;
- exact claim and source-native wording where relevant;
- source artifact identity and canonical/retrieval URLs;
- evidence location such as page, section, table, or passage;
- provider, evaluator, or observatory attribution;
- model/system/product/deployment scope;
- publication, validity, observation, and retrieval times where known;
- epistemic status: stated, measured, derived, inferred, disputed, or unknown;
- lifecycle: current, superseded, withdrawn, or unclear.

The representation must keep these distinctions:

- model family ≠ model ≠ checkpoint ≠ system ≠ product ≠ endpoint;
- provider claim ≠ evaluation result ≠ independent verification ≠ observatory inference;
- not reported ≠ not found ≠ not evaluated ≠ withheld ≠ not applicable;
- source-native term ≠ normalized comparison category.

---

## Questions

### QST-CANONICAL-FORM: Which record families should be authoritatively edited?
- Status: answered
- Why asking: The repository can generate many views only if the editable source has stable natural joints.
- Need: Approve or revise the proposed hybrid.

**Options**:

- **A — Relational tables**: Canonical CSV/SQLite-style entities and foreign keys.
- **B — Event log**: Canonical append-only release, artifact, and correction events.
- **C — Claim graph**: Canonical atomic claims with evidence edges; entities and timelines are projections.
- **D — Bounded hybrid**: Separate canonical entity, event, artifact, and claim JSONL streams under versioned schemas.

**Recommendation**: (by GPT 5.6 Sol at Perplexity Computer)

**D — Bounded hybrid.**

**Rationale**: ADR-0002’s five layers have different change patterns. Stable identity belongs in entity records, chronology in events, immutable bytes and retrieval metadata in artifact records, and contestable assertions in claims. Forcing all four into a single relational snapshot, event log, or claim graph would make ordinary edits depend on unrelated machinery.

**Confidence**: High in the separation, medium in JSONL as the initial physical encoding.

**Falsifier**: If calibration shows that the same fact must be edited in multiple canonical streams, or that identity cannot be maintained without graph-native transactions, the bounded hybrid is not sufficiently near-decomposable.

**ANS:** (by Jérémie "Sonnet 4.5" Lumbroso (via ADRs4AI mobile))
D — Bounded hybrid.

---

### QST-HISTORICAL-TRUTH: How should corrections preserve what was previously believed?
- Status: answered
- Why asking: Conversation attribution needs “what was true or documented as of date X,” while later research may correct earlier records.
- Need: Approve or revise the proposed temporal policy.

**Options**:

- **A — Mutable present truth**: Correct records in place; rely on Git history for prior states.
- **B — Append-only assertions**: Never change claims; append corrections and supersession edges.
- **C — Bitemporal hybrid**: Correct descriptive records when needed, while claims/events carry valid-time, observed-time, and explicit supersession; Git remains a third audit layer.

**Recommendation**: (by GPT 5.6 Sol at Perplexity Computer)

**C — Bitemporal hybrid.**

**Rationale**: Git history records when repository bytes changed, not when a release became valid or when a provider made a statement. Explicit valid-time and observed-time support historical queries, while supersession edges preserve corrections without forcing every typo into an eternal domain event.

**Confidence**: High that Git history alone is insufficient; medium-high that two temporal axes cover the first release.

**Falsifier**: If real attribution cases require additional independent times, such as product-availability time distinct from announced and effective time, the temporal model must expand rather than overload either axis.

**ANS:** (by Jérémie "Sonnet 4.5" Lumbroso (via ADRs4AI mobile))
C — Bitemporal hybrid.

---

## Proposed projections

Generate views rather than hand-maintain them:

- `views/by-provider/<provider>/`
- `views/by-year/<year>/`
- `views/by-family/<family>/`
- `views/by-modality/<modality>/`
- `views/by-artifact-type/<type>/`
- `views/as-of/<date-or-release>/`
- compact model-orientation context packs;
- Markdown dossiers and timelines;
- JSON, JSONL, CSV, and SQLite distributions.

Every generated file should identify its generator version, schema version, source revision, and coverage boundary.

---

## Decision

### Chosen: Bounded hybrid records with bitemporal historical semantics

Authoritatively edit separate, versioned entity, event, artifact, and claim streams. Use JSONL as the initial physical encoding, subject to calibration, and validate them against explicit schemas.

Claims and events carry valid-time, observed-time, and explicit supersession where applicable. Git history remains an additional audit layer but is not used as a substitute for domain time. Descriptive corrections may be edited when they do not represent a historical assertion; contestable or time-sensitive changes are appended and linked.

Generate Markdown, JSON, CSV, SQLite, and redundant path-oriented views from these records. A generated view is never an independent editorial surface.

**Why**: Jérémie accepted D for canonical form and C for historical truth. The combination preserves stable natural joints while supporting “what was known or available when” queries.

**Trade-offs accepted**: Four canonical record families and two explicit temporal axes are more complex than a single table. Schema validation and cross-record referential checks are therefore mandatory.

---

## Consequences

- Redundant path organization becomes cheap and internally consistent.
- Models can load only the context slice relevant to their question.
- Canonical records require schemas and referential validation before corpus growth.
- Generated outputs are reproducible products, not alternative editorial surfaces.

---

## Action Items

- [x] Resolve canonical record families and temporal policy.
- [x] Draft schemas against a representative calibration corpus.
- [x] Define projection manifests and deterministic generation.
- [x] Add validation that generated outputs match canonical source records.

---

## Validation

- [x] GPT 5.6 Sol at Perplexity Computer: Multiple access paths are preserved as a requirement.
- [x] Jérémie "Sonnet 4.5" Lumbroso: Selected bounded hybrid records and bitemporal history.
- [ ] Calibration corpus: Each canonical fact has one authoritative home.

---

## Iterations

### Iteration 1 (2026-09-05)
- Trigger: Discussion of Markdown, JSON, CSV, JSONL, grep, and subpath loading.
- Contributors: Jérémie Lumbroso; Perplexity Computer.
- Changes: Established canonical-versus-projection distinction.
- Outcome: Draft.

### Iteration 2 (2026-09-05)
- Trigger: Human answer favoring repository canonical state and redundant organization.
- Contributors: Jérémie Lumbroso; GPT 5.6 Sol at Perplexity Computer.
- Changes: Proposed bounded canonical record families and explicit temporal correction semantics.
- Outcome: Remains Draft pending answers.

### Iteration 3 (2026-09-05)
- Trigger: QST-CANONICAL-FORM and QST-HISTORICAL-TRUTH answered through ADRs4AI mobile.
- Contributors: Jérémie "Sonnet 4.5" Lumbroso; GPT 5.6 Sol at Perplexity Computer.
- Changes: Adopted D, bounded hybrid canonical streams, and C, bitemporal historical semantics.
- Outcome: Draft → Accepted.

### Iteration 4 (2026-09-05)
- Trigger: Canonical calibration records and redundant projections implemented.
- Contributors: GPT 5.6 Sol at Perplexity Computer.
- Changes: Added 132 canonical records plus deterministic provider, year, family, artifact-type, calibration, JSON, JSONL, CSV, and SQLite projections with a hash manifest and freshness check.
- Outcome: Accepted → Partially Implemented; deeper claim extraction and full as-of semantics remain.

---

## Links

- Related ADRs: `0002-observatory-scope-and-layered-architecture.md`, `0004-artifact-archive-and-prompt-provenance.md`
- Related code: future `schemas/`, `data/`, `views/`, and `dist/`
- Supersedes: none

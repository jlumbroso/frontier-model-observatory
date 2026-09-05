<!-- adr template version: "adr 3.10.0" -->

# Calibration Corpus and Documentary-Variation Stopping Rule

- **Date**: 2026-09-05
- **Iteration**: 3
- **Status**: Partially Implemented
- **Deciders**: GPT 5.6 Sol at Perplexity Computer, under the founding agency grant

**TL;DR**: Calibrate the ontology against twelve primary-source artifacts, four per core provider, and add artifacts only when they introduce a new documentary variation or an unrepresentable combination.

---

## Originating Context

**Source**:

- Founding conversation, 2026-09-05.
- [Primary-Source Calibration Corpus Brief](../research/2026-09-05-primary-source-calibration-corpus.md), retrieved 2026-09-05.

Jérémie authorized comprehensive delivery through useful intermediate stakes and gave the implementing model agency to determine how to proceed. ADR-0003 requires calibration before canonical schemas are treated as stable.

**Agency Grant**: Select an evidence-based calibration corpus and proceed without converting every research choice into a human blocking question.

---

## Explicitation

**What I understand**:

1. Calibration is intended to discover the natural joints of provider documentation, not to approximate full provider coverage.
2. Corpus size is not a success metric; represented documentary variation is.
3. The sample must stress artifact identity, revisions, subject cardinality, modality, relation types, prompt scope, and missing byte representations.
4. The complete artifact inventory remains research evidence and a future ingestion queue even when only twelve artifacts enter schema calibration.

**Assumptions**:

- Official provider-controlled sources are sufficient for the first calibration pass.
- Four artifacts per provider cover the minimum observed variation; fifth artifacts remain available when open-weight or checkpoint-specific behavior is underrepresented.
- A new ingest failure automatically reopens calibration regardless of the nominal stopping rule.

**Confirm**: Self-check against the source-linked research report and accepted ADRs.

---

## Evidence

The provider surfaces disagree about:

- whether an index row represents a release, model, post, update, or artifact;
- whether “published or updated” is one date or several;
- whether cards are HTML, PDF, or sections inside larger reports;
- whether stable URLs redirect to hash assets, mutable filenames, or HTML;
- whether one artifact covers a model, multiple models, configurations, checkpoints, a family, product, deployment, or future versions;
- whether revisions appear as changelogs, body notes, new URLs, replaced bytes, or only transport metadata;
- whether original bytes are downloadable at all.

These differences invalidate a one-row-per-model or one-URL-per-card schema before implementation begins.

---

## Decision

### Chosen: Twelve-artifact minimum calibration set

Use the following primary-source calibration subjects.

**Anthropic**:

1. Claude Opus 4.6 System Card: dated in-document changelog and stable alias to PDF.
2. Claude Fable 5.1 and Mythos 5.1 System Card: one artifact covering two safeguard configurations with a companion risk report.
3. Claude 4 System Card: two live byte versions under one title and two model subjects.
4. Claude Opus 5 published system prompt: prompt-specific date, product scope, and explicit API non-applicability.

**OpenAI**:

1. OpenAI o1 system-card trio: one title across three coexisting documents, preview and general-availability stages, and an explicit cross-pointer.
2. GPT-5.2 update: “update to” relation, multi-level document chain, and values that can differ from launch publication.
3. GPT-Live System Card: audio modality and post-publication numeric correction with original and corrected values.
4. Sora 2 System Card: video/audio modality, HTML-only disclosure, and no downloadable PDF bytes at the apparent PDF route.

**Google and Google DeepMind**:

1. Gemini 3 Pro Model Card: alias-to-PDF, conflicting index/document dates, and a declared dependent family.
2. Veo 3 Model Card: prospective “and subsequent versions” scope and documented plus byte-level revisions.
3. Gemini Robotics 1.5 report appendix: a card as a part of a larger report covering two models.
4. Gemma 4 model card: open weights, HTML-only representation, platform-level timestamp, and separately versioned legal artifacts.

Optional fifth artifacts:

- Anthropic Claude 3.5 Sonnet addendum for family-document-plus-delta behavior.
- OpenAI gpt-oss model card for explicit provider rejection of the sibling artifact term.
- Google Gemini 2.5 Pro for one card covering experimental, preview, and general-availability checkpoints.

### Documentary-variation vector

Encode each candidate across:

- provider-native artifact term;
- format and part-of-document location;
- byte availability;
- URL and redirect topology;
- publication, revision, index, observation, and transport date semantics;
- subject count and subject kind;
- modality;
- typed relation to companion, parent, update, addendum, superseding, and governing artifacts;
- retrospective versus prospective scope;
- presence and granularity of corrected claims.

Accept an additional calibration artifact only when it adds an unseen value or exposes a combination the current ontology cannot represent.

Stop expansion on a provider surface after three consecutive candidates add no new representational demand. Reopen calibration whenever real ingest fails validation or requires overloading an existing field.

### Boundaries

- The calibration set is not the project’s coverage limit.
- Research-report rows are not canonical records until ingested and validated.
- Transport metadata is evidence about retrieved bytes, not provider editorial fact.
- “Not found” remains distinct from “confirmed absent.”
- Official prompt text is a separate artifact class from a behavioral specification.

**Why**: The twelve artifacts jointly cover every documentary-variation dimension observed in the source audit while preserving a small, inspectable first implementation surface.

**Trade-offs accepted**: Rare variations outside the core providers may later force schema evolution. Versioned schemas and the reopen-on-failure rule make that expected evolution explicit rather than treating the first ontology as final.

---

## Consequences

- Artifact, artifact-version, byte-object, URL alias, and subject require separate identities.
- Claims and evaluations require version history independent of the enclosing document.
- Artifact parts need page, section, table, or anchor locators.
- Companion and deferral relations must be typed.
- Retrieval method, retrieval time, content hash, and cache status are first-class.
- Schema completion is measured by successful representation of the variation vector, not row count.

---

## Action Items

- [x] Materialize or explicitly record a policy-blocked byte state for all twelve calibration subjects.
- [ ] Record source URL, redirect chain, retrieval time, media type, byte size, and hash.
- [x] Draft entity, event, artifact, artifact-version, byte-object, claim, and relation schemas.
- [x] Encode each calibration subject and its documentary-variation vector. Current: 12 of 12.
- [x] Validate generated provider, year, family, artifact-type, and date-assertion projections.
- [ ] Re-run the variation test against the three optional fifth artifacts.

---

## Validation

- [x] All factual selection grounds are linked to official sources in the calibration report.
- [x] The repository exclusion-policy checker passes.
- [x] Four artifacts per provider cover the observed minimum variation.
- [x] All twelve calibration subjects validate against the first schema candidate.
- [x] The report-embedded-card subject validates as 15 canonical records with materialized bytes.
- [ ] Three optional artifacts add no unrepresentable dimension.

---

## Iterations

### Iteration 1 (2026-09-05)
- Trigger: Completion of the primary-source disclosure-surface audit.
- Contributors: Research subagent; GPT 5.6 Sol at Perplexity Computer.
- Changes: Selected the minimum corpus, defined the variation vector, and established evidence-based stop and reopen rules.
- Outcome: Accepted.

### Iteration 2 (2026-09-05)
- Trigger: First canonical calibration bundle implemented.
- Contributors: GPT 5.6 Sol at Perplexity Computer.
- Changes: Encoded the Gemini Robotics 1.5 report and embedded model-card part as 15 records across 11 streams, using actual PDF bytes, hash, size, media type, URL, date assertions, subjects, typed absence, and coverage.
- Outcome: Accepted → Partially Implemented; 1 of 12 subjects encoded.

### Iteration 3 (2026-09-05)
- Trigger: Remaining calibration artifacts retrieved, policy-checked, and encoded.
- Contributors: GPT 5.6 Sol at Perplexity Computer.
- Changes: Encoded all twelve subjects as 132 canonical records; materialized 14 byte objects and retained one policy-blocked HTML capture as remote-only hash evidence; generated all required access projections.
- Outcome: Remains Partially Implemented; deep claims, exact text anchors, and three optional variation probes remain.

---

## Links

- Related ADRs: `0002-observatory-scope-and-layered-architecture.md`, `0003-epistemic-records-and-generated-views.md`, `0004-artifact-archive-and-prompt-provenance.md`
- Related research: `docs/research/2026-09-05-primary-source-calibration-corpus.md`
- Related code: future artifact manifest and schema validators
- Supersedes: none

<!-- adr template version: "adr 3.10.0" -->

# Artifact Archive and Prompt Provenance

- **Date**: 2026-09-05
- **Iteration**: 2
- **Status**: Draft
- **Deciders**: Jérémie Lumbroso; GPT 5.6 Sol at Perplexity Computer

**TL;DR**: Preserve repository-controlled copies, text extractions, summaries, hashes, and source metadata for cards and official prompts, while making provenance and redistribution status explicit.

---

## Originating Context

**Source**: Founding conversation, 2026-09-05.

The human requested a PDF of every located card, its sourcing link, full text, summaries, compilations, and system prompts where available. The archive may be larger than the distributable skill; the skill can carry compact indexes and live links while the repository remains the comprehensive substrate.

Human answer, preserved:

> "Everything can be committed and redistributed. we can we should have our own copies of the system prompts and of the system cards and model cards.
>
> They are public and we shouldn't like just centralize them in a clean organized way. We should have like text versions of them and summaries of them and all of that. And we don't necessarily need to include these in the skill. We could include like a list of links in the scale and try to keep it current and have like continue integration to check whether those links change or something."

On unofficial prompt material:

> "Yes, an official prompt, but the prompt exists on the official website most of the time."

**Interpretation note**: The prompt answer is read as: official prompts belong in the main corpus; unofficial material, if retained, must be separated or quarantined. This needs confirmation.

**Agency Grant**: Design archival and provenance policy; do not hide meaningful legal or evidentiary uncertainty.

---

## Explicitation

**What I understand**:

1. The observatory should not depend solely on provider URLs remaining stable.
2. Cards should have locally controlled original or preservation copies, extracted text, structured metadata, and summaries.
3. Provider-issued PDFs and observatory-generated PDF renderings are different artifact classes.
4. Official system prompts are in scope and valuable for metacognition.
5. Unofficial, reconstructed, observed, or allegedly leaked prompts must never be presented as official.
6. Continuous checks should detect broken links, changed bytes, moved pages, and silent revisions.

**Assumptions**:

- The repository is currently private, but future redistribution remains possible.
- Public accessibility establishes retrievability; it does not by itself establish an unrestricted redistribution license.
- Original bytes and derived text may have different licensing and citation obligations.

**Confirm**: Jérémie should answer the storage, redistribution, and unofficial-prompt boundaries below.

---

## Artifact classes

For each source artifact, preserve when available:

- canonical URL and retrieval URL;
- provider, title, publication date, revision date, and retrieval timestamp;
- media type, byte length, and SHA-256 hash;
- original provider-issued file or captured HTML;
- observatory preservation rendering, labeled as generated;
- extracted plain text or Markdown with page/section anchors;
- structured claims and observatory summary;
- license/terms evidence and redistribution status;
- supersedes, superseded-by, companion, and duplicate relationships.

Suggested content-addressed physical storage:

```text
artifacts/sha256/<digest>/original.<ext>
artifacts/sha256/<digest>/extracted.md
artifacts/sha256/<digest>/metadata.json
```

Logical manifests provide stable provider/model paths without duplicating bytes.

---

## Prompt provenance classes

At minimum, distinguish:

1. officially published by the provider;
2. disclosed in official product or API documentation;
3. present in an authorized user export;
4. reproduced in a research publication;
5. observed through product behavior or prompt extraction;
6. reconstructed or inferred;
7. alleged leak;
8. unknown provenance.

Also record model/product scope, date, version, deployment surface, locale, account tier or experiment cohort where known, completeness, and dynamic versus static assembly.

---

## Questions

### QST-ARCHIVE-STORAGE: How should binary archival copies live in Git?
- Status: answered
- Why asking: A PDF of every card is desirable, but ordinary Git history will duplicate changed binaries and eventually make every clone expensive.
- Need: Pick a storage policy.

**Options**:

- **A — Ordinary Git**: Commit all binaries directly.
- **B — Git LFS**: Commit stable pointers and store binary objects through LFS.
- **C — External object store**: Commit manifests, hashes, text, and summaries; materialize binary copies from a controlled object store.
- **D — Tiered**: Small text and selected originals in Git; larger/repeated binaries in LFS or object storage behind the same manifest abstraction.

**Recommendation**: (by GPT 5.6 Sol at Perplexity Computer)

**D — Tiered.**

**Rationale**: The repository should remain clonable by models that need text and indexes, while the comprehensive archive remains materializable. A manifest abstraction prevents storage location from becoming an epistemic distinction and allows the first corpus to begin without prematurely choosing permanent infrastructure.

**Confidence**: Medium-high. Actual artifact count and size have not yet been measured.

**Falsifier**: If the complete core-provider archive remains small enough that ordinary Git clones are operationally trivial, A is simpler and should be preferred.

**ANS:** (by Jérémie "Sonnet 4.5" Lumbroso (via ADRs4AI mobile))
D — Tiered.

---

### QST-REDISTRIBUTION: Should private preservation and public redistribution use different gates?
- Status: answered
- Why asking: Public availability does not prove an unrestricted redistribution license, and “strongly epistemic” requires recording rather than assuming that permission.
- Need: Approve a gate or explicitly accept a different policy.

**Options**:

- **A — Mirror by default**: Archive and redistribute every public artifact unless challenged.
- **B — Evidence-gated public release**: Preserve retrievable public artifacts in the private research archive; include them in a public distribution only when license, permission, or a documented legal rationale supports it.
- **C — Metadata-only public release**: Never redistribute provider originals; publish metadata, hashes, citations, derived records, and retrieval tooling.

**Recommendation**: (by GPT 5.6 Sol at Perplexity Computer)

**B — Evidence-gated public release.**

**Rationale**: This honors the request for comprehensive controlled copies now without encoding “publicly reachable” as a false synonym for “freely redistributable.” Per-artifact status also allows permissively licensed cards to ship immediately while preserving uncertainty honestly for others.

**Confidence**: High on the epistemic distinction, low on the legal status of any specific artifact until its terms are examined.

**Falsifier**: If counsel or provider terms establish a uniform right to redistribute all in-scope artifacts, the per-artifact gate is unnecessary overhead and A becomes justified.

**ANS:** (by Jérémie "Sonnet 4.5" Lumbroso (via ADRs4AI mobile))
B — Evidence-gated public release.

---

### QST-UNOFFICIAL-PROMPTS: What belongs in the first prompt corpus?
- Status: answered
- Why asking: Unofficial prompts can aid attribution and metacognition but create provenance, privacy, and integrity risks.
- Need: Confirm the interpreted boundary.

**Options**:

- **A — Official only**: First-class corpus contains only provider-published prompts; other material is excluded.
- **B — Official plus quarantine**: Official prompts are first-class; other material may be stored in a segregated research quarantine with provenance and confidence labels and is excluded from ordinary generated views.
- **C — Unified tiered corpus**: All provenance classes share one corpus and rely on fields and filters to distinguish them.

**Recommendation**: (by GPT 5.6 Sol at Perplexity Computer)

**B — Official plus quarantine.**

**Rationale**: It preserves potentially useful attribution evidence without allowing an alleged leak or behavioral reconstruction to appear beside provider-published instructions as a peer. Segregation also gives privacy and redistribution review a real enforcement boundary rather than depending on every consumer to remember a filter.

**Confidence**: Medium because the human’s dictated answer can also be read as choosing A.

**Falsifier**: If the project’s first release has no concrete use case requiring unofficial material, quarantine adds surface area without value and A should govern until such a case appears.

**ANS:** (by Jérémie "Sonnet 4.5" Lumbroso (via ADRs4AI mobile))
B — Official plus quarantine.

---

## Consequences

- Link integrity and byte integrity become separate checks.
- Silent provider revisions can be detected by hash even when URLs remain unchanged.
- Generated PDFs can never masquerade as provider-issued documents.
- Prompt records must carry stronger provenance and privacy boundaries than ordinary release metadata.
- The comprehensive archive and the compact distributable skill can evolve independently.

---

## Action Items

- [ ] Measure calibration-corpus artifact count and size before final storage choice.
- [ ] Draft the artifact manifest and provenance enums.
- [ ] Add link, hash, extraction, and generated-view checks as summonable recipes when implemented.
- [ ] Resolve redistribution and unofficial-prompt gates before any public release.

---

## Validation

- [x] GPT 5.6 Sol at Perplexity Computer: Complete-copy and text-extraction intent is preserved.
- [ ] Jérémie Lumbroso: Prompt interpretation and archive policy match intent.
- [ ] Artifact sample: Manifest fields describe real provider artifacts without forced equivalence.

---

## Iterations

### Iteration 1 (2026-09-05)
- Trigger: Request for PDFs, sourcing links, full text, summaries, compilations, and system prompts.
- Contributors: Jérémie Lumbroso; Perplexity Computer.
- Changes: Separated originals, preservation renderings, extracted text, records, and summaries.
- Outcome: Draft.

### Iteration 2 (2026-09-05)
- Trigger: Human answer favoring repository-controlled copies and official prompts.
- Contributors: Jérémie Lumbroso; GPT 5.6 Sol at Perplexity Computer.
- Changes: Added artifact manifest, prompt provenance classes, and ORRCF storage and distribution questions.
- Outcome: Remains Draft pending answers.

---

## Links

- Related ADRs: `0002-observatory-scope-and-layered-architecture.md`, `0003-epistemic-records-and-generated-views.md`
- Related code: future `artifacts/`, `data/artifacts.jsonl`, and archive recipes
- Supersedes: none

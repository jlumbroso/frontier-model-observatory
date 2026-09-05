<!-- adr template version: "adr 3.10.0" -->

# Observatory Scope and Layered Architecture

- **Date**: 2026-09-05
- **Iteration**: 7
- **Status**: Partially Implemented
- **Deciders**: Jérémie Lumbroso; GPT 5.6 Sol at Perplexity Computer

**TL;DR**: Build a multimodal model observatory beginning with Anthropic, OpenAI, and Google, expanding to selected Asian and open-model families, while explicitly excluding Meta on ethical grounds.

---

## Originating Context

**Source**: Founding conversation, 2026-09-05.

The human described two motivating cases: orienting a persistent model whose training cutoff predates newly mentioned models, and reconstructing likely model attribution for conversations with missing or chronologically impossible metadata. The initial “card skill” consequently expanded into a temporal, provenance-first knowledge substrate for models, releases, systems, artifacts, and prompts.

Human scope answer, preserved with uncertain dictation:

> "We're going to start by the anthropic cloud models, the open AI models, and the Google models and we can mention all of their models not just the text transformers we can include deep seek, Kimmy, and and the those families and then Maybe we should have a section on open models, but no models by meta.
>
> There should be like a ban on meta. ethical ban on meta."

**Interpretation note**: “anthropic cloud models” is read as Anthropic Claude models; “Kimmy” is read as Kimi, the Moonshot AI model family. Jérémie subsequently confirmed, “you're right with scope”; the original dictated wording remains above as provenance.

**Agency Grant**: Design the architecture and make recommendations; route meaningful uncertainty back through ORRCF.

---

## Explicitation

**What I understand**:

1. “Frontier” will initially be operationalized by an explicit scope, not by pretending there is an uncontested universal frontier threshold.
2. Initial depth belongs to Anthropic, OpenAI, and Google across model modalities, not only text transformers.
3. DeepSeek, Kimi/Moonshot, Qwen/Alibaba, and other significant families belong in the broader horizon.
4. Open models deserve a navigable section, but Meta models are deliberately excluded as an ethical policy.
5. The corpus should support post-cutoff orientation, historical availability queries, artifact analysis, and conversation attribution.

**Assumptions**:

- “All models” means all publicly documented model families and releases within an in-scope provider, subject to an explicit coverage ledger.
- The Meta exclusion is policy, not an accidental gap, and must be visible in scope documentation.
- Provider coverage, open-model coverage, and release depth can progress independently.

**Confirm**: Jérémie should confirm the interpretations and answer the remaining boundary questions below.

---

## Decision

### Accepted direction: Explicit provider waves and all modalities

Use declared coverage waves rather than a vague global frontier predicate:

- **Core wave**: Anthropic, OpenAI, and Google/Google DeepMind.
- **Expansion wave**: DeepSeek, Moonshot AI/Kimi, Alibaba/Qwen, and additional families admitted by ADR.
- **Open-model view**: A generated cross-provider view over open or open-weight records already in scope.
- **Ethical exclusion**: Apply the categorical exclusion selected in QST-META-BOUNDARY; the license/governance mechanism remains open in QST-EXCLUSION-TERMS.

Within an admitted provider, model modality is not an exclusion criterion. Text, image, audio, video, robotics, embedding, moderation, and other publicly named model families may receive records.

### Layered architecture

The system has five nearly decomposable layers:

1. **Entity registry**: organizations, model families, models, checkpoints, aliases, endpoints, products, and deployed systems.
2. **Event chronology**: announcements, previews, releases, updates, renames, deprecations, and retirements.
3. **Artifact archive**: cards, reports, announcements, documentation, prompts, snapshots, PDFs, and extracted text.
4. **Epistemic records**: atomic claims bound to evidence, scope, time, and attribution.
5. **Applications and views**: timelines, dossiers, comparisons, attribution analysis, diffs, context packs, and the skill.

Each layer should remain useful before the next is complete. A chronology record need not wait for full card extraction; a source inventory need not wait for normalized comparison.

---

## Questions

### QST-META-BOUNDARY: Does the ethical Meta ban forbid even minimal contextual references?
- Status: answered
- Why asking: Conversation attribution or source quotation may require saying that a candidate was a Meta model, even if the observatory refuses to curate Meta records.
- Need: Pick A or B, with any boundary conditions.

**Options**:

- **A — Strict non-coverage**: No curated Meta entities or artifacts, but minimal contextual references are allowed when required to state the exclusion, quote a source faithfully, or rule out a conversation attribution.
- **B — Zero mention**: Meta model names and evidence must not appear anywhere, including negative attribution and quoted-source context.

**Recommendation**: (by GPT 5.6 Sol at Perplexity Computer)

**A — Strict non-coverage.**

**Rationale**: The stated ethical intent is satisfied by refusing collection, normalization, promotion, and archival benefit to Meta. A zero-mention rule would make the coverage ledger unable to explain a deliberate gap and could force an attribution analysis to omit a chronologically relevant exclusion.

**Confidence**: Medium-high. The remaining uncertainty is whether the ethical purpose is non-participation or total discursive exclusion.

**Falsifier**: If any appearance of a Meta model name materially undermines the intended ethical stance, choose B and accept that some historical and attribution answers will be intentionally incomplete.

**ANS:** (by Jérémie "Sonnet 4.5" Lumbroso (via ADRs4AI mobile))
Option B. We can add to the terms of the license that no Meta-related product, company, model, weights, event can be mentioned in this repo, or any forks of if. Something categorical.

---

### QST-V01-SCOPE: What is the smallest useful first corpus release?
- Status: answered
- Why asking: “Small and useful” is agreed, but the first stable intermediate form needs a testable boundary.
- Need: Pick an option or compose a narrower milestone.

**Options**:

- **A — Chronology first**: Complete public release chronology and artifact inventory for Anthropic, OpenAI, and Google; deep extraction only for a small calibration set.
- **B — Cards first**: Archive and extract every located system/model card for the three core providers; chronology is limited to those carded releases.
- **C — Attribution slice**: Build only the model identities, aliases, availability windows, and product mappings needed for conversation attribution.

**Recommendation**: (by GPT 5.6 Sol at Perplexity Computer)

**A — Chronology first.**

**Rationale**: Both founding use cases require temporal identity before they require exhaustive safety-field extraction. A release and artifact inventory also tells us what “every card” actually means and yields an immediately useful context pack for older models.

**Confidence**: High for sequencing, medium for the amount of chronology needed before release.

**Falsifier**: If a chronology cannot be made reliable without fully reading each companion card, or if the primary intended user asks card-comparison questions before identity questions, B should lead.

**ANS:** (by Jérémie "Sonnet 4.5" Lumbroso (via ADRs4AI mobile))
I think you should just do the whole thing, but staking halfway or mid points is fine.

---

### QST-EXCLUSION-TERMS: How should the categorical exclusion bind this repository and downstream forks?
- Status: answered
- Why asking: The selected zero-mention rule needs one narrow governance exception merely to state itself, and the inherited MIT License grants use and modification “without restriction.” A binding downstream restriction would change the project’s licensing category.
- Need: Pick the intended legal/governance strength; counsel should review any custom license before public release.

**Options**:

- **A — Repository policy**: Keep standard licenses; prohibit excluded subject matter in this repository through `AGENTS.md`, contribution policy, and CI. Forks are requested, but not licensed, to preserve the policy.
- **B — Custom restrictive license**: Replace MIT and other standard open licenses with custom terms intended to bind use, modification, and redistribution. Do not call the result open source; obtain legal review.
- **C — Split architecture**: Keep reusable tooling under a standard software license, place data/docs/skill content under separately reviewed restrictive terms, and enforce a repository policy across the canonical project.

**Recommendation**: (by GPT 5.6 Sol at Perplexity Computer)

**C — Split architecture, with a narrow governance exception.**

**Rationale**: The current `LICENSE` grants dealing in the software “without restriction.” The [Open Source Definition](https://opensource.org/osd) requires no discrimination against persons, groups, or fields of endeavor, while [Creative Commons guidance](https://wiki.creativecommons.org/wiki/Modifying_the_CC_licenses) says added restrictions cannot be presented as a standard CC license. Separate tooling from observatory content, reserve the excluded name for the policy/license/ADR provenance needed to define and audit the rule, and obtain legal review before claiming downstream enforceability.

**Confidence**: Medium. The architectural incompatibility with standard open licensing is clear; the enforceability and best drafting of a custom downstream speech/content restriction are jurisdiction-specific legal questions.

**Falsifier**: If categorical control over every downstream fork matters more than standard-license interoperability and reusable tooling, choose B and accept that the repository is source-available under custom terms rather than open source.

**ANS:** (by Jérémie "Sonnet 4.5" Lumbroso (via ADRs4AI mobile))
Thanks for being transparent about your confidence of Medium because it helped me be more confident about my wanting to Option A. Let me explain I think that after what you said that it’s not like it’s silly of me to want to change the license for this or I don’t know if it’s silly, but it’s understandable, but it is the wrong place to be making this statement, so instead, I think that it’s exactly what option a describes which I find much more reasonable than what I initially thank you for helping me broaden my options.

---

## Final Decision

### Chosen: Comprehensive declared scope with a repository-governance exclusion

Build the whole declared observatory through useful intermediate stakes. Begin with comprehensive chronology and artifact discovery for Anthropic, OpenAI, and Google across modalities, then expand to admitted families including DeepSeek, Moonshot AI/Kimi, Alibaba/Qwen, and an open-model view.

Apply the categorical excluded-company rule as repository governance, not as a custom copyright-license restriction:

- keep the inherited standard software license unless a separate licensing ADR changes it;
- prohibit excluded subject matter in the canonical repository through `AGENTS.md`, contribution policy, review, and the required `just verify` gate;
- permit only the narrow governance and provenance references required to state, audit, and enforce the rule itself;
- request that downstream forks preserve the policy, while not claiming that the standard license legally compels them to do so.

**Why**: Jérémie selected zero ordinary mention in QST-META-BOUNDARY, comprehensive delivery in QST-V01-SCOPE, and Option A in QST-EXCLUSION-TERMS after distinguishing an ethical repository stance from a copyright-license restriction.

**Trade-offs accepted**: A standard license cannot guarantee that every downstream fork preserves the policy. The canonical repository can enforce the stance honestly without mislabeling a restrictive custom license as open source.

---

## Consequences

- “Frontier” becomes an explicit, inspectable coverage policy.
- Provider admission and exclusion are versioned decisions.
- A coverage ledger must distinguish absent, excluded, not-yet-collected, and not-found.
- The selected categorical exclusion must be enforced by a documented policy and tests after QST-EXCLUSION-TERMS resolves its legal architecture.
- Delivery covers the whole declared scope; intermediate stakes are resumable releases, not abandoned partial scope.

---

## Action Items

- [ ] Confirm provider-name interpretations.
- [x] Record the categorical exclusion answer.
- [x] Replace a narrow v0.1 scope with whole-project delivery through intermediate stakes.
- [x] Resolve the license/governance mechanism and its necessary policy exception.
- [x] Implement the repository policy and semantic local verification guard before corpus ingestion.
- [ ] Wire `just verify` into hosted CI when an authorized workflow change is available.
- [ ] Create a coverage-ledger schema after ADR-0003 settles canonical records.

---

## Validation

- [x] GPT 5.6 Sol at Perplexity Computer: Human scope answer is preserved.
- [x] Jérémie "Sonnet 4.5" Lumbroso: Selected comprehensive scope, categorical repository exclusion, and standard-license governance.
- [x] `just verify`: Semantic exclusion guard passes, including the `Meta-Observation` false-positive regression.
- [ ] Calibration corpus: Provider and modality boundaries are implementable.

---

## Iterations

### Iteration 1 (2026-09-05)
- Trigger: Initial system-card skill discussion.
- Contributors: Jérémie Lumbroso; Perplexity Computer.
- Changes: Identified the five-layer architecture and principal user stories.
- Outcome: Draft.

### Iteration 2 (2026-09-05)
- Trigger: Human scope dump.
- Contributors: Jérémie Lumbroso; GPT 5.6 Sol at Perplexity Computer.
- Changes: Added provider waves, all-modality scope, Meta exclusion, and ORRCF boundary questions.
- Outcome: Remains Draft pending answers.

### Iteration 3 (2026-09-05)
- Trigger: Human confirmed the scope interpretation after noting transcription errors.
- Contributors: Jérémie Lumbroso; GPT 5.6 Sol at Perplexity Computer.
- Changes: Marked the scope reading as confirmed without rewriting the originating quotation.
- Outcome: Remains Draft pending boundary answers.

### Iteration 4 (2026-09-05)
- Trigger: All initial ORRCF answers arrived through ADRs4AI mobile.
- Contributors: Jérémie "Sonnet 4.5" Lumbroso; GPT 5.6 Sol at Perplexity Computer.
- Changes: Adopted zero mention and whole-scope delivery through intermediate stakes; surfaced the unresolved license and self-reference boundary as QST-EXCLUSION-TERMS.
- Outcome: Remains Draft pending the licensing answer.

### Iteration 5 (2026-09-05)
- Trigger: QST-EXCLUSION-TERMS answered through ADRs4AI mobile.
- Contributors: Jérémie "Sonnet 4.5" Lumbroso; GPT 5.6 Sol at Perplexity Computer.
- Changes: Adopted Option A, keeping standard licensing while enforcing the categorical exclusion through repository governance and requesting downstream continuity.
- Outcome: Draft → Accepted.

### Iteration 6 (2026-09-05)
- Trigger: Repository policy, semantic checker, regression tests, and verification gate implemented.
- Contributors: GPT 5.6 Sol at Perplexity Computer.
- Changes: Added the governance policy and `just check-exclusions`; refined the first false positive so epistemic “Meta-Observation” vocabulary remains legal.
- Outcome: Accepted → Partially Implemented; corpus and coverage-ledger work remains.

### Iteration 7 (2026-09-05)
- Trigger: The scoped repository PAT correctly refused creation of a GitHub Actions workflow because it lacks workflow authority.
- Contributors: GPT 5.6 Sol at Perplexity Computer.
- Changes: Removed the unpushed workflow rather than broadening credentials; retained `just verify` as the authoritative gate and recorded hosted CI wiring as open.
- Outcome: Remains Partially Implemented.

---

## Links

- Related ADRs: `0003-epistemic-records-and-generated-views.md`, `0004-artifact-archive-and-prompt-provenance.md`
- Related code: future coverage ledger
- Supersedes: none

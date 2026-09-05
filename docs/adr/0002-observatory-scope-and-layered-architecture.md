<!-- adr template version: "adr 3.10.0" -->

# Observatory Scope and Layered Architecture

- **Date**: 2026-09-05
- **Iteration**: 3
- **Status**: Draft
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
- **Ethical exclusion**: Do not curate Meta models or archive Meta model artifacts.

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
- Status: unanswered — routing to Jérémie
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

**ANS:** (by Jérémie Lumbroso)
[Fill this in]   <!-- literal placeholder — parser-significant, do not paraphrase -->

---

### QST-V01-SCOPE: What is the smallest useful first corpus release?
- Status: unanswered — routing to Jérémie
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

**ANS:** (by Jérémie Lumbroso)
[Fill this in]   <!-- literal placeholder — parser-significant, do not paraphrase -->

---

## Consequences

- “Frontier” becomes an explicit, inspectable coverage policy.
- Provider admission and exclusion are versioned decisions.
- A coverage ledger must distinguish absent, excluded, not-yet-collected, and not-found.
- Meta references, if allowed by QST-META-BOUNDARY, never imply in-scope curation.

---

## Action Items

- [ ] Confirm provider-name interpretations.
- [ ] Record the Meta boundary answer.
- [ ] Select the v0.1 stable intermediate form.
- [ ] Create a coverage-ledger schema after ADR-0003 settles canonical records.

---

## Validation

- [x] GPT 5.6 Sol at Perplexity Computer: Human scope answer is preserved.
- [ ] Jérémie Lumbroso: Scope and exclusion policy match intent.
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

---

## Links

- Related ADRs: `0003-epistemic-records-and-generated-views.md`, `0004-artifact-archive-and-prompt-provenance.md`
- Related code: future coverage ledger
- Supersedes: none

<!-- adr template version: "adr 3.10.0" -->

# Portable Agent Instructions

- **Date**: 2026-09-05
- **Iteration**: 1
- **Status**: Accepted
- **Deciders**: Jérémie Lumbroso; Perplexity Computer

**TL;DR**: Use `AGENTS.md` as the canonical, model-agnostic project instruction surface and retain tool-specific directories only for genuinely tool-specific integration.

---

## Originating Context

**Source**: Human instruction in the founding conversation, 2026-09-05.

> "You must make sure to tweak the CLAUDE.md (move it and all of them to AGENTS.md or whatever the right name is) to contain this project description and draft ADRs for what we've already decided."

**Agency Grant**: Adapt the inherited template while preserving its load-bearing collaboration directives.

---

## Explicitation

**What I understand**:

1. The repository is intended for collaboration across current and future models, not only Claude.
2. The project-wide instruction filename must not imply that one provider or harness owns the collaboration protocol.
3. Tool-specific assets may remain tool-specific when their location is part of that tool's interface.

**Assumptions**:

- `AGENTS.md` is the canonical portable instruction filename for this repository.
- Existing nested `AGENTS.md` files remain valid scoped instruction surfaces.
- `.claude/` may remain for Claude-specific settings and skill discovery; it must not be the only home of project truth.

**Confirm**: The human instruction is direct enough to accept this decision without another blocking question.

---

## Decision

### Chosen: Canonical `AGENTS.md` with explicit adapters only when demonstrated necessary

Rename the root `CLAUDE.md` to `AGENTS.md` and update repository references, hooks, manifests, and onboarding material accordingly. Do not keep a duplicate full-text `CLAUDE.md`; duplicated living instructions would drift.

Keep `.claude/` files whose paths are interfaces to Claude tooling. If a future harness demonstrably requires a provider-specific root instruction file, add a minimal generated or pointer adapter and record that compatibility decision in a new ADR.

**Why**: The observatory exists partly to make model identity and model change explicit. A provider-neutral canonical instruction surface is congruent with that purpose, while a duplicated compatibility file would introduce two competing sources of truth.

**Trade-offs accepted**: A tool that reads only `CLAUDE.md` may initially miss the canonical instructions. We prefer a visible compatibility failure and a narrow adapter over permanent silent duplication.

### Consequences

- Project guidance becomes model-agnostic at the root.
- References to the former filename must move atomically.
- Tool-specific integration remains near-decomposable from project-wide doctrine.

---

## Open Follow-ups

- [ ] Verify each intended harness discovers `AGENTS.md`; add only evidence-driven adapters.
- [ ] Keep template-update tooling aware that the inherited `CLAUDE.md` was deliberately renamed locally.

---

## Action Items

- [ ] Rename and specialize the root instruction file.
- [ ] Update all semantic references, the substrate hook, the crew read order, and the Kintsugi manifest.
- [ ] Verify that no canonical-guidance reference still points to `CLAUDE.md`.

---

## Validation

- [x] Perplexity Computer: Decision captured matches the human's explicit instruction.
- [x] Perplexity Computer: Prime and Secondary Directives remain load-bearing.
- [ ] Jérémie Lumbroso: Resulting instruction surface matches intent.

**Notes**: `just adr` could not be used because `just` is not installed in the execution environment. The ADR was manually minted as `0001`, after confirming that the repository contained no prior numbered ADR.

---

## Iterations

### Iteration 1 (2026-09-05)
- Trigger: Founding repository instruction.
- Contributors: Jérémie Lumbroso; Perplexity Computer.
- Changes: Recorded the portable instruction decision before modifying the inherited substrate.
- Outcome: Accepted.

---

## Links

- Related ADRs: none
- Related code: `AGENTS.md`, `kintsugi.yaml`, `scripts/hooks/remind-uncommitted-substrate.py`
- Supersedes: inherited root `CLAUDE.md` convention

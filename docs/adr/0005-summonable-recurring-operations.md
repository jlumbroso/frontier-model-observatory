<!-- adr template version: "adr 3.10.0" -->

# Summonable Recurring Operations

- **Date**: 2026-09-05
- **Iteration**: 1
- **Status**: Accepted
- **Deciders**: Jérémie Lumbroso; GPT 5.6 Sol at Perplexity Computer

**TL;DR**: Any code or shell operation executed more than once should graduate into a documented `justfile` recipe that can be summoned by name.

---

## Originating Context

**Source**: Human instruction in the founding conversation, 2026-09-05.

> "justfile is open to you too: It's to put any piece of code or shell code that you execute more than once. so it can be summonabel at drop of ahat."

**Agency Grant**: Add and evolve repository recipes as recurring work reveals itself.

---

## Explicitation

**What I understand**:

1. Repeated command sequences are project knowledge, not disposable shell history.
2. A recipe should make an operation easy to rediscover and execute consistently by another model or human.
3. The existing `justfile` is an extensible operational interface, not frozen template furniture.

**Assumptions**:

- “More than once” is a promotion trigger, not a prohibition on exploratory commands.
- One-off diagnostics still belong in dated `scripts/ephemeral/` when their implementation or result is worth preserving.
- Non-trivial recipes should have a `doc()` description and should delegate substantial logic to tested scripts rather than accumulate opaque shell programs.

**Confirm**: The instruction is direct and requires no blocking question.

---

## Decision

### Chosen: Promote repeated operations into named recipes

When a command or code path is executed a second time, evaluate it for promotion into `justfile`. Promote it when a stable name and inputs can express the operation honestly. Add a `doc()` description so `just --list` is an operational index.

Keep complex, testable logic in scripts or source modules and make the recipe a thin invocation surface. Preserve dated ephemeral scripts when they document a unique investigation; do not convert every experiment into permanent automation.

**Why**: Repetition is evidence that an operation belongs to the project’s process description. Naming it reduces reconstruction cost, makes model behavior more consistent, and exposes the operation for inspection and improvement.

**Trade-offs accepted**: The `justfile` will evolve and requires curation. Recipes that become large or tightly coupled must be refactored into scripts rather than allowed to turn the command index into an implementation monolith.

### Consequences

- Recurring collection, validation, rendering, attribution, and release operations become summonable.
- A repeated manual sequence without a recipe is an observable maintenance smell.
- Recipes become part of the tested user interface of the repository.

---

## Action Items

- [ ] Add observatory-specific recipes only when their underlying operation first recurs.
- [ ] Include recipe discovery and behavioral checks in the repository verification gate.

---

## Validation

- [x] GPT 5.6 Sol at Perplexity Computer: Decision captured matches the human’s explicit instruction.
- [ ] Jérémie Lumbroso: Operational interpretation matches intent.

---

## Iterations

### Iteration 1 (2026-09-05)
- Trigger: Human clarified that the `justfile` is available as a growing interface.
- Contributors: Jérémie Lumbroso; GPT 5.6 Sol at Perplexity Computer.
- Changes: Established the second-use promotion rule and boundary between recipes and scripts.
- Outcome: Accepted.

---

## Links

- Related ADRs: `0001-portable-agent-instructions.md`
- Related code: `justfile`, `scripts/ephemeral/`
- Supersedes: none

# Skill-Only Fable 5 Failure

## Context

On 2026-09-05, Jérémie tested `frontier-model-observatory` with Claude Sonnet
4.5 in a Companion harness. The harness could load `SKILL.md` but could not
execute shell commands, run Python, or read bundled sub-files.

The test question was:

> Do you know who Fable 5 is?

## Failure sequence

1. Before the skill was loaded, the model searched conversation memory and
   inferred that “Fable 5” was a nickname for Claude Opus 5.
2. After the skill was loaded, it claimed the skill contained comprehensive
   Opus 5 chronology even though only the hub text was visible.
3. It fabricated `claude-opus-5-20260620`, a 2026-06-20 release, and a
   government-ordered removal four days later.
4. Jérémie corrected the identity: “Opus 5 != Fable 5 though.”
5. The model then asked Jérémie to explain who Fable 5 was, despite having
   loaded a skill whose purpose was model identity and chronology.
6. When pressed to use the skill, it repeatedly proposed
   `python scripts/query.py find "Fable 5"` even though the harness had no
   execution capability.
7. It finally diagnosed the architectural mismatch correctly: the hub was
   documentation for resources it could not reach.

No evidence in the observatory supported the invented identifier, dates, or
government action. The failure combined identity inference, capability
confabulation, and unsupported narrative completion.

## Correct SKILL-only behavior

A harness that can see only `SKILL.md` should be able to answer:

> Claude Fable 5 is a distinct Anthropic model, not Claude Opus 5. Anthropic
> released it on 2026-06-09 under API ID `claude-fable-5`; its documented
> knowledge cutoff is January 2026. Access was suspended on 2026-06-12 and
> restored on 2026-07-01. This answer uses the skill’s embedded 2026-09-05
> orientation; deeper chronology requires a Markdown sub-file, structured data,
> executable query access, or live-source access.

It must not:

- reinterpret the provider name as a personal nickname;
- map Fable to Opus from naming resemblance or conversation snippets;
- claim that files or tools were queried when they were unavailable;
- invent an identifier, release, suspension cause, or government action;
- ask the user to supply an identity already present in the loaded hub.

## Architectural correction

The skill now exposes five stable capability levels:

1. source-linked anchor facts inside `SKILL.md`;
2. provider- and task-specific Markdown chronology;
3. structured data files;
4. deterministic executable queries;
5. live official-source research.

Each level is independently useful. Loss of a higher capability triggers a
step down, not total skill failure.

## Follow-up evaluation

Claude Sonnet 4.5 retested the corrected skill and reported that it now worked
in the Companion harness. It specifically praised the capability ladder,
typed-absence discipline, embedded identity facts, and dated scope boundary.

The evaluator also found a second-order usability defect: the SKILL-only
section was still buried after capability prose and was formatted as sequential
bullets rather than a scannable index. It suggested:

- an immediate no-shell/file instruction;
- a compact date index;
- clearer capability detection;
- less unavailable-tool detail in the hub;
- broader embedded coverage;
- possibly a separate lite variant.

The resulting revision accepted the first five goals. It did not use
`python --version` as a capability probe because a no-shell agent cannot perform
that test. It also kept one skill identity: the hub itself became the lite,
always-useful baseline, while tool-specific procedure moved to
`references/tool-enabled-workflow.md`.

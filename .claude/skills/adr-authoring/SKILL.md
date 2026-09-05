---
name: adr-authoring
description: Use BEFORE writing or editing any ADR, seed, or QST/ANS block in docs/adr/ — the template's minimal shape, the QST grammar and handles, the catch-the-author Recommendation form, and the four real-world malformations that break parsing. This skill IS the read-the-template step; skipping it re-creates the failure it exists to fix.
---

<!-- skill version: "adr-authoring 3.10.0" — co-versioned with human-ai-collaboration-template-A; assembled from Rubricator 5's corpus-adherence syllabus -->

# Writing parseable ADRs, seeds, and questions

**ADR expands to *Architectural Deliberation Record*** — the family name for the deliberative substrate (ADRs, seeds, debriefs), in homage to Herbert Simon: the records are structural members of the falsifiability machine, harnessing the *architecture* of complexity. (Ratified 2026-08-13; the older *Architecture Decision Record* reading stays a welcome ancestor — see `adr-madr.md`'s homage line.)

## 1. Why the form matters (one paragraph, not a treatise)

Across ~1,100 real specimens, 76% of documents that clearly *attempt* this methodology's template still skip its one mandatory field (`TL;DR`), and 88% of documents that don't follow the template at all were written in repos where the template file was sitting right there, often edited the same session. The template being *referenced* does not make it *read*. This skill exists to be the thing that actually gets read — it loads into context automatically, not because someone remembered to open a file. If you are about to write an ADR, a seed, or a QST block: this skill *is* the read-the-template step.

## What asking a human costs (read this before writing any QST, Recommendation, or tour)

Human attention is **scheduled, not just spent**: an open question, a recommendation round, or a tour announcement causes the human to *plan* a focus slot, turn every context dial to the right place — and a malformed or unready ask converts that prepared depth into logistics. In the founder's own words, when a broken batched ask met a scheduled deep-focus slot: *"it makes it scream. It psych'ed itself up… and it is being left with nothing to do."* A silent failure is worse — *"the human is the only one witnessing the problem… it's like being gaslit by the software."* So the machinery below is not formatting: the Recommendation form exists so answering degrades to accept/override; status tokens exist so whose-ball-it-is never needs re-deriving; and the readiness bar for anything that schedules human attention is **walked-yourself-first** — a green parse is not readiness, and never let an unready ask *render* as ready. Tours are the extreme case; the tours field guide is their authority.

## 2. The minimal shape — what every ADR needs, no exceptions

```
- **Date**: YYYY-MM-DD  |  **Iteration**: N  |  **Status**: Draft|Accepted|Partially Implemented|Implemented|Superseded  |  **Deciders**: names

**TL;DR**: one line. Mandatory — if you can't write it in one line, the ADR isn't done.

## Questions
### QST: <question, or QST-<id>: for a citable handle>
- Status: unanswered   <!-- open family: unanswered (human's ball) | unresolved (model's ball) | deferred; closing family + annotations: references/questions-reference.md -->
- Why asking: ...
- Need: yes/no | explanation | code example

**Recommendation**: (by <model-name>)
**<Letter> — <short pick>.** Because <evidence named specifically enough to check — a file, an ADR, a measurement>. If wrong: <what breaks, by name>.

**ANS:** (by <name>, <date optional>)
[Fill this in]   <!-- literal placeholder — parser-significant, do not paraphrase -->
```

The document `Status:` enum above is the **frozen five** (case-insensitive read, canonical-case write) — annotations decorate *question*-level status only, never the document line. The ANS byline needs the `by`/`from` keyword — `**ANS:** (Jérémie)` is answer *content*, not an attribution; a pending note goes on the Status line (`- Status: unanswered — routing to <name>`) or in a `[Pending: …]` bracket, never as bare prose in the ANS slot: **the ANS text IS the answer**, and every tool leans on that contract.

That trailing comment on `[Fill this in]` is real, current template text (v3.9.0) — tooling checks for the literal placeholder to detect unanswered blocks; "helpfully" rewording it as filler prose breaks that check silently. Leave it exactly as-is until there's a real answer to put there.

That block — frontmatter, one QST, one catch-the-author Recommendation — is the load-bearing 80%. Everything else (Explicitation, Supporting Materials, Validation, Iterations, Glossary) matters and lives in the depth reference; this is what must never be skipped. Mint new ADRs with `just adr "<title>"` — never hand-number.

## 3. The four things the wild actually gets wrong (never this / always this)

Every pair below is a real, uncorrected specimen from this ecosystem's own corpus — not a hypothetical.

**Never** — a bolded pseudo-heading (parses as prose to every tool):
> `**QST-1 (Recommendation protocol — "YES TO ALL THREE").**`
**Always**:
> `### QST-1: Recommendation protocol — accept all three?`
*(33 real instances — the single largest malformation class.)*

**Never** — a number where the grammar wants a hyphen:
> `### QST 1: Delivery ledger — where does it live?`
**Always**:
> `### QST-1: Delivery ledger — where does it live?`
*(24 instances — the second-largest class; written the way you'd say it aloud, not the way the grammar parses.)*

**Never** — a `Status: unanswered` line with no QST heading above it (the answer surface lies in *both* directions: looks open when nothing's asking, or the real question is invisible):
> a bare `- Status: unanswered` floating under prose
**Always**: every `- Status:` line sits directly under a `### QST:` heading, no exceptions.
*(14 instances.)*

**Never** — wrong heading depth (`##` or `####`; parsers scan `###` only):
> `## QST-1 (ANSWERED 2026-07-03): official mechanism exists`
**Always**: `### QST-1: ...` — exactly three hashes, always.
*(4 instances.)*

## 4. The handle grammar, in one line (plus the fragility worth knowing)

`### QST:` is always valid. `### QST-<id>:` adds a citable handle when anything will refer back to the question — `id` is 1–24 letters/digits with interior hyphens (`QST-STATUS-AUTHORITY` is valid; `QST_2` and `QST-` are not). Once a handle is cited anywhere, it never changes — reword the question freely, the id is the anchor. A plain `### QST:` heading still gets an *auto-derived* handle slugified from its text — fragile: retitling silently changes it and breaks existing references; prefer an explicit id (or an `<!-- @adr-anchor: qst-... -->` comment placed *after* the heading) for anything tour- or citation-bound.

## 5. Load the references when

Read `references/depth.md` (same skill directory) when: writing a **seed** instead of an ADR; questions don't fit one QST block cleanly (**batched / embedded shapes**); choosing between **`adr.md` / `adr-madr.md` / `seed.md`**; or touching **Validation, Iterations, Action Items**. Read `references/questions-reference.md` when: **closing a question** (the four closing tokens and the three-agents rule live there); writing **status annotations**; attributing or **deferring an answer**; using **anchor comments or the `@adr-*` reserved channel**. Read `references/freshening.md` when asked to **comb, sweep, audit, or freshen existing ADRs** — status-vs-reality, iterations debt, remainder inventories, recommendation updates, and new questions for unbuilt problems all have a protocol; do not improvise one. For QuestionTours (referencing questions from tour files), the tours field guide is the authority — not this skill.

---

*Curriculum: Rubricator 5 (Claude Sonnet 5), from corpus-adherence findings over ~1,100 specimens + the qst-lint census (75 findings, 21 files). Assembly: Shipwright 5 (Claude Fable 5), v3.9.0 pre-launch sprint. Placeholder convention: Sextant 5's catch. Bounds ("crisp; field guide, not treatise"): Jérémie Lumbroso.*

<!-- adr template version: "adr 3.10.0" -->

# [ADR Title - Decision/Topic]

- **Date**: [YYYY-MM-DD]
- **Iteration**: [N]
- **Status**: [Draft | Accepted | Partially Implemented | Implemented | Superseded]   <!-- the frozen five (v1 core, ratified 2026-08-12): case-insensitive read, canonical-case write; strict enum at document level — no annotations here -->
- **Deciders**: [Names / roles of contributors]

**TL;DR**: [One-line summary of the decision, written by the author at point of decision. May go stale as the ADR iterates; treat as the author's intent at write-time, not the canonical current rendering. Mandatory field — if you cannot write this in one line, the ADR is not done yet.]

---

## Quick Reference

**Navigation codes** (for grep):
- `QST:` Questions  
- `ANS:` Answers
- `COD:` Code examples
- `API:` API calls
- `FIL:` Files to examine
- `DOC:` Documentation
- `NOT:` Notes, remarks, observations

**Find things**:
```bash
grep -E '^### QST(-[A-Za-z0-9-]{1,24})?:' file.md   # All questions, both canonical forms — a bare-QST grep silently misses every handled question
grep 'Status: unanswered' file.md                   # Awaiting the human (by design, this misses unresolved/deferred — those are not the human's ball)
grep '^### COD:' file.md                             # Code examples
```

---

## Originating Context

**Source**: [Type and link to where this ADR originated, e.g.:
- `Human dump (below)` — stream-of-consciousness from a contributor
- `Brief: <path/to/brief.md>` — a brief from another contributor (see also: [INBOX-PROTOCOL.md](../../../INBOX-PROTOCOL.md) if your project uses the inbox-based coordination protocol)
- `Seed: <path/to/seed.md>` — a seed that was chunked into multiple ADRs
- `Prior ADR open question: <ADR-xxxx#QST-N>` — a follow-up
- `Code review / observation / external discussion / etc.`

Multiple sources may be listed.]

[If the source is a human dump, drop the stream-of-consciousness here — no structure needed, just everything that's on your mind about this decision]

[If the source is a brief, seed, or other reference, you may summarize the originating constraints here in a paragraph, OR rely on the link above.]

**Agency Grant**: [Optional: What freedom does the author have? "Implement as you see fit" / "Explore options" / "Just structure my thoughts"]

---

## Explicitation

*Making explicit what the Originating Context implied or contained tacitly. The author reflects back what they understand the problem to be, so misalignment surfaces here, not later.*

**What I understand**:

1. [Thread/topic 1] — [why it matters]
2. [Thread/topic 2] — [why it matters]

**Assumptions**:

- [Assumption 1]
- [Assumption 2]

**Confirm**: [Who is the author asking to confirm? Could be the originator (if a brief or dump), another contributor, or a self-check before moving on.]

---

## Questions

**Use the `QST:` / `ANS:` codes for open questions.** They're required for grep-ability and for any tooling (e.g., the ADRs4AI extension) that parses ADRs as structured documents. Open questions outside this format are invisible to those tools.

**Protocol** (added 2026-04-22 by Opus 4.7): every QST block must include a `**Recommendation**: (by [model-name])` section between the options and the `**ANS:**` block. The human should not have to extract the AI's lean from prose — put it under its own heading with a clear pick and a short justification grounded in evidence (data, prior ADRs, constraints). Lead the recommendation with a bold pick (`**B — short name.**`) so a skim reveals the AI's position without reading. If walking back an earlier lean during iteration, say so explicitly.

**Catch-the-author form** (strengthened 2026-07-16, v3.8.0, per a downstream project's nomination — companion-etude 0031): a recommendation is **claim + named justification + named consequence**. The claim is the bold pick. The justification cites evidence *named specifically enough to be checked* — a file, an ADR, a measurement — never "best practice" or taste. The consequence names what breaks or follows if the pick is wrong. A recommendation whose author can be caught is worth more than one that can only be believed (see `docs/inbox/CONVENTIONS.md` §2, catchability over correctness).

**Status tokens & annotations** (frozen at the v3.10.0 pairing): the open family is `unanswered` (the human's ball) | `unresolved` (answered once, passed back — the model's ball) | `deferred` (parked; nobody owes a move now). The closing family is `answered` | `withdrawn` (the asker acts) | `superseded` (a successor acts — point to it: `superseded — by QST-X`) | `moot` (the world acts). Any question-level token may carry a ` — <annotation>` (never parsed, always preserved — it is the pressure valve that keeps the token set small); whoever flips a status owes the one-line annotation saying why. The document-level `Status:` in the header stays a strict enum — when a document needs to say more, use structured fields, never a decorated enum value.

**Question identity — one story**: `### QST-<id>:` (1–24 letters/digits, interior hyphens) is the everyday citable handle, canonical-**optional** — add it when anything will refer back to the question; *a question that is referenced must have a handle*. The advanced form is an `<!-- @adr-anchor: <slug> -->` comment placed as the first non-blank content **after** the heading (placed before it, it silently binds to the previous section) — for when the heading must stay pure prose or the id must survive retitling; where both exist, the comment wins resolution. HTML comments shaped `<!-- @adr-<action>: <value> -->` are the reserved machine channel (`@adr-anchor`, `<!-- @adr-dismissed: <reason-slug> -->` on a heading line). The one grandfathered exception to that shape is this file's own line-1 version marker, `<!-- adr template version: "<stem> X.Y.Z" -->`, blessed exactly as-is — and version markers on *existing* documents are historical truth: never re-stamp them.

**Answering**: the `by`/`from` keyword is what makes a byline — `**ANS:** (by <name>, <date optional>)`; a bare `(Name)` stays part of the answer text. Pending state lives on the Status line (`- Status: unanswered — routing to <name>`) or in a bracketed `[Pending: …]` — never as bare prose in the ANS slot, because **the ANS text IS the answer** and every tool that layers, prefills, or writes leans on that contract. `[Fill this in]` is the sole empty-answer form tools emit and this template teaches.

### QST: [Question text]
- Status: unanswered
- Why asking: [How this shapes my approach]
- Need: [yes/no | explanation | code example | etc]

[List the options A / B / C ... with a short description of each]

**Recommendation**: (by [model-name, e.g. Opus 4.7])

[Claim: one sentence naming the pick — e.g. "**B — persistent annotation.**" Justification: 2–4 sentences from evidence named specifically enough to be checked (a file, an ADR, a measurement). Consequence: one sentence naming what breaks or follows if this pick is wrong. If walking back an earlier lean, say so explicitly.]

**ANS:** (by [name])
[Fill this in]   <!-- literal placeholder — parser-significant, do not paraphrase -->

---

### QST: [Another question]
- Status: unanswered  
- Why asking: [Context]
- Need: [Format]

**Recommendation**: (by [model-name])

[Claim + named justification + named consequence.]

**ANS:** (by [name])
[Fill this in]   <!-- literal placeholder — parser-significant, do not paraphrase -->

---

## Supporting Materials

Use these only when needed - delete unused sections.

### COD: [example-name]
```python
# Your code here
```

### API: [call-name]
**Request:**
```http
POST /endpoint
{"param": "value"}
```

**Response:**
```json
{"result": "data"}
```

### FIL: [files-to-read]
- `/path/file.py` - [What to look for]
- `/path/file.md` - [Why it matters]

### DOC: [reference-name]
[Documentation excerpt or link]

---

## Decision

### Context
[What problem are we solving? Why does it matter?]

### Options

**Option A**: [Name]
- Pros: [Benefits]
- Cons: [Drawbacks]

**Option B**: [Name]  
- Pros: [Benefits]
- Cons: [Drawbacks]

### Chosen: [Option name]

**Why**: [Rationale from our discussion]

**Trade-offs accepted**: [What we're giving up]

### Consequences
- [Immediate impact 1]
- [Immediate impact 2]
- [Long-term consideration]

---

## Open Follow-ups

*Concerns, observations, or questions surfaced during this ADR that don't block acceptance but shouldn't be lost. Use `QST:` for questions wanting answers; use bullets for declarative concerns or future tasks.*

### QST: [Open question to revisit later]
- Status: unresolved
- Why deferring: [Reason it's not blocking this ADR]

**ANS:** [Fill when resolved; or link to the ADR / discussion that resolved it]   <!-- literal placeholder — parser-significant, do not paraphrase -->

---

- [ ] [Concern: a worry we accepted but want to monitor]
- [ ] [Future task: something this decision implies but doesn't require now]
- [ ] [Unverified assumption: something to verify before [milestone]]

---

## Action Items

- [ ] [Task 1] - Owner: [name / role]
- [ ] [Task 2] - Owner: [name / role]

---

## Validation

*Each contributor confirms (add rows as needed; the prescribed examples are illustrative — replace with what's actually being confirmed):*

- [ ] [Name / role]: Decision captured matches intent
- [ ] [Name / role]: Reasoning is sound
- [ ] [Name / role]: Approach is implementable
- [ ] [Name / role]: Risks are acknowledged
- [ ] [Name / role]: [What they're confirming]

**Notes**: [Any caveats or follow-up needed]

---

## Iterations

*Each iteration captures how the ADR evolved. `Trigger` records what caused this iteration (a brief, a code review, an observation, an external event, etc.); `Outcome` records what changed and any status transition.*

### Iteration 1 ([date])
- Trigger: [What caused this iteration — e.g., initial draft from human dump / brief at <path> / etc.]
- Contributors: [Who contributed to this iteration]
- Changes: [What evolved]
- Outcome: [Status transition if any — e.g., `Draft → Proposed`]

### Iteration 2 ([date])
- Trigger: [What caused this iteration]
- Contributors: [Who contributed]
- Changes: [How approach evolved]
- Outcome: [Status transition if any]

---

## Glossary (optional)

*Project-specific terms introduced or used in this ADR, glossed for future readers. Terminology drifts over months; preserving meaning at time-of-decision matters.*

- **[Term]**: [Definition at time-of-decision]
- **[Term]**: [Definition]

---

## Links

- Related ADRs: [links]
- Related code: [links]
- Supersedes: [if applicable]

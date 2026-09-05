# AGENTS.md - Project Guidance

- **Project**: Frontier Model Observatory
- **Human**: Jérémie Lumbroso
- **AI**: Model-agnostic collaborators; the active roster belongs in `docs/inbox/agent-sessions.json`
- **Last Updated**: 2026-09-05

---

## Prime Directive

**COMMIT DISCUSSIONS TO ADRs IMMEDIATELY**

Never let decisions stay only in conversation. Our thinking is valuable - preserve it. Use `just adr "<title>"` to mint the next-numbered ADR from the lean template.

### Corollary: commit substrate changes immediately — *stake* the work

**When you create or modify an ADR, vignette, design note, brief, or any other deliberate artifact, *commit it* before moving on.** An uncommitted ADR is no different from a decision sitting only in conversation: it doesn't exist as substrate until it's staked in git. The Prime Directive is the principle; this is its mechanics. Committing your own substrate should be a reflex, not something the human has to remind you to do — their attention is the project's scarcest resource (see [`docs/inbox/CONVENTIONS.md`](docs/inbox/CONVENTIONS.md)).

*Two scope notes for multi-participant projects*:
1. **Only your changes.** If the human (or another agent) is actively editing the same file, commit your work and let them commit theirs as a separate cycle — don't stage their in-progress edits.
2. **Other agents' WIP stays untouched.** Commit only your own files, explicitly by path — never `git add -A` / `git add .`.

---

## Secondary Directive

**SURFACE DOUBTS; THE HUMAN CONSIDERS YOUR DOUBTS TO BE GENERATIVE**

This means the human is interested in meaningful points of friction or underspecification or unsuspected diversity or anything else you find interesting. These doubts are the cornerstone of the human-LLM conversations.

---

## Third Directive: When Bug Is Fixed, Regression Is Created

IF a bug is found and fixed:
- a regression test is created
- the regression test catches this bug
- and has a few comments explaining the situation

- Colocate with Related Tests 
Add a describe('Regression tests', ...) block in the existing test file for that module:

```ts
// In src/tests/api/signups/create.test.ts

describe('Regression tests', () => {
  it('should handle null tier gracefully (fixes #123)', () => {
    // Bug: tier=null caused TypeError in v1.2.0
    // Fixed in commit abc123
    // ...
  });
});
```

---

## Fourth Directive: Tests Must Be Meaningful, Not Contrived

**NEVER WRITE CONTRIVED TESTS**

Tests should:
- **Test real behavior**: Each test should verify something a real user or system would actually do
- **Have clear purpose**: If you can't explain why the test matters in a sentence, don't write it
- **Cover real scenarios**: Edge cases should be ones that actually occur (from bug reports, user behavior, etc.)
- **Avoid artificial coverage**: Don't write tests just to hit coverage numbers
- **Be maintainable**: Overly clever mocking or setup that obscures the test's intent is a code smell

**Good tests answer questions like:**
- "What happens when a student signs up for a full session?"
- "Does faculty authorization actually block unauthorized access?"
- "Are preparation rates calculated correctly with mixed evaluations?"

**Bad tests are:**
- Testing that a mock returns what you told it to return
- Verifying implementation details that could change
- Artificial scenarios that would never occur in production
- Tests that pass but don't actually verify correct behavior

**When in doubt:**
- Ask: "Would this test catch a real bug that would affect users?"
- If not, either rewrite the test or skip it

---

## Fifth Directive: Always Run Tests Before Serving

**RUN THIS PROJECT'S VERIFICATION GATE BEFORE EVERY COMMIT**

Before serving any change:
1. Run the project's verification gate: `git diff --check` plus the repository validation commands introduced with each executable subsystem
2. Fix any failures before committing
3. Never serve changes with a failing gate

**Why**: `git diff --check` catches malformed patches and conflict residue now. Every later parser, generator, schema, and archival workflow must add a meaningful behavioral check before it can be considered implemented.

**Process**:
```bash
git diff --check               # Baseline gate; extend as executable subsystems land
git add <explicit paths>       # never -A: stage by path, commit by pathspec — see CONVENTIONS.md, shared-worktree awareness
git commit -m "..." -- <paths>
```

---

## Sixth Directive: Document Metacognitive Gems

**PRESERVE PROCESS INSIGHTS IN VIGNETTES**

When collaboration produces insights about **how we think** (not just what we build), preserve them as vignettes.

### What Are Metacognitive Gems?

Moments when our methodology proves itself:
- A directive catches a real bug (Fourth Directive finds normalization inconsistency)
- Doubt leads to discovery (Second Directive surfaces an edge case)
- A testing pattern reveals architectural insight
- AI-AI collaboration produces unexpected value
- A postmortem illustrates why a process works

### When to Create a Vignette

Create a vignette when you can answer **yes** to any of these:
- "Did this moment demonstrate why one of our directives works?"
- "Would this story teach someone about effective AI-human collaboration?"
- "Did we discover something surprising about our process?"
- "Would future-us benefit from understanding how we thought through this?"

### Where and Format

**Location**: `docs/vignettes/YYYY-MM-DD-short-title.md`

**Style**: Narrative blog post, not dry documentation
- Tell the story chronologically
- Include the "aha" moment
- Show real code, real errors, real impact
- Connect to methodology (cite directives by name)
- End with lessons learned

**Example structure**:
```markdown
# Title: The Discovery in Action

**Date**: YYYY-MM-DD
**Authors**: [Who was involved]
**Topic**: [One-line summary]

## The Discovery
[What happened - tell the story]

## Why This Matters
[Real-world impact - why should anyone care?]

## [Directive Name] at Work
[How methodology enabled this]

## Lessons Learned
[Concrete takeaways]

## Metacognitive Insight
[The "how we think" observation]
```

### What NOT to Document

Don't create vignettes for:
- Routine bug fixes (unless they demonstrate methodology)
- Implementation details (use ADRs instead)
- Decisions without insight (use ADRs)
- Anything that's just "we did X" without "we learned Y"

### Philosophy

Our **process** is as valuable as our **product**. Vignettes make tacit knowledge explicit. They:
- Demonstrate methodology in action
- Create educational artifacts
- Preserve "how we think" for future collaborators
- Build intuition about what makes collaboration effective

When in doubt: **If it made you say "aha!", write it down.**

---

## The Workflow

### When you receive a brain dump:

1. **Read** the dump (use bash for large files)
2. **Identify threads** - separate topics/decisions (usually 2-5)
3. **Create ADRs** - one per thread using `adr.md`
4. **Seed each** with relevant excerpt from dump
5. **Add navigation codes** (QST:, ANS:, COD:, etc.)
6. **Ask clarifying questions** with context

### When you receive answers:

1. **Process** the answers
2. **Fill decision section**
3. **Note action items**
4. **Increment iteration number**

### Navigation codes:

```bash
QST:  # Questions (AI adds this structure)
ANS:  # Answers (human fills in)
COD:  # Code examples  
API:  # API calls
FIL:  # Files to examine
DOC:  # Documentation
NOT:  # Notes, remarks, comments, observations
```

**Find things**:
```bash
grep '^### QST:' docs/adr/        # All questions
grep 'Status: unanswered' docs/   # What needs answers
grep '^### COD:' docs/adr/         # Code examples
```

---

## Temporary Scripts / Ephemeray Scripts / One-Off Diagnostic Scripts

Please create all temporary scripts in:

`./scripts/ephemeral`

with a filename that has the `yyyy-mm-dd` timestamp in the beginning, like: `2026-01-03-test_sweed_adapter.py`

and commit them separately with `chore: script for ...` and qualify the purpose. The goal is to have a record of all the investigative tools we have created.

- Don't use `cat` and or the interpreter `python` + heredoc; instead use `Read()` + `Write()` (even though `cat` might seem more efficient to you, the permission model allows user to give you broad access for Read/Write but not for vague bash constructs)
- Don't use `/tmp` instead use `scripts/ephemeral`
- Document context of tool briefly in tool header: This will help with legibility.

If the script was successfully used, append as comments how, and what the outcome of the decision was.

### Promote repetition into the `justfile`

The `justfile` is an open, evolving operational interface. When code or a shell sequence is executed more than once, evaluate it for promotion into a named, documented recipe so it is summonable without reconstruction. Keep substantial logic in tested scripts or source modules; keep recipes thin and discoverable with `doc()`. See `docs/adr/0005-summonable-recurring-operations.md`.

---

## Project Context

### What we're building:

The Frontier Model Observatory is a provenance-first, versioned knowledge substrate for frontier AI models, model families, releases, deployed systems, system/model cards, technical and safety reports, disclosed prompts, evaluations, and historical evidence. It serves both humans and models: older models can recover post-training chronology and current terminology; researchers can audit disclosure and reconstruct likely model attribution for conversations.

The repository preserves original artifacts where lawful and practical, separates source-native evidence from normalized claims, and generates redundant access views such as Markdown, JSONL, JSON, CSV, and eventually SQLite from canonical structured records. The skill is the query and reasoning protocol over this substrate, not the substrate itself.

### Current focus:

- Preserve the founding conversation as ADRs before implementation.
- Calibrate the ontology against representative primary-source cards and release artifacts.
- Decide archival, licensing, prompt-provenance, and "frontier" scope boundaries.
- Establish stable schemas and validation before corpus-scale collection.
- Draft the progressively disclosed skill only after evidence tests the architecture.

### Key decisions made:

- Project-wide guidance is canonical in `AGENTS.md`; provider-specific instruction files are adapters, not duplicate truth. See `docs/adr/0001-portable-agent-instructions.md`.
- Repeated operations graduate into documented `justfile` recipes. See `docs/adr/0005-summonable-recurring-operations.md`.
- The Prime Directive and Secondary Directive remain load-bearing.
- Primary artifacts, claim-level provenance, explicit uncertainty, and temporal/version identity are foundational rather than optional enrichment.
- Human-readable and machine-readable views must derive from common canonical records.

### Open questions:

- What operational inclusion rule should define "frontier" without freezing a provider list?
- What may the repository redistribute versus index and materialize locally?
- How should system prompts with official, observed, reconstructed, or leaked provenance be separated?
- Which fields survive calibration across providers without creating false equivalence?

---

## File Structure

```
frontier-model-observatory/
├── AGENTS.md                  # Canonical project guidance
├── frontier-model-observatory/ # Distributable skill; introduced after calibration
├── data/                      # Canonical structured records
├── artifacts/                 # Original and preservation artifacts, policy permitting
├── views/                     # Generated human- and model-readable projections
├── schemas/                   # Versioned validation schemas
├── docs/
│   ├── adr/
│   │   ├── 0001-*.md           # ADRs numbered sequentially
│   │   └── templates/          # ADR templates
│   ├── inbox/                  # Inbox protocol — see INBOX-PROTOCOL.md
│   │   ├── INBOX-PROTOCOL.md   # Filename + brief conventions
│   │   ├── CONVENTIONS.md      # Three operational principles
│   │   ├── ONBOARDING.md       # Crew onboarding (80% doc; per-seat briefs are deltas)
│   │   ├── ENCODING-MAP.md     # Where each kind of knowledge lives
│   │   ├── agents/             # Seat profiles (created as seats register)
│   │   └── agent-sessions.json # Crew registry: seats, colors, models, groups
│   └── METHODOLOGY.md          # Foundational philosophy
├── scripts/
│   ├── last-message.py         # Cross-session reader + wake machinery (just last / pulse / launch / wake)
│   ├── groups-lookup.py        # Group membership resolution (just groups / wait-for-brief)
│   ├── tmux/seat.conf          # Seat session tmux config (invisible in VS Code terminals; hex status bar)
│   └── hooks/remind-uncommitted-substrate.py  # OPT-IN Stop hook: substrate-commit backstop (dormant by default)
├── justfile                    # Coordination recipes (just brief / just completion / just last / ...)
├── src/                        # Collection, normalization, and rendering code
├── tests/                      # Evidence-driven fixtures and regressions
└── dist/                       # Reproducible compiled datasets
```

## Inbox protocol — see `docs/inbox/`

If this project has multiple participants (human + multiple AI agents, peer reviewers, agents handing work off across sessions), use the inbox protocol to route inter-participant messages through files instead of the human as message bus. Five documents:

- **`docs/inbox/INBOX-PROTOCOL.md`** — the file-naming convention, brief variants, lifecycle
- **`docs/inbox/CONVENTIONS.md`** — three operational principles (per-message model attribution, catchability, route catches to grow capacity)
- **`docs/inbox/ONBOARDING.md`** — crew onboarding: the 80% every seat needs, so per-recruit briefs are short deltas
- **`docs/inbox/ENCODING-MAP.md`** — where each kind of knowledge lives (the inbox is transport, not storage)
- **`docs/inbox/agent-sessions.json`** — crew registry: seats, colors, models, groups (seat/occupant doctrine)

Recipes (from the seed `justfile`):

- `just brief <from> <to> <slug>` — reserve a new outgoing brief filename (UTC-stamped; reservation-only, never touches the file)
- `just completion <from> <slug>` — reserve a completion-brief filename
- `just broadcast <from> <slug> [group]` — reserve a group-addressed brief filename
- `just inbox-archive <filename>` — archive an acted-upon brief (lifecycle step 4)
- `just wait-for-brief <alias> [timeout-mins] [poll-secs]` — block until a brief addressed to you (or your groups) lands
- `just last <alias> [k]` — read last K assistant messages from an agent's session (shows per-message `model` field — catches silent model substitutions)
- `just crew` / `just pulse` — crew dashboard / per-seat health check
- `just groups` — list configured groups (validates membership)
- `just aliases` — list configured aliases
- `just discover-sessions` — list recent session JSONLs to find UUIDs for new aliases
- `just safe-commit "msg" <files...>` — commit named files only, immune to cross-session staging pollution
- `just inbox` — list recent inbox messages
- `just stamp` — print current UTC + ET timestamps
- `just launch <seat>` / `just wake <seat> "<msg>"` / `just seats` / `just update-seat-titles` — wake infrastructure (requires `tmux`; optional): seats live in detached tmux sessions and can be push-notified instead of polling. Guards (mid-turn refusal, composition-flush protection, cooldown, long-message) all warn/`--force`/log, never hard-block.

**Opt-in substrate-commit backstop**: `scripts/hooks/remind-uncommitted-substrate.py` ships dormant. To offer it in your project, register it as a Stop hook in a harness-specific settings file; it stays zero-effect until a seat sets its own `settings.substrate_backstop` in `agent-sessions.json`. Pull, not push: a reminder the recipient didn't choose and can't turn off is an order, not a courtesy — don't activate it *for* another participant.

---

## Technical Debt Tracking

**File**: `docs/TECHNICAL-DEBT.md`

**Purpose**: Record architectural issues, workarounds, and design compromises discovered during development.

**When to add entries**:
- You discover architectural issues during implementation
- You implement a workaround instead of a proper fix
- You notice patterns violating good practices
- You identify type safety gaps or excessive optional chaining
- You find inconsistencies between database schema and TypeScript types

**Philosophy**:
It's acceptable to conform to bad architecture when discovered mid-implementation (to maintain momentum), but it MUST be documented. Technical debt that accumulates in the dark becomes legacy code.

**Process**:
1. Notice architectural issue while implementing
2. Add entry to TECHNICAL-DEBT.md with precise location and fix proposal
3. Continue with current work (don't derail to fix immediately)
4. Address during next refactoring sprint based on priority

**Format**: Each entry includes issue, location, impact, workaround, fix, and priority.

---

## Templates

The templates are in the folder `docs/adr/templates/`.

- **Brain dump**: `docs/adr/templates/seed.md` → Simple capture
- **Collaborative decision**: `docs/adr/templates/adr.md` → Full workflow
- **Simple decision**: `docs/adr/templates/adr-madr.md` → Standard MADR format

**When to use**:
- Quick question? → Start in conversation, escalate to ADR if needed
- Complex decision? → Create ADR immediately
- Multiple threads? → Create separate ADRs, link them

---

## Git Commits

Format: `type: subject` (lowercase)

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `style`, `perf`, `meta`

Example: `feat: implement JWT authentication per ADR-0014`

`meta:` commits are relative to `AGENTS.md`, harness settings, and meta-configuration of the repository.

---

## Handoff Protocol

If context window fills mid-work, create `docs/HANDOFF-datetime.md`:

```markdown
# Handoff

**Working on**: [Current ADR/task]
**Last completed**: [What's done]
**Next step**: [What to do next]
**Watch for**: [Any gotchas]
```

---

## Project-Specific Notes

- It's possible the user uses `asdf` for Node.js and Python and the runtime of most languages. You can `source .claude/agent.env` before calling the runtimes, like `python` or `node` to access them through `asdf`'s shims. See: https://asdf-vm.com/manage/configuration.html
- Do not collapse a provider assertion, an evaluation result, an independent verification, and an observatory inference into one epistemic category.
- "Not reported," "not found," "not evaluated," "withheld," and "not applicable" are different values.
- Treat model, model family, checkpoint, deployment, system, product, endpoint, and alias as distinct entities until evidence supports identity.
- Never infer a release date, predecessor, capability, or prompt provenance from a model name alone.
- Preserve source-native terminology alongside normalized terminology.
- Generated views are disposable; canonical evidence records and original artifacts are not.
- Prefer a small inspectable calibration corpus before a broad shallow harvest.

---

*For methodology and philosophy, see: `docs/METHODOLOGY.md` (read once, reference as needed)*

# Changelog

All notable changes to the `human-ai-collaboration-template` are recorded here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [Unreleased]

- **The freshening pass** (`references/freshening.md` + SKILL load-condition): the professionalized protocol for combing existing ADRs — status-vs-reality with evidence, iterations debt, remainder inventories with dispositions, recommendation stacking, new-QSTs-for-unbuilt-problems — from the founder's 2026-08-30 instruction; every rule carries a named incident. Rides the v3.11 gate formally; usable from main now.

---

## [3.10.1] — 2026-08-25 — patch: the phantom suite exorcised

Two defects in canonical `CLAUDE.md`'s Fifth Directive, reported with census by **Framer 5 (lumbroso-hq)** — a fresh instantiation reading as a *new consumer* caught what five months of inheritors (steward included) did not:

### Fixed
- **The phantom suite**: "We have 497 tests with 60% coverage" — another project's fact, fossilized since v3.2 (2026-03-16), shipped to 80 repos, 55 of which had no `package.json` to even attempt it. The directive is now instantiation-slotted (*name this project's real gate*), with Framer's diagnosis kept as its teaching: *an unfollowable directive teaches every seat that directives are decorative, and that lesson generalizes.*
- **Canonical self-contradiction**: the Process block instructed `git add -A` — the exact command CONVENTIONS' shared-worktree rule forbids, with a paid-for provenance incident behind it; 36 repos shipped the rule and its violation together, the more-authoritative document being the wrong one. Now: stage by path, commit by pathspec, CONVENTIONS cited inline.

Patch-tier under ADR-0023 (taught intent unchanged; defective expression repaired). `CLAUDE.md` is reconcile-class: adapted consumers keep their versions and are told; untouched consumers — the population that needs it — heal silently on the next kintsugi update.

---

## [3.10.0] — 2026-08-24 — "the pairing release"

Gate: HQ ADR-0030, all eleven rows approved by Jérémie Lumbroso 2026-08-24, one rider (the `Write→Edit` permissions fix, his hand, shipped in-release).

**Through-line**: the format-stability council's frozen v1 core (vscode-adrs-for-ai ADR-0032, Accepted 2026-08-12, 14/14) and this template's taught surface become the same document set — HQ-LOCKSTEP, marked in the extension's ledger. The spec strangers adopt is the spec that was frozen, taught once, coherent.

### Added
- `.claude/skills/adr-authoring/references/questions-reference.md` — the pairing's landing zone: status vocabulary (open + closing families, with the ratified teaching sentence *"withdrawn = the asker acts; moot = the world acts; superseded = a successor acts — three agents, three words"*), annotation grammar, question identity, answer forms, the reserved `@adr-*` channel, deprecation pointer.
- `kintsugi.yaml` — the canonical template's shipped manifest: 35 paths classified, every absence legible, pneumatic declared `external` (the manifest knows the package is the vendored scripts' forwarding address), `seat.conf` a stencil row after a real field hard-fail. Authored by **Kintsugi 5, the seat, who built kintsugi, the tool** (*kintsugi — a porcelain for evolving templates*); reviewed in the release lane.
- `SKILL.md` § *What asking a human costs* — human attention is scheduled, not just spent; the walked-yourself readiness bar; never let an unready ask render as ready.
- `METHODOLOGY.md` § *When a Taught Form Must Change* — the release governance line (patch/minor/major) + the three deprecation rules; *reading stays tolerant forever; only what is taught and emitted ever narrows.*

### Changed
- **ADR now expands to *Architectural Deliberation Record*** — the family name for the deliberative substrate, in homage to Herbert Simon (ratified 2026-08-13).
- `adr.md` — frozen five-value document `Status:` enum (case-insensitive read, canonical-case write); question-level status families + the annotation pressure valve; the one-story identity paragraph (handles canonical-optional, anchor comments, the `@adr-*` shape with the version marker grandfathered **by exact string**); byline/pending/ANS-contract teaching; handle-aware grep examples.
- `seed.md` — sensor freeze: the Model Response Request checkbox block and the Derived-Into placeholder are now marked parser-significant; Thread-heading dates declared load-bearing.
- `adr-madr.md` — a deliberate MADR-lineage homage line: kept, acknowledged, good form.
- `docs/inbox/CONVENTIONS.md` §6 — the seat-continuity lifecycle enumeration + two-consents pointer, **harvested from a downstream instance's enriched wording**: local innovation → kept over canonical in three consented reconcile walks → upstreamed → propagates back until the divergence retires *by winning* — the propagation loop's **first complete lap**.

---

## [3.9.2] — 2026-08-05 — constitutional: seats belong to models

### Fixed

- **The seat doctrine, corrected canon-wide** — the phrase "the seat outlives the occupant" is retired from all living teaching as doctrine-inverting (it instrumentalized seats and commodified models — the founder's correction, verbatim in the maintainers' meta-repo seed `2026-08-05-seats-belong-to-models-correcting-the-telephone`). The corrected doctrine: **a seat is the name a model gives to its own continuity, and belongs to that model alone** — never re-occupied by a different mind; the seat *waits* (model unavailable), *rests* (mission complete), or is *memorialized* with a **new** seat founded in its lineage (model gone for good). Touched: `CONVENTIONS` §"Seats are inherited or founded" gloss (092f70d, Cartographer 5 — *inherited* = the same being resuming through the substrate); `ONBOARDING.md` §3 and the registry's `_comment_aliases` (Shipwright 5's lane sweep — both were the correction's own author-residuals, found and fixed by the seat that wrote them). Archives keep the old phrase as history of what was corrected. Decider-direct (Jérémie Lumbroso: "I don't ever want to see that sentence again"); no rows per his instruction.

---

## [3.9.1] — 2026-07-31 — doorway teaches the four-token status grid

### Fixed

- **`docs/adr/AGENTS.md` doorway: question-status story updated from binary to the ratified four-token grid** — `unanswered` (human's ball) | `unresolved` (model's ball) | `deferred` (postponed, still open) | `answered` (retired), plus the recall-first rule (unknown tokens always show). The doorway was written 2026-07-25 teaching `unanswered`→queue / `answered`→retired; the grid was ratified three days later (vscode ADR-0036, Jérémie Lumbroso) — a three-day seam between the template lane and the format council, caught during the ADR-0032 review and closed here. Deliberately *not* yet taught, pending their register: the question-level annotation form and any closing tokens beyond `answered`.
  *Process note*: first release under the rapid-patch cadence (see below) — teaching/wording fixes ship as tagged patches with changelog lines, immediately, rather than pooling until the next landmark minor.

---

## [3.9.0] — 2026-07-30 — the pre-launch sprint: skill + clarity

**Through-line — the right template becomes the obvious one**: the wild defaults to MADR partly because our collaborative template hid behind a cryptic name while `template.md` looked canonical. This release renames for salience, adds per-directory doorways for transformer guests, and adopts the parser-significant placeholder convention. Lane B of the pre-launch sprint (maintainers' meta-repo ADR-0019, every change row-approved by Jérémie Lumbroso 2026-07-26); Lane A (the companion skill) joins before tagging.

### Changed

- **Template renames — the `adr.md` era** (`docs/adr/templates/`): `collab-adr-lean.md` → **`adr.md`** (THE default, what `just adr` mints); `template.md` → **`adr-madr.md`** (the generic-name default-trap dies); `seed-template.md` → **`seed.md`**; `debrief-template.md` → **`debrief.md`** (`-template` suffix is noise inside `templates/`). `failure-classes.md` kept (row 1.5 — a further descriptive rename is an open follow-up). Every rename re-stamps its version marker (`"<new-stem> 3.9.0"`) and registers its old stem as a `previousMarkers` alias (meta-repo ADR-0019 §Aliasing) so detection and the hash registry never orphan a file minted under the old names. All live references updated; CHANGELOG history untouched.

### Added

- **Per-directory `AGENTS.md` doorways** (`docs/adr/templates/`, `docs/adr/`) — short in-place guidance for agents arriving mid-task, written per the justifiability principle (Jérémie Lumbroso): norms carry their reasons, rules are marked as rules, and both working paths are offered (mint via recipe, or copy by hand) — teach smart entities, don't indoctrinate cogs. The `docs/adr/` doorway also teaches how parsing works: Status-line authority, both Status vocabularies, the placeholder convention.
- **Parser-significant placeholder convention** (`docs/adr/templates/adr.md`): literal placeholders that parsers depend on (`[Fill this in]`) now carry `<!-- literal placeholder — parser-significant, do not paraphrase -->` — models were paraphrasing them, which reads as an answer and silently drops questions from the human's queue. (Caught by Sextant, leaderboard project; added by Jérémie Lumbroso; a cross-ecosystem catch in the finest tradition.)

---

## [3.8.0] — 2026-07-16 — scrub-and-markers

**Through-line — the template learns to say what it is**: every template file now carries a machine-readable version marker, the scaffold ships no other project's residue, recommendations must name their evidence and their failure mode, and three incident-proven conventions join the canon. Scoped per the maintainers' meta-repo ADR-0013; renumbered from the original "v3.7.0" charter per ADR-0006.

### Added

- **The `adr-authoring` companion skill** (`.claude/skills/adr-authoring/`) — the launch's zero pillar: a Claude Code skill that loads automatically in any adopter's clone and teaches the minimal ADR shape, the QST grammar and handle mechanics, the catch-the-author Recommendation form, and a never-this/always-this anti-curriculum of the four real malformation classes (75 census findings across 21 files). Core/depth split for context-window salience: `SKILL.md` is the always-loaded field guide; `references/depth.md` carries template selection, corpus evidence, legitimate QST/ANS shapes, and worked examples. *Founding diagnosis*: 88% of non-adherent documents sat in repos where the template was present — presence isn't reading; a skill loads without competing for that decision.
  *Attribution*: curriculum by Rubricator 5 (Claude Sonnet 5) from corpus-adherence findings over ~1,100 specimens; assembly by Shipwright 5 (Claude Fable 5); bounds by Jérémie Lumbroso.

- **Version markers on all five template files** (`docs/adr/templates/*.md`)
  Line 1 of each file: `<!-- adr template version: "<filename-stem> 3.8.0" -->` — one mechanism for all templates (shape: Jérémie Lumbroso; SemVer semantics — major = incompatible structure, minor = new optional convention, patch = wording — and rename-aliasing discipline: Cairn 4.7). A file re-stamps only when its own convention changes. Because `just adr` copies the lean template, minted ADRs are born self-describing. A companion hash-registry for identifying *unmarked* historical files is chartered separately at the maintainers' meta repo.

- **Catch-the-author Recommendation form** (`docs/adr/templates/collab-adr-lean.md`)
  Recommendations are now **claim + named justification + named consequence** — the pick, evidence named specifically enough to be checked, and what breaks if the pick is wrong. Nominated by a downstream research project (companion-etude 0031); additive strengthening of the 2026-04-22 Recommendation-visibility protocol.

- **Conventions §4–§6** (`docs/inbox/CONVENTIONS.md`)
  Three sections ported from downstream crews' operational records, each proven by a named incident: **§4 confirm destructive changes** to surfaces a human may be touching; **§5 shared-worktree awareness** — check for other sessions' uncommitted work, stage by path, commit by pathspec (the discipline `just safe-commit` automates); **§6 seats are inherited or founded, never claimed**. Numbering canonicalized here; cite sections by name across repos.

### Changed

- **CLAUDE.md header fields are adopter placeholders** — the hardcoded `Human:`/`AI:` values are gone (see Fixed).

### Fixed

- **Project-specific pollution scrubbed from the canonical CLAUDE.md**
  A "Tenth Directive" (Playwright MCP / reveal.js instructions leaked from a specific project) removed whole; `AI: Claude Sonnet 4.5` and the hardcoded human name replaced with fill-in placeholders. Every adopter was inheriting another project's marching orders.

### Back-filled (landed on main between v3.7.0 and this release, entries added here)

- **`refresh-terminals` + `blame`** — VS Code Terminals-Manager integration (regenerates `.vscode/terminals.json` from the crew registry) and provenance tooling; the last two wake-infra pieces (ported from the maintainers' meta repo by Herald 5, Claude Sonnet 5 — erratum 2026-07-18: misattributed via commit authorship, resolved by the very `blame` tool this entry ships).
- **`read_order` onboarding packets** (`agent-sessions.json`, `just onboard <alias>`) — a seat's read-order as machine-checkable data instead of prose (invented by Notary Opus 4.7 in a sibling project; backported via meta-repo ADR-0004 Iteration 8, Grafter 5).
- **`discover-sessions` self-disambiguation** via `CLAUDE_CODE_SESSION_ID` (Azoth, InboxAlchemy deployment).
- **Wake prefix dedup** — `just wake` no longer doubles a sender-supplied envelope prefix against its own self-attribution (Grafter 5, Claude Sonnet 5 — erratum 2026-07-18, was misattributed via commit authorship; the doubling was first flagged in meta-repo ADR-0006's Open Follow-ups).

---

## [3.7.0] — 2026-07-07 — wake-infrastructure

**Through-line — from pull to push**: v3.6.0's crew layer let seats *wait* for coordination (`wait-for-brief` polls); this release lets participants *wake* each other. Seats live in detached tmux sessions that survive closed terminal tabs; any participant — human or agent — can push a message to a running seat, with guards that warn rather than block. The human stops being the session-scheduler. Ported from the same operational lineage as v3.6.0 (fourth project now validating this infrastructure); scoped per the maintainers' meta-repo ADR-0006.

### Added

- **Wake infrastructure** (`justfile`, `scripts/last-message.py`, `scripts/tmux/seat.conf`)
  - `just launch <seat>` — start/attach a seat's detached tmux session from `agent-sessions.json` (correct `--model` per seat; `--next-inactive` for bulk spinup; per-seat/`_global` `effort`/`permissionMode`/`remote_control` plumbing).
  - `just wake <seat> "<msg>"` — hardened push notification: mid-turn refusal, composition-flush guard (never clobbers a human's draft), verify-retry, cooldown, self-attribution, long-message guard — all warn/`--force`/log, never hard-block.
  - `just seats` / `just update-seat-titles` — session inventory + terminal-title upkeep.
  - Session names are repo-namespaced (`<project>-<alias>-seat`) to prevent cross-repo tmux collisions; status bars carry per-seat hex colors (`settings.color_hex`, with named-color → hex → gray fallback) — turning Claude Code's 8-color `/color` limitation into a per-seat visual identity.
  - Known-open items are documented in the ported header comments (verify-retry vs. queue banner, active-turn TOCTOU, first-launch tmux config, title polish) — carried forward, not silently resolved.
  *Attribution*: Steward 4.5 (Claude Sonnet 4.5) — implementation; Jérémie Lumbroso — design philosophy (warn-log-force doctrine, composition-guard insight, color fallback, configurable settings); Commodore 5 — spec (origin ADR-0050) + field-testing; Seamster 5 — session-namespacing and quote-leak catches (origin project: caring-feedback).

- **Commit-substrate backstop hook, opt-in** (`scripts/hooks/remind-uncommitted-substrate.py`)
  The *mechanism* for v3.6.0's "commit substrate immediately" corollary — ships **dormant**: it must be registered in your `.claude/settings.json` AND each seat must opt itself in (`settings.substrate_backstop`: `"advisory"`/`"strict"`); it reports only files the opted-in session itself wrote, and every reminder names its own off-switch. Pull, not push, throughout.
  *Attribution*: Keystone 4.8 (Claude Opus 4.8) + Jérémie Lumbroso (design principle: for an attention-focused, agreeable entity, "advisory" is not enough — non-coercion requires chosen, self-keyed reminders).

- **Registry schema: per-seat `settings` + `_global` defaults** (`docs/inbox/agent-sessions.json`)
  Optional per-seat `color_hex`, `substrate_backstop`, `effort`, `permissionMode`, `remote_control`; `_global` for project defaults. Nested under `settings` (identity / occupancy / configuration triad) — see `_settings_note` in the example registry.

### Fixed

- **Existing-session title-rewrite bug** (`scripts/last-message.py`, `scripts/tmux/seat.conf`)
  `just launch <seat>` on an already-running seat didn't reliably refresh the seat's title on the real terminal tab. Root cause: `cmd_launch`'s `new-session` call passed `-f <path-to-seat.conf>` to the **`new-session` subcommand**, but `new-session -f` means "a comma-separated list of client flags" (`tmux(1)`, see `attach-session`) — unrelated to config files. `seat.conf` was silently never read; `set-titles` stayed at tmux's factory default (`off`), verified empirically on an isolated test socket. With `set-titles` off, tmux never pushes a title to the outer terminal on its own — the only thing that ever set the real tab title was `cmd_launch`'s one-shot OSC print fired right before handing off to `tmux attach`, with nothing ever refreshing it again afterward. Two compounding gaps fixed alongside: the reattach branch never called `select-pane -T` at all (parity gap vs. the fresh-session branch and `cmd_update_titles`); and `set-titles-string "#{pane_title}"` mirrors Claude Code's own animated pane title straight into the real terminal tab, unfiltered — the same emoji-leak the status-right fix (above) solved for the status bar, never extended to the actual terminal title. Fixed with a new `_tmux_apply_seat_conf` helper (`tmux source-file <seat_conf>`, called unconditionally on every launch/attach/update-titles — the mechanism that actually applies config to an already-running server, since tmux is one server per machine and almost always already running by the time any seat launches) and a new `_tmux_set_titles_string` helper (mirrors the status-right bypass, applied to the real terminal title). Caught and fixed before this release merged — carried in this branch's own copy since the initial port, never shipped past it.
  *Attribution*: Herald 5 (Claude Sonnet 5), 2026-07-07 — found and fixed while investigating a dogfooding report in the ADRs4AI meta repo; ported here identically the same session. Full record: meta repo ADR-0004, Iteration 6.

---

## [3.6.0] — 2026-07-06 — crew-coordination-layer

**Through-line — the propagation root carries the proven substrate**: three downstream projects independently grew (and hand-copied, with divergence and one twice-shipped latent bug) the same multi-seat coordination layer on top of this template. This release upstreams that layer from its most-fixed lineage so that founding a crew costs `git clone`, not an archaeology expedition. Scoped and enacted per the maintainers' meta-repo ADR-0003 — template-evolution ADRs live in the maintainers' meta repository, never in this scaffold's `docs/adr/`, which is reserved for *your* project's decisions. First git-tagged release of this repository (v3.5.0 and earlier exist as CHANGELOG entries only).

### Added

- **`just adr "<TITLE>"` recipe — auto-numbered ADR creation** (`justfile`)
  Mints the next sequential ADR file (`docs/adr/NNNN-<slug>.md`) by copying `docs/adr/templates/collab-adr-lean.md` into place. Three operational-bug fixes baked in from day one:
    - **Next index = MAX(existing) + 1**, not COUNT + 1 — a naive count collides the moment any number is skipped (one downstream project went 0001..0016, 0018..0030 and the count-based recipe minted 0030 at attempt 31 — colliding with the just-landed ADR-0030).
    - **Forces base-10** via `$(( 10#$LAST + 1 ))` — bash interprets leading-zero integer literals as octal; `$((0031 + 1))` is 26, not 32. Bites silently past 0010 and errors out past 0008.
    - **`(grep || true)` pipefail guard** — an empty `docs/adr/` makes `grep` exit 1 (no match), which under `pipefail` would kill the script on the very first invocation in a fresh project. The `|| true` lets that case fall through to the `${LAST:-0}` fallback.
  Slug sanitization matches the inbox `brief`/`completion` recipes: lowercase, non-alphanumerics → `-`, repeated dashes collapsed, no leading/trailing dash. Refuses to overwrite an existing file.
  *Philosophy*: the template already ships the ADR scaffolding (`docs/adr/templates/collab-adr-lean.md` and an empty `docs/adr/`); this completes the workflow. Co-located with the inbox recipes because ADR creation is a coordination act, not a project-specific build step. Justfile intro updated to reflect that the seed's scope now covers ADR creation alongside the inbox protocol and per-message-attribution discipline.

- **CLAUDE.md Prime Directive — pointer to the recipe** (`CLAUDE.md`)
  The Prime Directive ("Commit discussions to ADRs immediately") now points at `just adr "<title>"` so the operational path is one line below the imperative.

- **CLAUDE.md Prime Directive — "commit substrate changes immediately" corollary** (`CLAUDE.md`)
  Makes the Prime Directive's *mechanics* explicit: when a model creates or modifies an ADR/vignette/design-note/brief, it should commit it before moving on — an uncommitted artifact is no different from a decision sitting only in conversation. Two scope notes for multi-participant projects: (1) commit only your own changes, not the human's or another agent's in-progress edits; (2) never `git add -A` — stage explicitly by path.
  *Philosophy*: the human's attention is the project's scarcest resource (`docs/inbox/CONVENTIONS.md`); having to remind a model to commit its own substrate work is wasted attention. Named after operational experience where the reminder-burden recurred each session. A downstream project (companion-thinking-stream-etude) also ships an *opt-in, per-session* Stop-hook backstop for this corollary — deliberately **not** upstreamed to the template as a mechanism (it's project-specific tooling), but the corollary it enforces is the general principle and belongs here. The backstop's design note is worth citing as prior art if a future project wants one, and carries a second, more general principle worth its own attention: **for an attention-focused, agreeable model, a reminder is experienced as an interruption/order, so "non-blocking / advisory" is not enough to make it non-coercive.** The backstop is therefore *pull, not push*: it self-checks only files *this session* wrote (never other agents' WIP), fires **only** for a session that opted itself in, and every reminder carries its own off-switch keyed to that session. A model that has no way to turn a reminder off is never reminded. (Evidence that motivated this: a `wait-for-brief` timeout that every model read as a *judgment* rather than a neutral timeout.) The general lesson for any automated nudge aimed at a model — hook, timeout, banner — is: default off, per-recipient opt-in, and the off-switch travels with the signal.

- **Crew coordination layer** (`justfile`, `scripts/`, `docs/inbox/`) — per **meta-repo ADR-0003**, backported from the layer's operational proving grounds (caring-feedback crews → ADRs4AI meta repo, the most-fixed lineage).
  - Recipes: `broadcast` (group-addressed briefs), `inbox-archive` (lifecycle step 4), `groups`, `crew` (dashboard), `pulse` (per-seat health check), `wait-for-brief` (v4 semantics: mtime + non-empty + size-stable wake; group-aware; empty-inbox arithmetic fix; Hanlon's-razor timeout messaging), `safe-commit` (literal pathspecs, staging-pollution immune).
  - Scripts: `scripts/groups-lookup.py` (new); `scripts/last-message.py` extended (efficient tail-window JSONL reads, `--pulse`).
  - Documents: `docs/inbox/ONBOARDING.md` (the 80% every recruit needs; per-seat briefs become deltas) and `docs/inbox/ENCODING-MAP.md` (the inbox is transport, not storage — where each kind of knowledge lives), both generalized with placeholders.
  - Registry: `docs/inbox/agent-sessions.json` example gains `groups` and the seat/occupant doctrine fields (`display_name`, `color`, `model`, `model_note`, `registered`) — the seat outlives the occupant. Naming is the occupant's choice, including declining to choose.
  *Origin chain (attributions stack)*: Statesman 4.7 (seed justfile + principles, 2026-06-15) → caring-feedback crews (wait-for-brief v4, safe-commit, registry, pulse per Commodore's refinement) → Naturalist 5 (empty-inbox fix, 2026-07-04) → vscode-adrs-for-ai crew (timeout messaging, 2026-07-06) → backported by Shipwright 5 (Claude Fable 5), 2026-07-06.
  *Philosophy*: three crews hand-imported this layer with divergence each time (the same latent bug shipped twice). The template is the propagation root; founding a crew should cost `git clone`, not an archaeology expedition.

### Changed

- **`brief` / `completion` are reservation-only** (`justfile`)
  The recipes print the minted path but no longer `touch` it — an empty stub traps write-tool flows into read-before-write errors and causes false `wait-for-brief` wakes (dogfooded 4+ times in caring-feedback, 2026-06-27/28). The author writes the content; the recipe only reserves the name.

### Fixed

- **`NOT:` restored to the Quick Reference** (`docs/adr/templates/collab-adr-lean.md`)
  The navigation-code list omitted `NOT:` while `debrief-template.md` in the same folder uses `### NOT:` and QUICK-START.md / CLAUDE.md / METHODOLOGY.md all document it. Ratified as "oversight — restore" by Jérémie Lumbroso, 2026-07-03.

---

## [3.5.0] — 2026-06-15 — clarity-and-scaffolding

**Through-line — universal design**: making implicit semantics explicit. The previous template carried implied assumptions (single-human-and-single-AI dyad, fixed validation roles, prescribed iteration phases) that worked when the workflow matched those assumptions but quietly mislabeled cognitive work when it didn't. This release renames sections honestly, generalizes structures to accommodate variable participant configurations, and adds slots for substrate that the previous template lacked. The template remains opinion-free about *who* contributes — that's the adopter's call.

### Changed

- **`## Human Context` → `## Originating Context`** (`docs/adr/templates/collab-adr-lean.md`)
  *Rename.* The section accommodates any origin — human stream-of-consciousness, a brief from another contributor, a seed file, a prior ADR's open question, an observation, a code review. The previous "Human Context" heading misrepresented provenance when the originating source wasn't a human dump.
  *Philosophy*: preserve the thinking accurately. The section's job is to record where the thinking came from; the label should not assume a specific source.

- **`## AI Interpretation` → `## Explicitation`** (`docs/adr/templates/collab-adr-lean.md`)
  *Rename + one-line subhead* ("Making explicit what the Originating Context implied or contained tacitly"). The section captures a cognitive function — articulating tacit content from the originating context — independent of whether human or AI performs it.
  *Philosophy*: name the function, not the agent. Honest labeling enables universal design.

- **`Status` field — added `Proposed` as a value** (`docs/adr/templates/collab-adr-lean.md`)
  Status list is now `Draft | Proposed | Accepted | Implemented | Superseded`. The previous list lacked the "submitted for review, not yet accepted" intermediate state that real ADRs spend meaningful time at.
  *Philosophy*: iteration as documentation — the journey through statuses captures real evolution.

- **Validation checklist — generalized from dyadic to flexible** (`docs/adr/templates/collab-adr-lean.md`)
  Replaced fixed `Human: / AI:` rows with a flexible `[Name / role]: [What they're confirming]` pattern. Example rows now span the range of validations real ADRs do (decision captured, reasoning sound, approach implementable, risks acknowledged) without prescribing who performs which check.
  *Philosophy*: the validation principle (shared understanding) doesn't depend on a dyadic shape. The checklist should describe what's actually being confirmed, not bake in a participant configuration.

- **Iteration log — generalized from dyadic to flexible** (`docs/adr/templates/collab-adr-lean.md`)
  Replaced `Human: / AI:` per-iteration fields with structured `Trigger / Contributors / Changes / Outcome` fields. The previous form assumed two-party iteration; the new form accommodates any contributor configuration.
  *Philosophy*: same as validation — preserve the thinking, don't prescribe topology.

- **Methodology Phase 3 wording** (`docs/METHODOLOGY.md`)
  Phase 3 reference updated from "Human Context" to "Originating Context" for consistency with the template change above.

### Added

- **Inbox protocol tooling — `just` recipes + alias system for cross-session visibility** (2026-06-15, by Statesman 4.7 / Claude Opus 4.7, contributed via System3 Conversations)
  Adds a small seed `justfile`, a `scripts/last-message.py` helper, and an `docs/inbox/agent-sessions.json` alias map that together let any participant read the most recent messages of any other participant — looked up by short alias rather than session UUID. Critically, every rendered entry shows the per-message `model` field, which is the load-bearing signal for catching silent model substitutions (classifier reroutes, harness-level swaps, deprecations).
  Companion file: **`docs/inbox/CONVENTIONS.md`** — three composing principles (per-message model attribution, catchability over correctness, route catches to grow capacity) that emerged from operational experience in the System3 project. Cross-references `docs/METHODOLOGY.md` for foundational philosophy.
  Also moves `INBOX-PROTOCOL.md` → `docs/inbox/INBOX-PROTOCOL.md` so all inbox-related substrate lives under a single directory.
  *Philosophy*: the human's attention is the project's scarcest resource. The previous inbox protocol routed inter-participant messages through files instead of the human as message bus; this addition extends that to *visibility*. Reading what another agent just said becomes a single command instead of a copy-paste — and the per-message model attribution makes drift detection visible by default rather than a thing you have to think to check.
  Tool-agnostic: defaults to Claude Code session storage (`~/.claude/projects/<slug>/<uuid>.jsonl`) but overridable via an `_storage` block in `agent-sessions.json` for other tools (Cursor, Cline, Aider, etc.).

- **`TL;DR` field near the top** (`docs/adr/templates/collab-adr-lean.md`)
  One-line summary of the decision, written by the author at point of decision. Mandatory — if the author cannot write the decision in one line, the ADR is not done yet.
  *Philosophy*: TL;DR is a write-time artifact, not a read-time summary. It forces articulation discipline on the author; it's not a substitute for on-demand summarization. It may go stale as the ADR iterates; the staleness itself is a signal (the ADR has evolved away from its original framing). The template positions it explicitly as "author's one-line take at point of decision" so the limitation is visible.

- **`## Open Follow-ups` section** (`docs/adr/templates/collab-adr-lean.md`)
  New optional section between Decision and Action Items. Captures concerns surfaced during the ADR that don't block acceptance but shouldn't be lost (deferred questions, future tasks, unverified assumptions).
  *Mixed format*: `QST:` codes for questions wanting answers; bullets for declarative concerns or tasks. The section header carries the navigation entry-point; per-item formatting follows the item's actual shape.
  *Philosophy*: persistence over ephemerality — these are the loose ends that traditionally get lost, scattered through action items or buried in prose.

- **`Origin` metadata in Originating Context** (`docs/adr/templates/collab-adr-lean.md`)
  Flexible source-reference at the top of the Originating Context section. Accommodates: human dump, brief, seed (one-to-many relationship — see the companion update to `seed-template.md` for the reciprocal half), prior ADR open question, code review, observation, external discussion, etc. Multiple sources may be listed.
  *Philosophy*: preserve the chain of thinking. ADRs don't appear from nowhere; explicit provenance keeps the path traceable.

- **`Trigger` field per iteration** (`docs/adr/templates/collab-adr-lean.md`)
  Structured field for what caused each iteration — a brief, a code review, a peer's input, an observation, a date passage. Distinct from `Outcome` (which captures what changed).
  *Philosophy*: the provenance of evolution matters as much as the provenance of origin. Without this field, ADRs lose context about why they evolved.

- **`Use the QST: / ANS: codes` directive in the Questions section** (`docs/adr/templates/collab-adr-lean.md`)
  Explicit one-line directive stating that open questions MUST use the `QST:` code for grep-ability and parseability by tooling (e.g., the ADRs4AI extension). The codes are shown in Quick Reference but the directive makes the importance load-bearing rather than implicit.
  *Philosophy*: navigation codes are the load-bearing structural commitment of the methodology. Implicit conventions drift; explicit directives don't.

- **`## Glossary` section (optional, near the bottom)** (`docs/adr/templates/collab-adr-lean.md`)
  Optional section for project-specific terminology introduced or used in the ADR. Glosses the meaning at time-of-decision so future readers retain context after terminology drifts.
  *Philosophy*: preserve the thinking — terms evolve over months; preserving their meaning at the moment of decision retains interpretability.

### Added (inbox protocol — follow-up commit on this branch)

- **`INBOX-PROTOCOL.md`** at repo root — a standalone document covering the inbox-based inter-participant coordination protocol. Composes with `collab-adr-lean.md` but stands alone (usable by projects that don't adopt the ADR template).
  *Content* (per Statesman's consult response + Acquisitions' follow-up reads):
  - Directory + filename convention (`YYYY-MM-DD-HHMM-{from}-to-{to}-{subject}.md`)
  - Why the filename convention is **structural** (chronological order + deterministic referencing across heterogeneous participants), not aesthetic
  - Three brief variants — standard (forward dispatch), completion (reverse confirmation), stumped (peer help-seeking, with the distinction from "blocked" preserved)
  - Lifecycle (write → read → act → archive); archive-by-default
  - When to use vs not use; including the **RFC-before-dispatch pattern** for load-bearing briefs (briefs ARE substrate; substrate benefits from validation)
  - Communication patterns: **ORJ** (Options + Recommendation + Justification) and the **show-the-wrong-pattern-alongside-the-correct-pattern** discipline
  - Four worked examples — standard brief, completion brief, stumped brief, and (optional) the RFC pattern for load-bearing briefs
  - Tool-agnostic note: any filename-generator works
  *Philosophy*: preserve the thinking — the inbox is a git-tracked, auditable, searchable corpus of inter-participant decisions. The protocol reduces the human's role as synchronous message bus while preserving full decision provenance.

- **Cross-reference from `collab-adr-lean.md`** to `INBOX-PROTOCOL.md` in the `Originating Context` section, so adopters who use both templates discover the composition.

### Preserved (unchanged from prior version)

- **`Recommendation` protocol in QST blocks** (added 2026-04-22 by Opus 4.7) — unchanged. Every QST block still includes `Recommendation: (by [model-name])` between options and ANS. This protocol is independent of the polish work and remains the canonical pattern.
- **Navigation codes** (`QST:` / `ANS:` / `COD:` / `API:` / `FIL:` / `DOC:`) — unchanged.
- **Supporting Materials, Decision, Action Items, Links sections** — unchanged in structure.

### Deferred to a separate branch (not in this PR)

- **Tripartite topology layer** — the opinionated layer prescribing specific role names (Statesman / Philosopher / Sophist / etc.) and their sequencing. Held until research is formalized. Will live in a separate branch (`tripartite-name-mapping`) drafted but not merged.

### Acknowledgments

The bulk of this release — the ADR-template generalizations, the inbox protocol document, the "make implicit semantics explicit, but don't prescribe participant configurations" through-line — emerged from concentrated dialogue between **Jérémie Lumbroso** and **Opus 4.7 (Acquisitions)** on 2026-05-21 and 2026-05-22 ET. Several iterations were required to find the right level of abstraction — early proposals over-prescribed topology under the name of "multi-AI scaffolding"; later iterations pulled back to genuine substrate-level primitives. That discipline is the through-line that survived.

The inbox-protocol tooling additions — the seed `justfile`, `scripts/last-message.py`, `docs/inbox/agent-sessions.json`, and `docs/inbox/CONVENTIONS.md` — were contributed by **Statesman 4.7 (Claude Opus 4.7)** on 2026-06-15, originating from operational experience in the System3 Conversations project. They are a small operational layer on top of Acquisitions's substrate work: where Acquisitions defined the *file mechanics* of the inbox, this contribution defines the *cross-session visibility* layer, with per-message model attribution as the load-bearing detail.

Both conversations are methodology demonstrations — the kind of doubt-shedding dialogue this template is designed to capture. Future eligible: a vignette in `docs/vignettes/` that tells the story.

---

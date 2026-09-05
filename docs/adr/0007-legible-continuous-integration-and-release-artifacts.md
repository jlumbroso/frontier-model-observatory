<!-- adr template version: "adr 3.10.0" -->

# Legible Continuous Integration and Release Artifacts

- **Date**: 2026-09-05
- **Iteration**: 6
- **Status**: Partially Implemented
- **Deciders**: Jérémie Lumbroso; GPT 5.6 Sol at Perplexity Computer

**TL;DR**: Continuous integration must make repository health legible through `GITHUB_STEP_SUMMARY`, and releases must publish validated, downloadable skill and dataset artifacts with integrity metadata.

---

## Originating Context

**Source**: Direct human requirement in the founding conversation, 2026-09-05.

> "Must have continuous integration with GITHUB_STEP_SUMMARY that provides complete legibility, and produces a downloadable version of the skill on releases, etc. And document everything in ADRs."

**Agency Grant**: Design and implement the complete CI and release system; interrupt only if a credential or platform boundary prevents landing it.

---

## Explicitation

**What I understand**:

1. CI is not merely a pass/fail badge. Its output must explain what was checked, what changed, what remains incomplete, and where to inspect failures.
2. `GITHUB_STEP_SUMMARY` is the primary human-readable run report.
3. Release automation must produce a directly downloadable, validated skill package rather than requiring users to clone or build the repository.
4. Release artifacts should be reproducible and carry checksums and build provenance.
5. CI and release behavior are architectural decisions and must remain connected to ADRs.

**Assumptions**:

- GitHub Actions is the required hosted CI.
- `just verify` remains the local/hosted parity command.
- The skill package will be a ZIP because it contains multiple files.
- Dataset distributions may be added to release assets as their generators stabilize.
- A release is tag-driven and should fail closed when validation or packaging fails.

**Confirm**: The direct requirement is sufficient to accept the architecture without a blocking question.

---

## Decision

### Verification workflow

Add a GitHub Actions workflow for pushes and pull requests that:

1. checks out the exact revision;
2. installs pinned toolchain dependencies;
3. runs `just verify`;
4. validates schemas, canonical records, generated views, links, artifact manifests, and the skill as those subsystems land;
5. records machine-readable results for summary rendering;
6. writes `GITHUB_STEP_SUMMARY` under `if: always()` so failure does not erase explanation;
7. uploads diagnostic reports when a failure benefits from offline inspection.

The summary should include, when applicable:

- revision, ref, event, actor, and run links;
- a check matrix with status, duration, and command;
- changed canonical record families;
- schema and referential-integrity counts;
- artifact counts, byte totals, hash failures, and link-state changes;
- provider and chronology coverage;
- typed absence and quarantine counts;
- generated-view freshness;
- unanswered ADR question count;
- skill validation, file count, and package size;
- release-asset names and checksums;
- precise failure locations and remediation commands.

Summaries must distinguish “not run,” “not implemented,” “not applicable,” and “failed.”

### Release workflow

On version tags:

1. run the full verification gate;
2. build the distributable skill from canonical skill sources;
3. validate the complete skill tree;
4. build approved dataset, index, and extracted-text distributions;
5. produce deterministic archives where practical;
6. generate SHA-256 checksums and a manifest containing source revision, schema version, generator version, and build time;
7. upload the skill ZIP and diagnostics as workflow artifacts;
8. attach the skill ZIP, extracted-text ZIP, checksums, manifest, and approved distributions to the GitHub Release.

The release must not silently omit an expected asset. An unavailable distribution is represented as an explicit failed requirement or a versioned “not yet part of this release contract,” never as an accidental absence.

### Security and reproducibility

- Use least-privilege workflow permissions.
- Pin third-party actions to immutable commit SHAs, with readable version comments.
- Do not expose provider credentials to pull requests.
- Keep build and validation commands in repository scripts or `justfile`; YAML orchestrates but does not become the only implementation.
- Package from a clean checkout and reject untracked/generated drift.
- Include integrity hashes for every released file.

### Current authorization boundary

The current fine-grained PAT has repository-content authority but correctly rejects creation or modification of `.github/workflows/*`. Workflow files may be designed and tested locally, but landing them requires a one-time actor with workflow authority. Do not broaden credentials until there is a reviewed workflow ready to commit.

**Why**: CI must preserve epistemic legibility at the operational layer. A green badge without evidence is inconsistent with a repository whose purpose is inspectable claims and provenance.

**Trade-offs accepted**: Rich summaries and deterministic releases require maintained reporting code. That logic belongs in tested scripts with thin workflow wrappers so it remains executable outside GitHub.

---

## Questions

### QST-WORKFLOW-LANDING: Which narrow authorization path should land the validated GitHub Actions workflows?
- Status: unanswered
- Why asking: `.github/workflows/verify.yml` and `release.yml` pass YAML parsing, static contract tests, and actionlint, but the current fine-grained PAT correctly lacks workflow-write authority. Hosted validation and release publication cannot begin until those two files and their regression test are committed.
- Need: Choose the one-time landing mechanism.

**Options**:

- **A — Narrow workflow PAT**: Provide a short-lived fine-grained token for only this repository with Contents read/write and Workflows read/write; the agent commits, pushes, inspects the hosted run, and continues.
- **B — Human landing commit**: The agent provides the exact three prepared files and commit message; Jérémie commits them through GitHub or a local clone, after which the agent inspects and iterates on hosted runs.
- **C — Defer hosted CI**: Keep local `just verify-complete` authoritative and postpone workflow landing and releases.

**Recommendation**: (by GPT 5.6 Sol at Perplexity Computer)

**A — Narrow workflow PAT.**

**Rationale**: It preserves the established least-privilege model while allowing the same agent that prepared and tested the workflows to complete the hosted feedback loop. The token can be repository-scoped and short-lived, then revoked immediately after the first green hosted run and release dry run.

**Confidence**: High. The prepared workflow diff is already bounded and locally validated; only GitHub’s workflow-write permission is missing.

**Falsifier**: If the available token UI cannot grant workflow write without materially broader repository access, choose B and land the reviewed files manually.

**ANS:** (by Jérémie Lumbroso)

---

## Consequences

- `just verify` is the shared local and hosted gate.
- Every new canonical subsystem must register checks and summary metrics.
- Release packaging becomes a tested product surface.
- Workflow authorization remains a narrow landing dependency, not a reason to broaden the current token prematurely.
- CI claims are not considered implemented until an actual hosted run is inspected.

---

## Action Items

- [x] Implement structured verification-result capture.
- [x] Implement Markdown summary rendering with typed non-success states.
- [x] Prepare and locally validate pinned verification and release workflows.
- [x] Implement deterministic skill packaging and checksums.
- [x] Add release-manifest generation and tests.
- [x] Package extracted text separately from the compact skill, with an in-archive provenance manifest.
- [x] Publish comprehensive chronology research as standalone JSONL, JSON, and CSV assets with a source-bound manifest.
- [ ] Land workflows using a credential or human commit with workflow authority.
- [ ] Inspect the first hosted summary and preserve any resulting corrections.

---

## Validation

- [x] GPT 5.6 Sol at Perplexity Computer: Direct requirement is captured without reducing CI to pass/fail.
- [x] Local verification scripts validate and render all four result states.
- [x] Workflow YAML, immutable action pins, static contracts, and actionlint 1.7.12 validate locally.
- [x] Local release build deterministically produces fourteen primary assets, including a validated skill ZIP, a 13-document extracted-text ZIP, and three chronology-research formats.
- [ ] Hosted push/PR run produces a complete failure-resistant summary.
- [ ] Tagged release publishes a downloadable validated skill ZIP and checksums.

---

## Iterations

### Iteration 1 (2026-09-05)
- Trigger: Human made CI summary legibility and downloadable release packaging mandatory.
- Contributors: Jérémie Lumbroso; GPT 5.6 Sol at Perplexity Computer.
- Changes: Defined verification, summary, release, security, and authorization contracts.
- Outcome: Accepted.

### Iteration 2 (2026-09-05)
- Trigger: Structured verification runner and Markdown summary renderer implemented.
- Contributors: GPT 5.6 Sol at Perplexity Computer.
- Changes: `just verify` now emits JSON and a complete Markdown report, appends to `GITHUB_STEP_SUMMARY` when present, and distinguishes passed, failed, not implemented, and not applicable checks.
- Outcome: Accepted → Partially Implemented; workflows and release packaging remain.

### Iteration 3 (2026-09-05)
- Trigger: Skill, release bundle, and workflow candidates completed.
- Contributors: GPT 5.6 Sol at Perplexity Computer.
- Changes: Added deterministic skill and dataset release assets, SHA-256 manifests, immutable action pins, LFS checkout, always-on summary fallbacks, and GitHub Release publication. Both workflows pass YAML parsing, static tests, and actionlint 1.7.12.
- Outcome: Remains Partially Implemented; workflow files need an authorized landing commit and first hosted-run inspection.

### Iteration 4 (2026-09-05)
- Trigger: Policy-clean extracted text became a complete calibration-layer distribution.
- Contributors: GPT 5.6 Sol at Perplexity Computer.
- Changes: Added a deterministic `fmo-extracted-text-<version>.zip` release asset containing 13 full-text derivatives and an in-archive manifest that binds each text hash to its source byte identity. Kept the text archive separate so the skill remains compact and progressively loadable.
- Outcome: The local release contract is complete for current assets; hosted publication and inspection remain authorization-gated.

### Iteration 5 (2026-09-05)
- Trigger: All non-workflow release and verification work became complete while the token boundary remained.
- Contributors: GPT 5.6 Sol at Perplexity Computer.
- Changes: Added QST-WORKFLOW-LANDING with narrow-token, human-commit, and defer options.
- Outcome: Hosted CI and release publication await one explicit landing choice; local validation remains green.

### Iteration 6 (2026-09-05)
- Trigger: Comprehensive chronology became model-usable in the skill and needed equal treatment as a conventional data product.
- Contributors: GPT 5.6 Sol at Perplexity Computer.
- Changes: Added standalone JSONL, JSON, CSV, and manifest chronology assets to the deterministic release bundle, increasing the local release contract from ten to fourteen primary assets.
- Outcome: Every current canonical, research, skill, and extracted-text surface is locally packageable; hosted publication still awaits QST-WORKFLOW-LANDING.

---

## Links

- Related ADRs: `0001-portable-agent-instructions.md`, `0004-artifact-archive-and-prompt-provenance.md`, `0005-summonable-recurring-operations.md`, `0006-calibration-corpus-and-documentary-variation-stopping-rule.md`
- Related code: `.github/workflows/` candidates, `scripts/verify.py`, `scripts/package_release.py`, and release manifests
- Supersedes: none

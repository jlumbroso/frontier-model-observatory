# Frontier Model Observatory

A provenance-first, versioned observatory of frontier AI models, releases,
deployed systems, system and model cards, prompts, evaluations, and historical
evidence.

The project is designed for both humans and models. It gives persistent models
an external source of post-training chronology and terminology, helps
researchers inspect provider disclosures, and supports evidence-based
attribution of conversations whose model metadata is missing or impossible.

## Status

The repository is in its constitutional and calibration phase.

Completed:

- the project-wide collaboration and epistemic directives;
- portable `AGENTS.md` guidance;
- founding scope, representation, archival, and governance ADRs;
- parser-backed ORRCF question routing;
- a local verification gate and repository exclusion-policy checker;
- a primary-source disclosure-surface inventory and twelve-artifact calibration
  decision.
- fifteen versioned JSON Schemas, layered semantic validation, and structural
  fixtures covering every record and entity kind.
- all twelve minimum calibration subjects represented by 146 canonical records;
- 13 policy-clean provider sources and 13 linked, content-addressed text
  derivatives, totaling 93,562,059 materialized bytes;
- deterministic Markdown, JSON, JSONL, CSV, and SQLite projections;
- a validated 16-file progressive skill with deterministic ZIP, dataset assets,
  release manifests, and SHA-256 checksums.

In progress:

- evidence anchors, corrected evaluation claims, summaries, and three optional
  documentary-variation probes;
- authorized landing and hosted inspection of the prepared CI workflows;
- provider-wide chronology and artifact inventory beyond calibration.

Not yet claimed:

- comprehensive provider coverage;
- a stable public dataset release;
- a complete artifact archive;
- comprehensive production-grade skill coverage beyond the calibration snapshot.

## Theory of the Case

Models and products change faster than a persistent model's training can.
Release names, aliases, endpoint identifiers, system compositions, cards,
prompts, and availability windows become external historical facts.

Provider documentation is fragmented and organized around provider-specific
terms. A “system card,” “model card,” “technical report,” and “safety report”
may overlap without being interchangeable. A durable observatory must preserve
source-native meaning before it attempts normalization.

The unit of trust is therefore not a polished summary. It is an
evidence-bearing claim connected to an identified artifact, evidence location,
subject scope, attribution, and time.

## Principal Uses

- **Post-training orientation**: identify an unfamiliar model name and place it
  in its provider, family, and release chronology.
- **Historical availability**: determine which models and products existed on
  a particular date.
- **Conversation attribution**: rule model candidates in or out using release,
  product, endpoint, and feature evidence.
- **Card interpretation**: locate and interpret the companion artifacts for a
  release.
- **Disclosure comparison**: compare what providers disclosed without forcing
  unlike evaluations into false equivalence.
- **Artifact history**: detect moved, revised, replaced, or silently changed
  source documents.
- **Prompt-supported metacognition**: inspect appropriately sourced system
  prompts while preserving provenance and deployment scope.

## Architecture

The accepted architecture has five nearly decomposable layers:

1. **Entity registry**: organizations, model families, models, checkpoints,
   aliases, endpoints, products, and deployed systems.
2. **Event chronology**: announcements, previews, releases, updates, renames,
   deprecations, and retirements.
3. **Artifact archive**: cards, reports, announcements, documentation, prompts,
   snapshots, PDFs, and extracted text.
4. **Epistemic records**: atomic claims connected to evidence, scope,
   attribution, and bitemporal history.
5. **Applications and views**: timelines, dossiers, comparisons, attribution
   analysis, diffs, context packs, and the distributable skill.

Canonical data will be a bounded hybrid of entity, event, artifact, and claim
streams under versioned schemas. Markdown, JSON, JSONL, CSV, SQLite, and
path-oriented indexes will be generated projections rather than independent
editorial surfaces.

## Epistemic Invariants

The project does not collapse:

- model family, model, checkpoint, system, product, endpoint, or alias;
- provider assertion, evaluation result, independent verification, or
  observatory inference;
- “not reported,” “not found,” “not evaluated,” “withheld,” or “not
  applicable”;
- source-native terminology and normalized comparison categories;
- publication time, validity time, observation time, or repository commit
  time;
- provider-issued originals and observatory-generated preservation renderings.

Claims that cannot preserve these distinctions are not ready for canonical
ingestion.

## Repository Map

```text
AGENTS.md                 canonical project and collaboration guidance
docs/adr/                 architectural deliberation records
docs/inbox/               asynchronous participant coordination protocol
docs/vignettes/           metacognitive process stories
docs/EXCLUSION-POLICY.md  canonical repository-governance boundary
policy/                   machine-readable governance configuration
scripts/                  inspectable operational tools
tests/                    behavioral and regression tests
justfile                  summonable project operations

data/                     canonical type-homogeneous JSONL records
schemas/                  versioned JSON Schema 2020-12 package
artifacts/                content-addressed originals and extracted text
views/                    generated path-oriented projections
dist/                     generated JSON, JSONL, CSV, and SQLite distributions
frontier-model-observatory/
                           validated progressive skill
```

## Collaboration

The Prime Directive is: **commit discussions to ADRs immediately**. The
Secondary Directive is: **surface doubts; the human considers your doubts to
be generative**.

Complex questions use ORRCF:

- Options
- Recommendation
- Rationale
- Confidence
- Falsifier

Each handled question retains an attributed human answer. Decisions, question
status, and participant identity remain parseable across Git, editor, mobile,
and model interfaces.

Start with:

```bash
just --list
just unanswered
just verify-complete
just check-extracted-text
```

When a code or shell operation is executed more than once, it should graduate
into a documented `justfile` recipe. Substantial logic remains in tested
scripts or source modules.

## Founding Decisions

- [ADR-0001](docs/adr/0001-portable-agent-instructions.md): portable agent
  instructions.
- [ADR-0002](docs/adr/0002-observatory-scope-and-layered-architecture.md):
  comprehensive provider scope, layered architecture, and repository
  governance.
- [ADR-0003](docs/adr/0003-epistemic-records-and-generated-views.md):
  bounded hybrid records and bitemporal history.
- [ADR-0004](docs/adr/0004-artifact-archive-and-prompt-provenance.md): tiered
  preservation, evidence-gated redistribution, and prompt quarantine.
- [ADR-0005](docs/adr/0005-summonable-recurring-operations.md): recurring
  operations as named recipes.
- [ADR-0006](docs/adr/0006-calibration-corpus-and-documentary-variation-stopping-rule.md):
  twelve-artifact calibration and documentary-variation stopping rule.

## License and Artifact Rights

Repository tooling currently retains the inherited [MIT License](LICENSE).
Provider artifacts, extracted text, summaries, datasets, and the future skill
may require separate rights records or licensing decisions.

Public accessibility is not treated as proof of unrestricted redistribution.
The private research archive may preserve retrievable evidence, while public
distribution remains evidence-gated per artifact.

The canonical repository also follows an ethical
[exclusion policy](docs/EXCLUSION-POLICY.md). Downstream forks are requested
to preserve it; that request is not represented as a restriction in the MIT
License.

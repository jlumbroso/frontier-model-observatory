# Frontier Model Observatory: first evidence-schema package

> **Research status**: This is the schema-design review preserved as evidence,
> not the final canonical specification. Implementation adds a required,
> human-readable `canonical_key` beside each opaque typed identifier so models
> retain grep-friendly handles without using mutable names as foreign keys.

## Recommendation in one sentence

Implement a versioned JSON Schema 2020-12 package with one common envelope, one discriminated entity schema, and separate schemas for events, artifacts, artifact versions, byte objects, URL locators, redirect observations, artifact parts, artifact relationships, claims, retrieval events, typed absences, and coverage-ledger entries; keep canonical records in type-homogeneous JSONL streams and enforce cross-record, temporal, byte-integrity, evidence-location, policy, and projection invariants outside JSON Schema.

This is a design recommendation only. No repository file was modified.

## 1. Package and physical layout

Recommended first package:

```text
schemas/1.0.0/
  common.schema.json
  entity.schema.json
  event.schema.json
  artifact.schema.json
  artifact-version.schema.json
  byte-object.schema.json
  url-alias.schema.json
  redirect-observation.schema.json
  artifact-part.schema.json
  artifact-relationship.schema.json
  claim.schema.json
  retrieval-event.schema.json
  absence.schema.json
  coverage-ledger-entry.schema.json
  record.schema.json
data/
  entities.jsonl
  events.jsonl
  artifacts.jsonl
  artifact-versions.jsonl
  byte-objects.jsonl
  url-aliases.jsonl
  redirect-observations.jsonl
  artifact-parts.jsonl
  artifact-relationships.jsonl
  claims.jsonl
  retrieval-events.jsonl
  absences.jsonl
  coverage-ledger.jsonl
```

`record.schema.json` is a convenience union for tools that validate a mixed record, not a recommendation to create a mixed canonical stream. Each JSONL file is UTF-8, one complete object per line, LF-terminated, with no comments or blank lines. Canonical writers sort by `id`; consumers must not infer meaning from line order.

Every schema uses:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://frontier-model-observatory.example/schemas/1.0.0/entity.schema.json",
  "unevaluatedProperties": false
}
```

The eventual public `$id` host can change before implementation. What matters now is that every `$id` is absolute, immutable for a released schema, and versioned in its path.

## 2. Common definitions

### 2.1 Record envelope

All canonical records require:

- `schema_version`: constant `"1.0.0"`.
- `record_type`: closed enum matching the stream.
- `id`: globally unique typed identifier.
- `recorded_at`: RFC 3339 instant when the record was first committed to the canonical dataset.
- `record_status`: `active`, `superseded`, or `withdrawn`.

All permit:

- `updated_at`: RFC 3339 instant, required after a descriptive in-place correction.
- `superseded_by_ids`: record IDs of the same record family.
- `notes`: observatory editorial note; never a substitute for a claim.
- `extensions`: object whose keys match reverse-DNS names, for example `org.example.field`; values are unrestricted JSON. No other unknown properties are allowed.

Do not use `recorded_at` as domain time or evidence-observation time. Git commit time is a third audit layer and is not serialized as a substitute for either.

### 2.2 Stable identifiers

Use opaque, typed UUIDv7 identifiers minted once and never recomputed from mutable names:

```text
fmo:org:<uuid>
fmo:family:<uuid>
fmo:model:<uuid>
fmo:checkpoint:<uuid>
fmo:configuration:<uuid>
fmo:product:<uuid>
fmo:deployment:<uuid>
fmo:endpoint:<uuid>
fmo:alias:<uuid>
fmo:event:<uuid>
fmo:artifact:<uuid>
fmo:artifact-version:<uuid>
fmo:url:<uuid>
fmo:redirect:<uuid>
fmo:part:<uuid>
fmo:artifact-relationship:<uuid>
fmo:claim:<uuid>
fmo:retrieval:<uuid>
fmo:absence:<uuid>
fmo:coverage:<uuid>
```

Byte objects are the exception: `fmo:sha256:<64 lowercase hex characters>`. Their identity is their bytes.

Why UUIDv7 rather than slugs or deterministic name hashes: titles, provider terms, model names, ownership, and even artifact boundaries can be corrected. Opaque IDs keep those corrections from rewriting every foreign key. A duplicate-detection index may use normalized natural keys, but those keys must not become identity.

The UUID choice is reversible before data lands. If a library lacks UUIDv7, UUIDv4 is an acceptable temporary generator with the same external syntax. Do not mix content-derived entity IDs with minted IDs.

### 2.3 Source-native plus normalized values

Use a reusable `VocabularyValue`:

```json
{
  "native": "Update to GPT-5 System Card",
  "normalized": "update",
  "vocabulary": "fmo:artifact-class:1",
  "language": "en"
}
```

- `native` is always required when a provider supplied a term.
- `normalized` is required when the observatory maps the value to a controlled vocabulary.
- Every controlled enum includes `other`; when `normalized` is `other`, `native` is required.
- `language` is optional BCP 47.
- Do not overwrite native capitalization or punctuation.

For names, use:

```json
{
  "value": "Gemini 3 Pro",
  "name_type": "provider_preferred",
  "language": "en",
  "valid_time": { "...": "..." }
}
```

### 2.4 Time types

Use two axes everywhere they are meaningful:

1. `valid_time`: when the assertion, event, deployment, alias, or relationship applies in the world.
2. `observed_time`: when the observatory encountered the evidence.

`TimeValue`:

- required `value`: lexical value matching its precision:
  - `instant`: RFC 3339 date-time;
  - `day`: `YYYY-MM-DD`;
  - `month`: `YYYY-MM`;
  - `year`: `YYYY`.
- required `precision`: `instant`, `day`, `month`, or `year`.
- optional `raw`: source-native rendering such as `"Jul 08, 2026"`.
- optional `qualifier`: `exact`, `approximate`, `before`, `after`, `uncertain`; default `exact`.
- optional `basis`: `artifact_body`, `artifact_cover`, `artifact_metadata`, `index_surface`, `transport_header`, `retrieval`, `observatory_inference`, or `other`.
- optional `evidence_locator`.

`TemporalExtent`:

- required `status`: `known`, `unknown`, or `open`.
- optional `start`, `end`: `TimeValue`.
- if `known`, at least one endpoint is required.
- if `unknown`, neither endpoint is allowed and `reason` is required.
- if `open`, `start` is required and `end` is forbidden.

`ObservationExtent` requires `first_observed` and permits `last_observed`, both `TimeValue`. Retrieval events additionally require one `retrieved_at`; the importer may use day precision for historical research notes that did not retain an instant, but all new automated retrievals must use `instant`.

Never place publication, update, index, and HTTP `last-modified` values in one overloaded date field. Artifact versions hold a `date_assertions` array whose members each have `date_role`: `published`, `revised`, `index_listed`, `cover_date`, `effective`, `transport_last_modified`, `platform_last_updated`, or `other`.

### 2.5 References and evidence locators

All foreign keys are strings with typed-prefix patterns. No canonical record embeds another canonical record.

An `EvidenceLocator` requires:

- `artifact_version_id`.
- at least one of `artifact_part_id`, `page`, `page_range`, `section`, `table`, `anchor`, `json_pointer`, `text_quote`, or `url_alias_id`.

Optional:

- `byte_object_id` when the location is byte-version-specific.
- `text_quote` with exact source text.
- `quote_prefix` and `quote_suffix` for robust re-anchoring.
- `selector_native` for a provider-native anchor.
- `extraction_method`.

Page numbers are source-visible PDF page numbers by default. If physical PDF indexes differ, use `{ "scheme": "printed" | "pdf_index" | "other", "start": n, "end": n }`.

## 3. Record families

### 3.1 Organizations/providers and all named subject entities

**Schema/stream:** `entity.schema.json` / `entities.jsonl`.

These concepts share one schema because they participate in the same identity registry, names, ownership, temporal aliases, and provenance mechanics. Use `kind` as the discriminator:

`organization`, `model_family`, `model`, `checkpoint`, `configuration`, `product`, `deployment`, `endpoint`, `alias`.

“Provider” is an organization role, not a separate identity kind. An organization requires `roles`, with normalized values `provider`, `publisher`, `developer`, `evaluator`, `platform_operator`, `rights_holder`, or `other`, plus native role text where available.

Common required fields:

- envelope;
- `kind`;
- `names` with at least one name;
- `preferred_name`;
- `observed_time`.

Common optional fields:

- `description`;
- `owner_org_ids`;
- `developer_org_ids`;
- `publisher_org_ids`;
- `valid_time`;
- `modalities`: array of `{native, normalized}` where normalized is `text`, `image`, `audio`, `video`, `robotics`, `embedding`, `moderation`, `music`, `tool_use`, or `other`;
- `source_claim_ids`;
- `external_identifiers`;
- `lifecycle`: `announced`, `preview`, `available`, `deprecated`, `retired`, `unknown`;
- `extensions`.

Kind-specific requirements:

| Kind | Required | Optional and invariant-bearing |
|---|---|---|
| `organization` | `roles` | `parent_org_id`; parent graph must be acyclic |
| `model_family` | `provider_org_id` | `parent_family_id`; `modality_profile` |
| `model` | `provider_org_id`, `family_id` | `based_on_model_ids`; one provider unless evidence supports joint provision |
| `checkpoint` | `model_id`, `stage` | provider identifier, release label, immutable-build assertion; `stage` is `experimental`, `preview`, `general_availability`, `snapshot`, or `other` |
| `configuration` | `configures_id`, `configuration_class` | access tier, safeguard regime, tuning; class is `safeguard`, `tuning`, `size`, `mode`, `input_modality`, `account_tier`, `experiment_cohort`, or `other` |
| `product` | `provider_org_id` | surfaces and product family |
| `deployment` | `product_id`, at least one of `model_id`, `checkpoint_id`, `configuration_ids` | availability interval, locale, account tier, cohort; do not equate deployment with model |
| `endpoint` | `provider_org_id`, `endpoint_class` | `product_id`, exposed model/checkpoint IDs, protocol, base URL alias; class is `api`, `web`, `mobile`, `desktop`, `repository`, or `other` |
| `alias` | `alias_value`, `alias_type`, exactly one `target_id` | valid time and scope; type is `provider_model_id`, `marketing_name`, `former_name`, `product_label`, `endpoint_model_id`, or `other` |

An alias must resolve directly to a non-alias entity. Family/model/checkpoint containment is acyclic. A checkpoint cannot belong directly to a family. A deployment cannot claim a checkpoint that belongs to a different model than its `model_id`.

Calibration examples: Anthropic is an `organization` with provider/publisher roles; Gemini 3 Pro is a `model`; the OpenAI o1 preview and general-availability stages exercise `checkpoint.stage`; Claude Fable 5.1 and Claude Mythos 5.1 exercise named `configuration` records; claude.ai is a `product`; its Claude Opus 5 use is a `deployment`; Claude API and Gemini API exercise `endpoint`; `claude-3-5-sonnet-20241022` exercises a provider model-ID `alias`.

### 3.2 Events

**Schema/stream:** `event.schema.json` / `events.jsonl`.

Required:

- envelope;
- `event_kind`;
- `title`;
- `subject_ids` (one or more entity/artifact/version IDs);
- `valid_time`;
- `observed_time`;
- `evidence` (one or more locators);
- `attributed_to_org_ids`.

Optional:

- `event_kind_native`;
- `description`;
- `related_event_ids`;
- `supersedes_event_ids`;
- `resulting_state`;
- `source_claim_ids`.

Observed/required chronology vocabulary: `announcement`, `preview`, `release`, `general_availability`, `publication`, `update`, `correction`, `rename`, `deprecation`, `retirement`, `withdrawal`, `move`, `supersession`, `other`. Some values come from accepted chronology requirements even if the twelve subjects do not instantiate every one.

For an event, `valid_time` is when the event occurred or took effect; `observed_time` is when the evidence was encountered. An artifact publication event dated by a month remains month-precision. Do not synthesize a day.

Example: the GPT-Live added appendix records a correction dated August 4, 2026; the correction event points to both affected evaluation claim IDs and the artifact version containing the appendix.

### 3.3 Artifacts

**Schema/stream:** `artifact.schema.json` / `artifacts.jsonl`.

An artifact is the enduring intellectual/documentary work, independent of revisions, representations, URLs, and bytes.

Required:

- envelope;
- `preferred_title`;
- `publisher_org_ids`;
- `artifact_class`;
- `native_artifact_type`;
- `subject_refs`;
- `observed_time`.

Optional:

- `alternative_titles`;
- `scope_temporality`: `retrospective`, `current`, `prospective`, `mixed`, `unclear`;
- `prospective_scope_native`;
- `language`;
- `officiality`: `provider_published`, `provider_documentation`, `authorized_export`, `research_publication`, `observed`, `reconstructed`, `alleged`, `unknown`;
- `corpus_partition`: `main` or `quarantine`;
- `redistribution_status`: `permitted`, `restricted`, `review_required`, `metadata_only`, `unknown`;
- `redistribution_evidence_claim_ids`;
- `current_version_ids`.

Normalized artifact classes justified by the report:

`model_disclosure`, `system_prompt`, `behavior_specification`, `technical_report`, `risk_report`, `governance_policy`, `legal_terms`, `evaluation_methodology`, `index`, `release_post`, `other`.

Do not make “model card” and “system card” separate normalized classes in v1. Both map to `model_disclosure`, while `native_artifact_type` preserves the provider’s exact term and intent. Addendum/update status belongs primarily in typed relationships, not in the class.

Subject references use `{subject_id, scope_role, scope_native}`. `scope_role` is `primary`, `configuration`, `checkpoint`, `product`, `deployment`, `prospective_family`, or `other`.

Examples: Sora 2 System Card is a `model_disclosure`; Claude Opus 5 system prompts are `system_prompt`; Gemma 4 terms are `legal_terms`; the Gemini Robotics 1.5 technical report is `technical_report`, with its card represented as a part.

### 3.4 Artifact versions

**Schema/stream:** `artifact-version.schema.json` / `artifact-versions.jsonl`.

Required:

- envelope;
- `artifact_id`;
- `version_ordinal` (positive integer scoped to artifact);
- `title_native`;
- `representation_kinds`;
- `date_assertions` (may be empty only with `dates_unreported_reason`);
- `observed_time`;
- `lifecycle`: `current`, `superseded`, `withdrawn`, or `unclear`.

Optional:

- `version_label_native`;
- `revision_notes_native`;
- `changelog_entries`: each with source-native text, date assertion, and locator;
- `subject_refs_override` when version scope differs from artifact scope;
- `byte_object_ids`;
- `url_alias_ids`;
- `supersedes_version_ids`;
- `superseded_by_version_ids`;
- `extracted_text_byte_id`;
- `generated_representation_byte_ids`;
- `page_count`;
- `transport_metadata`;
- `content_equivalence_status`: `identical`, `editorially_equivalent`, `different`, `unknown`.

`representation_kinds`: `pdf`, `html`, `markdown`, `plain_text`, `repository_file`, `document_part`, or `other`.

Uniqueness: `(artifact_id, version_ordinal)` is unique. A byte object can back more than one URL and representation observation, but a provider-issued byte and an observatory-generated rendering cannot occupy the same semantic field.

Examples: Claude 4 System Card has two artifact versions with distinct byte objects and the same title. The three OpenAI o1 documents are initially represented as three versions of one artifact, with version-specific preview/GA scope and an explicit pointer relationship. This follows the calibration report and is reversible: if later evidence establishes distinct works, split the artifact and retain a `same_series_as` relationship.

### 3.5 Byte objects

**Schema/stream:** `byte-object.schema.json` / `byte-objects.jsonl`.

Required:

- envelope except that `id` is the SHA-256 content ID;
- `sha256`;
- `byte_length`;
- `media_type_detected`;
- `storage`;
- `observed_time`.

Optional:

- `media_type_declared`;
- `file_extension`;
- `content_disposition_filename`;
- `etag_values`;
- `first_retrieval_event_id`;
- `storage` fields `backend`, `locator`, `availability`;
- `derivation`: `provider_original`, `captured_html`, `extracted_text`, `observatory_rendering`, `summary`, or `other`;
- `derived_from_byte_ids`.

`storage.backend`: `git`, `git_lfs`, `object_store`, `external_only`, or `none`. `availability`: `materialized`, `pointer_only`, `remote_only`, `missing`, or `quarantined`.

Invariants: recomputed SHA-256 and byte count must match; detected type must be checked from bytes; derived byte objects must point to their inputs; provider originals and generated renderings must be distinguishable.

Example: the two live Claude 4 PDFs must produce two byte-object records if their hashes differ, even though their `content-disposition` filenames are the same.

### 3.6 URL aliases

**Schema/stream:** `url-alias.schema.json` / `url-aliases.jsonl`.

A URL alias is a durable locator identity, not an assertion that the URL currently resolves.

Required:

- envelope;
- `url`;
- `url_normalized`;
- `url_role`;
- at least one `target_ref`;
- `observed_time`.

Optional:

- `host_org_id`;
- `valid_time`;
- `fragment`;
- `is_provider_controlled`;
- `canonicality`: `provider_declared`, `observatory_preferred`, `alias`, `unknown`;
- `lifecycle`: `active`, `redirecting`, `broken`, `moved`, `unknown`.

Roles: `canonical`, `vanity`, `landing`, `asset`, `download`, `index`, `snapshot`, `mirror`, `part_locator`, `download_candidate`, or `other`.

Normalization must preserve scheme, authority, path case, query, and fragment in `url`; `url_normalized` may lowercase scheme/host, remove a default port, and normalize percent encoding, but may not remove query parameters or fragments without evidence that they are irrelevant. Exact URL uniqueness is on `url`.

Example: the Gemini 3 Pro model-card path is a vanity/landing URL targeting its artifact, while the storage URL is an asset URL targeting an artifact version.

### 3.7 Redirect observations

**Schema/stream:** `redirect-observation.schema.json` / `redirect-observations.jsonl`.

Required:

- envelope;
- `retrieval_event_id`;
- `hop_index` (zero-based);
- `from_url_id`;
- `to_url_id`;
- `mechanism`;
- `observed_time`.

Optional:

- `status_code`;
- `location_native`;
- `cache_status`;
- `response_headers`;
- `is_terminal`.

Mechanisms: `http`, `meta_refresh`, `javascript`, or `other`. HTTP status, when present, is constrained to 300–399.

Uniqueness: `(retrieval_event_id, hop_index)`. The `from` URL of hop \(n+1\) must equal the `to` URL of hop \(n\). A redirect observation is immutable; a later change creates a new retrieval and new observations.

Examples: the Anthropic Opus 4.6 vanity route exercises an HTTP 307 chain to PDF; the Sora 2 apparent PDF route exercises a 302 back to HTML and must not be interpreted as downloadable PDF bytes.

### 3.8 Artifact parts

**Schema/stream:** `artifact-part.schema.json` / `artifact-parts.jsonl`.

Required:

- envelope;
- `artifact_version_id`;
- `part_kind`;
- `locator`;
- `title_native` or `label_native`;
- `observed_time`.

Optional:

- `parent_part_id`;
- `ordinal`;
- `subject_refs`;
- `byte_object_id`;
- `extracted_text_byte_id`;
- `artifact_class_override`;
- `native_artifact_type`.

Kinds: `page_range`, `section`, `subsection`, `table`, `appendix`, `anchor`, `passage`, `prompt_block`, or `other`.

Part locators must resolve within the parent version. Parent-part graphs are acyclic. If a part itself functions as a disclosure artifact, retain the report as the artifact and classify the part with `artifact_class_override`; do not fabricate a downloadable standalone card.

Example: Appendix A, Model Card, Table 2 at page 30 of the Gemini Robotics 1.5 report is an artifact part that covers Gemini Robotics 1.5 and Gemini Robotics-ER 1.5.

### 3.9 Typed artifact relationships

**Schema/stream:** `artifact-relationship.schema.json` / `artifact-relationships.jsonl`.

Required:

- envelope;
- `source_ref`;
- `target_ref`;
- `relationship_type`;
- `relationship_type_native`;
- `valid_time`;
- `observed_time`;
- `evidence`.

Optional:

- `scope`;
- `supersedes_relationship_ids`;
- `qualifier`;

`source_ref` and `target_ref` may identify an artifact, version, or part and carry `record_type` explicitly.

Types: `addendum_to`, `updates`, `supersedes`, `supersedes_with_pointer`, `companion_to`, `governed_by`, `depends_on`, `defers_to`, `part_of`, `duplicate_of`, `alternate_representation_of`, `derived_from`, `same_series_as`, `corrects`, or `other`.

An “addendum to an update” is represented compositionally: an `addendum_to` edge targets an artifact whose own edge `updates` another artifact. This avoids a combinatorial relationship enum while preserving the three-level GPT-5 → GPT-5.2 → GPT-5.2-Codex chain described in the report.

No self-edge is allowed. Symmetric edges (`companion_to`, `duplicate_of`, `alternate_representation_of`, `same_series_as`) are stored once with lexically ordered IDs; reverse edges are generated views. `supersedes` graphs are acyclic.

Examples: GPT-5.2 `updates` GPT-5 System Card; the Anthropic risk report is `companion_to` the relevant disclosure; a Google model card can `defers_to` a parent card for architecture or training-data claims.

### 3.10 Claims and evaluation claims

**Schema/stream:** `claim.schema.json` / `claims.jsonl`.

Use one schema and stream with discriminator `claim_kind`: `assertion` or `evaluation`. They share identity, bitemporality, evidence, attribution, epistemic status, lifecycle, and correction semantics. `if/then` requires the evaluation block only for `evaluation`.

All claims require:

- envelope;
- `claim_kind`;
- `subject_refs`;
- `predicate` as a vocabulary value;
- `object` as one of `{text, number, boolean, entity_ref, artifact_ref, quantity, list, structured}`;
- `statement_native`;
- `attribution`;
- `epistemic_status`;
- `lifecycle`;
- `valid_time`;
- `observed_time`;
- `evidence` with at least one locator.

Optional:

- `statement_normalized`;
- `scope_refs`;
- `qualifiers`;
- `confidence` for observatory inference only;
- `supersedes_claim_ids`;
- `superseded_by_claim_ids`;
- `disputes_claim_ids`;
- `derived_from_claim_ids`;
- `correction_reason_native`.

Attribution requires `actor_type`: `provider`, `publisher`, `evaluator`, `observatory`, or `other`, and an actor organization/person reference or native actor name.

Epistemic statuses are exactly those accepted in ADR-0003: `stated`, `measured`, `derived`, `inferred`, `disputed`, `unknown`. Lifecycle: `current`, `superseded`, `withdrawn`, `unclear`.

An evaluation claim additionally requires:

- `evaluated_subject_id`;
- `benchmark`: `{native, normalized?}`;
- `metric`: `{native, normalized?}`;
- `reported_value`: string preserving formatting;
- `normalized_value`: number/string/boolean when lossless;
- `evaluation_context`;
- `asserted_at`: `TimeValue`;
- `artifact_version_id`.

`evaluation_context` requires `harness_native` or an explicit `harness_unreported: true`, and permits `harness_normalized`, `configuration_refs`, `split_native`, `aggregation_native`, `sample_size`, `attempt_count`, `pass_k`, `unit_native`, and `unit_normalized`. Unit enum: `proportion`, `percent`, `score`, `seconds`, `tokens`, `count`, or `other`.

The application-level logical key for duplicate detection is:

```text
(evaluated_subject_id, benchmark.native, metric.native,
 canonicalized evaluation_context, artifact_version_id, asserted_at)
```

It is not the stable ID. Corrections are separate claims linked by `supersedes_claim_ids`; never mutate 0.97 into 0.95. At an as-of cutoff, the query layer chooses the latest non-superseded claim observed by that cutoff.

Examples: GPT-Live’s original and corrected illicit-behavior scores become two evaluation claims linked by supersession. Claude Opus 4.6 BrowseComp changes likewise remain separate claims. A provider statement that system-prompt updates do not apply to an API is an ordinary `assertion`, with provider wording and page locator preserved.

### 3.11 Retrieval events

**Schema/stream:** `retrieval-event.schema.json` / `retrieval-events.jsonl`.

Required:

- envelope;
- `requested_url_id`;
- `retrieved_at`;
- `method`;
- `agent`;
- `outcome`;
- `cache_status`.

Optional:

- `final_url_id`;
- `status_code`;
- `redirect_observation_ids`;
- `byte_object_id`;
- `response_headers`;
- `media_type_declared`;
- `error_class`;
- `error_native`;
- `duration_ms`;
- `retry_of_retrieval_id`;
- `artifact_version_candidate_id`.

Methods: `http_get`, `http_head`, `browser`, `managed_fetch`, `repository_checkout`, `local_parse`, or `other`. Outcomes: `success`, `redirected_success`, `not_modified`, `http_error`, `timeout`, `too_large`, `blocked`, `parse_error`, or `other`. Cache status: `live`, `cache_hit`, `cache_miss`, `bypassed`, or `unknown`.

Invariants: successful byte-bearing retrieval requires a byte ID; `status_code` agrees with outcome; redirect IDs form one ordered chain; final URL equals the last hop; cached and live captures are distinct events even when requested URL is identical.

Example: the report’s 2026-09-05 live-versus-cached divergence for the Model Spec requires separate retrieval events, separate hashes when content differs, and explicit cache statuses.

### 3.12 Typed absences

**Schema/stream:** `absence.schema.json` / `absences.jsonl`.

An absence is an evidence-bearing negative research result, not a null and not a coverage-plan status.

Required:

- envelope;
- `absence_type`;
- `target`: subject reference and/or source-native description;
- `expected_record_type` or `expected_artifact_class`;
- `search_scope`;
- `checked_at`;
- `observed_time`;
- `basis`;
- `lifecycle`;

Optional:

- `method_native`;
- `surfaces_checked_url_ids`;
- `retrieval_event_ids`;
- `evidence`;
- `next_check_at`;
- `supersedes_absence_ids`;
- `resolved_by_record_ids`;
- `confidence`.

Types:

`not_reported`, `not_found`, `not_evaluated`, `withheld`, `not_applicable`, `not_retrieved`, `not_fetched`, `not_resolved`, `unverified`, `confirmed_absent`, `not_yet_collected`, `excluded_by_policy`, or `other`.

Use `confirmed_absent` only when an authoritative source explicitly asserts absence or an exhaustive, defined universe makes absence provable. `not_found` requires a bounded search scope and normally a `next_check_at`. `not_applicable` requires source evidence when provider-scoped.

Examples: no official system prompt publication was found for two provider surfaces in the report; these are `not_found`, not `confirmed_absent`. The Sora 2 downloadable PDF is `not_found`/`not_retrievable_as_file` only if the native type is carried through `other`; the stronger positive observation is the redirect event back to HTML. Claude Opus 5 prompt applicability to the API is `not_applicable` with direct provider evidence.

### 3.13 Coverage-ledger entries

**Schema/stream:** `coverage-ledger-entry.schema.json` / `coverage-ledger.jsonl`.

Coverage records are operational assessments of intended scope. They reference evidence and absences but do not replace them.

Required:

- envelope;
- `scope_key`: immutable object containing provider/subject/surface and desired record class;
- `scope_description`;
- `coverage_status`;
- `assessed_at`;
- `observed_time`;
- `coverage_basis`;

Optional:

- `subject_refs`;
- `provider_org_id`;
- `surface_url_ids`;
- `desired_artifact_classes`;
- `covered_record_ids`;
- `absence_ids`;
- `expected_count`;
- `observed_count`;
- `completeness_note`;
- `next_action`;
- `next_review_at`;
- `blocked_by`;
- `supersedes_coverage_ids`.

Statuses: `covered`, `partially_covered`, `not_yet_collected`, `not_found`, `confirmed_absent`, `excluded_by_policy`, `out_of_scope`, `blocked`, or `unknown`.

If status is `covered`, at least one covered record is required and unresolved blocking absences are forbidden. `not_found` requires an absence reference. `confirmed_absent` requires a `confirmed_absent` reference. `excluded_by_policy` requires a policy citation but no subject corpus record. `expected_count` and `observed_count` are meaningful only when the assessed universe is explicitly bounded.

Example: a ledger entry for the twelve-artifact calibration slice can report 12 expected and 12 encoded only after all twelve fixture bundles validate; this does not imply complete provider coverage.

## 4. What shares a schema and what remains separate

Share:

1. All identity-registry subjects use `entity.schema.json` with `kind`; their common behavior is stronger than their differences, and conditional branches can enforce kind-specific fields.
2. Organizations and providers share `organization`; provider is a role.
3. Ordinary and evaluation claims share `claim.schema.json` and `claims.jsonl`; evaluation is a strict conditional subtype, preserving uniform bitemporal and epistemic query behavior.

Remain separate:

1. Artifact, artifact version, byte object, and URL alias have independent identities and change rates.
2. URL alias and redirect observation are separate: one is a durable locator; the other is a time-bound network observation.
3. Artifact parts are separate from artifacts because a section can be cited and scoped without pretending it is a standalone document.
4. Typed artifact relationships are first-class edges because they have their own evidence, valid time, native wording, and supersession.
5. Retrieval events are operational observations, not artifact versions.
6. Absences are epistemic records; coverage entries are operational scope assessments. Combining them would make “not looked yet” indistinguishable from “looked and not found.”
7. Events remain separate from claims. An event says something occurred; claims are the sourced assertions that support or contest it.

## 5. JSON Schema implementation details

Use `$defs` in `common.schema.json` for:

- `typedId`, with one regex per prefix;
- `vocabularyValue`;
- `timeValue`;
- `temporalExtent`;
- `observationExtent`;
- `recordEnvelope`;
- `typedRef`;
- `name`;
- `evidenceLocator`;
- `dateAssertion`;
- `subjectScope`;
- `attribution`.

Use `allOf` to combine the envelope and family body, `oneOf` for entity kinds and claim kinds, and `if/then` for conditional requirements. Put `unevaluatedProperties: false` only on each final schema to avoid false failures caused by composed subschemas.

Examples of machine-checkable conditionals:

- entity `kind=checkpoint` requires `model_id` and `stage`;
- entity `kind=alias` requires `target_id`, `alias_value`, and `alias_type`;
- claim `claim_kind=evaluation` requires `evaluation`;
- artifact `scope_temporality=prospective` requires `prospective_scope_native`;
- absence `absence_type=not_found` requires `search_scope` and `next_check_at` or a documented waiver;
- retrieval `outcome=success|redirected_success` plus body bytes requires `byte_object_id`;
- vocabulary `normalized=other` requires nonempty `native`.

JSON Schema cannot enforce global ID uniqueness, foreign-key existence/type, digest correctness, acyclicity, bitemporal as-of selection, URL-hop continuity across files, or quote resolution. Those belong in the semantic validator.

## 6. Validation beyond JSON Schema

Run these layers in order:

1. **Framing:** UTF-8, one object per line, no duplicate JSON keys, no blank lines, terminal LF.
2. **Schema:** Draft 2020-12 validation, exact schema version, no unknown properties outside `extensions`.
3. **Registry:** global ID uniqueness, prefix/type agreement, referential existence, and target-type constraints.
4. **Graph:** no family/model/part/alias/supersession cycles; direct alias resolution; symmetric relationship canonical ordering; deployment/checkpoint consistency.
5. **Temporal:** lexical value matches precision, interval ordering, observed time not after record creation except for imported historical records with explicit importer note, superseding records do not begin before the evidence that supports them, and as-of resolution returns one current claim unless disagreement is explicitly modeled.
6. **Content integrity:** recompute SHA-256, byte length, and media sniff; check storage locator; distinguish originals from generated representations.
7. **Retrieval integrity:** status/outcome consistency, redirect-hop continuity, final URL, cache status, and byte linkage.
8. **Evidence resolution:** artifact version and part exist; page/section/table is in range; exact quotes can be found in the referenced extraction or carry a documented extraction exception.
9. **Epistemic policy:** load-bearing normalized facts have claims or intrinsic artifact-version evidence; source-native terms remain present; `inferred` claims identify observatory attribution and confidence; corrected values are linked rather than overwritten.
10. **Archive/distribution policy:** quarantine cannot appear in ordinary views; public bundles include originals only when redistribution status permits; generated PDFs cannot be labeled provider originals.
11. **Coverage logic:** status agrees with referenced records/absences; `confirmed_absent` meets its stronger proof rule; scheduled rechecks are present for provisional negatives.
12. **Repository policy:** run the existing exclusion guard over canonical data, schemas, fixtures, generated views, and filenames.
13. **Projection reproducibility:** regenerate Markdown, JSON, CSV, SQLite, provider/year/family/type/as-of views; compare byte-for-byte; manifests record generator version, schema version, source revision, and coverage boundary.

These should become thin `justfile` recipes only after the underlying operation recurs, in keeping with ADR-0005.

## 7. Minimal behavioral test suite covering all twelve subjects

Use twelve evidence fixture bundles, not contrived unit objects. Each bundle contains only the smallest records needed to represent the observed documentary variation.

1. **Claude Opus 4.6 System Card**
   - Validate one artifact, at least one version, vanity and asset URLs, the 307 redirect chain, PDF byte object, and four dated changelog entries.
   - Assert that a transport `last-modified` value cannot overwrite printed/changelog dates.
   - Assert native “System Card” remains present beside normalized `model_disclosure`.

2. **Claude Fable 5.1 & Claude Mythos 5.1 System Card**
   - Validate two configuration entities scoped by one artifact.
   - Validate the companion risk-report edge.
   - Reject collapsing the two configurations into aliases of one another.

3. **Claude 4 System Card**
   - Validate one artifact, two model subjects, two versions, and two distinct byte objects under the same title/filename.
   - As-of queries before and after the later observation choose the appropriate known version without deleting the earlier live asset.

4. **Claude Opus 5 system prompts**
   - Validate `system_prompt` class, dated snapshot, product/deployment scope, and provider-stated API non-applicability.
   - Reject normalization as a behavior specification.
   - Ordinary views include the official prompt; quarantine rules are not invoked.

5. **OpenAI o1 system-card trio**
   - Validate one conceptual artifact with three versions, version-specific preview/GA subjects, three live URLs, and the pointer to the December document.
   - Reject deduplication solely by title.

6. **GPT-5.2 update**
   - Validate `updates` rather than `addendum_to`.
   - Add the GPT-5.2-Codex addendum and traverse the compositional three-level chain.
   - Preserve the native warning that comparison values may differ from launch publication.

7. **GPT-Live System Card**
   - Validate audio modality, HTML and PDF representations, and original/corrected evaluation claims.
   - An as-of query before the correction returns the original claim; after it, the corrected current claim; history returns both.

8. **Sora 2 System Card**
   - Validate HTML-only artifact version.
   - Record the apparent PDF URL and its redirect to HTML without creating a PDF byte object.
   - Reject treating HTTP success at the final HTML page as evidence of downloadable PDF bytes.

9. **Gemini 3 Pro Model Card**
   - Validate vanity alias → PDF, index date, printed release date, printed last-updated month, and transport date as distinct date assertions.
   - Validate declared dependent-family subject scope without converting every dependent into the same model.

10. **Veo 3 Model Card**
    - Validate retrospective publication, explicit update, later transport-only byte observation, and prospective “and subsequent versions” scope.
    - Reject inventing future model entities from prospective prose.

11. **Gemini Robotics 1.5 report appendix**
    - Validate the technical report as artifact, Appendix A/Table 2/page locator as artifact part, and two model subjects on the part.
    - Reject creating a standalone card byte object.

12. **Gemma 4 model card**
    - Validate HTML-only representation, open-weight family with size/tuning configurations, platform-level timestamp, and separate legal artifacts.
    - Validate legal-artifact version/supersession independently from model-card versioning.

Cross-fixture tests:

- Every source-native term survives a normalized export and round-trip import.
- The provider/year/family/artifact-type/as-of views regenerate deterministically.
- No third-party mirror becomes the provenance root.
- Every negative in the fixtures is typed; no `null` means “absent.”
- All 12 bundles pass the repository policy guard.
- The three optional subjects can be added as a variation-regression test: each must either fit without field overloading or produce a deliberate schema-evolution failure.

## 8. Example record fragments

These fragments use only facts in the calibration report; UUIDs are placeholders minted by the implementation.

Artifact and version:

```json
{
  "record_type": "artifact",
  "id": "fmo:artifact:<uuid>",
  "preferred_title": "Veo 3 Model Card",
  "artifact_class": "model_disclosure",
  "native_artifact_type": {"native": "Model card", "normalized": "model_disclosure"},
  "scope_temporality": "prospective",
  "prospective_scope_native": "covers Veo 3 and subsequent versions"
}
```

Date assertions on its version:

```json
[
  {
    "date_role": "published",
    "value": {"value": "2025-05-23", "precision": "day", "raw": "May 23, 2025", "basis": "artifact_body"}
  },
  {
    "date_role": "revised",
    "value": {"value": "2026-01-13", "precision": "day", "raw": "Jan 13, 2026", "basis": "artifact_body"}
  },
  {
    "date_role": "transport_last_modified",
    "value": {"value": "2026-03-26", "precision": "day", "basis": "transport_header"}
  }
]
```

Artifact part:

```json
{
  "record_type": "artifact_part",
  "id": "fmo:part:<uuid>",
  "artifact_version_id": "fmo:artifact-version:<uuid>",
  "part_kind": "appendix",
  "title_native": "Appendix A. Model Card",
  "locator": {
    "page_range": {"scheme": "pdf_index", "start": 30, "end": 30},
    "table": "Table 2"
  },
  "artifact_class_override": "model_disclosure"
}
```

Evaluation correction:

```json
{
  "record_type": "claim",
  "id": "fmo:claim:<new-uuid>",
  "claim_kind": "evaluation",
  "epistemic_status": "measured",
  "lifecycle": "current",
  "supersedes_claim_ids": ["fmo:claim:<old-uuid>"],
  "evaluation": {
    "benchmark": {"native": "illicit-behavior evaluation"},
    "reported_value": "0.95",
    "normalized_value": 0.95,
    "artifact_version_id": "fmo:artifact-version:<uuid>"
  }
}
```

Typed absence:

```json
{
  "record_type": "absence",
  "id": "fmo:absence:<uuid>",
  "absence_type": "not_found",
  "target": {"description_native": "officially published system prompt"},
  "expected_artifact_class": "system_prompt",
  "search_scope": {"description": "provider-controlled publication surfaces checked in the calibration session"},
  "checked_at": {"value": "2026-09-05", "precision": "day"},
  "lifecycle": "current"
}
```

## 9. Non-blocking doubts and reversible choices

No unresolved design choice blocks implementation.

Make these reversible v1 choices:

1. **o1 documentary identity:** follow the calibration report and use one artifact with three versions. Permit a future split connected by `same_series_as`.
2. **UUID flavor:** prefer UUIDv7; fall back to UUIDv4 without changing the public ID grammar.
3. **Artifact class granularity:** normalize model/system cards together as `model_disclosure`, preserving the exact native term. If queries later require stable subclasses, add a vocabulary version rather than rewriting native values.
4. **URL normalization:** retain exact URLs as identity-bearing data and treat normalized URLs only as duplicate candidates.
5. **Date uncertainty:** use precision-bearing values rather than synthetic dates.
6. **Evaluation vocabulary:** keep benchmark, metric, harness, and split as native-first vocabulary values in v1 rather than prematurely creating benchmark entities.

The only point worth revisiting after the twelve fixtures are encoded is whether artifact-version scope overrides occur often enough to deserve first-class scope records. That is a calibration question, not a blocker.

## 10. Acceptance criteria for the first implementation

The schema package is ready to stake when:

- all schemas validate against the official Draft 2020-12 meta-schema;
- all twelve evidence fixture bundles validate;
- every fixture passes semantic, temporal, graph, retrieval, byte, evidence-location, coverage, and repository-policy checks;
- the correction and as-of tests return the expected historical claims;
- the HTML-only and part-of-report fixtures do not fabricate missing bytes;
- generated provider/year/family/type/as-of projections are deterministic;
- source-native terms and date bases survive round-trip projection;
- optional calibration subjects require no field overloading;
- `just verify` includes meaningful behavioral checks for every implemented subsystem.

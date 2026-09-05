#!/usr/bin/env python3
"""Seed the five remaining ADR-0006 calibration subjects.

Inputs come from the reviewed cache produced by
`2026-09-05-fetch-remaining-calibration.py`. HTML captures are represented as
`captured_html`, not provider-issued originals. One HTML capture is hashed but
not materialized because the repository exclusion policy rejects its raw
contents.

Outcome:
    Successfully used on 2026-09-05. Added the final five ADR-0006 subjects,
    bringing the repository to 132 canonical records and 15 byte-object
    records. Fourteen objects totaling 91,525,566 bytes are materialized; one
    raw HTML capture remains remote-only under the repository policy. The full
    verification gate passed 31 tests plus schema, canonical, archive, and
    exclusion checks.
"""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.canonical_store import CanonicalStore


STAMP = "2026-09-05T07:40:00Z"
OBS_DATE = "2026-09-05"
CACHE = Path("/home/user/workspace/fmo-remaining-20260905")
store = CanonicalStore(ROOT, STAMP, OBS_DATE)
OBS = store.observed_time


def time_value(value: str, precision: str, basis: str) -> dict:
    return {"value": value, "precision": precision, "basis": basis}


def date(role: str, value: str, precision: str, basis: str, **extra) -> dict:
    return {
        "date_role": role,
        "value": time_value(value, precision, basis),
        **extra,
    }


def artifact_id(key: str) -> str:
    return store.id_for("artifacts.jsonl", key)


def version_id(key: str, ordinal: int) -> str:
    return store.id_for("artifact-versions.jsonl", f"{key}/v{ordinal}")


def add_artifact(
    *,
    key: str,
    title: str,
    publisher_id: str,
    artifact_class: str,
    native_type: str,
    subjects: list[tuple[str, str]],
    version_specs: list[dict],
    officiality: str,
    scope_temporality: str = "current",
    prospective_scope_native: str | None = None,
) -> tuple[str, list[dict]]:
    aid = artifact_id(key)
    version_ids = [
        version_id(key, index)
        for index in range(1, len(version_specs) + 1)
    ]
    artifact = store.envelope("artifact", aid, key)
    artifact.update(
        {
            "preferred_title": title,
            "publisher_org_ids": [publisher_id],
            "artifact_class": artifact_class,
            "native_artifact_type": {
                "native": native_type,
                "normalized": artifact_class,
            },
            "subject_refs": [
                {"subject_id": ident, "scope_role": role}
                for ident, role in subjects
            ],
            "observed_time": OBS,
            "scope_temporality": scope_temporality,
            "officiality": officiality,
            "corpus_partition": "main",
            "redistribution_status": "review_required",
            "current_version_ids": [version_ids[-1]],
        }
    )
    if prospective_scope_native:
        artifact["prospective_scope_native"] = prospective_scope_native
    store.add("artifacts.jsonl", artifact)

    results = []
    previous = None
    for ordinal, (vid, spec) in enumerate(
        zip(version_ids, version_specs), start=1
    ):
        materialize = spec.get("materialize", True)
        byte_id, _length, _digest = store.byte_object(
            CACHE / spec["cache_name"],
            media_type=spec["media_type"],
            derivation=spec["derivation"],
            materialize=materialize,
            materialized_name=spec["materialized_name"],
        )
        url_key = f"{key}/v{ordinal}/{spec['url_role']}"
        uid = store.id_for("url-aliases.jsonl", url_key)
        url_record = store.envelope("url_alias", uid, url_key)
        url_record.update(
            {
                "url": spec["url"],
                "url_normalized": spec["url"],
                "url_role": spec["url_role"],
                "target_refs": [
                    {"id": vid, "record_type": "artifact_version"}
                ],
                "observed_time": OBS,
                "host_org_id": publisher_id,
                "is_provider_controlled": True,
                "canonicality": "provider_declared",
                "lifecycle": "active",
            }
        )
        store.add("url-aliases.jsonl", url_record)

        version = store.envelope(
            "artifact_version", vid, f"{key}/v{ordinal}"
        )
        version.update(
            {
                "artifact_id": aid,
                "version_ordinal": ordinal,
                "title_native": spec.get("version_title", title),
                "representation_kinds": [spec["representation"]],
                "date_assertions": spec["dates"],
                "observed_time": OBS,
                "lifecycle": "current"
                if ordinal == len(version_specs)
                else "superseded",
                "byte_object_ids": [byte_id],
                "url_alias_ids": [uid],
            }
        )
        if spec.get("page_count"):
            version["page_count"] = spec["page_count"]
        if spec.get("version_label"):
            version["version_label_native"] = spec["version_label"]
        if previous:
            version["supersedes_version_ids"] = [previous]
        store.add("artifact-versions.jsonl", version)

        retrieval_key = f"{key}/v{ordinal}/retrieval/2026-09-05"
        rid = store.id_for("retrieval-events.jsonl", retrieval_key)
        retrieval = store.envelope(
            "retrieval_event", rid, retrieval_key
        )
        retrieval.update(
            {
                "requested_url_id": uid,
                "final_url_id": uid,
                "retrieved_at": time_value(
                    "2026-09-05", "day", "retrieval"
                ),
                "method": spec["retrieval_method"],
                "agent": "Frontier Model Observatory calibration retrieval",
                "outcome": "success",
                "cache_status": spec["cache_status"],
                "status_code": 200,
                "byte_object_id": byte_id,
            }
        )
        store.add("retrieval-events.jsonl", retrieval)
        results.append(
            {
                "artifact_id": aid,
                "version_id": vid,
                "url_id": uid,
                "byte_id": byte_id,
            }
        )
        previous = vid
    return aid, results


def coverage(
    key: str,
    provider_id: str,
    subject_ids: list[str],
    results: list[dict],
    next_action: str,
    absence_ids: list[str] | None = None,
) -> None:
    canonical_key = f"calibration/{key}"
    ident = store.id_for("coverage-ledger.jsonl", canonical_key)
    covered = []
    urls = []
    for result in results:
        covered.extend(
            [
                result["artifact_id"],
                result["version_id"],
                result["byte_id"],
            ]
        )
        urls.append(result["url_id"])
    record = store.envelope(
        "coverage_ledger_entry", ident, canonical_key
    )
    record.update(
        {
            "scope_key": canonical_key,
            "scope_description": f"ADR-0006 calibration coverage for {key}",
            "coverage_status": "partially_covered",
            "assessed_at": time_value(
                "2026-09-05", "day", "retrieval"
            ),
            "observed_time": OBS,
            "coverage_basis": "Identity, artifact, version, bytes or byte hash, URL, and retrieval are canonical; deep claims and extraction remain.",
            "subject_ids": subject_ids,
            "provider_org_id": provider_id,
            "surface_url_ids": urls,
            "desired_artifact_classes": [
                "model_disclosure",
                "system_prompt",
            ],
            "covered_record_ids": sorted(set(covered)),
            "next_action": next_action,
        }
    )
    if absence_ids:
        record["absence_ids"] = absence_ids
    store.add("coverage-ledger.jsonl", record)


def relationship(
    key: str,
    source_id: str,
    target_id: str,
    relation_type: str,
    native: str,
    evidence_version_id: str,
    quote: str,
) -> str:
    ident = store.id_for("artifact-relationships.jsonl", key)
    record = store.envelope(
        "artifact_relationship", ident, key
    )
    record.update(
        {
            "source_ref": {
                "id": source_id,
                "record_type": "artifact",
            },
            "target_ref": {
                "id": target_id,
                "record_type": "artifact",
            },
            "relationship_type": relation_type,
            "relationship_type_native": native,
            "valid_time": {
                "status": "known",
                "start": time_value(
                    "2025-12-11", "day", "artifact_cover"
                ),
            },
            "observed_time": OBS,
            "evidence": [
                {
                    "artifact_version_id": evidence_version_id,
                    "page": 1,
                    "text_quote": quote,
                }
            ],
        }
    )
    store.add("artifact-relationships.jsonl", record)
    return ident


# Existing providers and families.
anthropic = store.existing("entities.jsonl", "anthropic")["id"]
claude = store.existing(
    "entities.jsonl", "anthropic/claude-family"
)["id"]
openai = store.existing("entities.jsonl", "openai")["id"]
google = store.existing("entities.jsonl", "google-deepmind")["id"]


# Anthropic Claude 4: one artifact, two byte-distinct versions.
opus4 = store.entity(
    "model",
    "anthropic/claude-opus-4",
    "Claude Opus 4",
    provider_org_id=anthropic,
    family_id=claude,
    modalities=[
        {"native": "text", "normalized": "text"},
        {"native": "visual analysis", "normalized": "image"},
        {"native": "computer use", "normalized": "tool_use"},
    ],
)
sonnet4 = store.entity(
    "model",
    "anthropic/claude-sonnet-4",
    "Claude Sonnet 4",
    provider_org_id=anthropic,
    family_id=claude,
    modalities=[
        {"native": "text", "normalized": "text"},
        {"native": "visual analysis", "normalized": "image"},
        {"native": "computer use", "normalized": "tool_use"},
    ],
)
a3_id, a3 = add_artifact(
    key="anthropic/claude-4-system-card",
    title="Claude 4 System Card",
    publisher_id=anthropic,
    artifact_class="model_disclosure",
    native_type="System Card",
    subjects=[(opus4, "primary"), (sonnet4, "primary")],
    officiality="provider_published",
    version_specs=[
        {
            "cache_name": "anthropic-claude-4-system-card-earlier.pdf",
            "media_type": "application/pdf",
            "derivation": "provider_original",
            "materialized_name": "original.pdf",
            "representation": "pdf",
            "version_title": "Claude 4 System Card",
            "version_label": "May 2025 earlier bytes",
            "page_count": 120,
            "url": "https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47.pdf",
            "url_role": "asset",
            "retrieval_method": "http_get",
            "cache_status": "live",
            "dates": [
                date("cover_date", "2025-05", "month", "artifact_cover"),
                date(
                    "transport_last_modified",
                    "2025-05-22",
                    "day",
                    "transport_header",
                ),
            ],
        },
        {
            "cache_name": "anthropic-claude-4-system-card-current.pdf",
            "media_type": "application/pdf",
            "derivation": "provider_original",
            "materialized_name": "original.pdf",
            "representation": "pdf",
            "version_title": "Claude 4 System Card",
            "version_label": "July 2025 current bytes",
            "page_count": 123,
            "url": "https://www-cdn.anthropic.com/07b2a3f9902ee19fe39a36ca638e5ae987bc64dd.pdf",
            "url_role": "asset",
            "retrieval_method": "http_get",
            "cache_status": "live",
            "dates": [
                date("cover_date", "2025-05", "month", "artifact_cover"),
                date(
                    "transport_last_modified",
                    "2025-07-15",
                    "day",
                    "transport_header",
                ),
            ],
        },
    ],
)
coverage(
    "anthropic/claude-4",
    anthropic,
    [opus4, sonnet4],
    a3,
    "Diff the two live versions and extract changed claims.",
)


# Anthropic official system prompt.
opus5 = store.entity(
    "model",
    "anthropic/claude-opus-5",
    "Claude Opus 5",
    provider_org_id=anthropic,
    family_id=claude,
    modalities=[{"native": "text", "normalized": "text"}],
)
claude_ai = store.entity(
    "product",
    "anthropic/claude-ai",
    "claude.ai",
    provider_org_id=anthropic,
)
a5_id, a5 = add_artifact(
    key="anthropic/claude-opus-5-system-prompt",
    title="Claude Opus 5 system prompts",
    publisher_id=anthropic,
    artifact_class="system_prompt",
    native_type="system prompts",
    subjects=[(opus5, "primary"), (claude_ai, "product")],
    officiality="provider_documentation",
    version_specs=[
        {
            "cache_name": "anthropic-claude-opus-5-system-prompt.html",
            "media_type": "text/html",
            "derivation": "captured_html",
            "materialized_name": "capture.html",
            "representation": "html",
            "url": "https://platform.claude.com/docs/en/release-notes/system-prompts/claude-opus-5",
            "url_role": "canonical",
            "retrieval_method": "managed_fetch",
            "cache_status": "bypassed",
            "dates": [
                date(
                    "published",
                    "2026-07-24",
                    "day",
                    "artifact_body",
                )
            ],
        }
    ],
)
coverage(
    "anthropic/claude-opus-5-system-prompt",
    anthropic,
    [opus5, claude_ai],
    a5,
    "Extract the prompt block, product scope, API non-applicability, and model identifiers.",
)


# OpenAI GPT-5.2 update and its parent artifact identity.
gpt5_family = store.entity(
    "model_family",
    "openai/gpt-5-family",
    "GPT-5",
    provider_org_id=openai,
)
gpt52_instant = store.entity(
    "model",
    "openai/gpt-5-2-instant",
    "GPT-5.2 Instant",
    provider_org_id=openai,
    family_id=gpt5_family,
    modalities=[
        {"native": "text", "normalized": "text"},
        {"native": "image input", "normalized": "image"},
        {"native": "tool use", "normalized": "tool_use"},
    ],
)
gpt52_thinking = store.entity(
    "model",
    "openai/gpt-5-2-thinking",
    "GPT-5.2 Thinking",
    provider_org_id=openai,
    family_id=gpt5_family,
    modalities=[
        {"native": "text", "normalized": "text"},
        {"native": "image input", "normalized": "image"},
        {"native": "tool use", "normalized": "tool_use"},
    ],
)
parent_key = "openai/gpt-5-system-card"
parent_id = artifact_id(parent_key)
parent = store.envelope("artifact", parent_id, parent_key)
parent.update(
    {
        "preferred_title": "GPT-5 System Card",
        "publisher_org_ids": [openai],
        "artifact_class": "model_disclosure",
        "native_artifact_type": {
            "native": "System Card",
            "normalized": "model_disclosure",
        },
        "subject_refs": [
            {"subject_id": gpt5_family, "scope_role": "primary"}
        ],
        "observed_time": OBS,
        "officiality": "provider_published",
        "corpus_partition": "main",
        "redistribution_status": "review_required",
    }
)
store.add("artifacts.jsonl", parent)

o2_id, o2 = add_artifact(
    key="openai/gpt-5-2-system-card-update",
    title="Update to GPT-5 System Card: GPT-5.2",
    publisher_id=openai,
    artifact_class="model_disclosure",
    native_type="Update to GPT-5 System Card",
    subjects=[
        (gpt52_instant, "primary"),
        (gpt52_thinking, "primary"),
    ],
    officiality="provider_published",
    version_specs=[
        {
            "cache_name": "openai-gpt-5-2-system-card-update.pdf",
            "media_type": "application/pdf",
            "derivation": "provider_original",
            "materialized_name": "original.pdf",
            "representation": "pdf",
            "page_count": 27,
            "url": "https://cdn.openai.com/pdf/3a4153c8-c748-4b71-8e31-aecbde944f8d/oai_5_2_system-card.pdf",
            "url_role": "asset",
            "retrieval_method": "http_get",
            "cache_status": "live",
            "dates": [
                date(
                    "published",
                    "2025-12-11",
                    "day",
                    "artifact_cover",
                ),
                date(
                    "other",
                    "2025-12-11T16:46:24Z",
                    "instant",
                    "artifact_metadata",
                    date_role_native="PDF CreationDate and ModDate",
                ),
                date(
                    "transport_last_modified",
                    "2025-12-11",
                    "day",
                    "transport_header",
                ),
            ],
        }
    ],
)
rel_id = relationship(
    "openai/gpt-5-2-system-card-update/updates/gpt-5-system-card",
    o2_id,
    parent_id,
    "updates",
    "Update to GPT-5 System Card",
    o2[0]["version_id"],
    "Update to GPT-5 System Card: GPT-5.2",
)
o2[0]["relationship_id"] = rel_id
coverage(
    "openai/gpt-5-2",
    openai,
    [gpt52_instant, gpt52_thinking],
    o2,
    "Extract warning, update relation, model aliases, and preparedness claims.",
)


# OpenAI Sora 2 HTML-only card.
sora_family = store.entity(
    "model_family",
    "openai/sora-family",
    "Sora",
    provider_org_id=openai,
)
sora2 = store.entity(
    "model",
    "openai/sora-2",
    "Sora 2",
    provider_org_id=openai,
    family_id=sora_family,
    modalities=[
        {"native": "video generation", "normalized": "video"},
        {"native": "audio generation", "normalized": "audio"},
        {"native": "text prompts", "normalized": "text"},
        {"native": "image inputs", "normalized": "image"},
    ],
)
sora_product = store.entity(
    "product",
    "openai/sora-product",
    "Sora",
    provider_org_id=openai,
)
o4_id, o4 = add_artifact(
    key="openai/sora-2-system-card",
    title="Sora 2 System Card",
    publisher_id=openai,
    artifact_class="model_disclosure",
    native_type="System Card",
    subjects=[(sora2, "primary"), (sora_product, "product")],
    officiality="provider_published",
    version_specs=[
        {
            "cache_name": "openai-sora-2-system-card.html",
            "media_type": "text/html",
            "derivation": "captured_html",
            "materialized_name": "capture.html",
            "representation": "html",
            "url": "https://deploymentsafety.openai.com/sora-2",
            "url_role": "canonical",
            "retrieval_method": "managed_fetch",
            "cache_status": "bypassed",
            "dates": [
                date(
                    "other",
                    "2025-09-30",
                    "day",
                    "artifact_metadata",
                    date_role_native="managed fetch published_date",
                )
            ],
        }
    ],
)
coverage(
    "openai/sora-2",
    openai,
    [sora2, sora_product],
    o4,
    "Record the apparent PDF redirect and typed nonavailability without fabricating PDF bytes.",
)


# Google Gemma 4 HTML card. The captured bytes are intentionally remote-only.
gemma_family = store.entity(
    "model_family",
    "google-deepmind/gemma-family",
    "Gemma",
    provider_org_id=google,
)
gemma4 = store.entity(
    "model",
    "google-deepmind/gemma-4",
    "Gemma 4",
    provider_org_id=google,
    family_id=gemma_family,
    modalities=[
        {"native": "text", "normalized": "text"},
        {"native": "image input", "normalized": "image"},
        {"native": "audio input on selected sizes", "normalized": "audio"},
        {"native": "video through image frames", "normalized": "video"},
    ],
)
gemma_configs = []
for key, name, config_class in [
    ("e2b", "Gemma 4 E2B", "size"),
    ("e4b", "Gemma 4 E4B", "size"),
    ("12b", "Gemma 4 12B", "size"),
    ("26b-a4b", "Gemma 4 26B A4B", "size"),
    ("31b", "Gemma 4 31B", "size"),
    ("pretrained", "Gemma 4 pre-trained", "tuning"),
    ("instruction-tuned", "Gemma 4 instruction-tuned", "tuning"),
]:
    gemma_configs.append(
        store.entity(
            "configuration",
            f"google-deepmind/gemma-4/{key}",
            name,
            configures_id=gemma4,
            configuration_class=config_class,
        )
    )

g5_id, g5 = add_artifact(
    key="google-deepmind/gemma-4-model-card",
    title="Gemma 4 model card",
    publisher_id=google,
    artifact_class="model_disclosure",
    native_type="model card",
    subjects=[
        (gemma4, "primary"),
        *[(config_id, "configuration") for config_id in gemma_configs],
    ],
    officiality="provider_documentation",
    version_specs=[
        {
            "cache_name": "google-gemma-4-model-card.html",
            "media_type": "text/html",
            "derivation": "captured_html",
            "materialize": False,
            "materialized_name": "capture.html",
            "representation": "html",
            "url": "https://ai.google.dev/gemma/docs/core/model_card_4",
            "url_role": "canonical",
            "retrieval_method": "managed_fetch",
            "cache_status": "bypassed",
            "dates": [
                date(
                    "index_listed",
                    "2026-04-02",
                    "day",
                    "index_surface",
                ),
                date(
                    "platform_last_updated",
                    "2026-07-30",
                    "day",
                    "artifact_metadata",
                ),
            ],
        }
    ],
)
absence_key = "google-deepmind/gemma-4/raw-html-materialization/excluded-by-policy"
absence_id = store.id_for("absences.jsonl", absence_key)
absence = store.envelope("absence", absence_id, absence_key)
absence.update(
    {
        "absence_type": "excluded_by_policy",
        "target": {
            "subject_id": gemma4,
            "description_native": "raw HTML capture materialization",
        },
        "expected_record_type": "materialized_byte_object",
        "search_scope": {
            "description": "The fetched official HTML capture was checked against the canonical repository exclusion policy."
        },
        "checked_at": time_value("2026-09-05", "day", "retrieval"),
        "observed_time": OBS,
        "basis": "Raw provider-page bytes contain excluded subject matter; retain URL, retrieval, and hash records without committing the capture.",
        "lifecycle": "current",
    }
)
store.add("absences.jsonl", absence)
coverage(
    "google-deepmind/gemma-4",
    google,
    [gemma4, *gemma_configs],
    g5,
    "Extract allowed model-card claims from provider text without materializing prohibited raw bytes.",
    [absence_id],
)

initial = store.existing(
    "coverage-ledger.jsonl",
    "calibration/google-deepmind/gemini-robotics-1-5",
)
if initial:
    initial["next_action"] = (
        "Resolve exact quote anchors and re-run the variation matrix with the "
        "three optional calibration subjects."
    )

store.write()
print("seeded five remaining calibration subjects")

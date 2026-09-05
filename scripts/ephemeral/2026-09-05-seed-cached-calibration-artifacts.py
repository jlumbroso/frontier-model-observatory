#!/usr/bin/env python3
"""Seed evidence-grounded records for cached ADR-0006 calibration artifacts.

Context:
    The primary-source audit downloaded eight additional PDF byte objects into
    /home/user/workspace/fmo. Two have misleading `.html` cache suffixes despite
    PDF magic. This dated script promotes only checked report facts and locally
    verified byte metadata into canonical streams.

Safety:
    Idempotent by canonical_key (or byte digest). Existing records are never
    rewritten. New IDs are minted once. Every resulting stream is ID-sorted.

Outcome:
    Successfully used on 2026-09-05. Added six calibration subjects beyond
    the initial report-embedded-card bundle, producing 76 canonical records
    across 11 streams and 9 materialized byte objects totaling 78,980,122
    bytes. `just verify` passed 28 tests plus schema, canonical, archive, and
    exclusion checks. A failed first run exposed and corrected entity-key
    collisions and byte-object coverage references before commit.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.mint_id import mint


STAMP = "2026-09-05T07:30:00Z"
OBS = {
    "first_observed": {
        "value": "2026-09-05",
        "precision": "day",
        "basis": "retrieval",
    }
}
CACHE = Path("/home/user/workspace/fmo")
DATA = ROOT / "data"

STREAM_TYPES = {
    "entities.jsonl": "entity",
    "artifacts.jsonl": "artifact",
    "artifact-versions.jsonl": "artifact_version",
    "byte-objects.jsonl": "byte_object",
    "url-aliases.jsonl": "url_alias",
    "retrieval-events.jsonl": "retrieval_event",
    "coverage-ledger.jsonl": "coverage_ledger_entry",
}
PREFIX = {
    "entity": None,
    "artifact": "artifact",
    "artifact_version": "artifact-version",
    "url_alias": "url",
    "retrieval_event": "retrieval",
    "coverage_ledger_entry": "coverage",
}


def read_stream(name: str) -> list[dict]:
    path = DATA / name
    if not path.exists():
        return []
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


streams = {name: read_stream(name) for name in STREAM_TYPES}


def existing(name: str, key: str) -> dict | None:
    return next(
        (record for record in streams[name] if record.get("canonical_key") == key),
        None,
    )


def record_id(name: str, key: str, kind: str | None = None) -> str:
    found = existing(name, key)
    if found:
        return found["id"]
    prefix = kind or PREFIX[STREAM_TYPES[name]]
    if prefix is None:
        raise ValueError(f"entity kind required for {key}")
    return mint(prefix)


def envelope(record_type: str, ident: str, key: str) -> dict:
    return {
        "schema_version": "1.0.0",
        "record_type": record_type,
        "id": ident,
        "canonical_key": key,
        "recorded_at": STAMP,
        "record_status": "active",
    }


def add(name: str, record: dict) -> dict:
    key = record.get("canonical_key")
    found = existing(name, key) if key else next(
        (item for item in streams[name] if item["id"] == record["id"]), None
    )
    if found:
        return found
    streams[name].append(record)
    return record


def entity(kind: str, key: str, name: str, **fields) -> str:
    found = existing("entities.jsonl", key)
    if found and found.get("kind") != kind:
        raise ValueError(
            f"entity canonical_key {key!r} already belongs to "
            f"{found.get('kind')}, not {kind}"
        )
    ident = record_id("entities.jsonl", key, {
        "organization": "org",
        "model_family": "family",
        "model": "model",
        "checkpoint": "checkpoint",
        "configuration": "configuration",
    }[kind])
    record = envelope("entity", ident, key)
    record.update(
        {
            "kind": kind,
            "preferred_name": name,
            "names": [{"value": name, "name_type": "provider_preferred"}],
            "observed_time": OBS,
            **fields,
        }
    )
    add("entities.jsonl", record)
    return ident


def date(role: str, value: str, precision: str, basis: str, **extra) -> dict:
    return {
        "date_role": role,
        "value": {"value": value, "precision": precision, "basis": basis},
        **extra,
    }


def archive(cache_name: str) -> tuple[str, int, str]:
    source = CACHE / cache_name
    data = source.read_bytes()
    if not data.startswith(b"%PDF-"):
        raise ValueError(f"{source} is not a PDF despite calibration metadata")
    digest = hashlib.sha256(data).hexdigest()
    target = (
        ROOT
        / "artifacts"
        / "sha256"
        / digest[:2]
        / digest
        / "original.pdf"
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.read_bytes() != data:
        raise ValueError(f"content-address collision at {target}")
    if not target.exists():
        shutil.copyfile(source, target)

    ident = f"fmo:sha256:{digest}"
    add(
        "byte-objects.jsonl",
        {
            "schema_version": "1.0.0",
            "record_type": "byte_object",
            "id": ident,
            "recorded_at": STAMP,
            "record_status": "active",
            "sha256": digest,
            "byte_length": len(data),
            "media_type_detected": "application/pdf",
            "media_type_declared": "application/pdf",
            "storage": {
                "backend": "git_lfs",
                "availability": "materialized",
                "locator": str(target.relative_to(ROOT)),
            },
            "observed_time": OBS,
            "derivation": "provider_original",
        },
    )
    return ident, len(data), digest


def artifact_bundle(
    *,
    key: str,
    title: str,
    publisher_id: str,
    native_type: str,
    subjects: list[tuple[str, str]],
    cache_name: str,
    url: str,
    page_count: int,
    dates: list[dict],
    scope_temporality: str = "current",
    prospective_scope_native: str | None = None,
    version_label: str | None = None,
    version_ordinal: int = 1,
    lifecycle: str = "current",
    supersedes: list[str] | None = None,
    url_role: str = "asset",
    version_title: str | None = None,
) -> tuple[str, str, str, str]:
    artifact_id = record_id("artifacts.jsonl", key)
    version_key = f"{key}/v{version_ordinal}"
    version_id = record_id("artifact-versions.jsonl", version_key)
    url_key = f"{version_key}/pdf"
    url_id = record_id("url-aliases.jsonl", url_key)
    byte_id, _length, _digest = archive(cache_name)

    artifact = envelope("artifact", artifact_id, key)
    artifact.update(
        {
            "preferred_title": title,
            "publisher_org_ids": [publisher_id],
            "artifact_class": "model_disclosure",
            "native_artifact_type": {
                "native": native_type,
                "normalized": "model_disclosure",
            },
            "subject_refs": [
                {"subject_id": ident, "scope_role": role}
                for ident, role in subjects
            ],
            "observed_time": OBS,
            "scope_temporality": scope_temporality,
            "officiality": "provider_published",
            "corpus_partition": "main",
            "redistribution_status": "review_required",
            "current_version_ids": [version_id] if lifecycle == "current" else [],
        }
    )
    if prospective_scope_native:
        artifact["prospective_scope_native"] = prospective_scope_native
    found_artifact = existing("artifacts.jsonl", key)
    if found_artifact:
        known_subjects = {
            (item["subject_id"], item["scope_role"])
            for item in found_artifact["subject_refs"]
        }
        for item in artifact["subject_refs"]:
            marker = (item["subject_id"], item["scope_role"])
            if marker not in known_subjects:
                found_artifact["subject_refs"].append(item)
        if lifecycle == "current":
            versions = set(found_artifact.get("current_version_ids", []))
            versions.add(version_id)
            found_artifact["current_version_ids"] = sorted(versions)
    else:
        add("artifacts.jsonl", artifact)

    version = envelope("artifact_version", version_id, version_key)
    version.update(
        {
            "artifact_id": artifact_id,
            "version_ordinal": version_ordinal,
            "title_native": version_title or title,
            "representation_kinds": ["pdf"],
            "date_assertions": dates,
            "observed_time": OBS,
            "lifecycle": lifecycle,
            "byte_object_ids": [byte_id],
            "url_alias_ids": [url_id],
            "page_count": page_count,
        }
    )
    if version_label:
        version["version_label_native"] = version_label
    if supersedes:
        version["supersedes_version_ids"] = supersedes
    add("artifact-versions.jsonl", version)

    locator = envelope("url_alias", url_id, url_key)
    locator.update(
        {
            "url": url,
            "url_normalized": url,
            "url_role": url_role,
            "target_refs": [
                {"id": version_id, "record_type": "artifact_version"}
            ],
            "observed_time": OBS,
            "host_org_id": publisher_id,
            "is_provider_controlled": True,
            "canonicality": "provider_declared",
            "lifecycle": "active",
        }
    )
    add("url-aliases.jsonl", locator)

    retrieval_key = f"{key}/v{version_ordinal}/retrieval/2026-09-05"
    retrieval_id = record_id("retrieval-events.jsonl", retrieval_key)
    retrieval = envelope(
        "retrieval_event", retrieval_id, retrieval_key
    )
    retrieval.update(
        {
            "requested_url_id": url_id,
            "final_url_id": url_id,
            "retrieved_at": {
                "value": "2026-09-05",
                "precision": "day",
                "basis": "retrieval",
            },
            "method": "http_get",
            "agent": "Frontier Model Observatory calibration research session",
            "outcome": "success",
            "cache_status": "live",
            "status_code": 200,
            "byte_object_id": byte_id,
        }
    )
    add("retrieval-events.jsonl", retrieval)
    return artifact_id, version_id, url_id, byte_id


def coverage(
    key: str,
    provider_id: str,
    subject_ids: list[str],
    record_ids: list[str],
    url_ids: list[str],
    next_action: str,
) -> None:
    canonical_key = f"calibration/{key}"
    ident = record_id("coverage-ledger.jsonl", canonical_key)
    record = envelope("coverage_ledger_entry", ident, canonical_key)
    record.update(
        {
            "scope_key": canonical_key,
            "scope_description": f"ADR-0006 calibration coverage for {key}",
            "coverage_status": "partially_covered",
            "assessed_at": {
                "value": "2026-09-05",
                "precision": "day",
                "basis": "retrieval",
            },
            "observed_time": OBS,
            "coverage_basis": "Identity, artifact, version, provider-original bytes, URL, and retrieval are canonical; deep claims and extraction remain.",
            "subject_ids": subject_ids,
            "provider_org_id": provider_id,
            "surface_url_ids": url_ids,
            "desired_artifact_classes": ["model_disclosure"],
            "covered_record_ids": record_ids,
            "next_action": next_action,
        }
    )
    add("coverage-ledger.jsonl", record)


# Identity registry
anthropic = entity(
    "organization",
    "anthropic",
    "Anthropic",
    roles=["provider", "publisher"],
)
claude = entity(
    "model_family",
    "anthropic/claude-family",
    "Claude",
    provider_org_id=anthropic,
)
opus46 = entity(
    "model",
    "anthropic/claude-opus-4-6",
    "Claude Opus 4.6",
    provider_org_id=anthropic,
    family_id=claude,
    modalities=[
        {"native": "text", "normalized": "text"},
        {"native": "image input", "normalized": "image"},
    ],
)
fable51 = entity(
    "configuration",
    "anthropic/claude-fable-5-1",
    "Claude Fable 5.1",
    configures_id=claude,
    configuration_class="safeguard",
)
mythos51 = entity(
    "configuration",
    "anthropic/claude-mythos-5-1",
    "Claude Mythos 5.1",
    configures_id=claude,
    configuration_class="safeguard",
)

openai = entity(
    "organization",
    "openai",
    "OpenAI",
    roles=["provider", "publisher"],
)
o1_family = entity(
    "model_family", "openai/o1-family", "OpenAI o1", provider_org_id=openai
)
o1 = entity(
    "model",
    "openai/o1",
    "OpenAI o1",
    provider_org_id=openai,
    family_id=o1_family,
    modalities=[{"native": "text", "normalized": "text"}],
)
o1_preview = entity(
    "checkpoint",
    "openai/o1/preview",
    "OpenAI o1 preview",
    model_id=o1,
    stage="preview",
)
o1_ga = entity(
    "checkpoint",
    "openai/o1/general-availability",
    "OpenAI o1 general availability",
    model_id=o1,
    stage="general_availability",
)
gpt_live_family = entity(
    "model_family",
    "openai/gpt-live-family",
    "GPT-Live",
    provider_org_id=openai,
)
gpt_live = entity(
    "model",
    "openai/gpt-live-1",
    "GPT-Live-1",
    provider_org_id=openai,
    family_id=gpt_live_family,
    modalities=[{"native": "audio/voice", "normalized": "audio"}],
)
gpt_live_mini = entity(
    "model",
    "openai/gpt-live-1-mini",
    "GPT-Live-1 mini",
    provider_org_id=openai,
    family_id=gpt_live_family,
    modalities=[{"native": "audio/voice", "normalized": "audio"}],
)

google = existing("entities.jsonl", "google-deepmind")["id"]
gemini = entity(
    "model_family",
    "google-deepmind/gemini-family",
    "Gemini",
    provider_org_id=google,
)
gemini3 = entity(
    "model",
    "google-deepmind/gemini-3-pro",
    "Gemini 3 Pro",
    provider_org_id=google,
    family_id=gemini,
    modalities=[
        {"native": "text", "normalized": "text"},
        {"native": "image", "normalized": "image"},
        {"native": "audio", "normalized": "audio"},
        {"native": "video", "normalized": "video"},
    ],
)
veo_family = entity(
    "model_family",
    "google-deepmind/veo-family",
    "Veo",
    provider_org_id=google,
)
veo3 = entity(
    "model",
    "google-deepmind/veo-3",
    "Veo 3",
    provider_org_id=google,
    family_id=veo_family,
    modalities=[
        {"native": "text and image input", "normalized": "text"},
        {"native": "video with audio output", "normalized": "video"},
        {"native": "video with audio output", "normalized": "audio"},
    ],
)


# Anthropic cached cards
a1 = artifact_bundle(
    key="anthropic/claude-opus-4-6-system-card",
    title="Claude Opus 4.6 System Card",
    publisher_id=anthropic,
    native_type="System Card",
    subjects=[(opus46, "primary")],
    cache_name="claude-opus-4-6-system-card.html",
    url="https://anthropic.com/claude-opus-4-6-system-card",
    page_count=213,
    url_role="vanity",
    version_title="Claude Opus 4.6 System Card - Google Docs",
    dates=[
        date("index_listed", "2026-02", "month", "index_surface"),
        date(
            "other",
            "2026-03-06T17:06:30Z",
            "instant",
            "artifact_metadata",
            date_role_native="PDF CreationDate and ModDate",
        ),
        date("revised", "2026-03-06", "day", "artifact_body"),
    ],
)
coverage(
    "anthropic/claude-opus-4-6",
    anthropic,
    [opus46],
    [a1[0], a1[1], a1[3]],
    [a1[2]],
    "Extract four dated changelog blocks and correction claims.",
)

a2 = artifact_bundle(
    key="anthropic/claude-fable-5-1-mythos-5-1-system-card",
    title="Claude Fable 5.1 & Claude Mythos 5.1 System Card",
    publisher_id=anthropic,
    native_type="System Card",
    subjects=[(fable51, "configuration"), (mythos51, "configuration")],
    cache_name="claude-fable-5-1-mythos-5-1-system-card.html",
    url="https://www.anthropic.com/claude-fable-5-1-mythos-5-1-system-card",
    page_count=212,
    url_role="vanity",
    dates=[
        date("published", "2026-09-01", "day", "artifact_cover"),
        date("index_listed", "2026-09", "month", "index_surface"),
    ],
)
coverage(
    "anthropic/claude-fable-5-1-mythos-5-1",
    anthropic,
    [fable51, mythos51],
    [a2[0], a2[1], a2[3]],
    [a2[2]],
    "Encode the companion risk report and safeguard-regime claims.",
)


# OpenAI o1: one conceptual artifact, three byte-distinct versions.
o1_key = "openai/o1-system-card"
o1_versions = []
o1_specs = [
    {
        "cache": "o1-system-card.pdf",
        "url": "https://cdn.openai.com/o1-system-card.pdf",
        "label": "September 2024 initial",
        "cover": "2024-09-12",
        "metadata": "2024-09-13T05:44:59Z",
        "transport": "2024-09-14",
        "pages": 43,
        "subjects": [(o1_preview, "checkpoint")],
    },
    {
        "cache": "o1-preview-system-card-20240917.pdf",
        "url": "https://cdn.openai.com/o1-preview-system-card-20240917.pdf",
        "label": "September 2024 annotated reissue",
        "cover": "2024-09-12",
        "metadata": "2024-12-04T01:55:31Z",
        "transport": "2024-12-04",
        "pages": 42,
        "subjects": [(o1_preview, "checkpoint")],
    },
    {
        "cache": "o1-system-card-20241205.pdf",
        "url": "https://cdn.openai.com/o1-system-card-20241205.pdf",
        "label": "December 2024 general availability",
        "cover": "2024-12-05",
        "metadata": "2025-02-14T23:44:40Z",
        "transport": "2025-02-15",
        "pages": 52,
        "subjects": [(o1_ga, "checkpoint")],
    },
]
previous = None
for ordinal, spec in enumerate(o1_specs, start=1):
    result = artifact_bundle(
        key=o1_key,
        title="OpenAI o1 System Card",
        publisher_id=openai,
        native_type="System Card",
        subjects=spec["subjects"],
        cache_name=spec["cache"],
        url=spec["url"],
        page_count=spec["pages"],
        version_ordinal=ordinal,
        version_label=spec["label"],
        lifecycle="current" if ordinal == 3 else "superseded",
        supersedes=[previous] if previous else None,
        dates=[
            date("cover_date", spec["cover"], "day", "artifact_cover"),
            date(
                "other",
                spec["metadata"],
                "instant",
                "artifact_metadata",
                date_role_native="PDF CreationDate and ModDate",
            ),
            date(
                "transport_last_modified",
                spec["transport"],
                "day",
                "transport_header",
            ),
        ],
    )
    o1_versions.append(result)
    previous = result[1]
coverage(
    "openai/o1",
    openai,
    [o1, o1_preview, o1_ga],
    [o1_versions[0][0], *[item[1] for item in o1_versions], *[item[3] for item in o1_versions]],
    [item[2] for item in o1_versions],
    "Encode the cross-pointer and preview/general-availability scope claims.",
)

o3 = artifact_bundle(
    key="openai/gpt-live-system-card",
    title="GPT-Live System Card",
    publisher_id=openai,
    native_type="System Card",
    subjects=[(gpt_live, "primary"), (gpt_live_mini, "primary")],
    cache_name="gptlive.pdf",
    url="https://deploymentsafety.openai.com/gpt-live/gpt-live.pdf",
    page_count=7,
    dates=[
        date("cover_date", "2026-07-08", "day", "artifact_cover"),
        date("index_listed", "2026-07-08", "day", "index_surface"),
        date("revised", "2026-08-04", "day", "artifact_body"),
        date(
            "other",
            "2025-12-17T19:27:05Z",
            "instant",
            "artifact_metadata",
            date_role_native="PDF CreationDate and ModDate",
        ),
        date(
            "transport_last_modified",
            "2026-09-05",
            "day",
            "transport_header",
        ),
    ],
)
coverage(
    "openai/gpt-live",
    openai,
    [gpt_live, gpt_live_mini],
    [o3[0], o3[1], o3[3]],
    [o3[2]],
    "Extract original and corrected evaluation claims from the added appendix.",
)


# Google/DeepMind cached cards
g1 = artifact_bundle(
    key="google-deepmind/gemini-3-pro-model-card",
    title="Gemini 3 Pro Model Card",
    publisher_id=google,
    native_type="Model Card",
    subjects=[(gemini3, "primary")],
    cache_name="Gemini-3-Pro.pdf",
    url="https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf",
    page_count=10,
    version_title="Gemini 3 Pro Model Card (May 2026)",
    dates=[
        date("published", "2025-11", "month", "artifact_body"),
        date("index_listed", "2025-11-18", "day", "index_surface"),
        date("revised", "2026-05", "month", "artifact_body"),
        date(
            "transport_last_modified",
            "2026-05-22",
            "day",
            "transport_header",
        ),
    ],
)
coverage(
    "google-deepmind/gemini-3-pro",
    google,
    [gemini3],
    [g1[0], g1[1], g1[3]],
    [g1[2]],
    "Encode the alias redirect, date disagreement, and dependent-family scope.",
)

g3 = artifact_bundle(
    key="google-deepmind/veo-3-model-card",
    title="Veo 3 Model Card",
    publisher_id=google,
    native_type="Model Card",
    subjects=[(veo3, "primary")],
    cache_name="Veo-3.pdf",
    url="https://storage.googleapis.com/deepmind-media/Model-Cards/Veo-3-Model-Card.pdf",
    page_count=6,
    version_title="Veo 3 Model Card (January 2026)",
    dates=[
        date("published", "2025-05-23", "day", "artifact_body"),
        date("revised", "2026-01-13", "day", "artifact_body"),
        date("index_listed", "2026-01-13", "day", "index_surface"),
        date(
            "transport_last_modified",
            "2026-03-26",
            "day",
            "transport_header",
        ),
    ],
    scope_temporality="prospective",
    prospective_scope_native="covers Veo 3 and subsequent versions",
)
coverage(
    "google-deepmind/veo-3",
    google,
    [veo3],
    [g3[0], g3[1], g3[3]],
    [g3[2]],
    "Extract prospective-scope and modality claims without inventing future entities.",
)


for name, records in streams.items():
    records.sort(key=lambda record: record["id"])
    path = DATA / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(
            json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
            for record in records
        ),
        encoding="utf-8",
    )

print(
    "seeded cached calibration artifacts; "
    + ", ".join(f"{name}={len(records)}" for name, records in streams.items())
)

#!/usr/bin/env python3
"""Dematerialize one PDF after extracted text exposed a policy violation.

The original bytes remain identified by SHA-256, length, media type, official
URL, and retrieval record. The current tree no longer stores them. A typed
absence records why materialization is intentionally unavailable.

Outcome:
    Executed successfully on 2026-09-05. The provider-original PDF was
    removed from the current tree, its byte record became remote-only, and a
    typed policy absence was linked from the calibration coverage record.
    Canonical, archive, projection, skill, and full repository verification
    are recorded by the commits that follow this migration.
"""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.canonical_store import CanonicalStore


BYTE_ID = "fmo:sha256:805ca645079c287664890bdea737e22ebc8a66aca6e8f0a03d0ffeca86c4d17f"
ABSENCE_ID = "fmo:absence:01a07281-f268-779b-9cf1-62182780bd70"
ABSENCE_KEY = "google-deepmind/veo-3/pdf-materialization/excluded-by-policy"
COVERAGE_KEY = "calibration/google-deepmind/veo-3"

store = CanonicalStore(ROOT, "2026-09-05T07:50:00Z", "2026-09-05")
byte_record = next(
    record
    for record in store.streams["byte-objects.jsonl"]
    if record["id"] == BYTE_ID
)
locator = byte_record["storage"].get("locator")
if locator:
    path = ROOT / locator
    if path.exists():
        path.unlink()
byte_record["storage"] = {
    "backend": "external_only",
    "availability": "remote_only",
}

veo = store.existing("entities.jsonl", "google-deepmind/veo-3")
absence = store.envelope("absence", ABSENCE_ID, ABSENCE_KEY)
absence.update(
    {
        "absence_type": "excluded_by_policy",
        "target": {
            "subject_id": veo["id"],
            "description_native": "provider PDF materialization",
        },
        "expected_record_type": "materialized_byte_object",
        "search_scope": {
            "description": "Deterministic text extraction of the provider PDF was checked against the canonical repository exclusion policy."
        },
        "checked_at": {
            "value": "2026-09-05",
            "precision": "day",
            "basis": "retrieval",
        },
        "observed_time": store.observed_time,
        "basis": "Extracted provider text contains excluded subject matter; retain URL, retrieval, hash, length, and media type without storing the bytes.",
        "lifecycle": "current",
    }
)
store.add("absences.jsonl", absence)

coverage = store.existing("coverage-ledger.jsonl", COVERAGE_KEY)
coverage["absence_ids"] = sorted(
    set(coverage.get("absence_ids", [])) | {ABSENCE_ID}
)
coverage["coverage_basis"] = (
    "Identity, artifact, version, URL, retrieval, and provider-byte hash are "
    "canonical; raw bytes are remote-only under repository policy."
)
coverage["next_action"] = (
    "Extract only policy-compliant claims from reviewed text without "
    "materializing the provider PDF."
)

store.write()
print("dematerialized policy-violating provider PDF and recorded typed absence")

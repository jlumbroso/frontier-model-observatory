#!/usr/bin/env python3
"""Materialize policy-clean text derivatives and verify their provenance."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.canonical_store import CanonicalStore
from scripts.extract_artifact_text import extract, policy_matches, policy_rules


SOURCE_DERIVATIONS = {"provider_original", "captured_html"}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def load_records(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def eligible_sources(root: Path) -> list[dict]:
    return [
        record
        for record in load_records(root / "data" / "byte-objects.jsonl")
        if record.get("derivation") in SOURCE_DERIVATIONS
        and record["storage"]["availability"] == "materialized"
    ]


def extracted_by_source(root: Path) -> dict[str, dict]:
    result = {}
    for record in load_records(root / "data" / "byte-objects.jsonl"):
        if record.get("derivation") != "extracted_text":
            continue
        for source_id in record.get("derived_from_byte_ids", []):
            result[source_id] = record
    return result


def check(root: Path) -> list[str]:
    derivatives = extracted_by_source(root)
    errors = []
    for source in eligible_sources(root):
        derivative = derivatives.get(source["id"])
        if derivative is None:
            errors.append(f"{source['id']}: missing extracted-text derivative")
            continue
        storage = derivative["storage"]
        if storage["availability"] != "materialized":
            errors.append(f"{derivative['id']}: derivative is not materialized")
            continue
        path = root / storage["locator"]
        if not path.exists():
            errors.append(f"{derivative['id']}: missing {storage['locator']}")
            continue
        payload = path.read_bytes()
        digest = hashlib.sha256(payload).hexdigest()
        if digest != derivative["sha256"]:
            errors.append(f"{derivative['id']}: SHA-256 mismatch")
        if len(payload) != derivative["byte_length"]:
            errors.append(f"{derivative['id']}: byte-length mismatch")

    byte_records = {
        record["id"]: record
        for record in load_records(root / "data" / "byte-objects.jsonl")
    }
    for version in load_records(root / "data" / "artifact-versions.jsonl"):
        source_ids = {
            ident
            for ident in version.get("byte_object_ids", [])
            if ident in byte_records
            and byte_records[ident].get("derivation") in SOURCE_DERIVATIONS
            and byte_records[ident]["storage"]["availability"] == "materialized"
        }
        for source_id in source_ids:
            derivative = derivatives.get(source_id)
            if derivative and derivative["id"] not in version["byte_object_ids"]:
                errors.append(
                    f"{version['id']}: does not link derivative "
                    f"{derivative['id']}"
                )
    return errors


def materialize(
    root: Path, recorded_at: str, observed_date: str
) -> tuple[int, int]:
    rules = policy_rules(root)
    prepared = []
    for source in eligible_sources(root):
        path = root / source["storage"]["locator"]
        text = extract(path, source["media_type_detected"])
        matches = policy_matches(text, rules)
        if matches:
            labels = ", ".join(sorted({item["label"] for item in matches}))
            raise ValueError(
                f"{source['id']}: extracted text violates policy: {labels}"
            )
        payload = text.encode("utf-8")
        digest = hashlib.sha256(payload).hexdigest()
        prepared.append((source, payload, digest))

    store = CanonicalStore(root, recorded_at, observed_date)
    existing_ids = {
        record["id"] for record in store.streams["byte-objects.jsonl"]
    }
    source_to_derivative = {}
    created = 0
    for source, payload, digest in prepared:
        ident = f"fmo:sha256:{digest}"
        target = (
            root
            / "artifacts"
            / "sha256"
            / digest[:2]
            / digest
            / "extracted.txt"
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and target.read_bytes() != payload:
            raise ValueError(f"content-address collision at {target}")
        target.write_bytes(payload)
        record = {
            "schema_version": "1.0.0",
            "record_type": "byte_object",
            "id": ident,
            "recorded_at": recorded_at,
            "record_status": "active",
            "sha256": digest,
            "byte_length": len(payload),
            "media_type_detected": "text/plain",
            "storage": {
                "backend": "git",
                "availability": "materialized",
                "locator": str(target.relative_to(root)),
            },
            "observed_time": {
                "first_observed": {
                    "value": observed_date,
                    "precision": "day",
                    "basis": "retrieval",
                }
            },
            "derivation": "extracted_text",
            "derived_from_byte_ids": [source["id"]],
        }
        stored = store.add("byte-objects.jsonl", record)
        if ident not in existing_ids:
            created += 1
            existing_ids.add(ident)
        source_to_derivative[source["id"]] = stored["id"]

    linked = 0
    byte_records = {
        record["id"]: record
        for record in store.streams["byte-objects.jsonl"]
    }
    for version in store.streams["artifact-versions.jsonl"]:
        source_ids = [
            ident
            for ident in version.get("byte_object_ids", [])
            if ident in byte_records
            and byte_records[ident].get("derivation") in SOURCE_DERIVATIONS
            and byte_records[ident]["storage"]["availability"] == "materialized"
        ]
        derivative_ids = [
            source_to_derivative[ident]
            for ident in source_ids
            if ident in source_to_derivative
        ]
        before = set(version.get("byte_object_ids", []))
        version["byte_object_ids"] = sorted(before | set(derivative_ids))
        if set(version["byte_object_ids"]) != before:
            linked += 1
        if derivative_ids and "plain_text" not in version["representation_kinds"]:
            version["representation_kinds"].append("plain_text")
            version["representation_kinds"].sort()
    store.write()
    return created, linked


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--recorded-at", default=now_iso())
    parser.add_argument(
        "--observed-date",
        default=datetime.now(timezone.utc).date().isoformat(),
    )
    args = parser.parse_args()
    root = args.root.resolve()
    if args.write:
        created, linked = materialize(
            root, args.recorded_at, args.observed_date
        )
        print(
            f"materialized {created} new text derivative(s); "
            f"updated {linked} artifact version(s)"
        )
    errors = check(root)
    if errors:
        print("\n".join(errors))
        return 1
    print(
        f"verified extracted text for {len(eligible_sources(root))} "
        "eligible source artifact(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

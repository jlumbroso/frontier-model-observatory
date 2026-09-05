"""Small canonical-store API for evidence-grounded ingestion scripts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil

from scripts.mint_id import mint
from scripts.validate_records import CANONICAL_STREAM_TYPES


ENTITY_PREFIX = {
    "organization": "org",
    "model_family": "family",
    "model": "model",
    "checkpoint": "checkpoint",
    "configuration": "configuration",
    "product": "product",
    "deployment": "deployment",
    "endpoint": "endpoint",
    "alias": "alias",
}
TYPE_PREFIX = {
    "artifact": "artifact",
    "artifact_version": "artifact-version",
    "url_alias": "url",
    "retrieval_event": "retrieval",
    "artifact_part": "part",
    "artifact_relationship": "artifact-relationship",
    "claim": "claim",
    "event": "event",
    "absence": "absence",
    "coverage_ledger_entry": "coverage",
}


class CanonicalStore:
    def __init__(self, root: Path, recorded_at: str, observed_date: str):
        self.root = root.resolve()
        self.data = self.root / "data"
        self.recorded_at = recorded_at
        self.observed_date = observed_date
        self.observed_time = {
            "first_observed": {
                "value": observed_date,
                "precision": "day",
                "basis": "retrieval",
            }
        }
        self.streams = {
            filename: self._read(filename)
            for filename in CANONICAL_STREAM_TYPES
        }

    def _read(self, filename: str) -> list[dict]:
        path = self.data / filename
        if not path.exists():
            return []
        return [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    def existing(self, filename: str, canonical_key: str) -> dict | None:
        return next(
            (
                record
                for record in self.streams[filename]
                if record.get("canonical_key") == canonical_key
            ),
            None,
        )

    def id_for(
        self, filename: str, canonical_key: str, prefix: str | None = None
    ) -> str:
        found = self.existing(filename, canonical_key)
        if found:
            return found["id"]
        record_type = CANONICAL_STREAM_TYPES[filename]
        resolved_prefix = prefix or TYPE_PREFIX.get(record_type)
        if not resolved_prefix:
            raise ValueError(f"identifier prefix required for {record_type}")
        return mint(resolved_prefix)

    def envelope(
        self, record_type: str, ident: str, canonical_key: str
    ) -> dict:
        return {
            "schema_version": "1.0.0",
            "record_type": record_type,
            "id": ident,
            "canonical_key": canonical_key,
            "recorded_at": self.recorded_at,
            "record_status": "active",
        }

    def add(self, filename: str, record: dict) -> dict:
        key = record.get("canonical_key")
        found = (
            self.existing(filename, key)
            if key
            else next(
                (
                    item
                    for item in self.streams[filename]
                    if item["id"] == record["id"]
                ),
                None,
            )
        )
        if found:
            return found
        self.streams[filename].append(record)
        return record

    def entity(self, kind: str, key: str, name: str, **fields) -> str:
        found = self.existing("entities.jsonl", key)
        if found and found.get("kind") != kind:
            raise ValueError(
                f"entity canonical_key {key!r} belongs to "
                f"{found.get('kind')}, not {kind}"
            )
        ident = self.id_for(
            "entities.jsonl", key, ENTITY_PREFIX[kind]
        )
        record = self.envelope("entity", ident, key)
        record.update(
            {
                "kind": kind,
                "preferred_name": name,
                "names": [
                    {"value": name, "name_type": "provider_preferred"}
                ],
                "observed_time": self.observed_time,
                **fields,
            }
        )
        self.add("entities.jsonl", record)
        return ident

    def byte_object(
        self,
        source: Path,
        *,
        media_type: str,
        derivation: str,
        materialize: bool,
        materialized_name: str,
    ) -> tuple[str, int, str]:
        data = source.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        ident = f"fmo:sha256:{digest}"
        storage = {
            "backend": "external_only",
            "availability": "remote_only",
        }
        if materialize:
            target = (
                self.root
                / "artifacts"
                / "sha256"
                / digest[:2]
                / digest
                / materialized_name
            )
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and target.read_bytes() != data:
                raise ValueError(f"content-address collision at {target}")
            if not target.exists():
                shutil.copyfile(source, target)
            storage = {
                "backend": "git_lfs"
                if materialized_name.endswith(".pdf")
                else "git",
                "availability": "materialized",
                "locator": str(target.relative_to(self.root)),
            }

        self.add(
            "byte-objects.jsonl",
            {
                "schema_version": "1.0.0",
                "record_type": "byte_object",
                "id": ident,
                "recorded_at": self.recorded_at,
                "record_status": "active",
                "sha256": digest,
                "byte_length": len(data),
                "media_type_detected": media_type,
                "storage": storage,
                "observed_time": self.observed_time,
                "derivation": derivation,
            },
        )
        return ident, len(data), digest

    def write(self) -> None:
        self.data.mkdir(parents=True, exist_ok=True)
        for filename, records in self.streams.items():
            if not records:
                continue
            records.sort(key=lambda record: record["id"])
            (self.data / filename).write_text(
                "".join(
                    json.dumps(
                        record,
                        ensure_ascii=False,
                        separators=(",", ":"),
                    )
                    + "\n"
                    for record in records
                ),
                encoding="utf-8",
            )

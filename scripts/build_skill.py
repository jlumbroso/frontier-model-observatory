#!/usr/bin/env python3
"""Build or check the skill's deterministic bundled data snapshot."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "frontier-model-observatory"
VERSION = "0.1.1"
SNAPSHOT_DATE = "2026-09-05"
FILES = [
    "fmo-records.jsonl",
    "fmo-records.json",
    "entities.csv",
    "artifacts.csv",
    "chronology.csv",
    "coverage.csv",
    "fmo.sqlite",
]
RESEARCH_FILES = {
    "chronology-research.jsonl": ROOT / "research" / "chronology" / "rows.jsonl",
    "chronology-research-manifest.json": (
        ROOT / "research" / "chronology" / "manifest.json"
    ),
}


def build(target: Path) -> None:
    source_manifest = json.loads(
        (ROOT / "dist" / "manifest.json").read_text(encoding="utf-8")
    )
    target.mkdir(parents=True, exist_ok=True)
    entries = []
    for filename in FILES:
        source = ROOT / "dist" / filename
        destination = target / filename
        shutil.copyfile(source, destination)
        data = destination.read_bytes()
        entries.append(
            {
                "path": f"data/{filename}",
                "sha256": hashlib.sha256(data).hexdigest(),
                "byte_length": len(data),
            }
        )
    for filename, source in RESEARCH_FILES.items():
        destination = target / filename
        shutil.copyfile(source, destination)
        data = destination.read_bytes()
        entries.append(
            {
                "path": f"data/{filename}",
                "sha256": hashlib.sha256(data).hexdigest(),
                "byte_length": len(data),
            }
        )
    research_manifest = json.loads(
        RESEARCH_FILES["chronology-research-manifest.json"].read_text(
            encoding="utf-8"
        )
    )
    manifest = {
        "schema_version": 1,
        "skill_version": VERSION,
        "snapshot_date": SNAPSHOT_DATE,
        "comprehensive": False,
        "coverage_boundary": "Twelve ADR-0006 calibration subjects across three core providers.",
        "record_schema_version": "1.0.0",
        "record_count": source_manifest["record_count"],
        "coverage_scope_count": source_manifest["coverage_scope_count"],
        "canonical_data_sha256": source_manifest["canonical_data_sha256"],
        "research_chronology": {
            "semantic_status": research_manifest["semantic_status"],
            "source_sha256": research_manifest["source_sha256"],
            "data_row_count": research_manifest["data_row_count"],
            "table_count": research_manifest["table_count"],
        },
        "files": entries,
    }
    (target / "snapshot-manifest.json").write_text(
        json.dumps(manifest, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )


def file_map(path: Path) -> dict[str, bytes]:
    if not path.exists():
        return {}
    return {
        str(file.relative_to(path)): file.read_bytes()
        for file in path.rglob("*")
        if file.is_file()
    }


def check() -> list[str]:
    with tempfile.TemporaryDirectory() as directory:
        expected_root = Path(directory) / "data"
        build(expected_root)
        expected = file_map(expected_root)
    actual = file_map(SKILL / "data")
    errors = []
    for path in sorted(set(expected) | set(actual)):
        if path not in actual:
            errors.append(f"missing skill snapshot file: {path}")
        elif path not in expected:
            errors.append(f"unexpected skill snapshot file: {path}")
        elif actual[path] != expected[path]:
            errors.append(f"stale skill snapshot file: {path}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        errors = check()
        if errors:
            print("\n".join(errors))
            return 1
        print("skill snapshot: fresh")
        return 0
    data = SKILL / "data"
    if data.exists():
        shutil.rmtree(data)
    build(data)
    print(f"built skill snapshot {VERSION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

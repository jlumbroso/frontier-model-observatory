#!/usr/bin/env python3
"""Generate deterministic human/model views and machine distributions."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import shutil
import sqlite3
import tempfile
from typing import Iterable


GENERATOR_VERSION = "1.0.0"
ROOT = Path(__file__).resolve().parents[1]


def read_records(root: Path) -> list[dict]:
    records = []
    for path in sorted((root / "data").glob("*.jsonl")):
        records.extend(
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    return sorted(records, key=lambda r: (r["record_type"], r["id"]))


def references(value) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for item in value.values():
            found.update(references(item))
    elif isinstance(value, list):
        for item in value:
            found.update(references(item))
    elif isinstance(value, str) and value.startswith("fmo:"):
        found.add(value)
    return found


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_jsonl(path: Path, records: Iterable[dict]) -> None:
    write_text(
        path,
        "\n".join(
            json.dumps(record, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
            for record in records
        ),
    )


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    def cell(value: object) -> str:
        return str(value).replace("|", "\\|").replace("\n", " ")

    output = [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join("---" for _ in headers) + "|",
    ]
    output.extend(
        "| " + " | ".join(cell(value) for value in row) + " |" for row in rows
    )
    return "\n".join(output)


def provider_records(records: list[dict], org: dict) -> list[dict]:
    selected: set[str] = {org["id"]}
    for record in records:
        if (
            record.get("provider_org_id") == org["id"]
            or record.get("host_org_id") == org["id"]
            or org["id"] in record.get("publisher_org_ids", [])
        ):
            selected.add(record["id"])

    changed = True
    while changed:
        changed = False
        for record in records:
            refs = references(record)
            if record["id"] in selected:
                additions = refs - selected
                if additions:
                    selected.update(additions)
                    changed = True
            elif refs & selected:
                selected.add(record["id"])
                changed = True
    return [record for record in records if record["id"] in selected]


def related_to_artifacts(
    records: list[dict], artifact_ids: set[str]
) -> list[dict]:
    selected = set(artifact_ids)
    changed = True
    while changed:
        changed = False
        for record in records:
            if record["id"] in selected:
                continue
            if references(record) & selected:
                selected.add(record["id"])
                changed = True
    return [record for record in records if record["id"] in selected]


def artifact_title(record: dict, by_id: dict[str, dict]) -> str:
    if record["record_type"] == "artifact":
        return record["preferred_title"]
    artifact_id = record.get("artifact_id")
    if artifact_id and artifact_id in by_id:
        return by_id[artifact_id].get("preferred_title", artifact_id)
    return record.get("canonical_key", record["id"])


def generate_views(root: Path, views: Path, dist: Path) -> None:
    records = read_records(root)
    by_id = {record["id"]: record for record in records}
    entities = [r for r in records if r["record_type"] == "entity"]
    artifacts = [r for r in records if r["record_type"] == "artifact"]
    versions = [r for r in records if r["record_type"] == "artifact_version"]
    coverage = [
        r for r in records if r["record_type"] == "coverage_ledger_entry"
    ]

    for path in (views, dist):
        if path.exists():
            shutil.rmtree(path)
        path.mkdir(parents=True)

    provider_rows = []
    providers = [
        entity
        for entity in entities
        if entity.get("kind") == "organization"
        and "provider" in entity.get("roles", [])
    ]
    for provider in sorted(providers, key=lambda r: r["canonical_key"]):
        subset = provider_records(records, provider)
        slug = provider["canonical_key"]
        write_jsonl(views / "by-provider" / slug / "records.jsonl", subset)
        models = [
            r for r in subset
            if r["record_type"] == "entity" and r.get("kind") == "model"
        ]
        provider_artifacts = [
            r for r in subset if r["record_type"] == "artifact"
        ]
        provider_coverage = [
            r for r in subset if r["record_type"] == "coverage_ledger_entry"
        ]
        readme = [
            f"# {provider['preferred_name']}",
            "",
            f"Canonical provider key: `{provider['canonical_key']}`",
            "",
            f"- Models currently encoded: **{len(models)}**",
            f"- Artifacts currently encoded: **{len(provider_artifacts)}**",
            f"- Coverage assessments: **{len(provider_coverage)}**",
            "",
            "## Models",
            "",
            markdown_table(
                ["Canonical key", "Name", "Lifecycle"],
                [
                    [
                        f"`{model['canonical_key']}`",
                        model["preferred_name"],
                        model.get("lifecycle", "not reported"),
                    ]
                    for model in sorted(models, key=lambda r: r["canonical_key"])
                ],
            ),
            "",
            "## Artifacts",
            "",
            markdown_table(
                ["Canonical key", "Title", "Class", "Redistribution"],
                [
                    [
                        f"`{artifact['canonical_key']}`",
                        artifact["preferred_title"],
                        artifact["artifact_class"],
                        artifact["redistribution_status"],
                    ]
                    for artifact in sorted(
                        provider_artifacts, key=lambda r: r["canonical_key"]
                    )
                ],
            ),
            "",
            "This is a generated projection. Edit canonical JSONL, not this file.",
        ]
        write_text(views / "by-provider" / slug / "README.md", "\n".join(readme))
        provider_rows.append(
            [
                provider["preferred_name"],
                f"`{slug}`",
                len(models),
                len(provider_artifacts),
                len(provider_coverage),
            ]
        )

    chronology: list[dict] = []
    for version in versions:
        for assertion in version.get("date_assertions", []):
            value = assertion["value"]["value"]
            year = value[:4] if len(value) >= 4 and value[:4].isdigit() else "unknown"
            row = {
                "year": year,
                "date": value,
                "precision": assertion["value"]["precision"],
                "date_role": assertion["date_role"],
                "date_basis": assertion["value"].get("basis", "not reported"),
                "artifact_version_id": version["id"],
                "artifact_id": version["artifact_id"],
                "artifact_title": artifact_title(version, by_id),
                "canonical_key": version["canonical_key"],
            }
            chronology.append(row)
    chronology.sort(
        key=lambda row: (
            row["year"],
            row["date"],
            row["canonical_key"],
            row["date_role"],
        )
    )
    for year in sorted({row["year"] for row in chronology}):
        rows = [row for row in chronology if row["year"] == year]
        write_text(
            views / "by-year" / year / "README.md",
            "\n".join(
                [
                    f"# Artifact date assertions: {year}",
                    "",
                    "Publication, revision, index, metadata, and transport dates remain distinct.",
                    "",
                    markdown_table(
                        ["Date", "Precision", "Role", "Basis", "Artifact"],
                        [
                            [
                                row["date"],
                                row["precision"],
                                row["date_role"],
                                row["date_basis"],
                                row["artifact_title"],
                            ]
                            for row in rows
                        ],
                    ),
                    "",
                    "This is a generated projection. Dates are assertions, not a single overloaded chronology.",
                ]
            ),
        )

    families = [
        entity for entity in entities if entity.get("kind") == "model_family"
    ]
    for family in sorted(families, key=lambda r: r["canonical_key"]):
        members = [
            entity
            for entity in entities
            if entity.get("family_id") == family["id"]
        ]
        member_ids = {member["id"] for member in members}
        configurations = [
            entity
            for entity in entities
            if entity.get("configures_id") in member_ids | {family["id"]}
        ]
        subject_ids = member_ids | {family["id"]} | {
            record["id"] for record in configurations
        }
        family_artifacts = [
            artifact
            for artifact in artifacts
            if {
                subject["subject_id"]
                for subject in artifact.get("subject_refs", [])
            }
            & subject_ids
        ]
        subset = related_to_artifacts(
            records, {artifact["id"] for artifact in family_artifacts}
        )
        selected_ids = {record["id"] for record in subset} | subject_ids
        selected_ids.add(family["id"])
        subset = [record for record in records if record["id"] in selected_ids]
        slug = family["canonical_key"]
        write_jsonl(views / "by-family" / slug / "records.jsonl", subset)
        write_text(
            views / "by-family" / slug / "README.md",
            "\n".join(
                [
                    f"# {family['preferred_name']}",
                    "",
                    markdown_table(
                        ["Canonical key", "Name", "Kind"],
                        [
                            [
                                f"`{record['canonical_key']}`",
                                record["preferred_name"],
                                record["kind"],
                            ]
                            for record in sorted(
                                [*members, *configurations],
                                key=lambda r: r["canonical_key"],
                            )
                        ],
                    ),
                    "",
                    f"Related artifacts: **{len(family_artifacts)}**",
                    "",
                    "This is a generated projection.",
                ]
            ),
        )

    for artifact_class in sorted(
        {artifact["artifact_class"] for artifact in artifacts}
    ):
        class_artifacts = {
            artifact["id"]
            for artifact in artifacts
            if artifact["artifact_class"] == artifact_class
        }
        subset = related_to_artifacts(records, class_artifacts)
        write_jsonl(
            views / "by-artifact-type" / artifact_class / "records.jsonl",
            subset,
        )
        write_text(
            views / "by-artifact-type" / artifact_class / "README.md",
            "\n".join(
                [
                    f"# Artifact class: {artifact_class}",
                    "",
                    markdown_table(
                        ["Canonical key", "Title", "Native type"],
                        [
                            [
                                f"`{artifact['canonical_key']}`",
                                artifact["preferred_title"],
                                artifact["native_artifact_type"]["native"],
                            ]
                            for artifact in sorted(
                                (
                                    item
                                    for item in artifacts
                                    if item["id"] in class_artifacts
                                ),
                                key=lambda r: r["canonical_key"],
                            )
                        ],
                    ),
                    "",
                    "Normalized class does not replace the provider-native term.",
                ]
            ),
        )

    write_text(
        views / "calibration" / "coverage.md",
        "\n".join(
            [
                "# Calibration coverage",
                "",
                markdown_table(
                    ["Scope", "Status", "Next action"],
                    [
                        [
                            f"`{record['scope_key']}`",
                            record["coverage_status"],
                            record.get("next_action", ""),
                        ]
                        for record in sorted(
                            coverage, key=lambda r: r["scope_key"]
                        )
                    ],
                ),
                "",
                "Coverage is an operational assessment, not evidence of complete provider coverage.",
            ]
        ),
    )
    write_text(
        views / "README.md",
        "\n".join(
            [
                "# Generated views",
                "",
                markdown_table(
                    ["Provider", "Key", "Models", "Artifacts", "Coverage rows"],
                    provider_rows,
                ),
                "",
                f"- Canonical records projected: **{len(records)}**",
                f"- Calibration scopes: **{len(coverage)}**",
                f"- Artifact date assertions: **{len(chronology)}**",
                "",
                "Browse by provider, year, family, artifact type, or calibration coverage.",
                "Regenerate with `just views`; verify freshness with `just check-views`.",
            ]
        ),
    )

    write_jsonl(dist / "fmo-records.jsonl", records)
    write_text(
        dist / "fmo-records.json",
        json.dumps(records, sort_keys=True, ensure_ascii=False, indent=2),
    )
    write_csv(
        dist / "entities.csv",
        ["id", "canonical_key", "kind", "preferred_name", "provider_org_id", "family_id"],
        [
            {
                "id": record["id"],
                "canonical_key": record["canonical_key"],
                "kind": record["kind"],
                "preferred_name": record["preferred_name"],
                "provider_org_id": record.get("provider_org_id", ""),
                "family_id": record.get("family_id", ""),
            }
            for record in entities
        ],
    )
    write_csv(
        dist / "artifacts.csv",
        ["id", "canonical_key", "preferred_title", "artifact_class", "native_type", "redistribution_status"],
        [
            {
                "id": record["id"],
                "canonical_key": record["canonical_key"],
                "preferred_title": record["preferred_title"],
                "artifact_class": record["artifact_class"],
                "native_type": record["native_artifact_type"]["native"],
                "redistribution_status": record["redistribution_status"],
            }
            for record in artifacts
        ],
    )
    write_csv(
        dist / "chronology.csv",
        ["year", "date", "precision", "date_role", "date_basis", "artifact_title", "artifact_version_id"],
        chronology,
    )
    write_csv(
        dist / "coverage.csv",
        ["scope_key", "coverage_status", "scope_description", "next_action"],
        coverage,
    )
    write_sqlite(dist / "fmo.sqlite", records, chronology)

    data_hash = hashlib.sha256()
    for path in sorted((root / "data").glob("*.jsonl")):
        data_hash.update(path.name.encode())
        data_hash.update(b"\0")
        data_hash.update(path.read_bytes())
    generated = [
        path
        for base in (views, dist)
        for path in base.rglob("*")
        if path.is_file() and path.name != "manifest.json"
    ]
    def output_label(path: Path) -> str:
        if path.is_relative_to(views):
            return f"views/{path.relative_to(views)}"
        return f"dist/{path.relative_to(dist)}"

    manifest = {
        "schema_version": 1,
        "generator_version": GENERATOR_VERSION,
        "canonical_data_sha256": data_hash.hexdigest(),
        "record_count": len(records),
        "coverage_scope_count": len(coverage),
        "files": [
            {
                "path": output_label(path),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "byte_length": path.stat().st_size,
            }
            for path in sorted(generated)
        ],
    }
    write_text(
        dist / "manifest.json",
        json.dumps(manifest, sort_keys=True, indent=2),
    )


def write_csv(path: Path, fields: list[str], rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    for row in rows:
        writer.writerow({field: row.get(field, "") for field in fields})
    path.write_text(buffer.getvalue(), encoding="utf-8")


def write_sqlite(path: Path, records: list[dict], chronology: list[dict]) -> None:
    connection = sqlite3.connect(path)
    connection.execute(
        "CREATE TABLE records (record_type TEXT NOT NULL, id TEXT PRIMARY KEY, canonical_key TEXT, json TEXT NOT NULL)"
    )
    connection.execute(
        "CREATE INDEX records_by_type_key ON records(record_type, canonical_key)"
    )
    connection.executemany(
        "INSERT INTO records VALUES (?, ?, ?, ?)",
        [
            (
                record["record_type"],
                record["id"],
                record.get("canonical_key"),
                json.dumps(record, sort_keys=True, ensure_ascii=False, separators=(",", ":")),
            )
            for record in records
        ],
    )
    connection.execute(
        "CREATE TABLE chronology (year TEXT, date TEXT, precision TEXT, date_role TEXT, date_basis TEXT, artifact_title TEXT, artifact_version_id TEXT)"
    )
    connection.executemany(
        "INSERT INTO chronology VALUES (?, ?, ?, ?, ?, ?, ?)",
        [
            (
                row["year"],
                row["date"],
                row["precision"],
                row["date_role"],
                row["date_basis"],
                row["artifact_title"],
                row["artifact_version_id"],
            )
            for row in chronology
        ],
    )
    connection.execute("PRAGMA user_version = 1")
    connection.commit()
    connection.execute("VACUUM")
    connection.close()


def file_map(root: Path) -> dict[str, bytes]:
    return {
        str(path.relative_to(root)): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }


def check_freshness(root: Path) -> list[str]:
    with tempfile.TemporaryDirectory() as directory:
        temporary = Path(directory)
        generated_views = temporary / "views"
        generated_dist = temporary / "dist"
        generate_views(root, generated_views, generated_dist)
        expected = {
            f"views/{path}": data
            for path, data in file_map(generated_views).items()
        }
        expected.update(
            {
                f"dist/{path}": data
                for path, data in file_map(generated_dist).items()
            }
        )
        actual = {}
        for name in ("views", "dist"):
            base = root / name
            if base.exists():
                actual.update(
                    {
                        f"{name}/{path}": data
                        for path, data in file_map(base).items()
                    }
                )
    errors = []
    for path in sorted(set(expected) | set(actual)):
        if path not in actual:
            errors.append(f"missing generated file: {path}")
        elif path not in expected:
            errors.append(f"unexpected generated file: {path}")
        elif expected[path] != actual[path]:
            errors.append(f"stale generated file: {path}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        errors = check_freshness(ROOT)
        if errors:
            print("\n".join(errors))
            return 1
        print("generated views: fresh")
        return 0
    generate_views(ROOT, ROOT / "views", ROOT / "dist")
    print("generated views and distributions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

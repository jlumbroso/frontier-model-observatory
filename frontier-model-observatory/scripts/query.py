#!/usr/bin/env python3
"""Query the bundled Frontier Model Observatory snapshot."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load_records() -> list[dict]:
    path = DATA / "fmo-records.jsonl"
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def load_manifest() -> dict:
    return json.loads(
        (DATA / "snapshot-manifest.json").read_text(encoding="utf-8")
    )


def load_research_rows() -> list[dict]:
    path = DATA / "chronology-research.jsonl"
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def search_text(record: dict) -> str:
    values = [
        record.get("canonical_key", ""),
        record.get("preferred_name", ""),
        record.get("preferred_title", ""),
        record.get("title_native", ""),
        record.get("url", ""),
        record.get("alias_value", ""),
    ]
    values.extend(
        item.get("value", "") for item in record.get("names", [])
    )
    return " ".join(values).casefold()


def rank(record: dict, query: str) -> tuple[int, str]:
    needle = query.casefold()
    key = record.get("canonical_key", "").casefold()
    names = {
        record.get("preferred_name", "").casefold(),
        record.get("preferred_title", "").casefold(),
        record.get("title_native", "").casefold(),
    }
    if needle == key or needle in names:
        score = 0
    elif key.endswith("/" + needle) or any(name.startswith(needle) for name in names):
        score = 1
    elif needle in key:
        score = 2
    else:
        score = 3
    return score, key


def provider_maps(records: list[dict]) -> tuple[dict[str, str], dict[str, str]]:
    orgs = {
        record["id"]: record["canonical_key"]
        for record in records
        if record["record_type"] == "entity"
        and record.get("kind") == "organization"
    }
    artifacts = {
        record["id"]: orgs.get(record.get("publisher_org_ids", [""])[0], "")
        for record in records
        if record["record_type"] == "artifact"
    }
    return orgs, artifacts


def record_provider(
    record: dict,
    by_id: dict[str, dict],
    orgs: dict[str, str],
    artifacts: dict[str, str],
) -> str:
    direct = (
        record.get("provider_org_id")
        or record.get("host_org_id")
        or (record.get("publisher_org_ids") or [None])[0]
    )
    if direct in orgs:
        return orgs[direct]
    artifact_id = record.get("artifact_id")
    if artifact_id in artifacts:
        return artifacts[artifact_id]
    for ref in references(record):
        target = by_id.get(ref)
        if target and target is not record:
            provider = record_provider_shallow(target, orgs, artifacts)
            if provider:
                return provider
    return ""


def record_provider_shallow(
    record: dict, orgs: dict[str, str], artifacts: dict[str, str]
) -> str:
    direct = (
        record.get("provider_org_id")
        or record.get("host_org_id")
        or (record.get("publisher_org_ids") or [None])[0]
    )
    if direct in orgs:
        return orgs[direct]
    return artifacts.get(record.get("artifact_id"), "")


def references(value) -> set[str]:
    found = set()
    if isinstance(value, dict):
        for item in value.values():
            found.update(references(item))
    elif isinstance(value, list):
        for item in value:
            found.update(references(item))
    elif isinstance(value, str) and value.startswith("fmo:"):
        found.add(value)
    return found


def markdown_notice(manifest: dict) -> str:
    return (
        f"_Snapshot {manifest['snapshot_date']}; "
        f"{manifest['record_count']} records; "
        f"{manifest['coverage_scope_count']} calibration scopes; "
        "not comprehensive frontier coverage._"
    )


def markdown_records(records: Iterable[dict], manifest: dict) -> str:
    def escape(value: str) -> str:
        return value.replace("|", "\\|").replace("\n", " ")

    rows = []
    for record in records:
        label = (
            record.get("preferred_name")
            or record.get("preferred_title")
            or record.get("title_native")
            or record.get("url")
            or record.get("scope_description")
            or ""
        )
        rows.append(
            (
                record["record_type"],
                record.get("canonical_key", record["id"]),
                label,
            )
        )
    lines = [
        markdown_notice(manifest),
        "",
        "| Type | Canonical key | Label |",
        "|---|---|---|",
    ]
    lines.extend(
        f"| {rtype} | `{key}` | {escape(label)} |"
        for rtype, key, label in rows
    )
    return "\n".join(lines)


def emit(payload, *, as_json: bool, manifest: dict) -> None:
    if as_json:
        print(
            json.dumps(
                {
                    "snapshot": {
                        "date": manifest["snapshot_date"],
                        "record_count": manifest["record_count"],
                        "coverage_scope_count": manifest["coverage_scope_count"],
                        "comprehensive": False,
                    },
                    "results": payload,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(markdown_records(payload, manifest))


def typed_miss(query: str, manifest: dict, as_json: bool) -> int:
    payload = {
        "status": "not_found",
        "query": query,
        "search_scope": "bundled calibration snapshot",
        "snapshot_date": manifest["snapshot_date"],
        "next_action": "Search current official provider sources; do not infer confirmed absence.",
    }
    if as_json:
        print(json.dumps(payload, indent=2))
    else:
        print(markdown_notice(manifest))
        print()
        print(f"`{query}` was **not found** in the bundled calibration snapshot.")
        print("Search current official provider sources; this is not confirmed absence.")
    return 2


def emit_research(rows: list[dict], manifest: dict, as_json: bool) -> None:
    research = manifest["research_chronology"]
    if as_json:
        print(
            json.dumps(
                {
                    "research_projection": research,
                    "canonical": False,
                    "results": rows,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return
    print(
        f"_Official-source research projection; "
        f"{research['data_row_count']} data rows; not yet canonical._"
    )
    print()
    print("| Section | Source line | Matching row |")
    print("|---|---:|---|")
    for row in rows:
        values = list(row["cells"].values())
        summary = " · ".join(values[:2])
        summary = summary.replace("|", "\\|").replace("\n", " ")
        print(
            f"| {row['section']} | {row['source_line']} | {summary} |"
        )


def parse_date_floor(value: str) -> str:
    if re.fullmatch(r"\d{4}", value):
        return value + "-01-01"
    if re.fullmatch(r"\d{4}-\d{2}", value):
        return value + "-01"
    return value[:10]


def add_common(subparser) -> None:
    subparser.add_argument("--json", action="store_true")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    find_parser = sub.add_parser("find")
    find_parser.add_argument("query")
    find_parser.add_argument("--record-type")
    find_parser.add_argument("--limit", type=int, default=20)
    add_common(find_parser)

    artifact_parser = sub.add_parser("artifacts")
    artifact_parser.add_argument("--provider")
    artifact_parser.add_argument("--class", dest="artifact_class")
    add_common(artifact_parser)

    timeline_parser = sub.add_parser("timeline")
    timeline_parser.add_argument("--provider")
    timeline_parser.add_argument("--from-year", type=int)
    timeline_parser.add_argument("--to-year", type=int)
    add_common(timeline_parser)

    asof_parser = sub.add_parser("as-of")
    asof_parser.add_argument("date")
    asof_parser.add_argument("query", nargs="?")
    add_common(asof_parser)

    coverage_parser = sub.add_parser("coverage")
    coverage_parser.add_argument("--status")
    add_common(coverage_parser)

    id_parser = sub.add_parser("id")
    id_parser.add_argument("identifier")
    add_common(id_parser)

    research_parser = sub.add_parser("research")
    research_parser.add_argument("query")
    research_parser.add_argument("--section")
    research_parser.add_argument("--limit", type=int, default=20)
    add_common(research_parser)

    args = parser.parse_args(argv)
    records = load_records()
    manifest = load_manifest()
    by_id = {record["id"]: record for record in records}
    orgs, artifact_providers = provider_maps(records)

    if args.command == "research":
        needle = args.query.casefold()
        matches = [
            row
            for row in load_research_rows()
            if needle in json.dumps(
                row["cells"], ensure_ascii=False
            ).casefold()
            and (
                not args.section
                or args.section.casefold() in row["section"].casefold()
            )
        ]
        if not matches:
            return typed_miss(args.query, manifest, args.json)
        emit_research(matches[: args.limit], manifest, args.json)
        return 0

    if args.command == "find":
        needle = args.query.casefold()
        matches = [
            record
            for record in records
            if needle in search_text(record)
            and (
                not args.record_type
                or record["record_type"] == args.record_type
            )
        ]
        matches.sort(key=lambda record: rank(record, args.query))
        if not matches:
            return typed_miss(args.query, manifest, args.json)
        emit(matches[: args.limit], as_json=args.json, manifest=manifest)
        return 0

    if args.command == "id":
        record = by_id.get(args.identifier)
        if not record:
            return typed_miss(args.identifier, manifest, args.json)
        emit([record], as_json=args.json, manifest=manifest)
        return 0

    if args.command == "artifacts":
        matches = [
            record
            for record in records
            if record["record_type"] == "artifact"
            and (
                not args.artifact_class
                or record["artifact_class"] == args.artifact_class
            )
            and (
                not args.provider
                or record_provider(
                    record, by_id, orgs, artifact_providers
                )
                == args.provider
            )
        ]
        emit(matches, as_json=args.json, manifest=manifest)
        return 0

    if args.command == "coverage":
        matches = [
            record
            for record in records
            if record["record_type"] == "coverage_ledger_entry"
            and (
                not args.status
                or record["coverage_status"] == args.status
            )
        ]
        emit(matches, as_json=args.json, manifest=manifest)
        return 0

    versions = [
        record
        for record in records
        if record["record_type"] == "artifact_version"
    ]
    chronology = []
    cutoff = getattr(args, "date", None)
    for version in versions:
        provider = record_provider(
            version, by_id, orgs, artifact_providers
        )
        artifact = by_id.get(version["artifact_id"], {})
        if getattr(args, "provider", None) and provider != args.provider:
            continue
        if getattr(args, "query", None):
            if args.query.casefold() not in (
                search_text(version) + " " + search_text(artifact)
            ):
                continue
        for assertion in version.get("date_assertions", []):
            value = assertion["value"]["value"]
            year = int(value[:4])
            if getattr(args, "from_year", None) and year < args.from_year:
                continue
            if getattr(args, "to_year", None) and year > args.to_year:
                continue
            if cutoff and parse_date_floor(value) > cutoff:
                continue
            chronology.append(
                {
                    "record_type": "date_assertion",
                    "id": version["id"],
                    "canonical_key": version["canonical_key"],
                    "title_native": artifact.get(
                        "preferred_title", version["title_native"]
                    ),
                    "date": value,
                    "date_role": assertion["date_role"],
                    "date_basis": assertion["value"].get("basis"),
                    "provider": provider,
                }
            )
    chronology.sort(
        key=lambda item: (
            item["date"],
            item["canonical_key"],
            item["date_role"],
        )
    )
    emit(chronology, as_json=args.json, manifest=manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

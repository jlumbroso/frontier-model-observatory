#!/usr/bin/env python3
"""Generate deterministic machine-readable projections of the chronology report."""

from __future__ import annotations

import argparse
import csv
import hashlib
from io import StringIO
import json
from pathlib import Path
import re
import shutil
import tempfile


ROOT = Path(__file__).resolve().parents[1]
REPORT = (
    ROOT
    / "docs"
    / "research"
    / "2026-09-05-primary-source-model-release-chronology.md"
)
OUTPUT = ROOT / "research" / "chronology"
TYPED_ABSENCES = {
    "not_reported",
    "not_found",
    "not_applicable",
    "withheld",
    "unknown",
}
URL_PATTERN = re.compile(r"https://[^)\]>\s]+")


def slug(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return normalized or "table"


def split_markdown_row(line: str) -> list[str]:
    value = line.strip()
    if not value.startswith("|") or not value.endswith("|"):
        raise ValueError(f"not a complete Markdown table row: {line!r}")
    cells = []
    current = []
    escaped = False
    code = False
    for character in value[1:-1]:
        if escaped:
            current.append(character)
            escaped = False
        elif character == "\\":
            current.append(character)
            escaped = True
        elif character == "`":
            current.append(character)
            code = not code
        elif character == "|" and not code:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(character)
    cells.append("".join(current).strip())
    return cells


def is_delimiter(line: str) -> bool:
    if not line.strip().startswith("|"):
        return False
    return all(
        re.fullmatch(r":?-{3,}:?", cell.replace(" ", ""))
        for cell in split_markdown_row(line)
    )


def extract_rows(report: Path = REPORT) -> tuple[dict, list[dict]]:
    payload = report.read_bytes()
    lines = payload.decode("utf-8").splitlines()
    section = ""
    table_counts: dict[str, int] = {}
    rows = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("##"):
            section = line.lstrip("#").strip()
        if (
            line.startswith("|")
            and index + 1 < len(lines)
            and is_delimiter(lines[index + 1])
        ):
            headers = split_markdown_row(line)
            section_key = slug(section)
            ordinal = table_counts.get(section_key, 0) + 1
            table_counts[section_key] = ordinal
            table_id = f"{section_key}/{ordinal}"
            row_index = 0
            index += 2
            while index < len(lines) and lines[index].startswith("|"):
                values = split_markdown_row(lines[index])
                if len(values) != len(headers):
                    raise ValueError(
                        f"line {index + 1}: table {table_id} has "
                        f"{len(values)} cells; expected {len(headers)}"
                    )
                row_index += 1
                cell_map = dict(zip(headers, values))
                text = "\n".join(values)
                rows.append(
                    {
                        "schema_version": 1,
                        "table_id": table_id,
                        "table_row": row_index,
                        "source_line": index + 1,
                        "section": section,
                        "cells": cell_map,
                        "urls": sorted(set(URL_PATTERN.findall(text))),
                        "typed_absences": sorted(
                            value
                            for value in TYPED_ABSENCES
                            if re.search(rf"\b{re.escape(value)}\b", text)
                        ),
                    }
                )
                index += 1
            continue
        index += 1

    table_count = len({row["table_id"] for row in rows})
    manifest = {
        "schema_version": 1,
        "source_report": str(report.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(payload).hexdigest(),
        "data_row_count": len(rows),
        "markdown_table_line_count": len(rows) + (2 * table_count),
        "table_count": table_count,
        "formats": ["jsonl", "json", "csv"],
        "semantic_status": "research_projection_not_canonical",
    }
    return manifest, rows


def render(output: Path, manifest: dict, rows: list[dict]) -> None:
    output.mkdir(parents=True, exist_ok=True)
    (output / "manifest.json").write_text(
        json.dumps(manifest, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    (output / "rows.jsonl").write_text(
        "".join(
            json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n"
            for row in rows
        ),
        encoding="utf-8",
    )
    (output / "rows.json").write_text(
        json.dumps(
            {"manifest": manifest, "rows": rows},
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    buffer = StringIO(newline="")
    fields = [
        "table_id",
        "table_row",
        "source_line",
        "section",
        "cells_json",
        "urls_json",
        "typed_absences_json",
    ]
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow(
            {
                "table_id": row["table_id"],
                "table_row": row["table_row"],
                "source_line": row["source_line"],
                "section": row["section"],
                "cells_json": json.dumps(
                    row["cells"], ensure_ascii=False, separators=(",", ":")
                ),
                "urls_json": json.dumps(row["urls"], separators=(",", ":")),
                "typed_absences_json": json.dumps(
                    row["typed_absences"], separators=(",", ":")
                ),
            }
        )
    (output / "rows.csv").write_text(buffer.getvalue(), encoding="utf-8")


def generate(output: Path = OUTPUT) -> tuple[dict, list[dict]]:
    manifest, rows = extract_rows()
    render(output, manifest, rows)
    return manifest, rows


def check() -> list[str]:
    errors = []
    with tempfile.TemporaryDirectory() as directory:
        expected = Path(directory) / "chronology"
        generate(expected)
        expected_files = {
            path.name: path.read_bytes()
            for path in expected.iterdir()
            if path.is_file()
        }
    actual_files = (
        {
            path.name: path.read_bytes()
            for path in OUTPUT.iterdir()
            if path.is_file()
        }
        if OUTPUT.exists()
        else {}
    )
    if expected_files != actual_files:
        errors.append(
            "chronology research projections are stale; "
            "run `just chronology-projections`"
        )
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
        print("chronology research projections: fresh")
        return 0
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    manifest, rows = generate()
    print(
        f"generated {manifest['data_row_count']} chronology data row(s) "
        f"across {manifest['table_count']} table(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

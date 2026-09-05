#!/usr/bin/env python3
"""Generate Markdown-only skill views from chronology research rows."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "research" / "chronology" / "rows.jsonl"
OUTPUT = (
    ROOT
    / "frontier-model-observatory"
    / "references"
    / "chronology"
)
VIEWS = {
    "anthropic.md": ("Anthropic chronology", ("2a.",)),
    "openai.md": ("OpenAI chronology", ("2b",)),
    "google.md": ("Google and Google DeepMind chronology", ("2c.",)),
    "aliases.md": ("Aliases and endpoint identifiers", ("3.",)),
    "availability.md": ("Product and deployment availability", ("4.",)),
    "knowledge-cutoffs.md": ("Knowledge cutoffs", ("5.",)),
    "lifecycle.md": ("Deprecations and retirements", ("6.",)),
    "contradictions-and-gaps.md": (
        "Contradictions, ambiguous identities, and typed gaps",
        ("7.",),
    ),
}
NAME_FIELDS = (
    "Exact provider-preferred name",
    "Exact name",
    "Entity / label",
    "Alias / endpoint",
    "Subject",
    "Model / entity",
    "Contradiction",
    "Ambiguous identity",
    "Gap",
)


def load_rows() -> list[dict]:
    return [
        json.loads(line)
        for line in SOURCE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def label(row: dict) -> str:
    for field in NAME_FIELDS:
        if row["cells"].get(field):
            return row["cells"][field]
    return next(iter(row["cells"].values()), "Research row")


def render(title: str, prefixes: tuple[str, ...], rows: list[dict]) -> str:
    selected = [
        row for row in rows if row["section"].startswith(prefixes)
    ]
    lines = [
        f"# {title}",
        "",
        "Generated from the official-source chronology observed 2026-09-05.",
        "These are research projections, not canonical records. Preserve typed",
        "gaps, date precision, and competing provider values.",
        "",
        f"Rows: **{len(selected)}**.",
        "",
    ]
    for row in selected:
        lines.extend(
            [
                f"## {label(row)}",
                "",
                f"- Source report line: `{row['source_line']}`",
                f"- Research section: {row['section']}",
            ]
        )
        for field, value in row["cells"].items():
            lines.append(f"- **{field}**: {value}")
        if row["typed_absences"]:
            lines.append(
                "- **Typed absences**: "
                + ", ".join(f"`{item}`" for item in row["typed_absences"])
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def generate(output: Path = OUTPUT) -> None:
    rows = load_rows()
    output.mkdir(parents=True, exist_ok=True)
    for filename, (title, prefixes) in VIEWS.items():
        (output / filename).write_text(
            render(title, prefixes, rows), encoding="utf-8"
        )
    index = [
        "# Chronology Markdown Views",
        "",
        "Use the smallest relevant file. No shell, Python, JSON, or database",
        "access is required.",
        "",
    ]
    for filename, (title, prefixes) in VIEWS.items():
        count = sum(row["section"].startswith(prefixes) for row in rows)
        index.append(f"- [{title}]({filename}): {count} research rows")
    (output / "README.md").write_text(
        "\n".join(index) + "\n", encoding="utf-8"
    )


def file_map(path: Path) -> dict[str, bytes]:
    if not path.exists():
        return {}
    return {
        str(item.relative_to(path)): item.read_bytes()
        for item in path.rglob("*")
        if item.is_file()
    }


def check() -> list[str]:
    with tempfile.TemporaryDirectory() as directory:
        expected_root = Path(directory) / "chronology"
        generate(expected_root)
        expected = file_map(expected_root)
    actual = file_map(OUTPUT)
    if actual != expected:
        return [
            "skill Markdown chronology views are stale; run `just skill`"
        ]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        errors = check()
        if errors:
            print("\n".join(errors))
            return 1
        print("skill Markdown chronology views: fresh")
        return 0
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    generate()
    print(f"generated {len(VIEWS)} Markdown chronology view(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

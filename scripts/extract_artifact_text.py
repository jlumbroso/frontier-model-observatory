#!/usr/bin/env python3
"""Extract deterministic text from materialized artifacts and audit policy."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]


class VisibleTextParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip_depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "svg", "noscript"}:
            self.skip_depth += 1
        elif not self.skip_depth and tag in {
            "p", "div", "section", "article", "header", "footer", "nav",
            "li", "tr", "h1", "h2", "h3", "h4", "br",
        }:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in {"script", "style", "svg", "noscript"} and self.skip_depth:
            self.skip_depth -= 1
        elif not self.skip_depth and tag in {
            "p", "div", "section", "article", "header", "footer", "nav",
            "li", "tr", "h1", "h2", "h3", "h4",
        }:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip_depth:
            self.parts.append(data)

    def text(self) -> str:
        lines = []
        blank = False
        for raw in "".join(self.parts).splitlines():
            line = " ".join(raw.split())
            if line:
                lines.append(line)
                blank = False
            elif lines and not blank:
                lines.append("")
                blank = True
        return "\n".join(lines).strip() + "\n"


def extract(path: Path, media_type: str) -> str:
    if media_type == "application/pdf":
        result = subprocess.run(
            ["pdftotext", "-layout", str(path), "-"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return result.stdout.decode("utf-8", errors="replace").rstrip() + "\n"
    if media_type == "text/html":
        parser = VisibleTextParser()
        parser.feed(path.read_text(encoding="utf-8"))
        return parser.text()
    if media_type.startswith("text/"):
        return path.read_text(encoding="utf-8").rstrip() + "\n"
    raise ValueError(f"no deterministic extractor for {media_type}")


def policy_rules(root: Path) -> list[tuple[str, re.Pattern[str]]]:
    policy = json.loads(
        (root / "policy" / "exclusions.json").read_text(encoding="utf-8")
    )
    return [
        (
            item["label"],
            re.compile(
                item["pattern"],
                re.IGNORECASE if item.get("ignore_case") else 0,
            ),
        )
        for item in policy["terms"]
    ]


def policy_matches(
    text: str, rules: list[tuple[str, re.Pattern[str]]]
) -> list[dict]:
    matches = []
    for label, pattern in rules:
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            matches.append(
                {
                    "label": label,
                    "line": line,
                    "excerpt": text[
                        max(0, match.start() - 50): match.end() + 50
                    ].replace("\n", " "),
                }
            )
    return matches


def audit(root: Path) -> tuple[list[dict], list[str]]:
    byte_records = [
        json.loads(line)
        for line in (root / "data" / "byte-objects.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip()
    ]
    rules = policy_rules(root)
    results = []
    errors = []
    for record in byte_records:
        storage = record["storage"]
        if storage["availability"] != "materialized":
            continue
        if record.get("derivation") not in {
            "provider_original", "captured_html"
        }:
            continue
        path = root / storage["locator"]
        text = extract(path, record["media_type_detected"])
        matches = policy_matches(text, rules)
        results.append(
            {
                "byte_object_id": record["id"],
                "path": str(path.relative_to(root)),
                "media_type": record["media_type_detected"],
                "text_length": len(text.encode("utf-8")),
                "policy_matches": matches,
            }
        )
        if matches:
            errors.append(
                f"{path.relative_to(root)}: {len(matches)} extracted-text "
                "policy match(es)"
            )
    return results, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("build/artifact-text-audit.json"),
    )
    args = parser.parse_args()
    root = args.root.resolve()
    results, errors = audit(root)
    report = root / args.report
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "audited_count": len(results),
                "results": results,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    if errors:
        print("\n".join(errors))
        return 1
    print(f"audited extracted text for {len(results)} materialized artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

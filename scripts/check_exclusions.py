#!/usr/bin/env python3
"""Reject excluded subject matter outside explicit governance files."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re
import subprocess
from typing import Iterable


@dataclass(frozen=True)
class Rule:
    label: str
    pattern: re.Pattern[str]


@dataclass(frozen=True)
class Violation:
    path: Path
    line: int
    label: str
    excerpt: str


def load_policy(path: Path) -> tuple[list[Rule], set[str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    rules = [
        Rule(
            item["label"],
            re.compile(
                item["pattern"],
                re.IGNORECASE if item.get("ignore_case", False) else 0,
            ),
        )
        for item in data["terms"]
    ]
    return rules, set(data["exempt_paths"])


def candidate_paths(root: Path) -> list[Path]:
    result = subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
            "-z",
        ],
        check=True,
        stdout=subprocess.PIPE,
    )
    return [
        root / item.decode()
        for item in result.stdout.split(b"\0")
        if item and (root / item.decode()).is_file()
    ]


def inspect_paths(
    root: Path,
    paths: Iterable[Path],
    rules: Iterable[Rule],
    exempt_paths: set[str],
) -> list[Violation]:
    violations: list[Violation] = []
    for path in paths:
        relative = path.relative_to(root).as_posix()
        if relative in exempt_paths:
            continue

        for rule in rules:
            if rule.pattern.search(relative):
                violations.append(
                    Violation(path, 0, rule.label, f"forbidden filename: {relative}")
                )

        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            for rule in rules:
                match = rule.pattern.search(line)
                if match:
                    excerpt = line[max(0, match.start() - 40) : match.end() + 40].strip()
                    violations.append(
                        Violation(path, line_number, rule.label, excerpt)
                    )
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path.cwd(), help="repository root"
    )
    parser.add_argument(
        "--policy",
        type=Path,
        default=Path("policy/exclusions.json"),
        help="policy path relative to root",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    rules, exempt_paths = load_policy(root / args.policy)
    violations = inspect_paths(
        root, candidate_paths(root), rules, exempt_paths
    )
    for violation in violations:
        relative = violation.path.relative_to(root)
        print(
            f"{relative}:{violation.line}: {violation.label}: "
            f"{violation.excerpt}"
        )
    if violations:
        print(f"{len(violations)} exclusion-policy violation(s)")
        return 1
    print("exclusion policy: clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

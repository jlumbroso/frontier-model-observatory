#!/usr/bin/env python3
"""List ADR questions by the status line inside each QST block.

This parser backs `just unanswered`. It deliberately ignores status-like text
outside QST sections and surfaces missing or unknown statuses so malformed
questions cannot silently disappear from the human's queue.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


QST_RE = re.compile(
    r"^### QST(?:-([A-Za-z0-9](?:[A-Za-z0-9-]{0,22}[A-Za-z0-9])?))?:\s*(.*)$"
)
STATUS_RE = re.compile(r"^- Status:\s*([A-Za-z-]+)(?:\s+—\s+.*)?$")
KNOWN_STATUSES = {
    "unanswered",
    "unresolved",
    "deferred",
    "answered",
    "withdrawn",
    "superseded",
    "moot",
}


@dataclass(frozen=True)
class Question:
    path: Path
    line: int
    handle: str
    title: str
    status: str | None


def parse_questions(path: Path) -> list[Question]:
    """Parse QST sections and their authoritative local Status lines."""
    questions: list[Question] = []
    current: dict[str, object] | None = None

    def finish() -> None:
        nonlocal current
        if current is not None:
            questions.append(Question(**current))  # type: ignore[arg-type]
            current = None

    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        heading = QST_RE.match(line)
        if heading:
            finish()
            current = {
                "path": path,
                "line": line_number,
                "handle": heading.group(1) or "QST",
                "title": heading.group(2).strip(),
                "status": None,
            }
            continue

        if current is not None and line.startswith("## "):
            finish()
            continue

        if current is not None and current["status"] is None:
            status = STATUS_RE.match(line)
            if status:
                current["status"] = status.group(1).lower()

    finish()
    return questions


def adr_paths(roots: Iterable[Path]) -> list[Path]:
    """Return numbered ADR files, excluding templates and working material."""
    found: set[Path] = set()
    for root in roots:
        if root.is_file():
            found.add(root)
        elif root.is_dir():
            found.update(root.glob("[0-9][0-9][0-9][0-9]-*.md"))
    return sorted(found)


def should_show(question: Question, requested: str | None) -> bool:
    """Unknown and missing statuses always surface, even under a filter."""
    if question.status is None or question.status not in KNOWN_STATUSES:
        return True
    return requested is None or question.status == requested


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, default=[Path("docs/adr")])
    parser.add_argument("--status", help="show this status plus malformed questions")
    args = parser.parse_args()

    questions = [
        question
        for path in adr_paths(args.paths)
        for question in parse_questions(path)
        if should_show(question, args.status)
    ]

    for question in questions:
        status = question.status or "MISSING"
        print(
            f"{question.path}:{question.line}: "
            f"{question.handle} [{status}] {question.title}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

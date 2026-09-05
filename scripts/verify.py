#!/usr/bin/env python3
"""Run repository checks and render a legible local/GitHub summary."""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from typing import Iterable

try:
    from scripts.adr_questions import adr_paths, parse_questions
except ModuleNotFoundError:  # Direct execution places scripts/ on sys.path.
    from adr_questions import adr_paths, parse_questions


STATUS_ICON = {
    "passed": "PASS",
    "failed": "FAIL",
    "not_implemented": "NOT IMPLEMENTED",
    "not_applicable": "NOT APPLICABLE",
}


@dataclass(frozen=True)
class CheckResult:
    key: str
    label: str
    status: str
    command: str | None
    duration_seconds: float
    details: str


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return result.stdout.strip()


def run_check(
    root: Path, key: str, label: str, command: list[str]
) -> CheckResult:
    start = time.monotonic()
    result = subprocess.run(
        command,
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    duration = time.monotonic() - start
    details = result.stdout.strip() or (
        "Command completed without output."
        if result.returncode == 0
        else f"Command exited {result.returncode} without output."
    )
    return CheckResult(
        key=key,
        label=label,
        status="passed" if result.returncode == 0 else "failed",
        command=" ".join(command),
        duration_seconds=round(duration, 3),
        details=details,
    )


def pending_check(key: str, label: str, details: str) -> CheckResult:
    return CheckResult(key, label, "not_implemented", None, 0.0, details)


def count_jsonl_rows(root: Path) -> tuple[int, int]:
    files = list((root / "data").rglob("*.jsonl")) if (root / "data").exists() else []
    rows = 0
    for path in files:
        with path.open(encoding="utf-8") as handle:
            rows += sum(1 for line in handle if line.strip())
    return len(files), rows


def count_files_and_bytes(path: Path) -> tuple[int, int]:
    if not path.exists():
        return 0, 0
    files = [candidate for candidate in path.rglob("*") if candidate.is_file()]
    return len(files), sum(candidate.stat().st_size for candidate in files)


def repository_metrics(root: Path) -> dict[str, object]:
    questions = [
        question
        for path in adr_paths([root / "docs" / "adr"])
        for question in parse_questions(path)
    ]
    status_counts: dict[str, int] = {}
    for question in questions:
        key = question.status or "missing"
        status_counts[key] = status_counts.get(key, 0) + 1

    data_files, data_rows = count_jsonl_rows(root)
    artifact_files, artifact_bytes = count_files_and_bytes(root / "artifacts")
    view_files, view_bytes = count_files_and_bytes(root / "views")
    skill_files, skill_bytes = count_files_and_bytes(
        root / "frontier-model-observatory"
    )
    schema_files = len(list((root / "schemas").rglob("*.schema.json"))) if (root / "schemas").exists() else 0

    return {
        "adr_documents": len(adr_paths([root / "docs" / "adr"])),
        "questions": status_counts,
        "schema_files": schema_files,
        "canonical_jsonl_files": data_files,
        "canonical_jsonl_rows": data_rows,
        "artifact_files": artifact_files,
        "artifact_bytes": artifact_bytes,
        "generated_view_files": view_files,
        "generated_view_bytes": view_bytes,
        "skill_files": skill_files,
        "skill_bytes": skill_bytes,
    }


def repository_context(root: Path) -> dict[str, object]:
    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    repository = os.environ.get("GITHUB_REPOSITORY")
    run_id = os.environ.get("GITHUB_RUN_ID")
    run_url = (
        f"{server}/{repository}/actions/runs/{run_id}"
        if repository and run_id
        else None
    )
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "revision": git(root, "rev-parse", "HEAD"),
        "branch": git(root, "branch", "--show-current") or "(detached)",
        "dirty": bool(git(root, "status", "--porcelain")),
        "event": os.environ.get("GITHUB_EVENT_NAME", "local"),
        "actor": os.environ.get("GITHUB_ACTOR", os.environ.get("USER", "unknown")),
        "repository": repository or git(root, "remote", "get-url", "origin"),
        "run_url": run_url,
    }


def escape_cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def human_bytes(value: int) -> str:
    units = ["B", "KiB", "MiB", "GiB"]
    amount = float(value)
    for unit in units:
        if amount < 1024 or unit == units[-1]:
            return f"{amount:.1f} {unit}"
        amount /= 1024
    raise AssertionError("unreachable")


def render_summary(
    context: dict[str, object],
    metrics: dict[str, object],
    checks: Iterable[CheckResult],
) -> str:
    checks = list(checks)
    lines = [
        "# Frontier Model Observatory verification",
        "",
        "## Run",
        "",
        f"- Revision: `{context['revision']}`",
        f"- Branch: `{context['branch']}`",
        f"- Event: `{context['event']}`",
        f"- Actor: `{context['actor']}`",
        f"- Working tree dirty at report time: `{str(context['dirty']).lower()}`",
        f"- Generated: `{context['generated_at']}`",
    ]
    if context.get("run_url"):
        lines.append(f"- Run: {context['run_url']}")

    lines.extend(
        [
            "",
            "## Check matrix",
            "",
            "| Check | Status | Duration | Command |",
            "|---|---:|---:|---|",
        ]
    )
    for check in checks:
        lines.append(
            "| "
            + " | ".join(
                [
                    escape_cell(check.label),
                    STATUS_ICON[check.status],
                    f"{check.duration_seconds:.3f}s",
                    f"`{escape_cell(check.command)}`" if check.command else "—",
                ]
            )
            + " |"
        )

    question_counts = metrics["questions"]
    lines.extend(
        [
            "",
            "## Repository metrics",
            "",
            f"- ADR documents: **{metrics['adr_documents']}**",
            f"- Questions by status: `{json.dumps(question_counts, sort_keys=True)}`",
            f"- JSON Schema documents: **{metrics['schema_files']}**",
            f"- Canonical JSONL: **{metrics['canonical_jsonl_files']} files / {metrics['canonical_jsonl_rows']} rows**",
            f"- Archive: **{metrics['artifact_files']} files / {human_bytes(int(metrics['artifact_bytes']))}**",
            f"- Generated views: **{metrics['generated_view_files']} files / {human_bytes(int(metrics['generated_view_bytes']))}**",
            f"- Skill tree: **{metrics['skill_files']} files / {human_bytes(int(metrics['skill_bytes']))}**",
            "",
            "## Details",
        ]
    )
    for check in checks:
        lines.extend(
            [
                "",
                f"### {check.label}: {STATUS_ICON[check.status]}",
                "",
                check.details,
            ]
        )
    lines.append("")
    return "\n".join(lines)


def checks_for(root: Path) -> list[CheckResult]:
    checks = [
        run_check(root, "diff", "Patch hygiene", ["git", "diff", "--check"]),
        run_check(
            root,
            "tests",
            "Behavioral and regression tests",
            [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
        ),
        run_check(
            root,
            "exclusions",
            "Repository exclusion policy",
            [sys.executable, "scripts/check_exclusions.py"],
        ),
    ]
    if (root / "schemas").exists():
        checks.append(
            run_check(
                root,
                "schemas",
                "Schema validation",
                [
                    sys.executable,
                    "scripts/validate_records.py",
                    "tests/fixtures/schema",
                    "--exclusion-policy",
                    "policy/exclusions.json",
                ],
            )
        )
    else:
        checks.append(
            pending_check("schemas", "Schema validation", "schemas does not exist yet.")
        )
    if (root / "data").exists():
        checks.append(
            run_check(
                root,
                "canonical",
                "Canonical record validation",
                [
                    sys.executable,
                    "scripts/validate_records.py",
                    "data",
                    "--exclusion-policy",
                    "policy/exclusions.json",
                ],
            )
        )
    else:
        checks.append(
            pending_check(
                "canonical",
                "Canonical record validation",
                "data does not exist yet.",
            )
        )
    if (root / "artifacts").exists() and (root / "data" / "byte-objects.jsonl").exists():
        checks.append(
            run_check(
                root,
                "archive",
                "Artifact integrity",
                [sys.executable, "scripts/check_artifacts.py"],
            )
        )
        checks.append(
            run_check(
                root,
                "artifact_text_policy",
                "Extracted artifact text policy",
                [sys.executable, "scripts/extract_artifact_text.py"],
            )
        )
        checks.append(
            run_check(
                root,
                "extracted_text_completeness",
                "Extracted-text completeness",
                [sys.executable, "scripts/materialize_extracted_text.py"],
            )
        )
    else:
        checks.append(
            pending_check(
                "archive",
                "Artifact integrity",
                "artifacts or data/byte-objects.jsonl does not exist yet.",
            )
        )
    if (root / "views").exists() and (root / "dist").exists():
        checks.append(
            run_check(
                root,
                "views",
                "Generated-view freshness",
                [sys.executable, "scripts/generate_views.py", "--check"],
            )
        )
    else:
        checks.append(
            pending_check(
                "views",
                "Generated-view freshness",
                "views or dist does not exist yet.",
            )
        )
    if (root / "frontier-model-observatory" / "SKILL.md").exists():
        checks.append(
            run_check(
                root,
                "skill",
                "Skill validation and packaging",
                [sys.executable, "scripts/check_skill.py"],
            )
        )
    else:
        checks.append(
            pending_check(
                "skill",
                "Skill validation and packaging",
                "frontier-model-observatory/SKILL.md does not exist yet.",
            )
        )
    subsystems = []
    for key, label, path in subsystems:
        if not path.exists():
            checks.append(
                pending_check(
                    key, label, f"{path.relative_to(root)} does not exist yet."
                )
            )
        else:
            checks.append(
                pending_check(
                    key,
                    label,
                    f"{path.relative_to(root)} exists, but its validator is not registered yet.",
                )
            )
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--json-out", type=Path, default=Path("build/verification.json"))
    parser.add_argument(
        "--summary-out", type=Path, default=Path("build/verification-summary.md")
    )
    parser.add_argument(
        "--require-complete",
        action="store_true",
        help="treat not-implemented subsystems as failures",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    checks = checks_for(root)
    context = repository_context(root)
    metrics = repository_metrics(root)
    payload = {
        "schema_version": 1,
        "context": context,
        "metrics": metrics,
        "checks": [asdict(check) for check in checks],
    }
    summary = render_summary(context, metrics, checks)

    json_out = root / args.json_out
    summary_out = root / args.summary_out
    json_out.parent.mkdir(parents=True, exist_ok=True)
    summary_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    summary_out.write_text(summary, encoding="utf-8")

    github_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if github_summary:
        with Path(github_summary).open("a", encoding="utf-8") as handle:
            handle.write(summary)

    print(summary)
    failed = any(check.status == "failed" for check in checks)
    incomplete = any(check.status == "not_implemented" for check in checks)
    return int(failed or (args.require_complete and incomplete))


if __name__ == "__main__":
    raise SystemExit(main())

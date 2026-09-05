#!/usr/bin/env python3
"""Check skill freshness, format, query behavior, and deterministic packaging."""

from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts import build_skill, package_skill


def main() -> int:
    errors = build_skill.check()
    if errors:
        print("\n".join(errors))
        return 1

    subprocess.run(
        ["agentskills", "validate", "frontier-model-observatory"],
        cwd=ROOT,
        check=True,
    )
    smoke = subprocess.run(
        [
            sys.executable,
            "frontier-model-observatory/scripts/query.py",
            "coverage",
            "--json",
        ],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    )
    if b'"coverage_scope_count": 12' not in smoke.stdout:
        print("skill query smoke test did not report twelve calibration scopes")
        return 1

    with tempfile.TemporaryDirectory() as first_dir, tempfile.TemporaryDirectory() as second_dir:
        first = Path(first_dir)
        second = Path(second_dir)
        first_manifest = package_skill.build(first)
        second_manifest = package_skill.build(second)
        first_bytes = (first / first_manifest["archive"]).read_bytes()
        second_bytes = (second / second_manifest["archive"]).read_bytes()
        if first_bytes != second_bytes:
            print("skill package is not deterministic")
            return 1

    package = package_skill.build(ROOT / "build" / "releases")
    digest = hashlib.sha256(
        (ROOT / "build" / "releases" / package["archive"]).read_bytes()
    ).hexdigest()
    if digest != package["sha256"]:
        print("release manifest digest does not match package")
        return 1
    print(
        f"skill verified: {package['file_count']} files, "
        f"{package['byte_length']} bytes, sha256={package['sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

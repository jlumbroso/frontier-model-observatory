#!/usr/bin/env python3
"""Validate and create a deterministic downloadable skill ZIP."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "frontier-model-observatory"
VERSION = "0.1.0"
ARCHIVE_NAME = f"frontier-model-observatory-{VERSION}.zip"
FIXED_TIME = (1980, 1, 1, 0, 0, 0)


def skill_files() -> list[Path]:
    return sorted(
        path
        for path in SKILL.rglob("*")
        if path.is_file()
        and "__pycache__" not in path.parts
        and path.suffix not in {".pyc", ".pyo"}
    )


def build(output_dir: Path) -> dict:
    subprocess.run(
        ["agentskills", "validate", str(SKILL)],
        cwd=ROOT,
        check=True,
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / ARCHIVE_NAME
    with zipfile.ZipFile(
        archive,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as package:
        for path in skill_files():
            relative = Path(SKILL.name) / path.relative_to(SKILL)
            info = zipfile.ZipInfo(str(relative), FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (
                0o755 if path.suffix == ".py" else 0o644
            ) << 16
            package.writestr(info, path.read_bytes())

    data = archive.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    checksum = output_dir / "SHA256SUMS"
    checksum.write_text(f"{digest}  {ARCHIVE_NAME}\n", encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "skill_name": "frontier-model-observatory",
        "skill_version": VERSION,
        "archive": ARCHIVE_NAME,
        "sha256": digest,
        "byte_length": len(data),
        "file_count": len(skill_files()),
        "snapshot_manifest": "frontier-model-observatory/data/snapshot-manifest.json",
    }
    (output_dir / "release-manifest.json").write_text(
        json.dumps(manifest, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "build" / "releases",
    )
    args = parser.parse_args()
    manifest = build(args.output_dir)
    print(
        f"packaged {manifest['archive']}: {manifest['file_count']} files, "
        f"{manifest['byte_length']} bytes, sha256={manifest['sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

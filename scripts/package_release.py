#!/usr/bin/env python3
"""Build deterministic skill and dataset assets for a GitHub Release."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts import build_skill, package_skill


FIXED_TIME = (1980, 1, 1, 0, 0, 0)
DATASET_FILES = [
    "fmo-records.jsonl",
    "fmo-records.json",
    "entities.csv",
    "artifacts.csv",
    "chronology.csv",
    "coverage.csv",
    "fmo.sqlite",
    "manifest.json",
]


def extracted_text_records() -> list[dict]:
    records = []
    for line in (
        ROOT / "data" / "byte-objects.jsonl"
    ).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        if record.get("derivation") == "extracted_text":
            records.append(record)
    return records


def build_extracted_text_archive(destination: Path, version: str) -> None:
    records = sorted(extracted_text_records(), key=lambda record: record["id"])
    manifest = {
        "schema_version": 1,
        "release_version": version,
        "derivation": "extracted_text",
        "records": [
            {
                "byte_object_id": record["id"],
                "sha256": record["sha256"],
                "byte_length": record["byte_length"],
                "derived_from_byte_ids": record["derived_from_byte_ids"],
                "archive_path": (
                    f"sha256/{record['sha256']}/extracted.txt"
                ),
            }
            for record in records
        ],
    }
    with zipfile.ZipFile(
        destination,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        info = zipfile.ZipInfo("manifest.json", FIXED_TIME)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        archive.writestr(
            info,
            (json.dumps(manifest, sort_keys=True, indent=2) + "\n").encode(),
        )
        for record in records:
            source = ROOT / record["storage"]["locator"]
            archive_path = f"sha256/{record['sha256']}/extracted.txt"
            info = zipfile.ZipInfo(archive_path, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, source.read_bytes())


def build(output: Path, version: str) -> dict:
    if version != build_skill.VERSION:
        raise ValueError(
            f"release version {version} does not match skill version "
            f"{build_skill.VERSION}"
        )
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    with tempfile.TemporaryDirectory() as directory:
        skill_manifest = package_skill.build(Path(directory))
        skill_archive = Path(directory) / skill_manifest["archive"]
        shutil.copyfile(skill_archive, output / skill_archive.name)

    assets = [output / skill_manifest["archive"]]
    text_archive = output / f"fmo-extracted-text-{version}.zip"
    build_extracted_text_archive(text_archive, version)
    assets.append(text_archive)
    for filename in DATASET_FILES:
        source = ROOT / "dist" / filename
        destination = output / (
            "dataset-manifest.json" if filename == "manifest.json" else filename
        )
        shutil.copyfile(source, destination)
        assets.append(destination)

    asset_rows = [
        {
            "filename": path.name,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "byte_length": path.stat().st_size,
        }
        for path in sorted(assets)
    ]
    release_manifest = {
        "schema_version": 1,
        "release_version": version,
        "skill_version": build_skill.VERSION,
        "snapshot_date": build_skill.SNAPSHOT_DATE,
        "assets": asset_rows,
    }
    manifest_path = output / "release-manifest.json"
    manifest_path.write_text(
        json.dumps(release_manifest, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    manifest_row = {
        "filename": manifest_path.name,
        "sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "byte_length": manifest_path.stat().st_size,
    }
    all_rows = [*asset_rows, manifest_row]
    (output / "SHA256SUMS").write_text(
        "".join(
            f"{row['sha256']}  {row['filename']}\n"
            for row in sorted(all_rows, key=lambda item: item["filename"])
        ),
        encoding="utf-8",
    )
    return release_manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default=build_skill.VERSION)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "build" / "release",
    )
    args = parser.parse_args()
    manifest = build(args.output_dir, args.version)
    print(
        f"built release {args.version}: {len(manifest['assets'])} primary assets"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Verify materialized archive bytes against canonical byte-object records."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import subprocess

try:
    from scripts.validate_records import read_jsonl
except ModuleNotFoundError:  # Direct execution places scripts/ on sys.path.
    from validate_records import read_jsonl


def detected_media_type(data: bytes) -> str:
    if data.startswith(b"%PDF-"):
        return "application/pdf"
    prefix = data[:512].lstrip().lower()
    if prefix.startswith((b"<!doctype html", b"<html")):
        return "text/html"
    try:
        data.decode("utf-8")
    except UnicodeDecodeError:
        return "application/octet-stream"
    return "text/plain"


def inspect_materialized(
    root: Path, record: dict, check_lfs: bool = True
) -> list[str]:
    errors: list[str] = []
    locator = record["storage"].get("locator")
    if not locator:
        return [f"{record['id']}: materialized byte has no locator"]
    path = (root / locator).resolve()
    try:
        relative = path.relative_to(root.resolve())
    except ValueError:
        return [f"{record['id']}: storage path escapes repository root"]
    if not path.is_file():
        return [f"{record['id']}: missing materialized file {relative}"]

    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != record["sha256"]:
        errors.append(f"{record['id']}: SHA-256 mismatch for {relative}")
    if len(data) != record["byte_length"]:
        errors.append(f"{record['id']}: byte-length mismatch for {relative}")
    detected = detected_media_type(data)
    if detected != record["media_type_detected"]:
        errors.append(
            f"{record['id']}: media type {detected}, "
            f"record says {record['media_type_detected']}"
        )

    if record.get("derivation") == "provider_original":
        expected_prefix = Path("artifacts") / "sha256" / digest[:2] / digest
        if expected_prefix not in relative.parents:
            errors.append(
                f"{record['id']}: provider original is not under "
                f"{expected_prefix}"
            )

    if check_lfs and record["storage"]["backend"] == "git_lfs":
        result = subprocess.run(
            ["git", "-C", str(root), "check-attr", "filter", "--", str(relative)],
            check=True,
            stdout=subprocess.PIPE,
            text=True,
        )
        if not result.stdout.rstrip().endswith("filter: lfs"):
            errors.append(f"{record['id']}: {relative} is not tracked by Git LFS")
    return errors


def check_archive(root: Path) -> tuple[int, int, list[str]]:
    records, framing_errors = read_jsonl(root / "data" / "byte-objects.jsonl")
    errors = list(framing_errors)
    materialized = [
        record
        for _path, _line, record in records
        if record.get("storage", {}).get("availability") == "materialized"
    ]
    for record in materialized:
        errors.extend(inspect_materialized(root, record))

    referenced = {
        (root / record["storage"]["locator"]).resolve()
        for record in materialized
        if record.get("storage", {}).get("locator")
    }
    for path in (root / "artifacts").rglob("*"):
        if path.is_file() and path.name != "README.md" and path.resolve() not in referenced:
            errors.append(f"{path.relative_to(root)}: unreferenced archive file")
    return len(materialized), sum(record["byte_length"] for record in materialized), errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    count, byte_length, errors = check_archive(args.root.resolve())
    if errors:
        print("\n".join(errors))
        return 1
    print(f"verified {count} materialized byte object(s), {byte_length} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

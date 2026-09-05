#!/usr/bin/env python3
"""Mint one opaque typed FMO identifier."""

from __future__ import annotations

import argparse
import uuid


KINDS = {
    "org",
    "family",
    "model",
    "checkpoint",
    "configuration",
    "product",
    "deployment",
    "endpoint",
    "alias",
    "event",
    "artifact",
    "artifact-version",
    "url",
    "redirect",
    "part",
    "artifact-relationship",
    "claim",
    "retrieval",
    "absence",
    "coverage",
}


def mint(kind: str) -> str:
    if kind not in KINDS:
        raise ValueError(f"unknown identifier kind: {kind}")
    generator = getattr(uuid, "uuid7", uuid.uuid4)
    return f"fmo:{kind}:{generator()}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=sorted(KINDS))
    args = parser.parse_args()
    print(mint(args.kind))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

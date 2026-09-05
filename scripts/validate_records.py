#!/usr/bin/env python3
"""JSONL framing, Draft 2020-12, and cross-record semantic validation."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from referencing import Registry, Resource
except ImportError as exc:
    raise SystemExit("Install the declared dependency: python -m pip install -r requirements.txt") from exc

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas" / "1.0.0"
TYPE_SCHEMA = {
    "entity": "entity.schema.json", "event": "event.schema.json",
    "artifact": "artifact.schema.json", "artifact_version": "artifact-version.schema.json",
    "byte_object": "byte-object.schema.json", "url_alias": "url-alias.schema.json",
    "redirect_observation": "redirect-observation.schema.json",
    "artifact_part": "artifact-part.schema.json",
    "artifact_relationship": "artifact-relationship.schema.json",
    "claim": "claim.schema.json", "retrieval_event": "retrieval-event.schema.json",
    "absence": "absence.schema.json", "coverage_ledger_entry": "coverage-ledger-entry.schema.json"
}

def load_schemas():
    schemas = [json.loads(p.read_text(encoding="utf-8")) for p in SCHEMA_DIR.glob("*.schema.json")]
    for schema in schemas:
        Draft202012Validator.check_schema(schema)
    registry = Registry().with_resources(
        [(s["$id"], Resource.from_contents(s)) for s in schemas if "$id" in s]
    )
    return {p.name: json.loads(p.read_text(encoding="utf-8"))
            for p in SCHEMA_DIR.glob("*.schema.json")}, registry

def read_jsonl(path: Path):
    raw = path.read_bytes()
    errors = []
    if raw and not raw.endswith(b"\n"):
        errors.append(f"{path}: missing terminal LF")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        return [], [f"{path}: not UTF-8: {exc}"]
    records = []
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            errors.append(f"{path}:{number}: blank line")
            continue
        try:
            records.append((path, number, json.loads(line, object_pairs_hook=_no_duplicate_keys)))
        except (json.JSONDecodeError, ValueError) as exc:
            errors.append(f"{path}:{number}: {exc}")
    return records, errors

def _no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result

def schema_validate(records, schemas, registry):
    errors = []
    validators = {
        t: Draft202012Validator(schemas[name], registry=registry, format_checker=FormatChecker())
        for t, name in TYPE_SCHEMA.items()
    }
    for path, line, record in records:
        rtype = record.get("record_type")
        if rtype not in validators:
            errors.append(f"{path}:{line}: unknown record_type {rtype!r}")
            continue
        for err in sorted(validators[rtype].iter_errors(record), key=lambda e: list(e.absolute_path)):
            loc = "/".join(str(x) for x in err.absolute_path)
            errors.append(f"{path}:{line}:{loc}: {err.message}")
    return errors

def walk_values(value, key=None):
    if isinstance(value, dict):
        for k, v in value.items():
            yield from walk_values(v, k)
    elif isinstance(value, list):
        for v in value:
            yield from walk_values(v, key)
    else:
        yield key, value

def detect_cycle(edges):
    visiting, done = set(), set()
    def visit(node):
        if node in visiting:
            return True
        if node in done:
            return False
        visiting.add(node)
        for target in edges.get(node, set()):
            if target and visit(target):
                return True
        visiting.remove(node)
        done.add(node)
        return False
    return any(visit(node) for node in edges)

def time_floor(value):
    text = value["value"]
    if value["precision"] == "year":
        text += "-01-01"
    elif value["precision"] == "month":
        text += "-01"
    if value["precision"] == "instant":
        return datetime.fromisoformat(text.replace("Z", "+00:00")).timestamp()
    return datetime.fromisoformat(text).timestamp()

def semantic_validate(records):
    errors, by_id, key_seen = [], {}, {}
    for path, line, r in records:
        rid = r.get("id")
        if rid in by_id:
            errors.append(f"{path}:{line}: duplicate id {rid}")
        by_id[rid] = (path, line, r)
        if r.get("record_type") != "byte_object":
            pair = (r.get("record_type"), r.get("canonical_key"))
            if pair in key_seen:
                errors.append(f"{path}:{line}: duplicate canonical_key within record_type {pair}")
            key_seen[pair] = rid
        if r.get("record_type") == "byte_object":
            expected = "fmo:sha256:" + r.get("sha256", "")
            if rid != expected:
                errors.append(f"{path}:{line}: byte id does not equal sha256")

    # Foreign keys are explicit *_id(s), typed refs, and byte IDs.
    for path, line, r in records:
        for key, value in walk_values(r):
            candidates = []
            if isinstance(value, str) and value.startswith("fmo:") and key != "id":
                if key and (key.endswith("_id") or key.endswith("_ids") or key in {"target_id", "configures_id"}):
                    candidates = [value]
            for ref in candidates:
                if ref not in by_id:
                    errors.append(f"{path}:{line}: unresolved reference {ref}")
        for key, value in _walk_dicts(r):
            if key != "root" and isinstance(value, dict) and set(("id", "record_type")).issubset(value):
                target = by_id.get(value["id"])
                if target and target[2].get("record_type") != value["record_type"]:
                    errors.append(f"{path}:{line}: typed reference {value['id']} says {value['record_type']}")

    # Name/containment/part/alias and supersession cycles.
    edge_fields = ["parent_org_id", "parent_family_id", "parent_part_id"]
    for field in edge_fields:
        edges = {r["id"]: {r[field]} for _, _, r in records if field in r}
        if detect_cycle(edges):
            errors.append(f"semantic: cycle in {field}")
    alias_edges = {r["id"]: r["target_id"] for _, _, r in records
                   if r.get("record_type") == "entity" and r.get("kind") == "alias"}
    for source, target in alias_edges.items():
        target_record = by_id.get(target, (None, None, {}))[2]
        if target_record.get("kind") == "alias":
            errors.append(f"semantic: alias {source} targets another alias")
    for field in ["supersedes_version_ids", "supersedes_claim_ids", "supersedes_event_ids"]:
        edges = {}
        for _, _, r in records:
            for target in r.get(field, []):
                edges.setdefault(r["id"], set()).add(target)
        if detect_cycle(edges):
            errors.append(f"semantic: cycle in {field}")

    # Temporal ordering for any extent carrying comparable endpoints.
    for path, line, r in records:
        for _, value in _walk_dicts(r):
            if isinstance(value, dict) and value.get("status") == "known" and "start" in value and "end" in value:
                if time_floor(value["start"]) > time_floor(value["end"]):
                    errors.append(f"{path}:{line}: temporal extent ends before it starts")

    # Ordered redirect chain and retrieval final URL.
    redirects = {}
    for _, _, r in records:
        if r.get("record_type") == "redirect_observation":
            redirects.setdefault(r["retrieval_event_id"], []).append(r)
    for retrieval_id, hops in redirects.items():
        hops.sort(key=lambda x: x["hop_index"])
        if [h["hop_index"] for h in hops] != list(range(len(hops))):
            errors.append(f"semantic: redirect hops for {retrieval_id} are not contiguous")
        for left, right in zip(hops, hops[1:]):
            if left["to_url_id"] != right["from_url_id"]:
                errors.append(f"semantic: redirect chain discontinuity for {retrieval_id}")
        retrieval = by_id.get(retrieval_id, (None, None, {}))[2]
        if hops and retrieval.get("final_url_id") != hops[-1]["to_url_id"]:
            errors.append(f"semantic: final URL disagrees with redirect chain for {retrieval_id}")

    # Materialized byte checks.
    for path, line, r in records:
        if r.get("record_type") == "byte_object" and r["storage"]["availability"] == "materialized":
            locator = r["storage"].get("locator")
            if not locator:
                errors.append(f"{path}:{line}: materialized byte has no locator")
                continue
            file_path = (ROOT / locator).resolve()
            try:
                file_path.relative_to(ROOT)
            except ValueError:
                errors.append(f"{path}:{line}: materialized byte escapes repository root")
                continue
            if not file_path.is_file():
                errors.append(f"{path}:{line}: materialized byte missing at {locator}")
                continue
            data = file_path.read_bytes()
            if hashlib.sha256(data).hexdigest() != r["sha256"] or len(data) != r["byte_length"]:
                errors.append(f"{path}:{line}: materialized byte hash/length mismatch")

    # Stronger family rules.
    for path, line, r in records:
        if r.get("record_type") == "absence" and r.get("absence_type") == "not_found":
            if "next_check_at" not in r:
                errors.append(f"{path}:{line}: not_found absence requires next_check_at")
        if r.get("record_type") == "coverage_ledger_entry":
            status = r["coverage_status"]
            if status == "covered" and not r.get("covered_record_ids"):
                errors.append(f"{path}:{line}: covered entry needs covered_record_ids")
            if status in {"not_found", "confirmed_absent"} and not r.get("absence_ids"):
                errors.append(f"{path}:{line}: {status} entry needs absence_ids")
        if r.get("record_type") == "artifact_relationship" and r["source_ref"]["id"] == r["target_ref"]["id"]:
            errors.append(f"{path}:{line}: artifact relationship self-edge")
    return errors

def _walk_dicts(value, key="root"):
    if isinstance(value, dict):
        yield key, value
        for k, v in value.items():
            yield from _walk_dicts(v, k)
    elif isinstance(value, list):
        for v in value:
            yield from _walk_dicts(v, key)

def exclusion_validate(paths, policy_path):
    if not policy_path:
        return []
    policy = json.loads(Path(policy_path).read_text(encoding="utf-8"))
    errors = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for term in policy["terms"]:
            flags = re.IGNORECASE if term.get("ignore_case") else 0
            if re.search(term["pattern"], text, flags):
                errors.append(f"{path}: repository exclusion policy match ({term['label']})")
    return errors

def collect_paths(inputs):
    paths = []
    for raw in inputs:
        p = Path(raw)
        paths.extend(sorted(p.rglob("*.jsonl")) if p.is_dir() else [p])
    return paths

def validate(inputs, exclusion_policy=None):
    paths = collect_paths(inputs)
    schemas, registry = load_schemas()
    records, errors = [], []
    for path in paths:
        found, framing = read_jsonl(path)
        records.extend(found)
        errors.extend(framing)
    errors.extend(schema_validate(records, schemas, registry))
    errors.extend(semantic_validate(records))
    errors.extend(exclusion_validate(paths, exclusion_policy))
    return records, errors

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="+")
    parser.add_argument("--exclusion-policy")
    args = parser.parse_args(argv)
    records, errors = validate(args.inputs, args.exclusion_policy)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"validated {len(records)} records from {len(collect_paths(args.inputs))} JSONL file(s)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

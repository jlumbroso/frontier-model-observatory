import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import validate_records as validate

class CandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records, cls.errors = validate.validate(
            [ROOT / "tests" / "fixtures" / "schema"]
        )
        cls.raw = [r for _, _, r in cls.records]

    def test_complete_example_set_validates(self):
        self.assertEqual([], self.errors)
        kinds = {r["record_type"] for r in self.raw}
        self.assertEqual(set(validate.TYPE_SCHEMA), kinds)
        entity_kinds = {r["kind"] for r in self.raw if r["record_type"] == "entity"}
        self.assertEqual({"organization","model_family","model","checkpoint","configuration",
                          "product","deployment","endpoint","alias"}, entity_kinds)

    def test_canonical_keys_are_unique_within_type(self):
        mutated = copy.deepcopy(self.raw)
        artifacts = [r for r in mutated if r["record_type"] == "artifact"]
        artifacts[1]["canonical_key"] = artifacts[0]["canonical_key"]
        errors = validate.semantic_validate([(Path("memory"), i, r) for i, r in enumerate(mutated)])
        self.assertTrue(any("duplicate canonical_key" in e for e in errors))

    def test_foreign_keys_cannot_use_canonical_keys(self):
        schemas, registry = validate.load_schemas()
        record = copy.deepcopy(next(r for r in self.raw if r.get("kind") == "model"))
        record["provider_org_id"] = "google-deepmind"
        errors = validate.schema_validate([(Path("memory"), 1, record)], schemas, registry)
        self.assertTrue(any("provider_org_id" in e for e in errors))

    def test_not_found_requires_recheck(self):
        record = copy.deepcopy(next(r for r in self.raw if r["record_type"] == "absence"))
        del record["next_check_at"]
        errors = validate.semantic_validate([(Path("memory"), 1, record)])
        self.assertTrue(any("requires next_check_at" in e for e in errors))

    def test_redirect_final_url_must_match_chain(self):
        mutated = copy.deepcopy(self.raw)
        retrieval = next(r for r in mutated if r["record_type"] == "retrieval_event")
        retrieval["final_url_id"] = retrieval["requested_url_id"]
        errors = validate.semantic_validate([(Path("memory"), i, r) for i, r in enumerate(mutated)])
        self.assertTrue(any("final URL disagrees" in e for e in errors))

    def test_temporal_extent_rejects_reverse_interval(self):
        record = copy.deepcopy(next(r for r in self.raw if r["record_type"] == "event"))
        record["valid_time"] = {"status": "known",
            "start": {"value": "2026-09-05", "precision": "day"},
            "end": {"value": "2025-09-25", "precision": "day"}}
        errors = validate.semantic_validate([(Path("memory"), 1, record)])
        self.assertTrue(any("ends before" in e for e in errors))

    def test_calibration_matrix_has_all_twelve_subjects_and_stresses(self):
        matrix = json.loads(
            (ROOT / "tests" / "fixtures" / "calibration-matrix.json").read_text()
        )
        self.assertEqual(12, len(matrix))
        features = {feature for row in matrix for feature in row["features"]}
        required = {"changelog","configurations","two_byte_versions","system_prompt",
                    "preview_ga","three_level_chain","evaluation_correction","html_only",
                    "date_conflict","prospective_scope","artifact_part","open_weights"}
        self.assertTrue(required <= features)

    def test_multiple_supersession_edges_do_not_hide_a_cycle(self):
        """A node's second edge must not overwrite the edge that closes a cycle."""
        ids = [
            "fmo:claim:00000000-0000-4000-8000-000000000101",
            "fmo:claim:00000000-0000-4000-8000-000000000102",
            "fmo:claim:00000000-0000-4000-8000-000000000103",
        ]
        records = [
            {
                "record_type": "claim",
                "id": ids[0],
                "canonical_key": "cycle/a",
                "supersedes_claim_ids": [ids[1], ids[2]],
            },
            {
                "record_type": "claim",
                "id": ids[1],
                "canonical_key": "cycle/b",
                "supersedes_claim_ids": [ids[0]],
            },
            {
                "record_type": "claim",
                "id": ids[2],
                "canonical_key": "cycle/c",
            },
        ]
        errors = validate.semantic_validate(
            [(Path("memory"), i, record) for i, record in enumerate(records)]
        )
        self.assertTrue(any("cycle in supersedes_claim_ids" in e for e in errors))

    def test_claim_object_type_controls_value_shape(self):
        """A boolean claim cannot carry a numeric value merely because JSON accepts it."""
        schemas, registry = validate.load_schemas()
        record = copy.deepcopy(
            next(r for r in self.raw if r.get("claim_kind") == "assertion")
        )
        record["object"] = {"type": "boolean", "value": 1}
        errors = validate.schema_validate(
            [(Path("memory"), 1, record)], schemas, registry
        )
        self.assertTrue(any("object/value" in e for e in errors))

    def test_materialized_byte_cannot_escape_repository(self):
        """A storage locator must not make integrity validation read outside the repo."""
        record = copy.deepcopy(
            next(r for r in self.raw if r["record_type"] == "byte_object")
        )
        record["storage"] = {
            "backend": "git",
            "availability": "materialized",
            "locator": "../outside.pdf",
        }
        errors = validate.semantic_validate([(Path("memory"), 1, record)])
        self.assertTrue(any("escapes repository root" in e for e in errors))

    def test_native_vocabulary_can_remain_responsibly_unmapped(self):
        """Source-native terminology must not require a premature normalization."""
        schemas, registry = validate.load_schemas()
        record = copy.deepcopy(next(r for r in self.raw if r.get("kind") == "model"))
        record["modalities"] = [{"native": "provider-specific combined modality"}]
        errors = validate.schema_validate(
            [(Path("memory"), 1, record)], schemas, registry
        )
        self.assertEqual([], errors)

    def test_synthetic_records_cannot_masquerade_as_provider_evidence(self):
        """Structural fixtures use reserved hosts and explicit fixture names."""
        text = (
            ROOT / "tests" / "fixtures" / "schema" / "all-records.jsonl"
        ).read_text(encoding="utf-8")
        self.assertIn("example.invalid", text)
        self.assertIn("Fixture Provider", text)
        for provider_host in (
            "anthropic.com",
            "openai.com",
            "deepmind.google",
            "googleapis.com",
        ):
            self.assertNotIn(provider_host, text)

    def test_url_alias_preserves_identity_bearing_fragment(self):
        """A page anchor is evidence and must not be normalized away."""
        schemas, registry = validate.load_schemas()
        record = copy.deepcopy(
            next(r for r in self.raw if r["record_type"] == "url_alias")
        )
        record["url"] = record["url"].rstrip("/") + "/report.pdf#page=30"
        record["url_normalized"] = record["url"]
        record["fragment"] = "page=30"
        errors = validate.schema_validate(
            [(Path("memory"), 1, record)], schemas, registry
        )
        self.assertEqual([], errors)

    def test_canonical_stream_rejects_wrong_type_and_order(self):
        """Homogeneous, ID-sorted streams are part of the canonical contract."""
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            data = Path(directory) / "data"
            data.mkdir()
            path = data / "entities.jsonl"
            rows = [
                (path, 1, {"id": "fmo:model:z", "record_type": "entity"}),
                (path, 2, {"id": "fmo:model:a", "record_type": "artifact"}),
            ]
            old_root = validate.ROOT
            try:
                validate.ROOT = Path(directory)
                errors = validate.canonical_stream_validate(rows)
            finally:
                validate.ROOT = old_root

        self.assertTrue(any("expects entity" in error for error in errors))
        self.assertTrue(any("not sorted by id" in error for error in errors))

    def test_entity_canonical_key_is_unique_across_entity_kinds(self):
        """A family and model cannot silently share one grep-facing handle."""
        mutated = copy.deepcopy(self.raw)
        family = next(r for r in mutated if r.get("kind") == "model_family")
        model = next(r for r in mutated if r.get("kind") == "model")
        model["canonical_key"] = family["canonical_key"]
        errors = validate.semantic_validate(
            [(Path("memory"), i, record) for i, record in enumerate(mutated)]
        )
        self.assertTrue(any("duplicate canonical_key" in error for error in errors))

    def test_coverage_can_reference_content_addressed_bytes(self):
        """Coverage evidence includes both UUID records and SHA-256 byte objects."""
        schemas, registry = validate.load_schemas()
        record = copy.deepcopy(
            next(
                r
                for r in self.raw
                if r["record_type"] == "coverage_ledger_entry"
            )
        )
        byte_id = next(
            r["id"] for r in self.raw if r["record_type"] == "byte_object"
        )
        record["covered_record_ids"].append(byte_id)
        errors = validate.schema_validate(
            [(Path("memory"), 1, record)], schemas, registry
        )
        self.assertEqual([], errors)

if __name__ == "__main__":
    unittest.main()

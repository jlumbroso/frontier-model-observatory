"""Behavioral tests for reusable canonical ingestion mechanics."""

import hashlib
from pathlib import Path
import tempfile
import unittest

from scripts.canonical_store import CanonicalStore


class CanonicalStoreTests(unittest.TestCase):
    def make_store(self, root: Path) -> CanonicalStore:
        (root / "data").mkdir()
        return CanonicalStore(
            root, "2026-09-05T00:00:00Z", "2026-09-05"
        )

    def test_entity_upsert_preserves_first_minted_identity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = self.make_store(Path(directory))
            first = store.entity(
                "organization", "fixture-provider", "Fixture Provider",
                roles=["provider"],
            )
            second = store.entity(
                "organization", "fixture-provider", "Fixture Provider",
                roles=["provider"],
            )
        self.assertEqual(first, second)

    def test_entity_key_cannot_change_kind(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = self.make_store(Path(directory))
            store.entity(
                "organization", "fixture-provider", "Fixture Provider",
                roles=["provider"],
            )
            with self.assertRaisesRegex(ValueError, "belongs to organization"):
                store.entity(
                    "model_family",
                    "fixture-provider",
                    "Wrong reuse",
                    provider_org_id="fmo:org:00000000-0000-4000-8000-000000000001",
                )

    def test_policy_blocked_capture_can_be_hashed_without_materializing(self) -> None:
        content = b"<html>policy-blocked source bytes</html>"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            store = self.make_store(root)
            source = root / "capture.html"
            source.write_bytes(content)
            ident, length, digest = store.byte_object(
                source,
                media_type="text/html",
                derivation="captured_html",
                materialize=False,
                materialized_name="capture.html",
            )
            record = store.streams["byte-objects.jsonl"][0]

        self.assertEqual(digest, hashlib.sha256(content).hexdigest())
        self.assertEqual(ident, f"fmo:sha256:{digest}")
        self.assertEqual(length, len(content))
        self.assertEqual(record["storage"]["availability"], "remote_only")
        self.assertNotIn("locator", record["storage"])


if __name__ == "__main__":
    unittest.main()

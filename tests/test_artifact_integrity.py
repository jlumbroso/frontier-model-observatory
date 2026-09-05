"""Behavioral tests for content-addressed archive integrity."""

import hashlib
from pathlib import Path
import tempfile
import unittest

from scripts.check_artifacts import detected_media_type, inspect_materialized


class ArtifactIntegrityTests(unittest.TestCase):
    def test_valid_content_addressed_pdf_passes(self) -> None:
        data = b"%PDF-1.7\nfixture\n"
        digest = hashlib.sha256(data).hexdigest()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            relative = (
                Path("artifacts")
                / "sha256"
                / digest[:2]
                / digest
                / "original.pdf"
            )
            path = root / relative
            path.parent.mkdir(parents=True)
            path.write_bytes(data)
            record = {
                "id": f"fmo:sha256:{digest}",
                "sha256": digest,
                "byte_length": len(data),
                "media_type_detected": "application/pdf",
                "storage": {
                    "backend": "git",
                    "availability": "materialized",
                    "locator": str(relative),
                },
                "derivation": "provider_original",
            }
            errors = inspect_materialized(root, record, check_lfs=False)

        self.assertEqual([], errors)

    def test_wrong_hash_length_and_type_are_all_reported(self) -> None:
        data = b"not a pdf"
        claimed = "0" * 64
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            relative = (
                Path("artifacts")
                / "sha256"
                / claimed[:2]
                / claimed
                / "original.pdf"
            )
            path = root / relative
            path.parent.mkdir(parents=True)
            path.write_bytes(data)
            record = {
                "id": f"fmo:sha256:{claimed}",
                "sha256": claimed,
                "byte_length": 999,
                "media_type_detected": "application/pdf",
                "storage": {
                    "backend": "git",
                    "availability": "materialized",
                    "locator": str(relative),
                },
                "derivation": "provider_original",
            }
            errors = inspect_materialized(root, record, check_lfs=False)

        self.assertTrue(any("SHA-256 mismatch" in error for error in errors))
        self.assertTrue(any("byte-length mismatch" in error for error in errors))
        self.assertTrue(any("media type" in error for error in errors))

    def test_media_sniffing_distinguishes_pdf_html_and_text(self) -> None:
        self.assertEqual("application/pdf", detected_media_type(b"%PDF-1.4"))
        self.assertEqual("text/html", detected_media_type(b" <!doctype html>"))
        self.assertEqual("text/plain", detected_media_type("hello".encode()))


if __name__ == "__main__":
    unittest.main()

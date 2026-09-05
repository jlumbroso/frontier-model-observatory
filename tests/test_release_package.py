"""Tests for complete deterministic release assets."""

from pathlib import Path
from io import BytesIO
import json
import tempfile
import unittest
import zipfile

from scripts import package_release


class ReleasePackageTests(unittest.TestCase):
    def test_release_assets_are_deterministic_and_complete(self) -> None:
        with tempfile.TemporaryDirectory() as first_dir, tempfile.TemporaryDirectory() as second_dir:
            first = Path(first_dir)
            second = Path(second_dir)
            package_release.build(first, "0.1.0")
            package_release.build(second, "0.1.0")
            first_files = {
                path.name: path.read_bytes()
                for path in first.iterdir()
                if path.is_file()
            }
            second_files = {
                path.name: path.read_bytes()
                for path in second.iterdir()
                if path.is_file()
            }

        self.assertEqual(first_files, second_files)
        self.assertIn("frontier-model-observatory-0.1.0.zip", first_files)
        self.assertIn("fmo-extracted-text-0.1.0.zip", first_files)
        self.assertIn("fmo-records.jsonl", first_files)
        self.assertIn("fmo.sqlite", first_files)
        self.assertIn("dataset-manifest.json", first_files)
        self.assertIn("release-manifest.json", first_files)
        self.assertIn("SHA256SUMS", first_files)
        with zipfile.ZipFile(
            BytesIO(first_files["fmo-extracted-text-0.1.0.zip"])
        ) as archive:
            names = archive.namelist()
            manifest = json.loads(archive.read("manifest.json"))
        self.assertEqual(13, len(manifest["records"]))
        self.assertEqual(14, len(names))
        self.assertTrue(
            all(
                item["derived_from_byte_ids"]
                for item in manifest["records"]
            )
        )


if __name__ == "__main__":
    unittest.main()

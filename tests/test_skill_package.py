"""Regression tests for deterministic skill release artifacts."""

from pathlib import Path
import tempfile
import unittest
import zipfile

from scripts import package_skill


class SkillPackageTests(unittest.TestCase):
    def test_package_is_deterministic_and_has_one_root(self) -> None:
        with tempfile.TemporaryDirectory() as first_dir, tempfile.TemporaryDirectory() as second_dir:
            first = Path(first_dir)
            second = Path(second_dir)
            first_manifest = package_skill.build(first)
            second_manifest = package_skill.build(second)
            first_archive = first / first_manifest["archive"]
            second_archive = second / second_manifest["archive"]

            self.assertEqual(
                first_archive.read_bytes(), second_archive.read_bytes()
            )
            with zipfile.ZipFile(first_archive) as archive:
                names = archive.namelist()

        self.assertTrue(names)
        self.assertTrue(
            all(name.startswith("frontier-model-observatory/") for name in names)
        )
        self.assertIn("frontier-model-observatory/SKILL.md", names)
        self.assertIn(
            "frontier-model-observatory/data/snapshot-manifest.json", names
        )
        self.assertFalse(any("__pycache__" in name for name in names))


if __name__ == "__main__":
    unittest.main()

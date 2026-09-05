"""Behavioral tests for deterministic redundant projections."""

import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from scripts.generate_views import generate_views, read_records


ROOT = Path(__file__).resolve().parents[1]


class GeneratedViewsTests(unittest.TestCase):
    def test_generation_is_deterministic_and_complete(self) -> None:
        records = read_records(ROOT)
        with tempfile.TemporaryDirectory() as first_dir, tempfile.TemporaryDirectory() as second_dir:
            first = Path(first_dir)
            second = Path(second_dir)
            generate_views(ROOT, first / "views", first / "dist")
            generate_views(ROOT, second / "views", second / "dist")

            first_files = {
                str(path.relative_to(first)): path.read_bytes()
                for path in first.rglob("*")
                if path.is_file()
            }
            second_files = {
                str(path.relative_to(second)): path.read_bytes()
                for path in second.rglob("*")
                if path.is_file()
            }

        self.assertEqual(first_files, second_files)
        self.assertIn("views/by-provider/anthropic/README.md", first_files)
        self.assertIn("views/by-provider/openai/README.md", first_files)
        self.assertIn(
            "views/by-provider/google-deepmind/README.md", first_files
        )
        self.assertEqual(
            len(records),
            len(
                [
                    line
                    for line in first_files[
                        "dist/fmo-records.jsonl"
                    ].decode().splitlines()
                    if line
                ]
            ),
        )

    def test_calibration_view_has_all_twelve_scopes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            generate_views(ROOT, root / "views", root / "dist")
            text = (root / "views" / "calibration" / "coverage.md").read_text()
        self.assertEqual(12, text.count("| `calibration/"))

    def test_sqlite_contains_every_canonical_record(self) -> None:
        expected = len(read_records(ROOT))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            generate_views(ROOT, root / "views", root / "dist")
            connection = sqlite3.connect(root / "dist" / "fmo.sqlite")
            try:
                actual = connection.execute(
                    "SELECT COUNT(*) FROM records"
                ).fetchone()[0]
            finally:
                connection.close()
        self.assertEqual(expected, actual)

    def test_manifest_binds_every_generated_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            generate_views(ROOT, root / "views", root / "dist")
            manifest = json.loads(
                (root / "dist" / "manifest.json").read_text()
            )
            listed = {item["path"] for item in manifest["files"]}
            actual = {
                str(path.relative_to(root))
                for base in (root / "views", root / "dist")
                for path in base.rglob("*")
                if path.is_file() and path.name != "manifest.json"
            }
        self.assertEqual(listed, actual)

    def test_csv_projections_use_lf_line_endings(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            generate_views(ROOT, root / "views", root / "dist")
            csv_files = list((root / "dist").glob("*.csv"))
            self.assertTrue(csv_files)
            for path in csv_files:
                self.assertNotIn(b"\r\n", path.read_bytes(), path.name)


if __name__ == "__main__":
    unittest.main()

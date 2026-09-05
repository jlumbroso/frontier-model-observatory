"""Behavioral tests for chronology research projections."""

from pathlib import Path
import tempfile
import unittest

from scripts.generate_chronology_research import extract_rows, generate


class ChronologyResearchProjectionTests(unittest.TestCase):
    def test_every_table_row_preserves_source_and_cells(self):
        manifest, rows = extract_rows()
        self.assertEqual(438, manifest["data_row_count"])
        self.assertEqual(464, manifest["markdown_table_line_count"])
        self.assertEqual(manifest["data_row_count"], len(rows))
        self.assertTrue(all(row["source_line"] > 0 for row in rows))
        self.assertTrue(all(row["cells"] for row in rows))
        self.assertTrue(
            all(row["table_id"] and row["section"] for row in rows)
        )

    def test_generation_is_deterministic_and_lf_only(self):
        with tempfile.TemporaryDirectory() as first_directory:
            with tempfile.TemporaryDirectory() as second_directory:
                first = Path(first_directory)
                second = Path(second_directory)
                generate(first)
                generate(second)
                first_files = {
                    path.name: path.read_bytes() for path in first.iterdir()
                }
                second_files = {
                    path.name: path.read_bytes() for path in second.iterdir()
                }
        self.assertEqual(first_files, second_files)
        self.assertNotIn(b"\r\n", first_files["rows.csv"])


if __name__ == "__main__":
    unittest.main()

"""Repository contracts for content-addressed extracted text."""

from pathlib import Path
import subprocess
import sys
import unittest

from scripts.materialize_extracted_text import (
    check,
    eligible_sources,
    extracted_by_source,
)


ROOT = Path(__file__).resolve().parents[1]


class ExtractedTextMaterializationTests(unittest.TestCase):
    def test_verifier_runs_as_a_direct_script(self):
        result = subprocess.run(
            [sys.executable, "scripts/materialize_extracted_text.py"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.assertEqual(0, result.returncode, result.stderr)

    def test_every_eligible_source_has_a_verified_derivative(self):
        self.assertEqual([], check(ROOT))
        self.assertEqual(
            {record["id"] for record in eligible_sources(ROOT)},
            set(extracted_by_source(ROOT)),
        )


if __name__ == "__main__":
    unittest.main()

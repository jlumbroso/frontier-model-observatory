"""Behavioral tests for legible verification summaries."""

from pathlib import Path
import sys
import tempfile
import unittest

from scripts.verify import CheckResult, render_summary, run_check


class VerificationSummaryTests(unittest.TestCase):
    def test_runner_preserves_success_and_failure_evidence(self) -> None:
        """A failed command must remain legible rather than collapse to a badge."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            passed = run_check(
                root,
                "pass",
                "Passing check",
                [sys.executable, "-c", "print('evidence retained')"],
            )
            failed = run_check(
                root,
                "fail",
                "Failing check",
                [sys.executable, "-c", "print('specific failure'); raise SystemExit(3)"],
            )

        self.assertEqual(passed.status, "passed")
        self.assertIn("evidence retained", passed.details)
        self.assertEqual(failed.status, "failed")
        self.assertIn("specific failure", failed.details)

    def test_summary_distinguishes_all_typed_states(self) -> None:
        """Not implemented and not applicable must never render as success."""
        context = {
            "revision": "abc123",
            "branch": "main",
            "event": "test",
            "actor": "tester",
            "dirty": False,
            "generated_at": "2026-09-05T00:00:00+00:00",
            "run_url": None,
        }
        metrics = {
            "adr_documents": 7,
            "questions": {"answered": 8},
            "canonical_jsonl_files": 0,
            "canonical_jsonl_rows": 0,
            "artifact_files": 0,
            "artifact_bytes": 0,
            "generated_view_files": 0,
            "generated_view_bytes": 0,
            "skill_files": 0,
            "skill_bytes": 0,
        }
        checks = [
            CheckResult("a", "Pass", "passed", "true", 0.1, "ok"),
            CheckResult(
                "b", "Fail", "failed", "false | tee evidence.log", 0.2, "bad | exact"
            ),
            CheckResult("c", "Pending", "not_implemented", None, 0.0, "later"),
            CheckResult("d", "N/A", "not_applicable", None, 0.0, "irrelevant"),
        ]

        summary = render_summary(context, metrics, checks)

        self.assertIn("PASS", summary)
        self.assertIn("FAIL", summary)
        self.assertIn("NOT IMPLEMENTED", summary)
        self.assertIn("NOT APPLICABLE", summary)
        self.assertIn("`false \\| tee evidence.log`", summary)
        self.assertIn("bad | exact", summary)


if __name__ == "__main__":
    unittest.main()

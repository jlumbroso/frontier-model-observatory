"""Regression tests for the ADR question queue promised by repository docs."""

from pathlib import Path
import tempfile
import unittest

from scripts.adr_questions import parse_questions, should_show


class AdrQuestionRegressionTests(unittest.TestCase):
    def test_status_belongs_to_its_qst_not_nearby_examples(self) -> None:
        """A prose/example status must not put an answered QST back on the queue."""
        content = """\
# ADR

- Status: unanswered

### QST-FIRST: First question?
- Status: answered

Example: `- Status: unanswered`

### QST-SECOND: Second question?
- Status: unanswered — routing to Jérémie
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "0001-example.md"
            path.write_text(content, encoding="utf-8")
            questions = parse_questions(path)

        self.assertEqual(
            [(q.handle, q.status) for q in questions],
            [("FIRST", "answered"), ("SECOND", "unanswered")],
        )
        self.assertFalse(should_show(questions[0], "unanswered"))
        self.assertTrue(should_show(questions[1], "unanswered"))

    def test_unknown_or_missing_status_never_silently_vanishes(self) -> None:
        """Recall-first behavior shows malformed questions under any filter."""
        content = """\
### QST-UNKNOWN: New vocabulary?
- Status: awaiting-review

### QST-MISSING: Forgot the status?
No status was written.
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "0002-example.md"
            path.write_text(content, encoding="utf-8")
            questions = parse_questions(path)

        self.assertTrue(all(should_show(q, "unanswered") for q in questions))


if __name__ == "__main__":
    unittest.main()

"""Behavioral and regression tests for the repository exclusion guard."""

from pathlib import Path
import re
import tempfile
import unittest

from scripts.check_exclusions import Rule, inspect_paths


class ExclusionPolicyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.rules = [
            Rule(
                "organization",
                re.compile(
                    r"\b(?:Meta (?:Platforms|AI|models?|company|products?|"
                    r"weights?|releases?|events?)|(?:from|by) Meta)\b",
                    re.IGNORECASE,
                ),
            ),
            Rule("model", re.compile(r"\bLlama(?:Guard)?\b", re.IGNORECASE)),
        ]

    def test_rejects_excluded_subject_in_corpus_record(self) -> None:
        """A real provider record must not bypass the ethical scope decision."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            record = root / "data" / "models.jsonl"
            record.parent.mkdir()
            record.write_text('{"provider":"Meta AI","family":"Llama"}\n')

            violations = inspect_paths(root, [record], self.rules, set())

        self.assertEqual(len(violations), 2)

    def test_does_not_reject_epistemic_vocabulary(self) -> None:
        """Substring matching must not ban core words such as metadata."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            record = root / "docs" / "method.md"
            record.parent.mkdir()
            record.write_text(
                "Preserve metadata, metacognition, and Meta-Observation headings.\n",
                encoding="utf-8",
            )

            violations = inspect_paths(root, [record], self.rules, set())

        self.assertEqual(violations, [])

    def test_governance_path_is_explicitly_exempt(self) -> None:
        """The policy must be able to state the subject it prohibits."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            policy = root / "docs" / "EXCLUSION-POLICY.md"
            policy.parent.mkdir()
            policy.write_text("Meta AI and Llama are excluded.\n")

            violations = inspect_paths(
                root, [policy], self.rules, {"docs/EXCLUSION-POLICY.md"}
            )

        self.assertEqual(violations, [])


if __name__ == "__main__":
    unittest.main()

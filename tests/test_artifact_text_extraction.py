"""Tests for deterministic visible-text extraction and policy auditing."""

import unittest

from scripts.extract_artifact_text import (
    VisibleTextParser,
    policy_rules,
    policy_matches,
)


from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ArtifactTextExtractionTests(unittest.TestCase):
    def test_html_extraction_removes_scripts_but_preserves_visible_text(self):
        parser = VisibleTextParser()
        parser.feed(
            "<html><style>hidden style</style><body><h1>Title</h1>"
            "<script>hidden script</script><p>Visible text</p></body></html>"
        )
        text = parser.text()
        self.assertIn("Title", text)
        self.assertIn("Visible text", text)
        self.assertNotIn("hidden style", text)
        self.assertNotIn("hidden script", text)

    def test_extracted_text_is_checked_with_repository_policy_rules(self):
        # Construct the excluded organization name at runtime so the regression
        # fixture itself remains policy-clean under the repository text scan.
        excluded_name = "Me" + "ta"
        matches = policy_matches(
            f"benchmark material released by {excluded_name}",
            policy_rules(ROOT),
        )
        self.assertTrue(matches)
        self.assertEqual(matches[0]["line"], 1)


if __name__ == "__main__":
    unittest.main()

"""Static contracts for legible, pinned GitHub workflows."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"


class WorkflowContractTests(unittest.TestCase):
    def test_every_action_is_pinned_to_full_commit(self) -> None:
        for path in WORKFLOWS.glob("*.yml"):
            with self.subTest(path=path.name):
                for line in path.read_text().splitlines():
                    if "uses:" not in line:
                        continue
                    value = line.split("uses:", 1)[1].strip().split()[0]
                    self.assertRegex(value, r"^[^@]+@[0-9a-f]{40}$")

    def test_verify_workflow_has_complete_summary_contract(self) -> None:
        text = (WORKFLOWS / "verify.yml").read_text()
        self.assertIn("just verify-complete", text)
        self.assertIn("GITHUB_STEP_SUMMARY", text)
        self.assertIn("if: always()", text)
        self.assertIn("lfs: true", text)
        self.assertIn("contents: read", text)
        self.assertIn("just install-ci-system-dependencies", text)

    def test_release_workflow_publishes_downloadable_skill(self) -> None:
        text = (WORKFLOWS / "release.yml").read_text()
        self.assertIn("just package-release", text)
        self.assertIn("gh release upload", text)
        self.assertIn("build/release/SHA256SUMS", text)
        self.assertIn("GITHUB_STEP_SUMMARY", text)
        self.assertIn("contents: write", text)
        self.assertIn("just install-ci-system-dependencies", text)

    def test_no_workflow_uses_mutable_action_tag(self) -> None:
        text = "\n".join(
            path.read_text() for path in WORKFLOWS.glob("*.yml")
        )
        self.assertIsNone(re.search(r"uses:\s+\S+@v\d", text))


if __name__ == "__main__":
    unittest.main()

"""Contracts for skill-only and Markdown-only graceful degradation."""

from pathlib import Path
import tempfile
import unittest

from scripts import generate_skill_markdown


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "frontier-model-observatory" / "SKILL.md"


class SkillMarkdownFallbackTests(unittest.TestCase):
    def test_skill_only_payload_explains_itself_and_resolves_fable(self):
        text = SKILL.read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        body = text.split("# Frontier Model Observatory", 1)[1]
        opening = body[:800]
        self.assertIn("NO SHELL OR FILE ACCESS? START HERE", opening)
        self.assertIn("## No-tools orientation", opening)
        self.assertLess(
            text.index("## No-tools orientation"),
            text.index("## Capability upgrades"),
        )
        self.assertIn("## What this skill does", text)
        self.assertIn("## Capability upgrades", text)
        self.assertIn("### Embedded release index", text)
        self.assertIn("Claude Fable 5 is not Claude Opus 5", text)
        self.assertIn("SKILL-only", text)
        self.assertIn(
            "Do not infer identity from naming resemblance", normalized
        )
        self.assertIn("GPT-6 Astra", opening + text)
        self.assertIn("Lyria 3.5", text)
        self.assertIn("tool-enabled-workflow.md", text)

    def test_markdown_views_are_deterministic_and_partitioned(self):
        with tempfile.TemporaryDirectory() as first_directory:
            with tempfile.TemporaryDirectory() as second_directory:
                first = Path(first_directory)
                second = Path(second_directory)
                generate_skill_markdown.generate(first)
                generate_skill_markdown.generate(second)
                self.assertEqual(
                    generate_skill_markdown.file_map(first),
                    generate_skill_markdown.file_map(second),
                )
        self.assertEqual([], generate_skill_markdown.check())
        self.assertEqual(
            set(generate_skill_markdown.VIEWS) | {"README.md"},
            set(generate_skill_markdown.file_map(
                ROOT
                / "frontier-model-observatory"
                / "references"
                / "chronology"
            )),
        )
        chronology = (
            ROOT
            / "frontier-model-observatory"
            / "references"
            / "chronology"
        )
        self.assertIn(
            "Claude Fable 5",
            (chronology / "anthropic.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "GPT-5.6 Sol",
            (chronology / "openai.md").read_text(encoding="utf-8"),
        )


if __name__ == "__main__":
    unittest.main()

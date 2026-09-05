"""Behavioral tests for the packaged model-facing query interface."""

import contextlib
import io
import json
from pathlib import Path
import runpy
import unittest

from scripts import build_skill


ROOT = Path(__file__).resolve().parents[1]
QUERY = (
    ROOT
    / "frontier-model-observatory"
    / "scripts"
    / "query.py"
)


class SkillQueryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        build_skill.build(
            ROOT / "frontier-model-observatory" / "data"
        )
        namespace = runpy.run_path(str(QUERY), run_name="skill_query_tests")
        cls.main = staticmethod(namespace["main"])

    def invoke(self, argv: list[str]) -> tuple[int, str]:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = self.main(argv)
        return result, output.getvalue()

    def test_find_resolves_unfamiliar_model(self) -> None:
        code, output = self.invoke(["find", "Claude Opus 5", "--json"])
        payload = json.loads(output)
        self.assertEqual(0, code)
        self.assertTrue(
            any(
                item.get("canonical_key") == "anthropic/claude-opus-5"
                for item in payload["results"]
            )
        )
        self.assertFalse(payload["snapshot"]["comprehensive"])

    def test_unknown_name_is_typed_not_found(self) -> None:
        code, output = self.invoke(["find", "Definitely Unknown Model", "--json"])
        payload = json.loads(output)
        self.assertEqual(2, code)
        self.assertEqual("not_found", payload["status"])
        self.assertNotIn("confirmed_absent", output)

    def test_coverage_contains_twelve_calibration_scopes(self) -> None:
        code, output = self.invoke(["coverage", "--json"])
        payload = json.loads(output)
        self.assertEqual(0, code)
        self.assertEqual(12, len(payload["results"]))

    def test_timeline_preserves_date_roles(self) -> None:
        code, output = self.invoke(
            ["timeline", "--provider", "openai", "--json"]
        )
        payload = json.loads(output)
        roles = {item["date_role"] for item in payload["results"]}
        self.assertEqual(0, code)
        self.assertIn("cover_date", roles)
        self.assertIn("transport_last_modified", roles)

    def test_as_of_filters_future_date_assertions(self) -> None:
        code, output = self.invoke(
            ["as-of", "2025-12-31", "GPT-5.2", "--json"]
        )
        payload = json.loads(output)
        self.assertEqual(0, code)
        self.assertTrue(payload["results"])
        self.assertTrue(
            all(item["date"] <= "2025-12-31" for item in payload["results"])
        )

    def test_built_snapshot_matches_canonical_distribution(self) -> None:
        self.assertEqual([], build_skill.check())


if __name__ == "__main__":
    unittest.main()

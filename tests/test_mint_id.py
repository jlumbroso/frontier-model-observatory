"""Tests for stable identifier minting grammar."""

import re
import unittest

from scripts.mint_id import KINDS, mint


class MintIdTests(unittest.TestCase):
    def test_every_supported_kind_matches_typed_uuid_grammar(self) -> None:
        pattern = re.compile(
            r"^fmo:[a-z-]+:[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-"
            r"[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
        )
        for kind in KINDS:
            with self.subTest(kind=kind):
                self.assertRegex(mint(kind), pattern)

    def test_unknown_kind_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown identifier kind"):
            mint("model-card")


if __name__ == "__main__":
    unittest.main()

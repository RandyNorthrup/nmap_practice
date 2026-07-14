from __future__ import annotations

from pathlib import Path
import sys
import unittest


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import common  # noqa: E402


class TargetSafetyTests(unittest.TestCase):
    def test_accepts_private_loopback_and_link_local_targets(self) -> None:
        for target in (
            "localhost",
            "127.0.0.1",
            "10.20.30.40",
            "172.31.255.1",
            "192.168.50.0/24",
            "169.254.1.2",
            "fd00::1",
            "fe80::1",
        ):
            with self.subTest(target=target):
                self.assertTrue(common.is_private_target(target))

    def test_rejects_public_invalid_and_option_like_targets(self) -> None:
        self.assertFalse(common.is_private_target("8.8.8.8"))
        self.assertFalse(common.is_private_target("172.32.0.1"))
        self.assertFalse(common.is_private_target("198.51.100.1"))
        with self.assertRaisesRegex(ValueError, "Public or unresolved"):
            common.authorize_target("8.8.8.8", allow_public=False)
        with self.assertRaisesRegex(ValueError, "Invalid target syntax"):
            common.authorize_target("-iL", allow_public=True)

    def test_public_target_requires_explicit_opt_in(self) -> None:
        common.authorize_target("scanme.example", allow_public=True)


class PortValidationTests(unittest.TestCase):
    def test_accepts_lists_and_ranges(self) -> None:
        self.assertEqual("22,80,8000-8010", common.validate_port_spec("22,80,8000-8010"))
        self.assertEqual(
            "T:22,80,U:53,123",
            common.validate_port_spec("T:22,80,U:53,123"),
        )

    def test_rejects_bad_or_out_of_range_ports(self) -> None:
        for value in ("0", "65536", "22;whoami", "80,", "abc", "80-22", "22,U:"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                common.validate_port_spec(value)


if __name__ == "__main__":
    unittest.main()

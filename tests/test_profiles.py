from __future__ import annotations

from contextlib import redirect_stderr
import io
from pathlib import Path
import tempfile
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))
from profile_runner import run_profile  # noqa: E402
from profiles import PROFILES  # noqa: E402


class ProfileRegistryTests(unittest.TestCase):
    def test_catalog_exceeds_requested_hundred_scripts(self) -> None:
        self.assertGreaterEqual(len(PROFILES), 100)

    def test_every_profile_has_matching_entry_script(self) -> None:
        missing = [name for name in PROFILES if not (SCRIPTS / f"{name}.py").is_file()]
        self.assertEqual([], missing)

    def test_every_entry_script_names_its_profile(self) -> None:
        for name in PROFILES:
            with self.subTest(profile=name):
                source = (SCRIPTS / f"{name}.py").read_text(encoding="utf-8")
                self.assertIn(f'PROFILE_NAME = "{name}"', source)

    def test_high_risk_profiles_are_loopback_only(self) -> None:
        unsafe = [
            item.name for item in PROFILES.values()
            if item.risk == "high" and item.scope != "loopback"
        ]
        self.assertEqual([], unsafe)

    def test_no_brute_dos_exploit_or_fuzzer_profiles(self) -> None:
        forbidden = ("brute", "dos", "exploit", "fuzzer")
        unsafe = []
        for item in PROFILES.values():
            command = " ".join(item.arguments).lower()
            if any(word in command for word in forbidden):
                unsafe.append(item.name)
        self.assertEqual([], unsafe)

    def test_every_profile_builds_a_loopback_dry_run(self) -> None:
        with tempfile.TemporaryDirectory() as directory, redirect_stderr(io.StringIO()):
            for item in PROFILES.values():
                with self.subTest(profile=item.name):
                    output = str(Path(directory) / item.name)
                    self.assertEqual(
                        0,
                        run_profile(item, ["127.0.0.1", "--output", output, "--dry-run"]),
                    )

    def test_private_and_loopback_locks_cannot_use_public_opt_in(self) -> None:
        private = next(item for item in PROFILES.values() if item.scope == "private")
        loopback = next(item for item in PROFILES.values() if item.scope == "loopback")
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                run_profile(private, ["8.8.8.8", "--allow-public", "--dry-run"])
            with self.assertRaises(SystemExit):
                run_profile(loopback, ["192.168.1.2", "--dry-run"])


if __name__ == "__main__":
    unittest.main()

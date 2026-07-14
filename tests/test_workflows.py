from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SAMPLE = ROOT / "tests" / "fixtures" / "sample.xml"


class WorkflowTests(unittest.TestCase):
    def run_script(self, name: str, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPTS / name), *args],
            capture_output=True,
            text=True,
            check=False,
            cwd=ROOT,
        )

    def test_profile_catalog_json(self) -> None:
        result = self.run_script("profile_catalog.py", "--category", "discovery", "--json")
        self.assertEqual(0, result.returncode, result.stderr)
        items = json.loads(result.stdout)
        self.assertGreater(len(items), 5)
        self.assertTrue(all(item["category"] == "discovery" for item in items))

    def test_report_commands(self) -> None:
        expectations = {
            "report_summary.py": "127.0.0.1",
            "report_json.py": '"addresses":',
            "report_csv.py": "address,hostnames",
            "report_markdown.py": "| Host | Protocol/port |",
            "report_hosts.py": "127.0.0.1",
            "report_open_ports.py": "tcp/22",
            "report_services.py": "ssh:",
            "report_scripts.py": "ssh-hostkey",
            "report_validate.py": "VALID:",
        }
        for script, text in expectations.items():
            with self.subTest(script=script):
                result = self.run_script(script, str(SAMPLE))
                self.assertEqual(0, result.returncode, result.stderr)
                self.assertIn(text, result.stdout)

    def test_batch_profile_dry_run(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            targets = Path(directory) / "targets.txt"
            targets.write_text("127.0.0.1\n# comment\n192.168.1.2\n", encoding="utf-8")
            result = self.run_script(
                "batch_profile.py", "scan_tcp_top_10", str(targets),
                "--output-dir", directory, "--dry-run",
            )
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertEqual(2, result.stderr.count("Dry run: Nmap was not started."))

    def test_watch_profile_is_bounded_in_dry_run(self) -> None:
        result = self.run_script(
            "watch_profile.py", "scan_tcp_top_10", "127.0.0.1",
            "--count", "2", "--dry-run",
        )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(2, result.stderr.count("Dry run: Nmap was not started."))

    def test_rescan_open_ports_dry_run(self) -> None:
        result = self.run_script("rescan_open_ports.py", str(SAMPLE), "--dry-run")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("scan_services.py", result.stdout)
        self.assertIn("scan_udp.py", result.stdout)


if __name__ == "__main__":
    unittest.main()

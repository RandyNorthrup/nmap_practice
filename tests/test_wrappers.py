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
MOCK_NMAP = ROOT / "tests" / "fixtures" / "mock_nmap.py"


class WrapperTests(unittest.TestCase):
    def run_script(self, script: str, *arguments: str) -> tuple[subprocess.CompletedProcess[str], list[str]]:
        with tempfile.TemporaryDirectory() as directory:
            log = Path(directory) / "arguments.json"
            output = Path(directory) / "report"
            environment = os.environ.copy()
            environment.update({"NMAP_BIN": str(MOCK_NMAP), "MOCK_NMAP_LOG": str(log)})
            process = subprocess.run(
                [sys.executable, str(SCRIPTS / script), *arguments, "--output", str(output)],
                capture_output=True,
                text=True,
                env=environment,
                check=False,
            )
            recorded = json.loads(log.read_text(encoding="utf-8")) if log.exists() else []
            return process, recorded

    def test_tcp_wrapper_builds_expected_command(self) -> None:
        process, arguments = self.run_script(
            "scan_ports.py", "127.0.0.1", "--ports", "22,80-82"
        )
        self.assertEqual(0, process.returncode, process.stderr)
        self.assertIn("-sT", arguments)
        self.assertEqual("22,80-82", arguments[arguments.index("-p") + 1])
        self.assertEqual("127.0.0.1", arguments[-1])

    def test_discovery_wrapper_does_not_request_port_scan(self) -> None:
        process, arguments = self.run_script("scan_discovery.py", "192.168.1.0/24")
        self.assertEqual(0, process.returncode, process.stderr)
        self.assertIn("-sn", arguments)
        self.assertNotIn("-sT", arguments)

    def test_service_and_web_use_case_flags(self) -> None:
        service, service_args = self.run_script(
            "scan_services.py", "127.0.0.1", "--ports", "8000"
        )
        web, web_args = self.run_script("scan_web.py", "127.0.0.1", "--ports", "8000")
        self.assertEqual(0, service.returncode, service.stderr)
        self.assertIn("-sV", service_args)
        self.assertEqual(0, web.returncode, web.stderr)
        self.assertIn("http-title,http-headers", web_args)

    def test_public_target_is_blocked_before_nmap_runs(self) -> None:
        process, arguments = self.run_script("scan_ports.py", "8.8.8.8")
        self.assertNotEqual(0, process.returncode)
        self.assertEqual([], arguments)
        self.assertIn("Public or unresolved target blocked", process.stderr)

    def test_public_target_can_be_explicitly_allowed(self) -> None:
        process, arguments = self.run_script(
            "scan_ports.py", "scanme.example", "--allow-public"
        )
        self.assertEqual(0, process.returncode, process.stderr)
        self.assertEqual("scanme.example", arguments[-1])

    def test_all_scan_scripts_have_working_help(self) -> None:
        scripts = (
            "scan_discovery.py",
            "scan_ports.py",
            "scan_services.py",
            "scan_safe_scripts.py",
            "scan_udp.py",
            "scan_web.py",
            "scan_route.py",
            "scan_os.py",
            "compare_results.py",
            "lab.py",
            "catalog.py",
            "run_profile.py",
            "batch_scan.py",
            "watch_target.py",
            "report_summary.py",
            "report_json.py",
            "report_csv.py",
            "report_markdown.py",
            "report_stats.py",
            "report_open_ports.py",
            "rescan_open_ports.py",
        )
        for script in scripts:
            with self.subTest(script=script):
                process = subprocess.run(
                    [sys.executable, str(SCRIPTS / script), "--help"],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(0, process.returncode, process.stderr)
                self.assertIn("usage:", process.stdout.lower())


if __name__ == "__main__":
    unittest.main()

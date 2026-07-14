from __future__ import annotations

import csv
import io
import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
FIXTURE = ROOT / "tests" / "fixtures" / "sample.xml"
sys.path.insert(0, str(SCRIPTS))
import nmap_xml  # noqa: E402


class ReportParserTests(unittest.TestCase):
    def test_parses_hosts_ports_services_and_scripts(self) -> None:
        report = nmap_xml.parse_report(FIXTURE)
        self.assertEqual(1, len(report.hosts))
        self.assertEqual("127.0.0.1", report.hosts[0].primary_address)
        self.assertEqual(3, len(report.hosts[0].ports))
        self.assertEqual("ssh-hostkey", report.hosts[0].ports[0].scripts[0].script_id)


class ReportCliTests(unittest.TestCase):
    def run_tool(self, tool: str, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPTS / tool), *arguments],
            capture_output=True, text=True, check=False, cwd=ROOT,
        )

    def test_json_csv_markdown_summary_stats_and_open_ports(self) -> None:
        json_result = self.run_tool("report_json.py", str(FIXTURE))
        self.assertEqual(0, json_result.returncode, json_result.stderr)
        self.assertEqual("127.0.0.1", json.loads(json_result.stdout)["hosts"][0]["addresses"][0])

        csv_result = self.run_tool("report_csv.py", str(FIXTURE))
        self.assertEqual(0, csv_result.returncode, csv_result.stderr)
        rows = list(csv.DictReader(io.StringIO(csv_result.stdout)))
        self.assertEqual(3, len(rows))

        expected = {
            "report_markdown.py": "| 127.0.0.1 | tcp/22 |",
            "report_summary.py": "tcp/22",
            "report_stats.py": "Port records: 3",
            "report_open_ports.py": "tcp/22:ssh",
        }
        for tool, text in expected.items():
            with self.subTest(tool=tool):
                result = self.run_tool(tool, str(FIXTURE))
                self.assertEqual(0, result.returncode, result.stderr)
                self.assertIn(text, result.stdout)

    def test_rescan_open_ports_dry_run(self) -> None:
        result = self.run_tool("rescan_open_ports.py", str(FIXTURE), "--dry-run")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("scan_services.py", result.stdout)
        self.assertIn("scan_udp.py", result.stdout)
        self.assertIn("Hosts rescanned: 1", result.stdout)


if __name__ == "__main__":
    unittest.main()

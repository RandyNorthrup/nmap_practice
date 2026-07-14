from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import compare_results  # noqa: E402


def report_xml(ports: str) -> str:
    return (
        '<?xml version="1.0"?>\n'
        '<nmaprun><host><address addr="127.0.0.1" addrtype="ipv4"/>'
        f"<ports>{ports}</ports></host></nmaprun>"
    )


def port_xml(port: int, state: str, service: str = "unknown", version: str = "") -> str:
    version_attr = f' version="{version}"' if version else ""
    return (
        f'<port protocol="tcp" portid="{port}"><state state="{state}"/>'
        f'<service name="{service}"{version_attr}/></port>'
    )


class CompareResultsTests(unittest.TestCase):
    def parse(self, xml: str):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.xml"
            path.write_text(xml, encoding="utf-8")
            return compare_results.parse_report(path)

    def test_reports_added_removed_and_changed_ports(self) -> None:
        old = self.parse(
            report_xml(port_xml(22, "open", "ssh", "1.0") + port_xml(80, "open", "http"))
        )
        new = self.parse(
            report_xml(port_xml(22, "closed", "ssh", "1.0") + port_xml(443, "open", "https"))
        )
        changes = compare_results.compare(old, new)
        self.assertEqual(3, len(changes))
        self.assertTrue(any(line.startswith("CHANGED 127.0.0.1 tcp/22") for line in changes))
        self.assertTrue(any(line.startswith("REMOVED 127.0.0.1 tcp/80") for line in changes))
        self.assertTrue(any(line.startswith("ADDED   127.0.0.1 tcp/443") for line in changes))

    def test_equal_reports_have_no_changes(self) -> None:
        report = self.parse(report_xml(port_xml(8000, "open", "http")))
        self.assertEqual([], compare_results.compare(report, report))

    def test_invalid_xml_has_readable_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "broken.xml"
            path.write_text("<not-closed>", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Invalid Nmap XML"):
                compare_results.parse_report(path)


if __name__ == "__main__":
    unittest.main()

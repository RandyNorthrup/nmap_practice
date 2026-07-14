from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from nmap_xml import parse_report, port_version  # noqa: E402


class NmapXmlTests(unittest.TestCase):
    def test_parses_hosts_ports_versions_and_scripts(self) -> None:
        report = parse_report(ROOT / "tests" / "fixtures" / "sample.xml")
        self.assertEqual("7.95", report.version)
        self.assertEqual(1, len(report.hosts))
        host = report.hosts[0]
        self.assertEqual("127.0.0.1", host.primary_address)
        self.assertEqual(("localhost",), host.hostnames)
        self.assertEqual("clock-skew", host.scripts[0].script_id)
        self.assertEqual("open", host.ports[0].state)
        self.assertEqual("PracticeSSH 1.0", port_version(host.ports[0]))
        self.assertEqual("ssh-hostkey", host.ports[0].scripts[0].script_id)

    def test_rejects_non_nmap_xml(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "other.xml"
            path.write_text("<root/>", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Not an Nmap XML"):
                parse_report(path)


if __name__ == "__main__":
    unittest.main()

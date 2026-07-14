#!/usr/bin/env python3
"""Calculate host, state, protocol, and service counts from Nmap XML."""

import argparse
from collections import Counter
from pathlib import Path
import sys

from nmap_xml import parse_reports


def section(title: str, values: Counter[str]) -> list[str]:
    return [title, *(f"  {name}: {count}" for name, count in values.most_common())]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reports", nargs="+")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        reports = parse_reports(args.reports)
    except (FileNotFoundError, OSError, ValueError) as error:
        parser.error(str(error))
    hosts = [host for report in reports for host in report.hosts]
    ports = [port for host in hosts for port in host.ports]
    lines = [f"Reports: {len(reports)}", f"Hosts: {len(hosts)}", f"Port records: {len(ports)}", ""]
    lines += section("Host states", Counter(host.state for host in hosts)) + [""]
    lines += section("Port states", Counter(port.state for port in ports)) + [""]
    lines += section("Protocols", Counter(port.protocol for port in ports)) + [""]
    lines += section("Services", Counter(port.service for port in ports))
    text = "\n".join(lines) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

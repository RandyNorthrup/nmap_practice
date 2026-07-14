#!/usr/bin/env python3
"""Validate that a file is readable Nmap XML and print basic counts."""

import argparse

from nmap_xml import parse_report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("xml")
    args = parser.parse_args()
    try:
        report = parse_report(args.xml)
    except (FileNotFoundError, ValueError, OSError) as error:
        print(f"INVALID: {error}")
        return 1
    ports = sum(len(host.ports) for host in report.hosts)
    print(f"VALID: hosts={len(report.hosts)} ports={ports} nmap={report.version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

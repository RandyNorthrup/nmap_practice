#!/usr/bin/env python3
"""Group open Nmap findings by detected service name."""

import argparse
from collections import defaultdict

from nmap_xml import parse_report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("xml")
    args = parser.parse_args()
    try:
        report = parse_report(args.xml)
    except (FileNotFoundError, ValueError, OSError) as error:
        parser.error(str(error))
    groups: dict[str, list[str]] = defaultdict(list)
    for host in report.hosts:
        for port in host.ports:
            if port.state == "open":
                groups[port.service].append(f"{host.primary_address}:{port.port}/{port.protocol}")
    for service in sorted(groups):
        print(f"{service}: {', '.join(groups[service])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

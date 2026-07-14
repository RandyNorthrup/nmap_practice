#!/usr/bin/env python3
"""Extract one address per discovered host from Nmap XML."""

import argparse

from nmap_xml import parse_report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("xml")
    parser.add_argument("--up-only", action="store_true")
    args = parser.parse_args()
    try:
        report = parse_report(args.xml)
    except (FileNotFoundError, ValueError, OSError) as error:
        parser.error(str(error))
    for host in report.hosts:
        if not args.up_only or host.state == "up":
            print(host.primary_address)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

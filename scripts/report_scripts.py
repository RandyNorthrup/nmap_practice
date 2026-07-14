#!/usr/bin/env python3
"""Extract host and port NSE script findings from Nmap XML."""

import argparse

from nmap_xml import parse_report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("xml")
    args = parser.parse_args()
    try:
        report = parse_report(args.xml)
    except (FileNotFoundError, ValueError, OSError) as error:
        parser.error(str(error))
    for host in report.hosts:
        for finding in host.scripts:
            print(f"{host.primary_address} host {finding.script_id}: {finding.output}")
        for port in host.ports:
            for finding in port.scripts:
                print(f"{host.primary_address} {port.protocol}/{port.port} "
                      f"{finding.script_id}: {finding.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

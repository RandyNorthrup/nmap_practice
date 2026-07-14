#!/usr/bin/env python3
"""Export one row per Nmap port record as cross-platform CSV."""

import argparse
import csv
from pathlib import Path
import sys

from nmap_xml import parse_reports, port_version


HEADERS = ("address", "hostnames", "host_state", "protocol", "port", "port_state", "reason", "service", "version", "scripts", "source")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reports", nargs="+")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        reports = parse_reports(args.reports)
    except (FileNotFoundError, OSError, ValueError) as error:
        parser.error(str(error))
    handle = Path(args.output).open("w", encoding="utf-8", newline="") if args.output else sys.stdout
    try:
        writer = csv.DictWriter(handle, fieldnames=HEADERS)
        writer.writeheader()
        for report in reports:
            for host in report.hosts:
                for port in host.ports:
                    writer.writerow({
                        "address": host.primary_address, "hostnames": ";".join(host.hostnames),
                        "host_state": host.state, "protocol": port.protocol, "port": port.port,
                        "port_state": port.state, "reason": port.reason, "service": port.service,
                        "version": port_version(port),
                        "scripts": " | ".join(f"{item.script_id}: {item.output}" for item in port.scripts),
                        "source": str(report.path),
                    })
    finally:
        if args.output:
            handle.close()
    if args.output:
        print(f"Wrote {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

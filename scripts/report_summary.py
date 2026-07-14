#!/usr/bin/env python3
"""Create readable host, port, service, and NSE summary from Nmap XML."""

import argparse
from pathlib import Path
import sys

from nmap_xml import parse_reports, port_version


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reports", nargs="+")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        reports = parse_reports(args.reports)
    except (FileNotFoundError, OSError, ValueError) as error:
        parser.error(str(error))
    host_count = sum(len(report.hosts) for report in reports)
    lines = [f"Reports: {len(reports)} | Hosts: {host_count}"]
    for report in reports:
        lines.append(f"\nReport: {report.path} | Nmap {report.version}")
        for host in report.hosts:
            names = f" ({', '.join(host.hostnames)})" if host.hostnames else ""
            lines.append(f"{host.primary_address}{names} [{host.state}]")
            for port in host.ports:
                lines.append(f"  {port.protocol}/{port.port:<5} {port.state:<14} {port.service} {port_version(port)}".rstrip())
                lines.extend(f"    {item.script_id}: {item.output}" for item in port.scripts)
            lines.extend(f"  host-script: {item.script_id}: {item.output}" for item in host.scripts)
    text = "\n".join(lines) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

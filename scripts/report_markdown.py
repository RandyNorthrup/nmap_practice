#!/usr/bin/env python3
"""Create Markdown tables from one or more Nmap XML reports."""

import argparse
from pathlib import Path
import sys

from nmap_xml import parse_reports, port_version


def clean(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reports", nargs="+")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        reports = parse_reports(args.reports)
    except (FileNotFoundError, OSError, ValueError) as error:
        parser.error(str(error))
    lines = ["# Nmap report", "", "| Host | Protocol/port | State | Service | Product/version |", "|---|---:|---|---|---|"]
    for report in reports:
        for host in report.hosts:
            for port in host.ports:
                lines.append(
                    f"| {clean(host.primary_address)} | {port.protocol}/{port.port} | "
                    f"{clean(port.state)} | {clean(port.service)} | {clean(port_version(port))} |"
                )
    text = "\n".join(lines) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

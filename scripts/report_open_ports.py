#!/usr/bin/env python3
"""Print compact open-port lists from one or more Nmap XML reports."""

import argparse
from pathlib import Path
import sys

from nmap_xml import parse_reports


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reports", nargs="+")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        reports = parse_reports(args.reports)
    except (FileNotFoundError, OSError, ValueError) as error:
        parser.error(str(error))
    lines = []
    for report in reports:
        for host in report.hosts:
            ports = [f"{port.protocol}/{port.port}:{port.service}" for port in host.ports if port.state.startswith("open")]
            lines.append(f"{host.primary_address} {' '.join(ports) if ports else '(no open ports recorded)'}")
    text = "\n".join(lines) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

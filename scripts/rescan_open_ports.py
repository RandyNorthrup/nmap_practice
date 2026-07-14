#!/usr/bin/env python3
"""Re-run service detection only for open ports found in Nmap XML."""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
import subprocess
import sys

from nmap_xml import parse_reports


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reports", nargs="+")
    parser.add_argument("--allow-public", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-hosts", type=int, default=32)
    args = parser.parse_args()
    if not 1 <= args.max_hosts <= 256:
        parser.error("--max-hosts must be between 1 and 256")
    try:
        reports = parse_reports(args.reports)
    except (FileNotFoundError, OSError, ValueError) as error:
        parser.error(str(error))
    by_host: dict[str, dict[str, set[int]]] = defaultdict(lambda: defaultdict(set))
    for report in reports:
        for host in report.hosts:
            for port in host.ports:
                if port.state.startswith("open"):
                    by_host[host.primary_address][port.protocol].add(port.port)
    if len(by_host) > args.max_hosts:
        parser.error(f"reports contain {len(by_host)} hosts with open ports; cap is {args.max_hosts}")

    scripts = Path(__file__).resolve().parent
    failures = 0
    for target, protocols in by_host.items():
        for protocol, ports in protocols.items():
            script = "scan_udp.py" if protocol == "udp" else "scan_services.py"
            command = [sys.executable, str(scripts / script), target, "--ports", ",".join(map(str, sorted(ports)))]
            if args.allow_public:
                command.append("--allow-public")
            if args.dry_run:
                print(subprocess.list2cmdline(command))
            else:
                failures += subprocess.run(command, check=False).returncode != 0
    if not by_host:
        print("No open ports found.")
    print(f"Hosts rescanned: {len(by_host)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

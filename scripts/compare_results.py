#!/usr/bin/env python3
"""Compare host/port data from two Nmap XML reports on any Python 3 platform.

Customization: extend `PortFinding` and `parse_report` together to compare more
XML fields, such as hostnames or operating-system guesses.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import sys
import xml.etree.ElementTree as ET


@dataclass(frozen=True)
class PortFinding:
    state: str
    service: str
    version: str


Report = dict[tuple[str, str, int], PortFinding]


def resolve_xml_path(value: str) -> Path:
    path = Path(value)
    if path.suffix != ".xml":
        path = Path(f"{value}.xml")
    if not path.is_file():
        raise FileNotFoundError(f"Nmap XML report not found: {path}")
    return path


def service_text(service: ET.Element | None) -> tuple[str, str]:
    if service is None:
        return "unknown", ""
    name = service.get("name", "unknown")
    details = [
        service.get("product", ""),
        service.get("version", ""),
        service.get("extrainfo", ""),
    ]
    return name, " ".join(part for part in details if part)


def parse_report(path: Path) -> Report:
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as error:
        raise ValueError(f"Invalid Nmap XML in {path}: {error}") from error

    report: Report = {}
    for host in root.findall("host"):
        address_node = host.find("address[@addr]")
        if address_node is None:
            continue
        address = address_node.get("addr", "unknown")
        for port in host.findall("./ports/port"):
            state_node = port.find("state")
            state = state_node.get("state", "unknown") if state_node is not None else "unknown"
            service, version = service_text(port.find("service"))
            protocol = port.get("protocol", "unknown")
            port_id = int(port.get("portid", "0"))
            report[(address, protocol, port_id)] = PortFinding(state, service, version)
    return report


def format_key(key: tuple[str, str, int]) -> str:
    address, protocol, port = key
    return f"{address} {protocol}/{port}"


def format_finding(finding: PortFinding) -> str:
    service = finding.service
    if finding.version:
        service = f"{service} ({finding.version})"
    return f"{finding.state} {service}"


def compare(old: Report, new: Report) -> list[str]:
    lines: list[str] = []
    for key in sorted(old.keys() | new.keys()):
        if key not in old:
            lines.append(f"ADDED   {format_key(key)}: {format_finding(new[key])}")
        elif key not in new:
            lines.append(f"REMOVED {format_key(key)}: {format_finding(old[key])}")
        elif old[key] != new[key]:
            lines.append(
                f"CHANGED {format_key(key)}: "
                f"{format_finding(old[key])} -> {format_finding(new[key])}"
            )
    return lines


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compare host, port, state, service, and version data in Nmap XML reports."
    )
    parser.add_argument("old", help="Older .xml path or output prefix")
    parser.add_argument("new", help="Newer .xml path or output prefix")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        old_path = resolve_xml_path(args.old)
        new_path = resolve_xml_path(args.new)
        changes = compare(parse_report(old_path), parse_report(new_path))
    except (FileNotFoundError, OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Old: {old_path}")
    print(f"New: {new_path}")
    if not changes:
        print("No host, port, state, service, or version changes found.")
        return 0

    print(f"Changes: {len(changes)}")
    print(*changes, sep="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

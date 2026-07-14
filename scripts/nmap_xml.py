"""Shared Nmap XML parser for cross-platform reporting utilities.

Parser intentionally reads only data: no network requests and no external XML
entities. Extend dataclasses and `parse_report` together when adding report fields.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
import glob
from pathlib import Path
import xml.etree.ElementTree as ET


@dataclass(frozen=True, slots=True)
class ScriptFinding:
    script_id: str
    output: str


@dataclass(frozen=True, slots=True)
class PortRecord:
    protocol: str
    port: int
    state: str
    reason: str
    service: str
    product: str
    version: str
    extra_info: str
    tunnel: str
    scripts: tuple[ScriptFinding, ...] = ()


@dataclass(frozen=True, slots=True)
class HostRecord:
    state: str
    addresses: tuple[str, ...]
    hostnames: tuple[str, ...]
    ports: tuple[PortRecord, ...]
    scripts: tuple[ScriptFinding, ...] = ()

    @property
    def primary_address(self) -> str:
        return self.addresses[0] if self.addresses else "unknown"


@dataclass(frozen=True, slots=True)
class NmapReport:
    path: Path
    scanner: str
    version: str
    arguments: str
    start_time: str
    hosts: tuple[HostRecord, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, object]:
        data = asdict(self)
        data["path"] = str(self.path)
        return data


def _scripts(parent: ET.Element | None) -> tuple[ScriptFinding, ...]:
    if parent is None:
        return ()
    return tuple(
        ScriptFinding(node.get("id", "unknown"), node.get("output", ""))
        for node in parent.findall("script")
    )


def parse_report(path: str | Path) -> NmapReport:
    """Parse one Nmap XML file into immutable, reporting-friendly records."""
    source = Path(path)
    if not source.is_file():
        raise FileNotFoundError(f"Nmap XML report not found: {source}")
    try:
        root = ET.parse(source).getroot()
    except ET.ParseError as error:
        raise ValueError(f"Invalid Nmap XML in {source}: {error}") from error
    if root.tag != "nmaprun":
        raise ValueError(f"Not an Nmap XML report: root element is {root.tag!r}")

    hosts: list[HostRecord] = []
    for host_node in root.findall("host"):
        state_node = host_node.find("status")
        addresses = tuple(
            node.get("addr", "") for node in host_node.findall("address") if node.get("addr")
        )
        hostnames = tuple(
            node.get("name", "")
            for node in host_node.findall("./hostnames/hostname")
            if node.get("name")
        )
        ports: list[PortRecord] = []
        for port_node in host_node.findall("./ports/port"):
            state = port_node.find("state")
            service = port_node.find("service")
            ports.append(
                PortRecord(
                    protocol=port_node.get("protocol", "unknown"),
                    port=int(port_node.get("portid", "0")),
                    state=state.get("state", "unknown") if state is not None else "unknown",
                    reason=state.get("reason", "") if state is not None else "",
                    service=service.get("name", "unknown") if service is not None else "unknown",
                    product=service.get("product", "") if service is not None else "",
                    version=service.get("version", "") if service is not None else "",
                    extra_info=service.get("extrainfo", "") if service is not None else "",
                    tunnel=service.get("tunnel", "") if service is not None else "",
                    scripts=_scripts(port_node),
                )
            )
        hosts.append(
            HostRecord(
                state=state_node.get("state", "unknown") if state_node is not None else "unknown",
                addresses=addresses,
                hostnames=hostnames,
                ports=tuple(ports),
                scripts=_scripts(host_node.find("hostscript")),
            )
        )

    return NmapReport(
        path=source,
        scanner=root.get("scanner", "nmap"),
        version=root.get("version", "unknown"),
        arguments=root.get("args", ""),
        start_time=root.get("startstr", root.get("start", "")),
        hosts=tuple(hosts),
    )


def port_version(port: PortRecord) -> str:
    return " ".join(part for part in (port.product, port.version, port.extra_info) if part)


def resolve_reports(values: list[str]) -> list[Path]:
    """Expand XML paths, output prefixes, and globs on every platform."""
    paths: list[Path] = []
    for value in values:
        matches = [Path(item) for item in glob.glob(value)]
        if not matches:
            candidate = Path(value)
            if candidate.suffix != ".xml":
                candidate = candidate.with_suffix(".xml")
            matches = [candidate]
        for path in matches:
            if not path.is_file():
                raise FileNotFoundError(f"Nmap XML report not found: {path}")
            if path not in paths:
                paths.append(path)
    return paths


def parse_reports(values: list[str]) -> tuple[NmapReport, ...]:
    return tuple(parse_report(path) for path in resolve_reports(values))

"""Shared, cross-platform helpers for every Nmap practice script.

Modify this module when behavior should change everywhere. Individual scan files
only choose Nmap arguments; this module handles safety checks, result paths, and
process execution. It uses only Python's standard library.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import ipaddress
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TARGET_PATTERN = re.compile(r"^[A-Za-z0-9._:/%-]+$")
LOCAL_NETWORKS = tuple(
    ipaddress.ip_network(cidr)
    for cidr in (
        "10.0.0.0/8",
        "127.0.0.0/8",
        "169.254.0.0/16",
        "172.16.0.0/12",
        "192.168.0.0/16",
        "::1/128",
        "fc00::/7",
        "fe80::/10",
    )
)


def add_target_options(parser: argparse.ArgumentParser) -> None:
    """Add consistent target, output, and public-target options to a parser."""
    parser.add_argument("target", help="Authorized IP, CIDR range, or hostname")
    parser.add_argument(
        "--output",
        metavar="PREFIX",
        help="Result path prefix; Nmap adds .nmap, .gnmap, and .xml",
    )
    parser.add_argument(
        "--allow-public",
        action="store_true",
        help="Allow a non-private target after you confirm authorization",
    )


def add_port_options(parser: argparse.ArgumentParser, default_top_ports: int = 100) -> None:
    """Add mutually exclusive exact-port and top-port options."""
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--ports", metavar="LIST", help="Example: 22,80,8000-8010")
    group.add_argument(
        "--top-ports",
        type=int,
        default=default_top_ports,
        metavar="N",
        help=f"Scan N most common ports (default: {default_top_ports})",
    )


def is_private_target(target: str) -> bool:
    """Return True for loopback, private, or link-local IP/CIDR targets."""
    if target.lower() == "localhost":
        return True
    try:
        # strict=False accepts normal input such as 192.168.1.12/24.
        network = ipaddress.ip_network(target, strict=False)
    except ValueError:
        return False
    # Use explicit ranges promised in safety docs. `ipaddress.is_private` also
    # includes some reserved/documentation ranges that are not a user's LAN.
    return any(
        network.version == allowed.version and network.subnet_of(allowed)
        for allowed in LOCAL_NETWORKS
    )


def authorize_target(target: str, allow_public: bool) -> None:
    """Reject unsafe syntax and require explicit opt-in for non-private targets."""
    if not target or target.startswith("-") or not TARGET_PATTERN.fullmatch(target):
        raise ValueError(f"Invalid target syntax: {target}")
    if is_private_target(target):
        return
    if not allow_public:
        raise ValueError(
            "Public or unresolved target blocked. Use --allow-public only with "
            "explicit authorization."
        )
    print(
        f"Authorization guard bypassed for {target}. "
        "You are responsible for permission and scope.",
        file=sys.stderr,
    )


def validate_port_spec(value: str) -> str:
    """Validate comma-separated ports/ranges and return unchanged input."""
    # Supports ordinary lists plus Nmap's mixed protocol syntax, for example
    # `T:22,80,443,U:53,123`. Names/wildcards stay disabled for predictable scope.
    token = r"(?:[TUSP]:)?[0-9]+(?:-[0-9]+)?"
    if not re.fullmatch(rf"{token}(?:,{token})*", value, flags=re.IGNORECASE):
        raise ValueError(f"Invalid port list: {value} (example: 22,80,8000-8010)")

    mixed = ":" in value
    protocol_seen = False
    for token in value.split(","):
        if ":" in token:
            prefix, token = token.split(":", 1)
            if prefix.upper() not in {"T", "U", "S", "P"}:
                raise ValueError(f"Unknown port protocol prefix: {prefix}")
            protocol_seen = True
        elif mixed and not protocol_seen:
            raise ValueError("Mixed port lists must begin with T:, U:, S:, or P:")
        if not re.fullmatch(r"[0-9]+(?:-[0-9]+)?", token):
            raise ValueError(f"Invalid port token: {token}")
        bounds = [int(number) for number in token.split("-")]
        if any(number < 1 or number > 65535 for number in bounds):
            raise ValueError("Every port must be between 1 and 65535")
        if len(bounds) == 2 and bounds[0] > bounds[1]:
            raise ValueError(f"Port range must be ascending: {token}")
    return value


def port_arguments(args: argparse.Namespace) -> list[str]:
    """Convert common port CLI options into Nmap arguments."""
    if args.ports:
        return ["-p", validate_port_spec(args.ports)]
    if not 1 <= args.top_ports <= 65535:
        raise ValueError("--top-ports must be between 1 and 65535")
    return ["--top-ports", str(args.top_ports)]


def validate_common_args(parser: argparse.ArgumentParser, args: argparse.Namespace) -> None:
    """Turn shared validation errors into friendly argparse messages."""
    try:
        authorize_target(args.target, args.allow_public)
    except ValueError as error:
        parser.error(str(error))


def validate_ports_or_error(
    parser: argparse.ArgumentParser, args: argparse.Namespace
) -> list[str]:
    """Validate target and selected ports, reporting errors consistently."""
    validate_common_args(parser, args)
    try:
        return port_arguments(args)
    except ValueError as error:
        parser.error(str(error))


def result_prefix(label: str, target: str, requested: str | None) -> Path:
    """Create a stable output prefix without overwriting extensions accidentally."""
    if requested:
        prefix = Path(requested)
        if prefix.suffix in {".xml", ".nmap", ".gnmap"}:
            prefix = prefix.with_suffix("")
    else:
        safe_target = re.sub(r"[^A-Za-z0-9._-]", "_", target)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        prefix = PROJECT_ROOT / "results" / f"{timestamp}-{label}-{safe_target}"

    prefix.parent.mkdir(parents=True, exist_ok=True)
    return prefix


def nmap_command() -> list[str]:
    """Locate Nmap, with NMAP_BIN override support for tests/custom installs."""
    configured = os.environ.get("NMAP_BIN", "nmap")
    path = shutil.which(configured)
    if path is None and Path(configured).is_file():
        path = str(Path(configured).resolve())
    if path is None:
        raise FileNotFoundError(
            "Nmap was not found in PATH. Install Nmap or set NMAP_BIN to its path."
        )
    # Python mock tools are launched through current interpreter on every OS.
    return [sys.executable, path] if path.lower().endswith(".py") else [path]


def display_command(command: list[str]) -> str:
    """Format commands using native-looking quoting."""
    if os.name == "nt":
        return subprocess.list2cmdline(command)
    return shlex.join(command)


def run_scan(label: str, args: argparse.Namespace, nmap_args: list[str]) -> int:
    """Build and execute one Nmap command, saving all three standard formats."""
    dry_run = bool(getattr(args, "dry_run", False))
    if dry_run:
        # Dry runs remain useful on documentation machines without Nmap installed.
        command = [os.environ.get("NMAP_BIN", "nmap")]
    else:
        try:
            command = nmap_command()
        except FileNotFoundError as error:
            print(f"Error: {error}", file=sys.stderr)
            return 1

    prefix = result_prefix(label, args.target, args.output)
    command.extend([*nmap_args, "-oA", str(prefix), args.target])
    print(f"Running: {display_command(command)}", file=sys.stderr)
    print(f"Results prefix: {prefix}", file=sys.stderr)
    if dry_run:
        print("Dry run: Nmap was not started.", file=sys.stderr)
        return 0
    try:
        return subprocess.run(command, check=False).returncode
    except OSError as error:
        print(f"Error starting Nmap: {error}", file=sys.stderr)
        return 1

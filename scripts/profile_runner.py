"""Cross-platform CLI engine shared by focused profile entry scripts."""

from __future__ import annotations

import argparse
import ipaddress
import sys

from common import (
    add_target_options,
    authorize_target,
    is_private_target,
    run_scan,
    validate_port_spec,
)
from profiles import PROFILES, ScanProfile


def is_loopback_target(target: str) -> bool:
    if target.lower() == "localhost":
        return True
    try:
        return ipaddress.ip_network(target, strict=False).is_loopback
    except ValueError:
        return False


def build_parser(item: ScanProfile) -> argparse.ArgumentParser:
    details = (
        f"Category: {item.category} | Risk: {item.risk} | Scope: {item.scope}. "
        f"Core Nmap arguments: {' '.join(item.arguments)}"
    )
    parser = argparse.ArgumentParser(
        description=item.description,
        epilog=details,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    add_target_options(parser)
    if item.default_ports is not None:
        parser.add_argument(
            "--ports",
            default=item.default_ports,
            metavar="LIST",
            help=f"Override ports (default: {item.default_ports})",
        )
    parser.add_argument(
        "--timing",
        choices=("T0", "T1", "T2", "T3", "T4"),
        default=item.timing,
        help=f"Nmap timing template (default: {item.timing or 'profile-controlled'})",
    )
    parser.add_argument("--no-dns", action="store_true", help="Disable reverse DNS (-n)")
    parser.add_argument("--skip-host-discovery", action="store_true", help="Treat target as online (-Pn)")
    parser.add_argument(
        "--script-args",
        metavar="TEXT",
        help="Arguments for an NSE profile, such as ssh.user=practice",
    )
    parser.add_argument(
        "--extra-arg",
        action="append",
        default=[],
        metavar="OPTION",
        help="Append one Nmap option; use --extra-arg=--option for leading dashes",
    )
    parser.add_argument("-v", "--verbose", action="count", default=0, help="Increase Nmap verbosity")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print validated command without starting Nmap",
    )
    return parser


def validate_scope(parser: argparse.ArgumentParser, item: ScanProfile, args: argparse.Namespace) -> None:
    try:
        authorize_target(args.target, args.allow_public)
    except ValueError as error:
        parser.error(str(error))
    if item.scope == "private" and not is_private_target(args.target):
        parser.error("This profile is locked to private, link-local, or loopback targets.")
    if item.scope == "loopback" and not is_loopback_target(args.target):
        parser.error("This higher-impact profile is locked to localhost/loopback practice.")


def build_arguments(
    parser: argparse.ArgumentParser, item: ScanProfile, args: argparse.Namespace
) -> list[str]:
    arguments = list(item.arguments)
    if item.default_ports is not None:
        try:
            ports = validate_port_spec(args.ports)
        except ValueError as error:
            parser.error(str(error))
        arguments.extend(("-p", ports))
    if args.timing:
        arguments.append(f"-{args.timing}")
    if args.no_dns:
        arguments.append("-n")
    if args.skip_host_discovery and "-Pn" not in arguments:
        arguments.append("-Pn")
    if args.script_args:
        if "--script" not in arguments:
            parser.error("--script-args requires an NSE profile")
        arguments.extend(("--script-args", args.script_args))
    for extra in args.extra_arg:
        if extra.startswith(("-o", "-iL", "-iR", "--resume", "--datadir")):
            parser.error(f"--extra-arg cannot control scope or output: {extra}")
        arguments.append(extra)
    if "--reason" not in arguments:
        arguments.append("--reason")
    arguments.extend("-v" for _ in range(min(args.verbose, 3)))
    return arguments


def run_profile(item: ScanProfile, argv: list[str] | None = None) -> int:
    parser = build_parser(item)
    args = parser.parse_args(argv)
    validate_scope(parser, item, args)
    arguments = build_arguments(parser, item, args)
    print(
        f"Profile: {item.title} | category={item.category} "
        f"risk={item.risk} scope={item.scope}",
        file=sys.stderr,
    )
    if item.elevated:
        print(
            "Note: raw-packet profile may require sudo or an Administrator terminal/Npcap.",
            file=sys.stderr,
        )
    return run_scan(item.name.removeprefix("scan_"), args, arguments)


def run_named_profile(name: str) -> int:
    try:
        item = PROFILES[name]
    except KeyError:
        print(f"Error: unknown profile {name}", file=sys.stderr)
        return 2
    return run_profile(item)

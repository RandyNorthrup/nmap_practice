#!/usr/bin/env python3
"""Scan common or explicitly selected TCP ports.

Customization: edit DEFAULT_TOP_PORTS for broader/narrower defaults. Add a new
CLI option in `build_parser`, then append its Nmap flag in `main`.
"""

import argparse

from common import add_port_options, add_target_options, run_scan, validate_ports_or_error


DEFAULT_TOP_PORTS = 100


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scan TCP ports on an authorized target.")
    add_target_options(parser)
    add_port_options(parser, DEFAULT_TOP_PORTS)
    parser.add_argument(
        "--syn",
        action="store_true",
        help="Use raw-packet SYN scan; elevated privileges may be required",
    )
    parser.add_argument(
        "--show-closed",
        action="store_true",
        help="Show closed ports too (default output focuses on open ports)",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    port_args = validate_ports_or_error(parser, args)

    # -sT works without raw-packet privileges; -sS is optional for comparison.
    nmap_args = ["-sS" if args.syn else "-sT", *port_args, "--reason", "-T3"]
    if not args.show_closed:
        nmap_args.append("--open")
    return run_scan("tcp", args, nmap_args)


if __name__ == "__main__":
    raise SystemExit(main())

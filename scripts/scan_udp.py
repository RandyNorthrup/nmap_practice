#!/usr/bin/env python3
"""Scan a small list of UDP ports.

Customization: edit DEFAULT_PORTS for protocols present in your own lab. UDP can
be slow and ambiguous, so this script deliberately has no all-ports shortcut.
"""

import argparse

from common import add_target_options, run_scan, validate_common_args, validate_port_spec


DEFAULT_PORTS = "53,123,161,500,5353"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Scan selected UDP ports; elevated privileges may be required."
    )
    add_target_options(parser)
    parser.add_argument(
        "--ports", default=DEFAULT_PORTS, metavar="LIST", help=f"Default: {DEFAULT_PORTS}"
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    validate_common_args(parser, args)
    try:
        ports = validate_port_spec(args.ports)
    except ValueError as error:
        parser.error(str(error))

    # -sU uses UDP probes. --open includes open|filtered because silence is ambiguous.
    nmap_args = ["-sU", "-p", ports, "--reason", "--open", "-T3"]
    return run_scan("udp", args, nmap_args)


if __name__ == "__main__":
    raise SystemExit(main())

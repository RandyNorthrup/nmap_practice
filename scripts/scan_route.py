#!/usr/bin/env python3
"""Trace network path while performing host discovery only.

Customization: add `-6` in `nmap_args` for an IPv6-only exercise. Route results
can differ because routers may filter or rate-limit discovery packets.
"""

import argparse

from common import add_target_options, run_scan, validate_common_args


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Discover a target and show Nmap's network path to it."
    )
    add_target_options(parser)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    validate_common_args(parser, args)

    # --traceroute runs after discovery; -sn ensures this script does not scan ports.
    nmap_args = ["-sn", "--traceroute", "--reason", "-T3"]
    return run_scan("route", args, nmap_args)


if __name__ == "__main__":
    raise SystemExit(main())

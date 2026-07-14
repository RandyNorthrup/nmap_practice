#!/usr/bin/env python3
"""Attempt operating-system fingerprinting with restrained retry settings.

Customization: DEFAULT_TOP_PORTS controls how many TCP ports help find one open
and one closed port. OS guesses need raw-packet privileges and are not proof.
"""

import argparse

from common import add_target_options, run_scan, validate_common_args


DEFAULT_TOP_PORTS = 1000


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Attempt an OS fingerprint; elevated privileges may be required."
    )
    add_target_options(parser)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    validate_common_args(parser, args)

    # --osscan-limit avoids poor candidates; one retry keeps practice traffic bounded.
    nmap_args = [
        "-O",
        "--osscan-limit",
        "--max-os-tries",
        "1",
        "--top-ports",
        str(DEFAULT_TOP_PORTS),
        "--reason",
        "-T3",
    ]
    return run_scan("os", args, nmap_args)


if __name__ == "__main__":
    raise SystemExit(main())

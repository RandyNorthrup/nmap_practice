#!/usr/bin/env python3
"""Discover responding hosts without scanning their ports.

Customization: change DEFAULT_TIMING or add discovery probes to `nmap_args`.
Read `docs/script-guide.md` before increasing scan scope.
"""

import argparse

from common import add_target_options, run_scan, validate_common_args


DEFAULT_TIMING = "T3"  # T3 is Nmap's normal, conservative timing template.


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Find responding hosts on an authorized network without a port scan."
    )
    add_target_options(parser)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    validate_common_args(parser, args)

    # -sn disables port scanning; --reason explains why each host appears online.
    nmap_args = ["-sn", "--reason", f"-{DEFAULT_TIMING}"]
    return run_scan("discovery", args, nmap_args)


if __name__ == "__main__":
    raise SystemExit(main())

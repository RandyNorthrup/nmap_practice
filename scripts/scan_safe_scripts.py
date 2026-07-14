#!/usr/bin/env python3
"""Run Nmap scripts that belong to both `default` and `safe` categories.

Customization: keep DEFAULT_SCRIPT_EXPRESSION conservative on real systems.
Experiment with other NSE groups only inside the loopback practice lab.
"""

import argparse

from common import add_port_options, add_target_options, run_scan, validate_ports_or_error


DEFAULT_TOP_PORTS = 100
DEFAULT_SCRIPT_EXPRESSION = "default and safe"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run conservative NSE checks against an authorized target."
    )
    add_target_options(parser)
    add_port_options(parser, DEFAULT_TOP_PORTS)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    port_args = validate_ports_or_error(parser, args)

    # Timeouts prevent a single script or host from holding the practice run forever.
    nmap_args = [
        "-sT",
        "-sV",
        "--version-light",
        *port_args,
        "--script",
        DEFAULT_SCRIPT_EXPRESSION,
        "--script-timeout",
        "30s",
        "--host-timeout",
        "5m",
        "--reason",
        "--open",
        "-T3",
    ]
    return run_scan("nse-safe", args, nmap_args)


if __name__ == "__main__":
    raise SystemExit(main())

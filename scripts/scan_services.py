#!/usr/bin/env python3
"""Identify applications and versions listening on TCP ports.

Customization: default uses light probes to reduce traffic. Pass --version-all
for every probe, or change DEFAULT_TOP_PORTS for your own lab.
"""

import argparse

from common import add_port_options, add_target_options, run_scan, validate_ports_or_error


DEFAULT_TOP_PORTS = 100


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Probe open TCP ports to identify services and versions."
    )
    add_target_options(parser)
    add_port_options(parser, DEFAULT_TOP_PORTS)
    parser.add_argument(
        "--version-all",
        action="store_true",
        help="Try every version probe; slower and noisier",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    port_args = validate_ports_or_error(parser, args)

    # -sV sends application-level probes. --version-light uses fewer of them.
    intensity = "--version-all" if args.version_all else "--version-light"
    nmap_args = ["-sT", "-sV", intensity, *port_args, "--reason", "--open", "-T3"]
    return run_scan("services", args, nmap_args)


if __name__ == "__main__":
    raise SystemExit(main())

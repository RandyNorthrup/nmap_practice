#!/usr/bin/env python3
"""Inspect common web ports with low-impact HTTP NSE scripts.

Customization: edit DEFAULT_WEB_PORTS for development servers you use. Add only
NSE scripts whose behavior you understand and are authorized to run.
"""

import argparse

from common import add_target_options, run_scan, validate_common_args, validate_port_spec


DEFAULT_WEB_PORTS = "80,443,8000,8080,8443"
HTTP_SCRIPTS = "http-title,http-headers"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Identify web services, titles, and response headers."
    )
    add_target_options(parser)
    parser.add_argument(
        "--ports", default=DEFAULT_WEB_PORTS, metavar="LIST", help=f"Default: {DEFAULT_WEB_PORTS}"
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

    # These scripts read basic HTTP metadata; they do not brute-force content.
    nmap_args = [
        "-sT",
        "-sV",
        "--version-light",
        "-p",
        ports,
        "--script",
        HTTP_SCRIPTS,
        "--script-timeout",
        "30s",
        "--reason",
        "--open",
        "-T3",
    ]
    return run_scan("web", args, nmap_args)


if __name__ == "__main__":
    raise SystemExit(main())

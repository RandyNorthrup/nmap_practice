#!/usr/bin/env python3
"""AMQP information.

Use case: AMQP information: run the installed amqp-info NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script amqp-info --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_amqp_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_amqp_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

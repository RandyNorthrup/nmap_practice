#!/usr/bin/env python3
"""Modbus discovery.

Use case: Modbus discovery: run the installed modbus-discover NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script modbus-discover --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_modbus_discovery row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_modbus_discovery"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

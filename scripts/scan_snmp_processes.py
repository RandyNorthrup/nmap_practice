#!/usr/bin/env python3
"""SNMP process list.

Use case: SNMP process list: run the installed snmp-processes NSE script on expected service ports, with timeout and saved output.
Core flags: -sU -sV --version-light --script snmp-processes --script-timeout 30s --open
Risk: medium. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_snmp_processes row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_snmp_processes"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

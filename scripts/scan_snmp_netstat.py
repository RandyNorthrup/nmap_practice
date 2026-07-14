#!/usr/bin/env python3
"""SNMP network tables.

Use case: SNMP network tables: run the installed snmp-netstat NSE script on expected service ports, with timeout and saved output.
Core flags: -sU -sV --version-light --script snmp-netstat --script-timeout 30s --open
Risk: medium. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_snmp_netstat row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_snmp_netstat"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

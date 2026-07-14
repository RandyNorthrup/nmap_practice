#!/usr/bin/env python3
"""SNMP interfaces.

Use case: SNMP interfaces: run the installed snmp-interfaces NSE script on expected service ports, with timeout and saved output.
Core flags: -sU -sV --version-light --script snmp-interfaces --script-timeout 30s --open
Risk: medium. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_snmp_interfaces row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_snmp_interfaces"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

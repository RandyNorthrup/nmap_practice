#!/usr/bin/env python3
"""SNMP: Windows services.

Use case: Run bounded snmp-win32-services NSE checks for Windows services on authorized services.
Core flags: -sU -sV --version-light --script snmp-win32-services --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_snmp_win32_services row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_snmp_win32_services"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

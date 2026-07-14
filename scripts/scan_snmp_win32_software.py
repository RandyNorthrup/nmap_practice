#!/usr/bin/env python3
"""SNMP: Windows software.

Use case: Run bounded snmp-win32-software NSE checks for Windows software on authorized services.
Core flags: -sU -sV --version-light --script snmp-win32-software --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_snmp_win32_software row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_snmp_win32_software"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

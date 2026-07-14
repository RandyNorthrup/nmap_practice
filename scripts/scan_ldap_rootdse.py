#!/usr/bin/env python3
"""Infrastructure: LDAP Root DSE.

Use case: Run bounded ldap-rootdse NSE checks for LDAP Root DSE on authorized services.
Core flags: -sT -sV --version-light --script ldap-rootdse --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_ldap_rootdse row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ldap_rootdse"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

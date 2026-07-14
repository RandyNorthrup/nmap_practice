#!/usr/bin/env python3
"""Infrastructure: IPMI version.

Use case: Run bounded ipmi-version NSE checks for IPMI version on authorized services.
Core flags: -sU -sV --version-light --script ipmi-version --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized. Raw packets may need elevated privileges.
Modify matching scan_ipmi_version row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ipmi_version"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

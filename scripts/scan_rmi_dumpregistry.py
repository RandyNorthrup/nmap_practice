#!/usr/bin/env python3
"""Infrastructure: RMI bindings.

Use case: Run bounded rmi-dumpregistry NSE checks for RMI bindings on authorized services.
Core flags: -sT -sV --version-light --script rmi-dumpregistry --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_rmi_dumpregistry row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_rmi_dumpregistry"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

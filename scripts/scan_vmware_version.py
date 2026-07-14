#!/usr/bin/env python3
"""Infrastructure: VMware version.

Use case: Run bounded vmware-version NSE checks for VMware version on authorized services.
Core flags: -sT -sV --version-light --script vmware-version --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_vmware_version row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_vmware_version"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

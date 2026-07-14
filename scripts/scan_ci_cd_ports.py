#!/usr/bin/env python3
"""CI/CD service ports.

Use case: Inventory ci/cd service ports with TCP connect and light service detection.
Core flags: -sT -sV --version-light --reason --open
Risk: low. Scope: authorized.
Modify matching scan_ci_cd_ports row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ci_cd_ports"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

#!/usr/bin/env python3
"""Full service detection.

Use case: Try every registered service probe.
Core flags: -sT -sV --version-all --top-ports 100
Risk: medium. Scope: authorized.
Modify matching scan_service_all row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_service_all"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

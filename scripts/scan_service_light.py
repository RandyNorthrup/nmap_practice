#!/usr/bin/env python3
"""Light service detection.

Use case: Identify services with light probes.
Core flags: -sT -sV --version-light --top-ports 100
Risk: low. Scope: authorized.
Modify matching scan_service_light row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_service_light"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

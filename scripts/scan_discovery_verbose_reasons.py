#!/usr/bin/env python3
"""Verbose discovery reasons.

Use case: Verbose discovery reasons practice profile with bounded Nmap options and saved output.
Core flags: -sn --reason -vv
Risk: low. Scope: authorized.
Modify matching scan_discovery_verbose_reasons row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_discovery_verbose_reasons"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

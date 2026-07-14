#!/usr/bin/env python3
"""Monitoring service ports.

Use case: Inventory monitoring service ports with TCP connect and light service detection.
Core flags: -sT -sV --version-light --reason --open
Risk: low. Scope: authorized.
Modify matching scan_monitoring_ports row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_monitoring_ports"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

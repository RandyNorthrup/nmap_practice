#!/usr/bin/env python3
"""Cassandra information.

Use case: Cassandra information: run the installed cassandra-info NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script cassandra-info --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_cassandra_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_cassandra_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

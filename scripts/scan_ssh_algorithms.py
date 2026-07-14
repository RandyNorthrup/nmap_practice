#!/usr/bin/env python3
"""SSH algorithms.

Use case: SSH algorithms: run the installed ssh2-enum-algos NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script ssh2-enum-algos --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_ssh_algorithms row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ssh_algorithms"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

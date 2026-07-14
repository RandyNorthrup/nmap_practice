#!/usr/bin/env python3
"""Hadoop secondary NameNode.

Use case: Hadoop secondary NameNode: run the installed hadoop-secondary-namenode-info NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script hadoop-secondary-namenode-info --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_hadoop_secondary row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_hadoop_secondary"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

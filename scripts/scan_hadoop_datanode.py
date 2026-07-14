#!/usr/bin/env python3
"""Hadoop DataNode.

Use case: Hadoop DataNode: run the installed hadoop-datanode-info NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script hadoop-datanode-info --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_hadoop_datanode row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_hadoop_datanode"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

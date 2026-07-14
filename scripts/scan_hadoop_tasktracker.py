#!/usr/bin/env python3
"""Hadoop TaskTracker.

Use case: Hadoop TaskTracker: run the installed hadoop-tasktracker-info NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script hadoop-tasktracker-info --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_hadoop_tasktracker row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_hadoop_tasktracker"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

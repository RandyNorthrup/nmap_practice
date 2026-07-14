#!/usr/bin/env python3
"""CUPS queues.

Use case: CUPS queues: run the installed cups-queue-info NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script cups-queue-info --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_cups_queues row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_cups_queues"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

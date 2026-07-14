#!/usr/bin/env python3
"""Infrastructure: CUPS queues.

Use case: Run bounded cups-queue-info NSE checks for CUPS queues on authorized services.
Core flags: -sT -sV --version-light --script cups-queue-info --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_cups_queue_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_cups_queue_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

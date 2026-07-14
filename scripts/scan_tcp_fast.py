#!/usr/bin/env python3
"""Fast TCP.

Use case: Use Nmap fast-mode port set.
Core flags: -sT -F
Risk: low. Scope: authorized.
Modify matching scan_tcp_fast row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_fast"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

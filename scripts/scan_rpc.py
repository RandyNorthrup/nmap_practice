#!/usr/bin/env python3
"""RPC service scan.

Use case: Identify RPC programs and versions.
Core flags: -sT -sV -sR
Risk: medium. Scope: authorized.
Modify matching scan_rpc row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_rpc"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

#!/usr/bin/env python3
"""RPC service scan.

Use case: RPC service scan practice profile with bounded Nmap options and saved output.
Core flags: -sT -sR --reason --open
Risk: medium. Scope: authorized.
Modify matching scan_rpc_services row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_rpc_services"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

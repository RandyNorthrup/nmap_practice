#!/usr/bin/env python3
"""SMB: server statistics.

Use case: Run bounded smb-server-stats NSE checks for server statistics on authorized services.
Core flags: -sT -sV --version-light --script smb-server-stats --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_smb_server_stats row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_smb_server_stats"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

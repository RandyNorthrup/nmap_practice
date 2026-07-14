#!/usr/bin/env python3
"""FTP anonymous access.

Use case: FTP anonymous access: run the installed ftp-anon NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script ftp-anon --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_ftp_anonymous row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ftp_anonymous"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

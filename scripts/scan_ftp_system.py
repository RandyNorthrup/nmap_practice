#!/usr/bin/env python3
"""FTP system type.

Use case: FTP system type: run the installed ftp-syst NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script ftp-syst --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_ftp_system row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_ftp_system"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

#!/usr/bin/env python3
"""Telnet encryption.

Use case: Telnet encryption: run the installed telnet-encryption NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script telnet-encryption --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_telnet_encryption row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_telnet_encryption"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

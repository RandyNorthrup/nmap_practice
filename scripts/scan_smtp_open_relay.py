#!/usr/bin/env python3
"""SMTP open relay.

Use case: SMTP open relay: run the installed smtp-open-relay NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script smtp-open-relay --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_smtp_open_relay row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_smtp_open_relay"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

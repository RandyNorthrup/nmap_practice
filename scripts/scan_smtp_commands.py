#!/usr/bin/env python3
"""SMTP commands.

Use case: SMTP commands: run the installed smtp-commands NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script smtp-commands --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_smtp_commands row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_smtp_commands"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

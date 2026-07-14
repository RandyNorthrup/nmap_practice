#!/usr/bin/env python3
"""Infrastructure: IRC information.

Use case: Run bounded irc-info NSE checks for IRC information on authorized services.
Core flags: -sT -sV --version-light --script irc-info --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_irc_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_irc_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

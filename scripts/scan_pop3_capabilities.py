#!/usr/bin/env python3
"""Mail: POP3 capabilities.

Use case: Run bounded pop3-capabilities NSE checks for POP3 capabilities on authorized services.
Core flags: -sT -sV --version-light --script pop3-capabilities --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_pop3_capabilities row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_pop3_capabilities"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

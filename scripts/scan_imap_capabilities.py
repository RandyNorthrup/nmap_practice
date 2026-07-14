#!/usr/bin/env python3
"""Mail: IMAP capabilities.

Use case: Run bounded imap-capabilities NSE checks for IMAP capabilities on authorized services.
Core flags: -sT -sV --version-light --script imap-capabilities --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_imap_capabilities row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_imap_capabilities"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

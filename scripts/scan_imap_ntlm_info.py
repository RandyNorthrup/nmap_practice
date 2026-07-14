#!/usr/bin/env python3
"""Mail: IMAP NTLM metadata.

Use case: Run bounded imap-ntlm-info NSE checks for IMAP NTLM metadata on authorized services.
Core flags: -sT -sV --version-light --script imap-ntlm-info --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_imap_ntlm_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_imap_ntlm_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

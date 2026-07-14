#!/usr/bin/env python3
"""Mail: POP3 NTLM metadata.

Use case: Run bounded pop3-ntlm-info NSE checks for POP3 NTLM metadata on authorized services.
Core flags: -sT -sV --version-light --script pop3-ntlm-info --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_pop3_ntlm_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_pop3_ntlm_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

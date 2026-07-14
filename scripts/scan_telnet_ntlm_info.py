#!/usr/bin/env python3
"""Infrastructure: Telnet NTLM metadata.

Use case: Run bounded telnet-ntlm-info NSE checks for Telnet NTLM metadata on authorized services.
Core flags: -sT -sV --version-light --script telnet-ntlm-info --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_telnet_ntlm_info row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_telnet_ntlm_info"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

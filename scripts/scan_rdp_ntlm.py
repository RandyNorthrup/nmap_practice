#!/usr/bin/env python3
"""RDP NTLM metadata.

Use case: RDP NTLM metadata: run the installed rdp-ntlm-info NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script rdp-ntlm-info --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_rdp_ntlm row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_rdp_ntlm"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

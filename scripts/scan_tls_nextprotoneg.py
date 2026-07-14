#!/usr/bin/env python3
"""TLS: legacy next protocols.

Use case: Run bounded tls-nextprotoneg NSE checks for legacy next protocols on authorized services.
Core flags: -sT -sV --version-light --script tls-nextprotoneg --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_tls_nextprotoneg row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tls_nextprotoneg"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

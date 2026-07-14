#!/usr/bin/env python3
"""Bitcoin peer addresses.

Use case: Bitcoin peer addresses: run the installed bitcoin-getaddr NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script bitcoin-getaddr --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_bitcoin_peers row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_bitcoin_peers"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

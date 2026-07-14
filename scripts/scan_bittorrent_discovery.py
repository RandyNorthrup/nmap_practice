#!/usr/bin/env python3
"""BitTorrent discovery.

Use case: BitTorrent discovery: run the installed bittorrent-discovery NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script bittorrent-discovery --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_bittorrent_discovery row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_bittorrent_discovery"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

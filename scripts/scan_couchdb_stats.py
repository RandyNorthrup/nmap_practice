#!/usr/bin/env python3
"""CouchDB statistics.

Use case: CouchDB statistics: run the installed couchdb-stats NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script couchdb-stats --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_couchdb_stats row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_couchdb_stats"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

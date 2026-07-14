#!/usr/bin/env python3
"""Infrastructure: rsync modules.

Use case: Run bounded rsync-list-modules NSE checks for rsync modules on authorized services.
Core flags: -sT -sV --version-light --script rsync-list-modules --script-timeout 30s --host-timeout 5m --open
Risk: low. Scope: authorized.
Modify matching scan_rsync_list_modules row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_rsync_list_modules"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

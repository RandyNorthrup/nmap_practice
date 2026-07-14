#!/usr/bin/env python3
"""WebDAV inspection.

Use case: WebDAV inspection: run the installed http-webdav-scan NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script http-webdav-scan --script-timeout 30s --open
Risk: medium. Scope: private.
Modify matching scan_http_webdav row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_webdav"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

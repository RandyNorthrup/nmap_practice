#!/usr/bin/env python3
"""HTTP: WebDAV capabilities.

Use case: Run bounded http-webdav-scan NSE checks for WebDAV capabilities on authorized services.
Core flags: -sT -sV --version-light --script http-webdav-scan --script-timeout 30s --host-timeout 5m --open
Risk: medium. Scope: authorized.
Modify matching scan_http_webdav_scan row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_webdav_scan"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

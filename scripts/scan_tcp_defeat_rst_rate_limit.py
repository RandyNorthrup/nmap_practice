#!/usr/bin/env python3
"""RST rate-limit comparison.

Use case: RST rate-limit comparison practice profile with bounded Nmap options and saved output.
Core flags: -sS --top-ports 1000 --defeat-rst-ratelimit --reason --open
Risk: medium. Scope: private. Raw packets may need elevated privileges.
Modify matching scan_tcp_defeat_rst_rate_limit row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_defeat_rst_rate_limit"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

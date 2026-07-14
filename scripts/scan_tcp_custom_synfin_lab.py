#!/usr/bin/env python3
"""Custom SYN/FIN flags.

Use case: Custom SYN/FIN flags practice profile with bounded Nmap options and saved output.
Core flags: -sS --scanflags SYNFIN --top-ports 100 --reason
Risk: high. Scope: loopback. Raw packets may need elevated privileges.
Modify matching scan_tcp_custom_synfin_lab row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_tcp_custom_synfin_lab"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

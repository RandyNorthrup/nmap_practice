#!/usr/bin/env python3
"""Docker API version.

Use case: Docker API version: run the installed docker-version NSE script on expected service ports, with timeout and saved output.
Core flags: -sT -sV --version-light --script docker-version --script-timeout 30s --open
Risk: low. Scope: authorized.
Modify matching scan_docker_version row in scripts/profiles.py; shared behavior lives in
scripts/profile_runner.py. Use --help or --dry-run before scanning.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_docker_version"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))

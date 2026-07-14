#!/usr/bin/env python3
"""Start, inspect, and stop loopback-only synthetic practice services.

Works on Linux, macOS, and Windows using only Python's standard library.
Customization: change ports in `lab/server.py`, then update README and tests.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import secrets
import signal
import subprocess
import sys
import time
from urllib.error import URLError
from urllib.request import urlopen


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_DIR = Path(
    os.environ.get("NMAP_PRACTICE_RUNTIME_DIR", PROJECT_ROOT / ".runtime")
)
STATE_FILE = RUNTIME_DIR / "lab.json"
LOG_FILE = RUNTIME_DIR / "lab.log"
HEALTH_URL = "http://127.0.0.1:8000/health"


def load_state() -> dict[str, object] | None:
    try:
        state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return None
    if not isinstance(state.get("pid"), int) or not isinstance(state.get("token"), str):
        return None
    return state


def health_token() -> str | None:
    """Read current lab token so stale PID files cannot kill unrelated processes."""
    try:
        with urlopen(HEALTH_URL, timeout=0.5) as response:  # noqa: S310 - fixed loopback URL
            return response.read(256).decode("utf-8").strip()
    except (URLError, OSError, UnicodeError):
        return None


def is_our_lab(state: dict[str, object] | None) -> bool:
    return bool(state and secrets.compare_digest(str(state["token"]), health_token() or ""))


def start_lab() -> int:
    current = load_state()
    if is_our_lab(current):
        print(f"Practice lab already running (PID {current['pid']}).")
        return 0
    if health_token() is not None:
        print(f"Error: another service is using {HEALTH_URL}", file=sys.stderr)
        return 1

    RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
    token = secrets.token_urlsafe(24)
    server = PROJECT_ROOT / "lab" / "server.py"

    # Detached process lets lab stay up after this command returns.
    popen_options: dict[str, object] = {}
    if os.name == "nt":
        popen_options["creationflags"] = (
            subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS
        )
    else:
        popen_options["start_new_session"] = True

    with LOG_FILE.open("ab") as log:
        process = subprocess.Popen(
            [sys.executable, str(server), "--token", token],
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=subprocess.STDOUT,
            **popen_options,
        )

    state: dict[str, object] = {"pid": process.pid, "token": token}
    STATE_FILE.write_text(json.dumps(state), encoding="utf-8")
    for _attempt in range(50):
        if process.poll() is not None:
            print(f"Error: practice lab failed. Read {LOG_FILE}", file=sys.stderr)
            STATE_FILE.unlink(missing_ok=True)
            return 1
        if is_our_lab(state):
            print(f"Practice lab running on 127.0.0.1 (PID {process.pid}).")
            print("TCP: 2222, 8000, 9000 | UDP: 5353")
            return 0
        time.sleep(0.1)

    print(f"Error: practice lab start timed out. Read {LOG_FILE}", file=sys.stderr)
    return 1


def status_lab() -> int:
    state = load_state()
    if is_our_lab(state):
        print(f"running (PID {state['pid']})")
        print("TCP 127.0.0.1:2222, :8000, :9000 | UDP 127.0.0.1:5353")
        return 0
    print("stopped")
    return 1


def stop_lab() -> int:
    state = load_state()
    if not is_our_lab(state):
        # Refuse to signal a PID unless matching token proves it is our server.
        STATE_FILE.unlink(missing_ok=True)
        print("Practice lab already stopped.")
        return 0

    pid = int(state["pid"])
    try:
        os.kill(pid, signal.SIGTERM)
    except OSError as error:
        print(f"Error stopping lab PID {pid}: {error}", file=sys.stderr)
        return 1

    for _attempt in range(50):
        if not is_our_lab(state):
            STATE_FILE.unlink(missing_ok=True)
            print("Practice lab stopped.")
            return 0
        time.sleep(0.1)
    print(f"Error: lab PID {pid} did not stop within 5 seconds.", file=sys.stderr)
    return 1


def show_logs() -> int:
    try:
        lines = LOG_FILE.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as error:
        print(f"Error reading {LOG_FILE}: {error}", file=sys.stderr)
        return 1
    print(*lines[-80:], sep="\n")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Manage synthetic services bound only to 127.0.0.1."
    )
    parser.add_argument("action", choices=("start", "status", "stop", "logs"))
    return parser


def main() -> int:
    action = build_parser().parse_args().action
    return {
        "start": start_lab,
        "status": status_lab,
        "stop": stop_lab,
        "logs": show_logs,
    }[action]()


if __name__ == "__main__":
    raise SystemExit(main())

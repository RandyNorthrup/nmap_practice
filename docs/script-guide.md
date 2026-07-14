# Script explanations and modification guide

All scripts are small Python 3 programs using only standard library. They build an
argument list and launch installed `nmap` executable without a shell. This works on
Linux, macOS, and Windows and prevents target text from becoming shell commands.

## Shared flow

Every scan script follows same five steps:

1. Build command-line parser with readable `--help`.
2. Validate target and require `--allow-public` outside local/private ranges.
3. Validate ports as integers from 1 through 65535.
4. Build Nmap argument list for one use case.
5. Run Nmap and add `-oA PREFIX`, producing `.nmap`, `.gnmap`, and `.xml`.

Shared behavior lives in `scripts/common.py` and `scripts/profile_runner.py`.
Profile definitions live in `scripts/profiles.py` and `scripts/profile_extras.py`.
Each focused `scan_*.py` entry point maps to one registry key.

## What each file does

### `profiles.py`, `profile_extras.py`, and `profile_runner.py`

Registry records category, title, explanation, exact Nmap flags, default ports,
risk, scope, privilege expectation, and timing. Runner turns metadata into shared
CLI, applies guardrails, then launches Nmap. Entry scripts intentionally stay
small; their docstrings repeat use case, core flags, risk, scope, and edit point.

Scopes:

- `authorized`: private targets work directly; other targets require opt-in.
- `private`: public opt-in cannot unlock it.
- `loopback`: only localhost/loopback. All high-risk profiles use this scope.

Use `profile_catalog.py` instead of browsing hundreds of filenames manually.

### `common.py`

- Uses `ipaddress` to recognize loopback, private, and link-local targets.
- Blocks public hostnames/IPs unless user supplies `--allow-public`.
- Rejects option-like targets and malformed ports.
- Finds `nmap` through `PATH` or optional `NMAP_BIN` environment variable.
- Creates timestamped result prefixes and invokes Nmap without shell expansion.

To change default result directory, edit `result_prefix`. Keep `subprocess.run`
using list arguments and `shell=False` default.

### `lab.py` and `lab/server.py`

`lab.py` launches synthetic server as detached Python process. Random health token
proves process identity before stop, preventing stale PID file from killing an
unrelated process. Server binds only to `127.0.0.1`.

To change lab port:

1. Change port in `configurations` inside `lab/server.py`.
2. Update port summaries in `lab.py`, README, and labs.
3. Update `tests/test_lab.py`.
4. Run `python3 tests/run_tests.py` (or `py ...` on Windows).

### `scan_discovery.py`

Uses `-sn`: host discovery without port scan. `--reason` explains online decision.
Change `DEFAULT_TIMING` only after reading Nmap timing documentation.

### `scan_ports.py`

Defaults to unprivileged TCP connect scan (`-sT`) and top 100 ports. `--syn` uses
raw-packet SYN scan (`-sS`). `--show-closed` removes output filter.

To change default breadth, edit `DEFAULT_TOP_PORTS`.

### `scan_services.py`

Adds `-sV`. Default `--version-light` sends fewer probes; `--version-all` sends
every registered version probe. Change default breadth through `DEFAULT_TOP_PORTS`.

### `scan_safe_scripts.py`

Runs NSE expression `default and safe`, plus timeouts. Expression means script
must be in both categories. Keep real-system default conservative.

To test another category in loopback lab, copy this file, rename it, change
`DEFAULT_SCRIPT_EXPRESSION`, update module description, and add wrapper test.

### `scan_udp.py`

Uses `-sU` and intentionally narrow `DEFAULT_PORTS`. Silence often produces
`open|filtered`; UDP needs more time and usually elevated privileges.

### `scan_web.py`

Checks common web ports with service detection, `http-title`, and `http-headers`.
Edit `DEFAULT_WEB_PORTS` for your dev stack. Add script names only after running
`nmap --script-help SCRIPT_NAME` and reviewing safety/category.

### `scan_route.py`

Combines `-sn` and `--traceroute`, so it traces path without port scan. Add `-6`
to its `nmap_args` list for IPv6-only practice.

### `scan_os.py`

Uses `-O`, `--osscan-limit`, and one retry. This keeps fingerprinting bounded.
Requires raw-packet capability and enough port-state evidence for useful guesses.

### `compare_results.py`

Parses Nmap XML with `xml.etree.ElementTree`. Compares address, protocol, port,
state, service, and version. To compare another field, add it to `PortFinding`,
populate it in `parse_report`, then add tests in `test_compare_results.py`.

## Add a new profile use case

1. Add registry row with unique `scan_*` name.
2. Set precise category, description, argument tuple, ports, risk, and scope.
3. Copy closest profile entry script; change docstring and `PROFILE_NAME`.
4. Keep Nmap flags as tuple/list, never one shell command string.
5. Use `private` or `loopback` for broader/higher-impact profiles.
6. Run full test suite; it verifies wrapper, registry, dry run, and safety rules.
7. Smoke-test new profile only against loopback lab first.

Example modification in `scan_web.py`:

```python
DEFAULT_WEB_PORTS = "80,443,3000,8000,8080"
HTTP_SCRIPTS = "http-title,http-headers,http-server-header"
```

Before adding `http-server-header`, inspect it:

```bash
nmap --script-help http-server-header
```

## Test design

- `test_common.py`: target and port safety.
- `test_profiles.py`: every registry row, wrapper, dry run, and risk/scope lock.
- `test_nmap_xml.py`: shared report parser.
- `test_workflows.py`: catalog, exports, batch, watch, and rescan utilities.
- `test_wrappers.py`: command construction using mock Nmap; no network traffic.
- `test_compare_results.py`: XML parsing and changes.
- `test_lab.py`: real loopback TCP health, UDP response, and clean shutdown.
- `run_tests.py`: compiles all Python then runs all tests cross-platform.

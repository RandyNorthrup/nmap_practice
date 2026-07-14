# Script architecture and modification guide

This suite has two scanner styles plus workflow and reporting tools. All use
Python 3 standard library, pass Nmap arguments as a list, and never invoke a
shell for scan execution. Linux, macOS, and Windows use the same Python code.

Examples use `python3`; Windows PowerShell users replace it with `py`.

## Choose the right script type

| Need | Use | Example |
|---|---|---|
| One repeatable technique | Focused profile script | `scan_tls_certificate.py` |
| Ad hoc ports or basic service scan | Flexible scanner | `scan_ports.py`, `scan_services.py` |
| Search hundreds of profiles | Catalog | `profile_catalog.py` |
| Same profile across targets | Batch workflow | `batch_profile.py` |
| Repeated baseline comparison | Watch workflow | `watch_profile.py` |
| Convert saved XML | Report tools | `report_json.py`, `report_markdown.py` |

Focused scripts are intentionally small. Their behavior comes from registry
metadata, so 358 entry points share one validated execution engine.

## Profile execution flow

1. Entry script supplies a `PROFILE_NAME`.
2. `profiles.py` resolves metadata from core rows and `profile_extras.py`.
3. `profile_runner.py` builds shared CLI and enforces risk/scope rules.
4. `common.py` validates target and ports, creates output prefix, and locates Nmap.
5. Nmap runs with list arguments and `-oA`, producing `.nmap`, `.gnmap`, and `.xml`.

No profile entry script should call `subprocess` directly.

## Profile metadata

Each `ScanProfile` contains:

| Field | Meaning |
|---|---|
| `name` | Registry key and filename without `.py` |
| `category` | Catalog grouping such as `tls`, `discovery`, or `inventory` |
| `title` | Short user-facing name |
| `description` | Help text explaining intended use |
| `arguments` | Fixed Nmap argument tuple |
| `default_ports` | Optional user-overridable port expression |
| `scope` | `authorized`, `private`, or `loopback` |
| `risk` | `low`, `medium`, or `high` |
| `elevated` | Whether raw packets/Npcap may be required |
| `timing` | Default `T0` through `T4`, or `None` |

Registry rejects duplicate names and invalid risk/scope values. Extra high-risk
rows are forced to loopback scope during registry construction.

## Shared profile CLI

Run any profile with `--help` before editing it:

```bash
python3 scripts/scan_http_headers.py --help
python3 scripts/scan_http_headers.py 127.0.0.1 --ports 8000 --dry-run
```

| Option | Behavior |
|---|---|
| `TARGET` | Required IP, CIDR, or hostname |
| `--output PREFIX` | Override timestamped output prefix |
| `--allow-public` | Opt into non-private target; does not grant authorization |
| `--ports LIST` | Override ports only when profile defines `default_ports` |
| `--timing T0..T4` | Override timing; `T5` intentionally unavailable |
| `--no-dns` | Add `-n` and disable reverse DNS |
| `--skip-host-discovery` | Add `-Pn` for known-up target |
| `--script-args TEXT` | Add NSE arguments; rejected for non-NSE profiles |
| `--extra-arg OPTION` | Append one advanced Nmap argument |
| `-v`, `-vv`, `-vvv` | Increase Nmap verbosity, capped at three |
| `--dry-run` | Validate and print exact command without starting Nmap |

Advanced arguments cannot control target sources, Nmap data directories, resume
files, or output options. Those stay under runner control. For option/value pairs,
repeat the option:

```bash
python3 scripts/scan_tcp_top_100.py 127.0.0.1 \
  --extra-arg=--max-retries --extra-arg=2 --dry-run
```

Use `--extra-arg` sparingly. It changes traffic beyond documented profile.

## Scope and risk enforcement

| Scope | Allowed target behavior |
|---|---|
| `authorized` | Private/local works directly; other targets need `--allow-public` |
| `private` | Only private, link-local, or loopback; opt-in cannot unlock public |
| `loopback` | Only `localhost`, `127.0.0.0/8`, or `::1` |

| Risk | Intended use |
|---|---|
| `low` | Narrow discovery or information retrieval |
| `medium` | Broader, raw-packet, enumeration, or higher-traffic work |
| `high` | Loopback-only packet, intrusive, or vulnerability experiments |

Risk label describes traffic, not authorization. Even low-risk scans require
permission.

## File map

| Path | Responsibility |
|---|---|
| `scripts/common.py` | Target/port validation, output prefix, Nmap process |
| `scripts/profile_runner.py` | Shared profile CLI and scope enforcement |
| `scripts/profiles.py` | Core profiles, generated NSE families, registry merge |
| `scripts/profile_extras.py` | Additional explicit profile data |
| `scripts/scan_*.py` | One-purpose entry scripts |
| `scripts/profile_catalog.py` | Runtime search/filter tool |
| `scripts/generate_profile_catalog.py` | Rebuild committed Markdown catalog |
| `scripts/nmap_xml.py` | Shared immutable XML model and parser |
| `scripts/report_*.py` | XML validation, extraction, and conversion |
| `scripts/batch_profile.py` | Sequential target-file workflow |
| `scripts/watch_profile.py` | Finite repeated scans and diffs |
| `scripts/rescan_open_ports.py` | Focused TCP/UDP rescan from XML |
| `scripts/lab.py`, `lab/server.py` | Loopback-only synthetic services |

## Reading a focused script

`scan_http_drupal_loopback.py` is representative:

- Docstring states use case, core flags, risk, and scope.
- `PROFILE_NAME` points to matching registry row.
- Runner supplies all options and enforcement.
- Profile is high-risk and therefore loopback-only.
- Local lab is not Drupal, so script may correctly return no Drupal findings.

Inspect without traffic:

```bash
python3 scripts/scan_http_drupal_loopback.py --help
python3 scripts/scan_http_drupal_loopback.py 127.0.0.1 --dry-run
```

## Modify an existing profile

1. Find source row:

   ```bash
   rg 'scan_http_drupal_loopback' scripts/profiles.py scripts/profile_extras.py
   ```

2. Edit metadata in its source file.
3. Update entry script docstring if title, flags, risk, or scope changed.
4. Rebuild catalog:

   ```bash
   python3 scripts/generate_profile_catalog.py --output docs/profile-catalog.md
   ```

5. Verify dry run and full suite:

   ```bash
   python3 scripts/scan_http_drupal_loopback.py 127.0.0.1 --dry-run
   python3 tests/run_tests.py
   ```

6. Smoke-test against loopback lab when profile matches lab service.

## Add a new profile

Add data row to `EXTRA_PROFILE_DATA` in `profile_extras.py`. Example:

```python
{
    "name": "scan_http_practice_metadata",
    "category": "web",
    "title": "Practice HTTP metadata",
    "description": "Read title and server headers from loopback practice HTTP.",
    "arguments": [
        "-sT", "-sV", "--version-light",
        "--script", "http-title,http-server-header",
        "--script-timeout", "30s", "--open",
    ],
    "default_ports": "8000",
    "scope": "loopback",
    "risk": "low",
    "elevated": False,
    "timing": "T3",
},
```

Create matching entry script:

```python
#!/usr/bin/env python3
"""Practice HTTP metadata.

Use case: read title and server headers from loopback practice HTTP.
Risk: low. Scope: loopback.
"""

from profile_runner import run_named_profile


PROFILE_NAME = "scan_http_practice_metadata"


if __name__ == "__main__":
    raise SystemExit(run_named_profile(PROFILE_NAME))
```

Then regenerate catalog and run tests. Tests require every registry row to have
matching entry file and matching `PROFILE_NAME`.

## Add or modify report fields

`nmap_xml.py` is canonical parser. When adding XML data:

1. Add field to relevant immutable dataclass.
2. Populate field in `parse_report`.
3. Update `to_dict` behavior if needed.
4. Add fixture data and assertions in `test_nmap_xml.py`.
5. Update relevant `report_*.py` and workflow tests.

Do not use separate XML parsers for each report.

## Modify local lab

1. Change service/port in `lab/server.py`.
2. Update summaries in `scripts/lab.py` and README.
3. Update `tests/test_lab.py`.
4. Update affected practice labs.
5. Run full suite and verify clean shutdown.

Lab health token proves process identity before stop, preventing stale PID state
from signaling unrelated processes.

## Test coverage

- `test_common.py`: targets, port expressions, public opt-in.
- `test_profiles.py`: registry count, wrappers, dry runs, scope/risk locks.
- `test_nmap_xml.py`: canonical XML parser.
- `test_workflows.py`: catalog, batch, watch, reports, rescan.
- `test_docs.py`: documentation links, script references, catalog freshness.
- `test_wrappers.py`: flexible scanners with mock Nmap.
- `test_compare_results.py`: XML difference logic.
- `test_lab.py`: live loopback TCP/UDP lifecycle.

Run:

```bash
python3 tests/run_tests.py
```

Windows:

```powershell
py tests/run_tests.py
```

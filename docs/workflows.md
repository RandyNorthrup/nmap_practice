# Practical workflows

Examples use `python3`; Windows PowerShell users replace it with `py`. Preview
scan commands with `--dry-run` before sending traffic.

## Find the right profile

Search by protocol, product, purpose, category, risk, or scope:

```bash
python3 scripts/profile_catalog.py --search smb
python3 scripts/profile_catalog.py --category tls --risk low
python3 scripts/profile_catalog.py --scope loopback
python3 scripts/profile_catalog.py --category inventory --json
```

Catalog prints script name, category, risk, and title. Machine-readable JSON also
contains description, scope, privilege expectation, core arguments, and ports.
Full static table: [profile catalog](profile-catalog.md).

## Inspect exact command

```bash
python3 scripts/scan_tcp_top_100.py 127.0.0.1 --dry-run
python3 scripts/scan_tls_certificate.py 127.0.0.1 --ports 8443 --dry-run
python3 scripts/scan_ssh_auth_methods.py 127.0.0.1 \
  --script-args "ssh.user=practice" --dry-run
```

Dry run validates target, scope, ports, timing, script arguments, and output name,
then prints exact Nmap command without starting Nmap.

## Override profile behavior

Common safe overrides:

```bash
python3 scripts/scan_http_headers.py 127.0.0.1 \
  --ports 8000 --no-dns -vv --output results/http-headers

python3 scripts/scan_tcp_top_100.py 127.0.0.1 \
  --skip-host-discovery --timing T2 --dry-run
```

`--ports` exists only for profiles with default ports. `--timing` accepts `T0`
through `T4`; `T5` is excluded. `--script-args` works only on NSE profiles.

Advanced options use repeated `--extra-arg`:

```bash
python3 scripts/scan_tcp_top_100.py 127.0.0.1 \
  --extra-arg=--max-retries --extra-arg=2 --dry-run
```

Runner blocks extra arguments that could replace target source, data directory,
resume file, or output controls.

## Understand output files

Each scan receives `-oA PREFIX` and creates:

| File | Best use |
|---|---|
| `PREFIX.nmap` | Human-readable Nmap output |
| `PREFIX.gnmap` | Legacy line-oriented parsing |
| `PREFIX.xml` | Reporting, comparison, and rescans |

Without `--output`, prefix is timestamped under `results/`. With explicit output:

```bash
python3 scripts/scan_service_light.py 127.0.0.1 \
  --ports 2222,8000,9000 --output results/lab-baseline
```

## Baseline and focused rescan

1. Create baseline:

   ```bash
   python3 scripts/scan_tcp_top_1000.py 192.168.1.10 \
     --output results/device-baseline
   ```

2. Preview focused service rescans from open TCP and UDP ports:

   ```bash
   python3 scripts/rescan_open_ports.py results/device-baseline.xml --dry-run
   ```

3. Run rescan:

   ```bash
   python3 scripts/rescan_open_ports.py results/device-baseline.xml --max-hosts 32
   ```

Rescan accepts multiple XML paths, prefixes, or globs. It groups open ports by
host and protocol, invokes `scan_services.py` for TCP and `scan_udp.py` for UDP,
and uses their normal timestamped output. `--max-hosts` defaults to 32 and accepts
1 through 256. Public addresses still require `--allow-public`.

## Batch authorized targets

Create `targets.txt`:

```text
# One authorized IP, CIDR, or hostname per line
127.0.0.1
192.168.1.10
```

Preview, then run:

```bash
python3 scripts/batch_profile.py scan_tcp_top_100 targets.txt --dry-run
python3 scripts/batch_profile.py scan_tcp_top_100 targets.txt \
  --output-dir results/batch-top100
```

Batch behavior:

- Runs sequentially, never concurrently.
- Ignores blank lines and text after `#`.
- Uses selected profile defaults.
- Creates numbered output prefixes per target.
- Stops on first failure unless `--continue-on-error` is supplied.
- Applies profile scope rules independently to every target.

Review target file before running. Batch tool intentionally does not accept
profile port/timing overrides; create or edit a profile when repeatability matters.

## Watch bounded changes

```bash
python3 scripts/watch_profile.py scan_tcp_top_100 127.0.0.1 \
  --count 3 --interval 60 --output-dir results/watch-lab
```

Watch behavior:

- Requires finite count from 2 through 100.
- Requires at least five seconds between real scans.
- Saves every XML report.
- Compares each run with previous and prints added, removed, or changed ports.
- Keeps selected profile scope/risk enforcement.

Preview two runs without waiting:

```bash
python3 scripts/watch_profile.py scan_tcp_top_100 127.0.0.1 \
  --count 2 --dry-run
```

## Validate and summarize XML

Single-report tools:

```bash
python3 scripts/report_validate.py results/lab-baseline.xml
python3 scripts/report_hosts.py results/lab-baseline.xml --up-only
python3 scripts/report_services.py results/lab-baseline.xml
python3 scripts/report_scripts.py results/lab-baseline.xml
```

Multi-report tools accept paths, prefixes, and globs:

```bash
python3 scripts/report_summary.py "results/*.xml"
python3 scripts/report_stats.py "results/*.xml"
python3 scripts/report_open_ports.py "results/*.xml"
python3 scripts/report_json.py "results/*.xml" --output report.json
python3 scripts/report_csv.py "results/*.xml" --output report.csv
python3 scripts/report_markdown.py "results/*.xml" --output report.md
```

Quote globs so Python expands them consistently on Bash and PowerShell. JSON is
one object for one report and a list for multiple reports. CSV emits one row per
port record. Markdown emits one table row per port record.

## Compare two baselines

```bash
python3 scripts/compare_results.py results/old.xml results/new.xml
```

Comparator reports added, removed, and changed address/protocol/port records,
including state, service, and version changes.

## Public-target workflow

Only proceed with explicit written permission and exact scope:

```bash
python3 scripts/scan_tls_certificate.py authorized.example \
  --allow-public --ports 443 --dry-run
```

Then remove `--dry-run`. `--allow-public` only disables software guard; it does
not establish permission. `private` and `loopback` profiles cannot be unlocked.

## Troubleshooting

| Symptom | Likely cause | Next check |
|---|---|---|
| `Public or unresolved target blocked` | Non-private hostname/IP | Confirm permission; use opt-in only if authorized |
| `profile is locked` | Scope mismatch | Choose authorized profile or correct target |
| Raw-packet privilege error | SYN/UDP/OS/SCTP profile | Use `sudo` or Administrator/Npcap |
| `open|filtered` UDP | No UDP response | Compare neighbor ports and `--reason` |
| No NSE output | Service/script mismatch | Verify open service, script help, and arguments |
| XML parser error | Not Nmap XML or incomplete file | Run `report_validate.py` |
| Watch comparison missing | First run or dry-run | Comparison begins after second real XML report |

## Modify or add workflows

Follow [script architecture guide](script-guide.md). Keep workflows finite,
sequential by default, scope-aware, cross-platform, and covered by tests.

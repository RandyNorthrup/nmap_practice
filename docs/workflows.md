# Robust workflows

Examples use `python3`; Windows PowerShell uses `py`. Start with `--dry-run`.

## Find a script

```bash
python3 scripts/profile_catalog.py --search smb
python3 scripts/profile_catalog.py --category tls --risk low
python3 scripts/profile_catalog.py --scope loopback
```

Full table: [profile catalog](profile-catalog.md).

## Inspect command without scanning

```bash
python3 scripts/scan_tcp_top_100.py 127.0.0.1 --dry-run
python3 scripts/scan_tls_certificate.py 127.0.0.1 --ports 8443 --dry-run
```

Dry run validates target, ports, profile scope, timing, and output name, then
prints exact Nmap command without starting Nmap.

## Batch authorized targets

Create `targets.txt`:

```text
# One IP/CIDR per line
127.0.0.1
192.168.1.10
```

Preview, then run:

```bash
python3 scripts/batch_profile.py scan_tcp_top_100 targets.txt --dry-run
python3 scripts/batch_profile.py scan_tcp_top_100 targets.txt --output-dir results/batch-top100
```

Runs are sequential. Default stops on first error; add `--continue-on-error` to
finish file. Each target gets unique output prefix.

## Watch for bounded changes

```bash
python3 scripts/watch_profile.py scan_tcp_top_100 127.0.0.1 --count 3 --interval 60
```

Watch requires finite count from 2 through 100 and minimum five-second interval.
Each XML report is retained and compared with previous run.

## Focus rescan on discovered TCP ports

```bash
python3 scripts/rescan_open_ports.py results/baseline.xml --dry-run
python3 scripts/rescan_open_ports.py results/baseline.xml --output-dir results/rescan
```

Utility extracts open TCP ports per host and runs full service probes only on
those ports. Original XML target addresses pass same public/private guard.

## Convert and extract reports

```bash
python3 scripts/report_validate.py results/baseline.xml
python3 scripts/report_summary.py results/baseline.xml
python3 scripts/report_json.py results/baseline.xml > report.json
python3 scripts/report_csv.py results/baseline.xml --output report.csv
python3 scripts/report_markdown.py results/baseline.xml > report.md
python3 scripts/report_hosts.py results/baseline.xml --up-only
python3 scripts/report_open_ports.py results/baseline.xml
python3 scripts/report_services.py results/baseline.xml
python3 scripts/report_scripts.py results/baseline.xml
```

Shell redirection examples work in Bash and PowerShell. `report_csv.py --output`
avoids redirection and handles newline differences natively.

## Compare baselines

```bash
python3 scripts/compare_results.py results/old.xml results/new.xml
```

Reports added, removed, and changed state/service/version rows.

## Modify safely

Follow [script guide](script-guide.md). Always update tests and catalog-facing
metadata. Use loopback for new high-impact experiments.

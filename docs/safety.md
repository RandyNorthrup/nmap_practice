# Safety, authorization, scope, and risk

Nmap measures networks by sending packets and application probes. Scans can
trigger alerts, consume device resources, violate policy, or be treated as
hostile. Tool guardrails reduce mistakes; they do not create permission.

## Before every scan

1. Identify exact IP, hostname, or CIDR you may scan.
2. Confirm owner and explicit authorization.
3. Confirm allowed timing, scan types, ports, NSE scripts, and exclusions.
4. Start with one host, narrow ports, `T3`, and `--dry-run`.
5. Save output and stop if target becomes unstable.
6. Treat XML and reports as potentially sensitive inventory.

## Target guard

These ranges work without public opt-in:

- Loopback: `127.0.0.0/8`, `localhost`, `::1`
- RFC 1918: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`
- IPv4 link-local: `169.254.0.0/16`
- IPv6 private/link-local: `fc00::/7`, `fe80::/10`

Other targets require `--allow-public`. This only bypasses target guard after you
confirm authorization. It does not unlock `private` or `loopback` profiles.

## Profile scope

| Scope | Enforcement |
|---|---|
| `authorized` | Private/local directly; other targets require explicit opt-in |
| `private` | Private, link-local, or loopback only |
| `loopback` | Localhost/loopback only |

All high-risk registry profiles are forced to loopback scope. View them:

```bash
python3 scripts/profile_catalog.py --risk high
python3 scripts/profile_catalog.py --scope loopback
```

## Risk labels

| Risk | Typical behavior | Starting point |
|---|---|---|
| `low` | Narrow discovery or metadata retrieval | Authorized target, dry-run first |
| `medium` | Raw packets, broader ports, enumeration, more probes | One host, narrow override |
| `high` | Intrusive categories, vulnerability checks, packet experiments | Loopback only, enforced |

Low risk does not mean harmless or authorized.

## Safer learning order

1. Loopback lab.
2. TCP connect (`-sT`) and host discovery (`-sn`).
3. Narrow service detection (`-sV --version-light`).
4. Low-risk protocol-specific NSE profiles.
5. UDP, SYN, OS, SCTP, and medium profiles with elevation.
6. High-risk loopback profiles only after reading exact flags and NSE help.

## NSE cautions

- Read `nmap --script-help SCRIPT` first.
- Match script to service; do not spray every NSE profile at every port.
- Use `--script-args` only with values you understand.
- Empty output can mean script/service mismatch, filtered traffic, or no finding.
- Brute-force, denial-of-service, exploit, and fuzzer profiles are excluded.
- Intrusive/vulnerability practice profiles remain loopback-only.

## Elevated privileges

SYN, UDP, SCTP, OS, and raw-packet profiles may require:

- Linux/macOS: `sudo` or appropriate capabilities.
- Windows: Administrator terminal and functional Npcap.

Elevation expands packet capabilities and risk. Prefer unprivileged TCP connect
until raw-packet behavior is actual lesson.

## Timing and breadth

- Suite offers `T0` through `T4`; `T5` intentionally excluded.
- Full `-p-` and broad UDP profiles can be slow/noisy.
- Use `--ports` to narrow profiles that define default ports.
- Use one host before CIDR.
- Batch runs sequentially, but target file still needs manual review.
- Watch runs are finite and rate-limited; do not create infinite loops around scans.

## Advanced arguments

`--extra-arg` allows controlled experimentation but changes documented traffic.
Runner blocks target-file, random-target, resume, Nmap-data, and output controls.
Always use `--dry-run` and update notes when extra arguments are used.

## Results handling

Nmap reports can reveal:

- Live hosts and addressing.
- Open management interfaces.
- Software versions and platform clues.
- User/domain/service metadata from NSE.

Keep `results/` private, remove reports when no longer needed, and do not publish
inventory without owner approval.

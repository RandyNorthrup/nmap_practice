# Safe scanning rules

Nmap is a network measurement tool. A scan can trigger alerts, consume device
resources, violate a service agreement, or be treated as hostile.

## Before every scan

1. Identify the exact IP address or CIDR range you may scan.
2. Confirm who owns it and that you have explicit permission.
3. Agree on timing, scan types, rate limits, and excluded systems.
4. Start small: one host, common ports, normal timing (`-T3`).
5. Save results and stop if a device becomes unstable.

The wrappers allow these targets without an extra flag:

- Loopback: `127.0.0.0/8`, `localhost`, and `::1`
- RFC 1918 IPv4: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`
- Link-local IPv4: `169.254.0.0/16`
- Private/link-local IPv6: `fc00::/7` and `fe80::/10`

Other targets require `--allow-public`. That option only disables the software
guardrail. It does not establish authorization.

## Keep early practice low impact

- Use this repository's loopback lab first.
- Prefer `-sT`, `-sn`, `--top-ports`, and `-T3` while learning.
- Use `--script "default and safe"` before exploring other NSE categories.
- Avoid `brute`, `dos`, `exploit`, `fuzzer`, `intrusive`, and `vuln` NSE groups on
  real systems unless the owner explicitly approved those tests.
- UDP scans and full `-p-` scans can be slow and noisy. Narrow the port list.
- Never assume an Internet hostname is a practice target. Read its policy first.

## Elevated privileges

Nmap can perform more raw-packet scan types with elevated privileges. Extra
capability increases risk. Kit uses unprivileged TCP connect scans by default.
SYN, UDP, and OS scans may need `sudo` on Linux/macOS or an Administrator terminal
with Npcap on Windows.

#!/usr/bin/env python3
"""Render complete Markdown profile catalog from live registry metadata."""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
import sys

from profiles import PROFILES, ScanProfile


def code(value: str) -> str:
    escaped = value.replace("|", "\\|")
    return f"`{escaped}`"


def render_row(item: ScanProfile) -> str:
    ports = code(item.default_ports) if item.default_ports else "—"
    flags = code(" ".join(item.arguments))
    elevated = "yes" if item.elevated else "no"
    return (
        f"| `{item.name}.py` | {item.title} | {item.risk} | {item.scope} | "
        f"{elevated} | {ports} | {flags} |"
    )


def render_catalog() -> str:
    groups: dict[str, list[ScanProfile]] = defaultdict(list)
    for item in PROFILES.values():
        groups[item.category].append(item)

    lines = [
        "# Complete profile catalog",
        "",
        f"Generated from live registry. Contains **{len(PROFILES)} profiles**. Each script",
        "accepts shared options documented in [script guide](script-guide.md). Use",
        "`profile_catalog.py` for interactive search and filtering.",
        "",
        "```bash",
        "python3 scripts/profile_catalog.py --search tls",
        "python3 scripts/profile_catalog.py --category discovery --risk low",
        "```",
        "",
        "## Risk and scope",
        "",
        "- `low`: narrow discovery or information retrieval.",
        "- `medium`: broader, raw-packet, enumeration, or higher-traffic behavior.",
        "- `high`: loopback-only experiments enforced by runner.",
        "- `authorized`: private targets work directly; public/unresolved targets need explicit opt-in.",
        "- `private`: only private, link-local, or loopback targets.",
        "- `loopback`: only localhost, `127.0.0.0/8`, or `::1`.",
    ]
    for category in sorted(groups):
        items = sorted(groups[category], key=lambda item: item.name)
        lines.extend((
            "",
            f"## {category} ({len(items)})",
            "",
            "| Script | Purpose | Risk | Scope | Elevated | Default ports | Core flags |",
            "|---|---|---|---|---|---|---|",
            *(render_row(item) for item in items),
        ))
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", help="Write Markdown to path instead of stdout")
    parser.add_argument("--check", help="Fail when path differs from generated catalog")
    args = parser.parse_args()
    text = render_catalog()
    if args.check:
        try:
            current = Path(args.check).read_text(encoding="utf-8")
        except OSError as error:
            print(f"Error: {error}", file=sys.stderr)
            return 1
        if current != text:
            print(f"Catalog is stale: {args.check}", file=sys.stderr)
            return 1
        print(f"Catalog current: {args.check}")
        return 0
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

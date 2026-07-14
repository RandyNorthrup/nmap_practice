#!/usr/bin/env python3
"""Search/list all practice profiles without sending network traffic."""

from __future__ import annotations

import argparse
import json

from profiles import PROFILES


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Search the Nmap practice profile catalog.")
    parser.add_argument("--category", choices=sorted({p.category for p in PROFILES.values()}))
    parser.add_argument("--risk", choices=("low", "medium", "high"))
    parser.add_argument("--scope", choices=("authorized", "private", "loopback"))
    parser.add_argument("--search", help="Case-insensitive name/title/description search")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    items = sorted(PROFILES.values(), key=lambda item: (item.category, item.name))
    if args.category:
        items = [item for item in items if item.category == args.category]
    if args.risk:
        items = [item for item in items if item.risk == args.risk]
    if args.scope:
        items = [item for item in items if item.scope == args.scope]
    if args.search:
        needle = args.search.casefold()
        items = [
            item for item in items
            if needle in f"{item.name} {item.title} {item.description}".casefold()
        ]

    if args.json:
        print(json.dumps([
            {
                "name": item.name,
                "category": item.category,
                "title": item.title,
                "description": item.description,
                "risk": item.risk,
                "scope": item.scope,
                "elevated": item.elevated,
                "arguments": list(item.arguments),
                "default_ports": item.default_ports,
            }
            for item in items
        ], indent=2))
    else:
        for item in items:
            print(f"{item.name:42} {item.category:14} {item.risk:6} {item.title}")
        print(f"Profiles: {len(items)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

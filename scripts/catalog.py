#!/usr/bin/env python3
"""Search all profiles and display text, Markdown, or JSON catalog output."""

from __future__ import annotations

import argparse
from dataclasses import asdict
import json

from profiles import PROFILES


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Browse Nmap practice profiles.")
    parser.add_argument("query", nargs="?", default="", help="Search name/title/category/description")
    parser.add_argument("--category", help="Exact category filter")
    parser.add_argument("--format", choices=("text", "markdown", "json"), default="text")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    query = args.query.lower()
    items = sorted(PROFILES.values(), key=lambda item: (item.category, item.name))
    items = [
        item for item in items
        if (not args.category or item.category == args.category)
        and (not query or query in f"{item.name} {item.title} {item.category} {item.description}".lower())
    ]
    if args.format == "json":
        print(json.dumps([asdict(item) for item in items], indent=2))
    elif args.format == "markdown":
        print("| Profile | Category | Risk | Scope | Purpose |")
        print("|---|---|---|---|---|")
        for item in items:
            print(f"| `{item.name}` | {item.category} | {item.risk} | {item.scope} | {item.description} |")
    else:
        for item in items:
            elevated = " elevated" if item.elevated else ""
            print(f"{item.name:32} {item.category:16} {item.risk:6}{elevated:10} {item.title}")
        print(f"\n{len(items)} profile(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

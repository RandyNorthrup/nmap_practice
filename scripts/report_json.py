#!/usr/bin/env python3
"""Convert one or more Nmap XML reports, including run metadata, to JSON."""

import argparse
import json
from pathlib import Path
import sys

from nmap_xml import parse_reports


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reports", nargs="+", help="XML paths, prefixes, or globs")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        reports = parse_reports(args.reports)
    except (FileNotFoundError, OSError, ValueError) as error:
        parser.error(str(error))
    payload: object = reports[0].to_dict() if len(reports) == 1 else [item.to_dict() for item in reports]
    text = json.dumps(payload, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

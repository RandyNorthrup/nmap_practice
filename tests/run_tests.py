#!/usr/bin/env python3
"""Cross-platform syntax and unit/integration test runner."""

from __future__ import annotations

from pathlib import Path
import py_compile
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]


def compile_python_files() -> bool:
    files = [
        *ROOT.rglob("scripts/*.py"),
        *ROOT.rglob("lab/*.py"),
        *ROOT.rglob("tests/*.py"),
    ]
    success = True
    for path in files:
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as error:
            print(error, file=sys.stderr)
            success = False
    return success


def main() -> int:
    if not compile_python_files():
        return 1
    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"), pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())

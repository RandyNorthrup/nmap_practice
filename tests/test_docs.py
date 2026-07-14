from __future__ import annotations

from pathlib import Path
import re
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from generate_profile_catalog import render_catalog  # noqa: E402
from profiles import PROFILES  # noqa: E402


DOCS = (ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md")))


class DocumentationTests(unittest.TestCase):
    def test_profile_catalog_is_generated_from_current_registry(self) -> None:
        catalog = (ROOT / "docs" / "profile-catalog.md").read_text(encoding="utf-8")
        self.assertEqual(render_catalog(), catalog)
        self.assertEqual(len(PROFILES), catalog.count("| `scan_"))

    def test_documented_profile_count_is_current(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"{len(PROFILES)} focused scan profiles", readme)

    def test_relative_markdown_links_exist(self) -> None:
        link_pattern = re.compile(r"]\(([^)]+)\)")
        for document in DOCS:
            text = document.read_text(encoding="utf-8")
            for target in link_pattern.findall(text):
                if target.startswith(("http://", "https://", "#")):
                    continue
                path_text = target.split("#", 1)[0].strip("<>")
                if not path_text:
                    continue
                with self.subTest(document=document.name, target=target):
                    self.assertTrue((document.parent / path_text).exists())

    def test_referenced_scan_scripts_exist(self) -> None:
        profile_pattern = re.compile(r"\b(scan_[A-Za-z0-9_.-]+\.py)\b")
        for document in DOCS:
            text = document.read_text(encoding="utf-8")
            for filename in profile_pattern.findall(text):
                with self.subTest(document=document.name, script=filename):
                    self.assertTrue((SCRIPTS / filename).is_file())

    def test_guides_cover_current_workflows(self) -> None:
        script_guide = (ROOT / "docs" / "script-guide.md").read_text(encoding="utf-8")
        workflows = (ROOT / "docs" / "workflows.md").read_text(encoding="utf-8")
        labs = (ROOT / "docs" / "practice-labs.md").read_text(encoding="utf-8")
        for phrase in ("Shared profile CLI", "profile_extras.py", "generate_profile_catalog.py"):
            self.assertIn(phrase, script_guide)
        for phrase in ("Batch authorized targets", "Watch bounded changes", "Validate and summarize XML"):
            self.assertIn(phrase, workflows)
        self.assertGreaterEqual(len(re.findall(r"^## Lab ", labs, flags=re.MULTILINE)), 20)


if __name__ == "__main__":
    unittest.main()

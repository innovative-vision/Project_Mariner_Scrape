import tempfile
import unittest
from pathlib import Path

from scripts.check_readme import REQUIRED_PHRASES, validate_readme


class CheckReadmeTests(unittest.TestCase):
    def test_validate_readme_passes_when_all_required_sections_exist(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "README.md"
            path.write_text("\n".join(REQUIRED_PHRASES), encoding="utf-8")

            self.assertEqual([], validate_readme(path))

    def test_validate_readme_reports_missing_sections(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "README.md"
            path.write_text("# Project Mariner Scrape\n## Validation", encoding="utf-8")

            missing = validate_readme(path)

        self.assertIn("## Android phone access", missing)
        self.assertIn("## What else you'll need", missing)


if __name__ == "__main__":
    unittest.main()

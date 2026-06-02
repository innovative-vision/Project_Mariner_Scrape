import unittest

from project_mariner_scrape.setup_requirements import (
    build_repository_options,
    build_setup_checklist,
    render_checklist,
)


class SetupRequirementsTests(unittest.TestCase):
    def test_checklist_includes_android_and_laptop_sections(self) -> None:
        checklist = build_setup_checklist()

        self.assertIn("Android phone with Chrome installed", checklist["android"])
        self.assertIn("Laptop with Chrome tabs available for the Mariner session", checklist["laptop"])

    def test_missing_api_key_is_called_out_before_first_run(self) -> None:
        checklist = build_setup_checklist()

        self.assertIn("Get a Google AI Studio API key before first run", checklist["common"])

    def test_existing_api_key_removes_extra_prompt(self) -> None:
        checklist = build_setup_checklist(has_api_key=True)

        self.assertNotIn("Get a Google AI Studio API key before first run", checklist["common"])
        self.assertIn("Google AI Studio API key", checklist["common"])

    def test_rendered_output_contains_all_group_titles(self) -> None:
        rendered = render_checklist()

        self.assertIn("Common requirements:", rendered)
        self.assertIn("Laptop / Chrome tabs:", rendered)
        self.assertIn("Android phone access:", rendered)
        self.assertIn("Optional but recommended:", rendered)
        self.assertIn("Current repo choices:", rendered)

    def test_repository_options_include_current_and_legacy_paths(self) -> None:
        repositories = build_repository_options()

        self.assertTrue(any("google-gemini-spark/gemini-spark" in item for item in repositories))
        self.assertTrue(any("Fandry96/k3-mariner" in item for item in repositories))


if __name__ == "__main__":
    unittest.main()

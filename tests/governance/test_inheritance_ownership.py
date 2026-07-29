import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[2]
MANIFEST = ROOT / ".github/inheritance/manifest.json"
PROFILE = ROOT / ".github/inheritance/agent-profile.json"
PROJECT_OVERLAY = ROOT / ".ai/project/agent-overlay.md"
MODULE_PATH = ROOT / "scripts/template_inheritance.py"
SPEC = importlib.util.spec_from_file_location("template_inheritance", MODULE_PATH)
inheritance = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inheritance)

EXPECTED_AGENT_INPUTS = [
    {
        "layer": "foundation",
        "repository": "Yukihide-Mitsuoka/ai-dev-foundation",
        "path": ".ai/contracts/foundation/agent-entry.md",
    },
    {
        "layer": "project",
        "repository": "Yukihide-Mitsuoka/terraform-gcp-template",
        "path": ".ai/project/agent-overlay.md",
    },
]


class InheritanceOwnershipTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_shared_ai_contract_files_are_inherited(self):
        for path in (
            ".ai/project-document-maintenance.md",
            ".claude/README.md",
        ):
            with self.subTest(path=path):
                self.assertIn(path, self.manifest["inherited_paths"])

    def test_repository_changelog_is_protected(self):
        self.assertIn("CHANGELOG.md", self.manifest["protected_paths"])
        self.assertNotIn("CHANGELOG.md", self.manifest["inherited_paths"])

    def test_manifest_v2_declares_ordered_agent_profile(self):
        self.assertEqual(self.manifest["schema_version"], 2)
        profile = json.loads(PROFILE.read_text(encoding="utf-8"))
        self.assertEqual(profile["schema_version"], 1)
        self.assertEqual(profile["authority_policy"], "strengthen-only")
        self.assertEqual(profile["inputs"], EXPECTED_AGENT_INPUTS)

    def test_agent_profile_ownership_is_explicit(self):
        self.assertIn(
            ".ai/contracts/foundation/", self.manifest["inherited_paths"]
        )
        for path in (
            ".github/inheritance/agent-profile.json",
            ".ai/project/",
        ):
            with self.subTest(path=path):
                self.assertIn(path, self.manifest["protected_paths"])
        self.assertTrue(PROJECT_OVERLAY.is_file())

    def test_validator_reports_foundation_then_project(self):
        result = inheritance.validate_inheritance(ROOT)

        self.assertEqual(result["schema_version"], 2)
        self.assertEqual(
            result["agent_contract"]["authority_policy"], "strengthen-only"
        )
        self.assertEqual(result["agent_contract"]["inputs"], EXPECTED_AGENT_INPUTS)


if __name__ == "__main__":
    unittest.main()

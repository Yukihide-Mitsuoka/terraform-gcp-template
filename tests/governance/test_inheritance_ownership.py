import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[2]
MANIFEST = ROOT / ".github/inheritance/manifest.json"
PROFILE = ROOT / ".github/inheritance/agent-profile.json"
PROJECT_OVERLAY = ROOT / ".ai/project/agent-overlay.md"
CLAUDE_ADAPTER = ROOT / "CLAUDE.md"
AGENT_ADAPTER = ROOT / "AGENTS.md"
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

    def test_entry_adapters_are_thin_identity_free_and_profile_driven(self):
        claude = CLAUDE_ADAPTER.read_text(encoding="utf-8")
        agents = AGENT_ADAPTER.read_text(encoding="utf-8")
        agents_normalized = " ".join(agents.split())

        self.assertLessEqual(len(claude.splitlines()), 50)
        for required in (
            ".github/inheritance/agent-profile.json",
            "strengthen-only",
            "inputs[].path",
            "listed order",
            "must not recursively",
        ):
            with self.subTest(required=required):
                self.assertIn(required, claude)
        for identity in (
            "{{PROJECT_NAME}}",
            "{{STACK}}",
            "Yukihide-Mitsuoka/terraform-gcp-template",
            "Terraform on GCP",
        ):
            with self.subTest(identity=identity):
                self.assertNotIn(identity, claude)
        self.assertIn("CLAUDE.md", agents)
        self.assertIn("explicit agent profile", agents_normalized)

    def test_project_overlay_contains_only_terraform_repository_facts(self):
        overlay = PROJECT_OVERLAY.read_text(encoding="utf-8")

        self.assertIn("Yukihide-Mitsuoka/terraform-gcp-template", overlay)
        self.assertIn("Terraform on Google Cloud", overlay)
        for reusable_or_legacy_content in (
            "remain the active agent entry",
            ".ai/workflow.md",
            "make ",
            "Stop and ask",
        ):
            with self.subTest(content=reusable_or_legacy_content):
                self.assertNotIn(reusable_or_legacy_content, overlay)


if __name__ == "__main__":
    unittest.main()

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[2]
MANIFEST = ROOT / ".github/inheritance/manifest.json"
IGNORE = ROOT / ".templatesyncignore"
BUGFIX_SKILL = ROOT / ".skills/bugfix.skill.md"
PROFILE = ROOT / ".github/inheritance/agent-profile.json"
PROJECT_OVERLAY = ROOT / ".ai/project/agent-overlay.md"
TEMPLATE_OVERLAY = (
    ROOT
    / ".ai/contracts/templates/yukihide-mitsuoka/terraform-gcp-template/agent-overlay.md"
)
TEMPLATE_EXPORT = (
    ROOT
    / ".ai/contracts/templates/yukihide-mitsuoka/terraform-gcp-template/inheritance-export.json"
)
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
EXPECTED_EXPORT_INPUTS = [
    EXPECTED_AGENT_INPUTS[0],
    {
        "layer": "template",
        "repository": "Yukihide-Mitsuoka/terraform-gcp-template",
        "path": ".ai/contracts/templates/yukihide-mitsuoka/terraform-gcp-template/agent-overlay.md",
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

    def test_foundation_bugfix_skill_is_inherited_and_transportable(self):
        path = ".skills/bugfix.skill.md"
        ignored = {
            line.strip()
            for line in IGNORE.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        }
        skill = BUGFIX_SKILL.read_text(encoding="utf-8")

        self.assertIn(path, self.manifest["inherited_paths"])
        self.assertNotIn(path, self.manifest["protected_paths"])
        self.assertNotIn(path, ignored)
        self.assertIn("Sweep for siblings", skill)
        self.assertIn("Sibling occurrences searched; results reported", skill)
        for trigger in ("バグ修正", "不具合修正", "バグ", "障害"):
            with self.subTest(trigger=trigger):
                self.assertIn(trigger, skill)

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

    def test_owner_qualified_template_overlay_exports_only_family_rules(self):
        template_root = (
            ".ai/contracts/templates/yukihide-mitsuoka/terraform-gcp-template/"
        )
        overlay = TEMPLATE_OVERLAY.read_text(encoding="utf-8")

        self.assertIn(template_root, self.manifest["protected_paths"])
        self.assertIn("Terraform on Google Cloud", overlay)
        self.assertIn("iac-scan", overlay)
        self.assertIn("immutable release tags", overlay)
        self.assertNotIn("Repository: `Yukihide-Mitsuoka/terraform-gcp-template`", overlay)
        self.assertNotIn(".ai/project/", overlay)

    def test_owner_qualified_bootstrap_export_defines_direct_child_contract(self):
        export_path = (
            ".ai/contracts/templates/yukihide-mitsuoka/terraform-gcp-template/"
            "inheritance-export.json"
        )
        export = inheritance._validate_bootstrap_export(
            export_path,
            json.loads(TEMPLATE_EXPORT.read_text(encoding="utf-8")),
            "Yukihide-Mitsuoka/terraform-gcp-template",
        )

        self.assertEqual(export["agent_inputs"], EXPECTED_EXPORT_INPUTS)
        for inherited in (
            ".ai/contracts/templates/yukihide-mitsuoka/terraform-gcp-template/",
            ".github/governance/profiles/",
            "profiles/terraform-gcp/",
        ):
            with self.subTest(inherited=inherited):
                self.assertIn(inherited, export["inherited_paths"])
        for protected in (
            ".ai/project/",
            ".github/workflows/",
            "README.md",
            "infra/",
            "docs/inheritance/readmes/",
        ):
            with self.subTest(protected=protected):
                self.assertIn(protected, export["protected_paths"])


if __name__ == "__main__":
    unittest.main()

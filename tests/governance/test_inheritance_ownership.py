import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[2]
MANIFEST = ROOT / ".github/inheritance/manifest.json"


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


if __name__ == "__main__":
    unittest.main()

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[2]
MODULE_PATH = ROOT / "scripts/template_inheritance.py"
SPEC = importlib.util.spec_from_file_location("template_inheritance", MODULE_PATH)
inheritance = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inheritance)
PARENT_REPOSITORY = "Yukihide-Mitsuoka/terraform-gcp-template"
CHILD_REPOSITORY = "Yukihide-Mitsuoka/bootstrap-proof"
SOURCE_COMMIT = "a" * 40


class ChildBootstrapPortabilityTest(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory(dir=ROOT.parent)
        self.child = Path(self.temporary_directory.name) / "child"
        shutil.copytree(
            ROOT,
            self.child,
            ignore=shutil.ignore_patterns(
                ".git", ".terraform", "__pycache__", ".pytest_cache"
            ),
        )
        export_path = (
            self.child
            / ".ai/contracts/templates/yukihide-mitsuoka/terraform-gcp-template/inheritance-export.json"
        )
        export = inheritance._validate_bootstrap_export(
            export_path.relative_to(self.child).as_posix(),
            json.loads(export_path.read_text(encoding="utf-8")),
            PARENT_REPOSITORY,
        )
        desired = inheritance._bootstrap_desired(
            self.child,
            CHILD_REPOSITORY,
            PARENT_REPOSITORY,
            SOURCE_COMMIT,
            export,
        )
        for path, value in (
            (".github/inheritance/manifest.json", desired["manifest"]),
            (".github/inheritance/lock.json", desired["lock"]),
            (".github/inheritance/agent-profile.json", desired["agent_profile"]),
        ):
            (self.child / path).write_text(
                json.dumps(value, indent=2) + "\n", encoding="utf-8"
            )
        (self.child / ".templatesyncignore").write_text(
            "\n".join(desired["template_sync_ignore"]) + "\n", encoding="utf-8"
        )
        (self.child / ".ai/project/agent-overlay.md").write_text(
            "# Project Agent Overlay\n\n"
            f"- Repository: `{CHILD_REPOSITORY}`.\n"
            "- Stack: Terraform on Google Cloud.\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self.temporary_directory.cleanup()

    def test_seed_governance_tests_pass_for_bootstrapped_child(self):
        for relative_path in (
            "tests/governance/test_inheritance_ownership.py",
            "tests/governance/test_terraform_profile.py",
        ):
            with self.subTest(test=relative_path):
                result = subprocess.run(
                    [sys.executable, str(self.child / relative_path)],
                    cwd=self.child,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(
                    result.returncode,
                    0,
                    msg=f"{result.stdout}\n{result.stderr}",
                )


if __name__ == "__main__":
    unittest.main()

"""Native Task executes the repository-owned Terraform command boundary."""

import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class TaskfileTest(unittest.TestCase):
    def test_no_make_entry_or_optional_profile_copy_remains(self):
        for path in ("Makefile", "profiles/README.md", "profiles/python-uv/Makefile",
                     "profiles/typescript-node/Makefile", "profiles/terraform-gcp/Makefile"):
            with self.subTest(path=path):
                self.assertFalse((ROOT / path).exists())

    def test_all_canonical_tasks_are_listed_without_execution(self):
        result = subprocess.run(["task", "--list-all"], cwd=ROOT,
                                capture_output=True, text=True, check=True)
        for name in ("help", "setup", "format", "lint", "test", "test-unit",
                     "test-integration", "coverage", "build", "run", "plan",
                     "security-scan", "sbom", "clean", "doctor"):
            with self.subTest(task=name):
                self.assertIn(f"* {name}:", result.stdout)

    def test_file_argument_is_quoted_and_tool_failure_is_propagated(self):
        with tempfile.TemporaryDirectory() as directory:
            tool = Path(directory) / "terraform"
            capture = Path(directory) / "capture"
            tool.write_text('#!/bin/sh\nprintf "%s\\n" "$@" > "$CAPTURE_FILE"\n', encoding="utf-8")
            tool.chmod(0o755)
            env = os.environ.copy()
            env.update(PATH=f"{directory}:{env['PATH']}", CAPTURE_FILE=str(capture))
            file_name = 'sample "quoted" `printf BAD`.tf'
            subprocess.run(["task", "format", f"FILE={file_name}"], cwd=ROOT,
                           env=env, capture_output=True, text=True, check=True)
            self.assertEqual(capture.read_text(encoding="utf-8").splitlines(), ["fmt", file_name])
            tool.write_text("#!/bin/sh\nexit 23\n", encoding="utf-8")
            result = subprocess.run(["task", "format", "FILE=sample.tf"], cwd=ROOT,
                                    env=env, capture_output=True, text=True, check=False)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("exit status 23", result.stderr)

    def test_unknown_task_fails(self):
        result = subprocess.run(["task", "unknown-test-task"], cwd=ROOT,
                                capture_output=True, text=True, check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("does not exist", result.stderr)


if __name__ == "__main__":
    unittest.main()

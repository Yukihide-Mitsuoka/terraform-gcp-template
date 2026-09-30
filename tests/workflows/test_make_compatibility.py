"""The temporary Make entry point must only delegate to the Taskfile."""

import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGETS = (
    "help", "setup", "format", "lint", "test", "test-unit", "test-integration",
    "coverage", "build", "run", "plan", "security-scan", "sbom", "clean", "doctor",
)


class MakeCompatibilityTest(unittest.TestCase):
    def test_every_target_has_only_one_task_command(self):
        for target in TARGETS:
            with self.subTest(target=target):
                result = subprocess.run(
                    ["make", "--no-print-directory", "-n", target],
                    cwd=ROOT, capture_output=True, text=True, check=True,
                )
                self.assertEqual(len(result.stdout.splitlines()), 1)
                self.assertIn(f'task "{target}"', result.stdout)

    def test_file_and_environment_are_forwarded_as_single_arguments(self):
        with tempfile.TemporaryDirectory() as directory:
            fake_task = Path(directory) / "task"
            capture = Path(directory) / "capture"
            fake_task.write_text(
                '#!/bin/sh\nprintf "%s\\n" "$@" > "$CAPTURE_FILE"\n',
                encoding="utf-8",
            )
            fake_task.chmod(0o755)
            env = os.environ.copy()
            env.update(PATH=f"{directory}:{env['PATH']}", CAPTURE_FILE=str(capture))
            file_name = 'sample "quoted" `printf BAD`.tf'
            subprocess.run(
                ["make", "--no-print-directory", "format", f"FILE={file_name}"],
                cwd=ROOT, env=env, capture_output=True, text=True, check=True,
            )
            self.assertEqual(capture.read_text(encoding="utf-8").splitlines(),
                             ["format", f"FILE={file_name}"])
            subprocess.run(
                ["make", "--no-print-directory", "run", "ENV=staging"],
                cwd=ROOT, env=env, capture_output=True, text=True, check=True,
            )
            self.assertEqual(capture.read_text(encoding="utf-8").splitlines(),
                             ["run", "ENV=staging"])

    def test_task_failure_is_not_masked(self):
        with tempfile.TemporaryDirectory() as directory:
            fake_task = Path(directory) / "task"
            fake_task.write_text("#!/bin/sh\nexit 23\n", encoding="utf-8")
            fake_task.chmod(0o755)
            env = os.environ.copy()
            env["PATH"] = f"{directory}:{env['PATH']}"
            result = subprocess.run(
                ["make", "--no-print-directory", "help"],
                cwd=ROOT, env=env, capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()

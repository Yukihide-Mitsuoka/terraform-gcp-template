import unittest
from pathlib import Path


WORKFLOW = (Path(__file__).parents[2] / ".github/workflows/ci.yml").read_text(
    encoding="utf-8"
)


def job(name: str) -> str:
    prefix = f"  {name}:\n"
    start = WORKFLOW.index(prefix) + len(prefix)
    rest = WORKFLOW[start:]
    next_job = rest.find("\n  ", 1)
    while next_job != -1:
        line = rest[next_job + 1 :].split("\n", 1)[0]
        if line.endswith(":") and line.strip() == line[2:]:
            return rest[:next_job]
        next_job = rest.find("\n  ", next_job + 1)
    return rest


class TaskCiTest(unittest.TestCase):
    def test_quality_jobs_install_task_before_running_their_canonical_commands(self):
        expected = {
            "lint": ["setup", "lint"],
            "test": ["setup", "coverage"],
            "build": ["setup", "build"],
            "doctor": ["doctor"],
        }
        for name, tasks in expected.items():
            with self.subTest(job=name):
                steps = job(name)
                action = "uses: ./scripts/actions/setup-task"
                self.assertEqual(steps.count(action), 1)
                self.assertLess(steps.index("uses: actions/checkout@"), steps.index(action))
                self.assertLess(steps.index(action), steps.index("run: task "))
                self.assertEqual(
                    [line.strip().removeprefix("- run: task ") for line in steps.splitlines()
                     if line.strip().startswith("- run: task ")],
                    tasks,
                )
                self.assertNotIn("- run: make ", steps)


if __name__ == "__main__":
    unittest.main()

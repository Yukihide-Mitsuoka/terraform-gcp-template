import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
CI_WORKFLOW = REPOSITORY_ROOT / ".github/workflows/ci.yml"
PROJECT_POLICY = "src/ci/pr_size_policy.py"
INHERITED_POLICY = "scripts/pr_size_policy.py"


class PullRequestSizePolicyBindingTests(unittest.TestCase):
    def test_child_owned_workflow_uses_only_child_owned_policy(self) -> None:
        workflow = CI_WORKFLOW.read_text(encoding="utf-8")

        self.assertIn(PROJECT_POLICY, workflow)
        self.assertNotIn(INHERITED_POLICY, workflow)
        self.assertTrue((REPOSITORY_ROOT / PROJECT_POLICY).is_file())


if __name__ == "__main__":
    unittest.main()

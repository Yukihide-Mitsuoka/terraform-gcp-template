import unittest
from pathlib import Path


ROOT = Path(__file__).parents[2]
WORKFLOW_PATH = ROOT / ".github/workflows/release.yml"


class ReleaseWorkflowTest(unittest.TestCase):
    def test_terraform_is_installed_before_local_release_gates(self):
        workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
        setup = (
            "hashicorp/setup-terraform@"
            "b9cd54a3c349d3f38e8881555d616ced269862dd"
        )
        release_gates = "uses: ./scripts/actions/release-gates"

        self.assertIn(setup, workflow)
        self.assertIn(release_gates, workflow)
        self.assertLess(workflow.index(setup), workflow.index(release_gates))


if __name__ == "__main__":
    unittest.main()

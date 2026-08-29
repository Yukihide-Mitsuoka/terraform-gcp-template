import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PUBLIC_ONLY = "if: github.event.repository.visibility == 'public'"


class PrivateRepositoryVisibilityTest(unittest.TestCase):
    def test_plan_limited_security_jobs_are_public_only(self) -> None:
        for workflow_name, job_name in (
            ("codeql.yml", "analyze"),
            ("scorecard.yml", "analysis"),
        ):
            with self.subTest(workflow=workflow_name):
                workflow = (
                    ROOT / ".github" / "workflows" / workflow_name
                ).read_text(encoding="utf-8")
                job_body = workflow.split(f"  {job_name}:\n", maxsplit=1)[1]

                self.assertIn(f"    {PUBLIC_ONLY}\n", job_body)


if __name__ == "__main__":
    unittest.main()

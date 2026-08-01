import unittest

from src.ci.pr_size_policy import (
    evaluate_size,
    is_authenticated_template_sync,
    summarize_lockfiles,
)


class ProjectPullRequestSizePolicyTests(unittest.TestCase):
    def test_excludes_lockfile_churn_from_hard_limit(self) -> None:
        lockfile_stats = summarize_lockfiles(
            [
                {"filename": "package.json", "additions": 15, "deletions": 58},
                {"filename": "pnpm-lock.yaml", "additions": 300, "deletions": 700},
            ]
        )

        result = evaluate_size(315, 758, 2, lockfile_stats)

        self.assertEqual(result.changed_lines, 73)
        self.assertEqual(result.changed_files, 1)
        self.assertEqual(result.level, "ok")

    def test_authenticated_template_sync_may_exceed_only_numeric_limit(self) -> None:
        authenticated = is_authenticated_template_sync(
            pr_author="github-actions[bot]",
            head_repository="Yukihide-Mitsuoka/terraform-gcp-template",
            target_repository="Yukihide-Mitsuoka/terraform-gcp-template",
            head_ref="chore/template_sync_c3b5dbf",
            base_ref="main",
            pr_body=(
                "Direct-parent-source: "
                "https://github.com/Yukihide-Mitsuoka/ai-dev-foundation@"
                + "a" * 40
            ),
        )

        self.assertEqual(
            evaluate_size(1020, 168, 28, (0, 0, 0), authenticated).level,
            "mechanical",
        )

    def test_template_sync_authentication_fails_closed(self) -> None:
        valid = {
            "pr_author": "github-actions[bot]",
            "head_repository": "Yukihide-Mitsuoka/terraform-gcp-template",
            "target_repository": "Yukihide-Mitsuoka/terraform-gcp-template",
            "head_ref": "chore/template_sync_c3b5dbf",
            "base_ref": "main",
            "pr_body": (
                "Direct-parent-source: "
                "https://github.com/Yukihide-Mitsuoka/ai-dev-foundation@"
                + "a" * 40
            ),
        }
        invalid_overrides = (
            {"pr_author": "maintainer"},
            {"head_repository": "attacker/fork"},
            {"target_repository": "attacker/repository"},
            {"head_ref": "chore/manual-sync_c3b5dbf"},
            {"head_ref": "chore/template_sync_abc123"},
            {"base_ref": "release"},
            {
                "pr_body": (
                    "Direct-parent-source: https://github.com/attacker/foundation@"
                    + "a" * 40
                )
            },
            {
                "pr_body": (
                    "Direct-parent-source: "
                    "https://github.com/Yukihide-Mitsuoka/ai-dev-foundation@"
                    + "a" * 39
                )
            },
        )

        self.assertTrue(is_authenticated_template_sync(**valid))
        for override in invalid_overrides:
            with self.subTest(override=override):
                self.assertFalse(is_authenticated_template_sync(**(valid | override)))

    def test_rejects_malformed_or_excessive_exclusions(self) -> None:
        with self.assertRaises(ValueError):
            summarize_lockfiles(
                [{"filename": "pnpm-lock.yaml", "additions": "300", "deletions": 0}]
            )
        with self.assertRaises(ValueError):
            evaluate_size(10, 10, 1, (11, 0, 1))

    def test_preserves_soft_and_hard_limits_for_ordinary_prs(self) -> None:
        self.assertEqual(evaluate_size(401, 0, 1, (0, 0, 0)).level, "soft")
        self.assertEqual(evaluate_size(801, 0, 1, (0, 0, 0)).level, "hard")


if __name__ == "__main__":
    unittest.main()

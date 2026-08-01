import unittest

from scripts.pr_size_policy import (
    evaluate_size,
    is_authenticated_template_sync,
    summarize_lockfiles,
)


class PullRequestSizePolicyTests(unittest.TestCase):
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

    def test_recognizes_nested_lockfiles_across_paginated_responses(self) -> None:
        payload = [
            [{"filename": "infra/.terraform.lock.hcl", "additions": 8, "deletions": 3}],
            [{"filename": "services/api/poetry.lock", "additions": 10, "deletions": 5}],
        ]

        self.assertEqual(summarize_lockfiles(payload), (18, 8, 2))

    def test_does_not_exclude_similarly_named_source_files(self) -> None:
        payload = [
            {"filename": "docs/pnpm-lock.yaml.md", "additions": 1000, "deletions": 0},
            {"filename": "src/package-lock.json.ts", "additions": 1000, "deletions": 0},
        ]

        self.assertEqual(summarize_lockfiles(payload), (0, 0, 0))

    def test_rejects_malformed_file_statistics(self) -> None:
        with self.assertRaises(ValueError):
            summarize_lockfiles(
                [{"filename": "pnpm-lock.yaml", "additions": "300", "deletions": 0}]
            )

    def test_rejects_exclusions_larger_than_aggregate_statistics(self) -> None:
        with self.assertRaises(ValueError):
            evaluate_size(10, 10, 1, (11, 0, 1))

    def test_preserves_soft_and_hard_limits(self) -> None:
        self.assertEqual(evaluate_size(401, 0, 1, (0, 0, 0)).level, "soft")
        self.assertEqual(evaluate_size(801, 0, 1, (0, 0, 0)).level, "hard")

    def test_authenticated_template_sync_may_exceed_only_numeric_limit(self) -> None:
        authenticated = is_authenticated_template_sync(
            pr_author="github-actions[bot]",
            head_repository="Yukihide-Mitsuoka/terraform-gcp-template",
            target_repository="Yukihide-Mitsuoka/terraform-gcp-template",
            head_ref="chore/template_sync_aa217a9",
            base_ref="main",
            pr_body=(
                "Template Sync\n\n"
                "Direct-parent-source: "
                "https://github.com/Yukihide-Mitsuoka/ai-dev-foundation@"
                + "a" * 40
            ),
        )

        result = evaluate_size(900, 36, 25, (0, 0, 0), authenticated)

        self.assertEqual(result.level, "mechanical")

    def test_template_sync_authentication_fails_closed(self) -> None:
        valid = {
            "pr_author": "github-actions[bot]",
            "head_repository": "Yukihide-Mitsuoka/terraform-gcp-template",
            "target_repository": "Yukihide-Mitsuoka/terraform-gcp-template",
            "head_ref": "chore/template_sync_aa217a9",
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
            {"head_ref": "chore/manual-sync_aa217a9"},
            {"head_ref": "chore/template_sync_abc123"},
            {"base_ref": "release"},
            {
                "pr_body": (
                    "Direct-parent-source: "
                    "https://github.com/attacker/foundation@" + "a" * 40
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
                candidate = valid | override
                self.assertFalse(is_authenticated_template_sync(**candidate))


if __name__ == "__main__":
    unittest.main()

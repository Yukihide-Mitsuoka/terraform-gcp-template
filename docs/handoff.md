---
id: project-handoff
title: Template Inheritance Handoff
status: active
updated: 2026-07-16
---

# Template Inheritance Handoff

This document records the verified restart point for Issue
[#2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/2). It is a
mutable status document, not a decision record. Update it when the accepted parent lock,
next task, or external governance state changes.

## Restart point

| Item | Verified state |
|------|----------------|
| Child repository | `Yukihide-Mitsuoka/terraform-gcp-template` |
| Child baseline | `main` at merge commit `d8fc759220007751d534f7d50f917db4c89f08cd` |
| Last completed change | [PR #18](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/pull/18), exposed the confirmed public governance `apply` CLI without executing it |
| Accepted parent lock | `70ea07add78ea3a80e75d790cb08e6dd43977111` |
| Observed parent target | `9ab06004ed129d0d27e4a1876aa03b04d067cc71` on local `../ai-dev-foundation` `origin/main` |
| Next parent commit | `d4c284c263b7a5b27034288b46558850c79913ae` — enforce vulnerability intake controls |
| Open child issues | Issue #2 only |
| Cloud state | No GCP resource is required or was created by this inheritance work |

The baseline above was verified on 2026-07-16 after PR #18 merged. The child worktree
was clean before this document branch was created. PR #18 made no GitHub repository
setting change and no GCP operation.

## Completed capability

- The manifest and lock implement one-first-parent-commit-at-a-time inheritance under
  [ADR-0003](adr/0003-adopt-direct-parent-template-inheritance.md).
- Governance policy currently resolves zero required approvals, Renovate, merged-branch
  deletion, and the foundation checks plus `scan`. The `scan` entry is unresolved state,
  not an approved enforcement target; accepted ADR-0003 prohibits requiring the current
  path-filtered check.
- `validate` is offline. `plan` and `audit` use GET-only GitHub discovery. Command and
  exit-code contracts are documented in
  [the governance policy README](../.github/governance/README.md).
- The apply-action planner returns ordered REST request data, side effects, and verification
  controls. The public `apply` CLI requires an exact `--repo` and `--confirm-repo` match
  before GitHub discovery, then delegates to the internal execution boundary: one action,
  read-back, verification, and fresh replanning at a time.
- Existing managed rulesets can produce an update action only when stricter supported
  review, merge-method, and check-integration constraints are preserved; unsupported
  state fails closed.
- `apply` was not invoked. Its presence is not authorization for a live repository write;
  it still requires an owner-approved target, actions, side effects, and `scan` resolution.
- `scripts/setup-github.sh` remains for legacy settings that policy does not own yet,
  including vulnerability alerts and private vulnerability reporting. Do not remove it
  until policy-owned adapters exist (GR-030).
- PR #18's required CI, security, and link checks succeeded, and GitHub reported the PR
  mergeable before merge.

## Current external governance state

A GET-only `plan` against this repository after PR #18 merged on 2026-07-16 returned
`status: drift` with no `unknown` controls.

| State | Controls |
|-------|----------|
| Drift | The managed ruleset is absent, so pull-request, required-check, force-push, and admin-bypass controls have no current managed value |
| Drift | `scan` is required by child policy but was not observed on the current `main` head |
| Drift | `delete_branch_on_merge` is `false`; policy requires `true` |
| Compliant | Dependabot security updates are disabled because Renovate is selected |
| Compliant | Secret scanning and push protection are enabled |

The `scan` workflow currently has IaC path filters. A non-IaC merge such as PR #18 does
not produce a `scan` check on the new branch head. Accepted
[ADR-0003](adr/0003-adopt-direct-parent-template-inheritance.md) has higher authority than
Issue #2 and the current repository policy: `scan` must not be applied as a required
check until it exposes a unique, always-reported context. Otherwise non-IaC PRs may
become unmergeable after enforcement.

## Next recommended task

Create one PR for parent commit `d4c284c263b7a5b27034288b46558850c79913ae`, using a
branch such as `feat/2-enforce-vulnerability-intake-controls`.

The verified inheritance plan reports:

| Classification | Paths |
|----------------|-------|
| Add | None |
| Modify | `.ai/security.md`, `.github/governance/README.md`, `.github/governance/foundation.json`, `scripts/github_governance.py`, `scripts/tests/test_github_governance.py`, `scripts/tests/test_github_governance_apply_actions.py`, `scripts/tests/test_github_governance_comparison.py`, `scripts/tests/test_github_governance_discovery.py` |
| Protected | `docs/usage.md`, `docs/usage.ja.md` |
| Candidate delete / unowned | None |

The parent slice makes Dependabot vulnerability alerts and private vulnerability reporting
immutable `SEC-003` foundation minimums. It distinguishes a known disabled setting from a
permission-limited `unknown` state and plans only enable-only actions for confirmed drift.
The inherited `.ai/security.md` must match the parent blob exactly, including its `SEC-003`
rules. Review the protected usage guides for an accurate child-specific explanation while
preserving Terraform onboarding content.

The public `apply` command is available but remains unauthorized for live use in this
child. The unresolved `scan` preflight and the required per-target owner approval still
prohibit a write. Keep `scripts/setup-github.sh` until policy-owned adapters exist; do
not remove it during this inheritance.

Preserve inherited file content and modes exactly. The parent `README.md` and usage guides
are protected here; do not copy them automatically. Review whether child-specific usage
documentation needs an adapted update while preserving Terraform onboarding content. Do
not overwrite the protected decision log; review the parent entry and append a
child-specific entry only if the decision applies here. Advance the lock to `70ea07a...` only
in the same reviewed PR as the accepted inherited files.

### Acceptance checks

1. Confirm `main` is clean and current, then run the inheritance validator and planner
   from [the inheritance guide](troubleshooting/template-inheritance.md).
2. Confirm the planner still selects `d4c284c...`. Stop if the lock, origin identity,
   or first-parent result differs from this document.
3. Verify inherited blobs and executable modes against that parent commit. Assess the
   protected usage documentation separately rather than copying it automatically.
4. Run `make format`, `make lint`, `make doctor`, `make test-unit`, `make test`,
   `make security-scan`, and `make build`; report unavailable local scanners honestly.
5. Run governance `validate`. A live `plan` is permitted only as GET-only evidence and
   must leave the worktree and GitHub settings unchanged. Do not invoke `apply`.
6. Open a complete Issue #2 PR, wait for green CI, and stop before command execution or
   the next parent commit.

## Remaining parent queue after the next task

Process each row as a separate reviewed PR in first-parent order. Re-run the planner
after every lock advance; this table is orientation, not authority.

| Order | Parent commit | Parent change | Child review focus |
|-------|---------------|---------------|--------------------|
| 6 | `cce70e4` | Model repository collaboration settings | Preserve the child solo-development defaults |
| 7 | `91276b9` | Migrate legacy setup to the policy wrapper | Breaking parent change; update child usage and migration guidance |
| 8 | `32c1f29` | Propose hardened template inheritance | Parent architecture is protected child content; evaluate against child ADR-0003 rather than copying it |
| 9 | `5632f8d` | Adopt solo-friendly defaults | Compare with the existing child override; do not erase Terraform-required checks |
| 10 | `4035dbd` | Add inheritance contract validation | The child bootstrap may already match; trust planner classification |
| 11 | `1e99d39` | Add next-parent planner | The child bootstrap may already match; trust planner classification |
| 12 | `9ab0600` | Add governance template profile chain | Verify direct-parent ownership and downstream `secure-ga4-bq-template` effects |

## Approval boundaries and open decisions

- Continue read-only inheritance PRs without GitHub setting writes or GCP operations.
- Do not execute governance `apply` merely because the command is available. First present
  its target, ordered actions, side effects, and the `scan` resolution; obtain explicit
  human approval for that specific write execution.
- Issue #2 acceptance checkboxes are not yet updated. Update or close the issue only
  after the parent queue is accepted and the separately approved live reconciliation is
  read back successfully, or after the owner narrows the issue scope.
- Before propagation to `secure-ga4-bq-template`, complete this direct-child proof and
  review that repository's protected paths and required-check profile independently.

## Verified restart commands

```bash
git switch main
git pull --ff-only origin main
python3 scripts/template_inheritance.py validate --root .
python3 scripts/template_inheritance.py plan --root . --parent-root ../ai-dev-foundation
python3 scripts/github_governance.py validate --root .
```

The synchronization commands were run successfully on 2026-07-16 before this document
branch was created; `git pull` fast-forwarded main to PR #18. The three Python commands
were also verified against the merged content. The GET-only governance `plan` was refreshed
after PR #18 and produced the external state recorded above. The inheritance planner
performs no fetch, so refreshing the parent repository is a separate deliberate action.

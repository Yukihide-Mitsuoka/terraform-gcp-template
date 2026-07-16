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
| Child baseline | `main` at merge commit `5ced34ffbcac664d77a552d02a79a0c29c49eddb` |
| Last completed change | [PR #10](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/pull/10), public GET-only governance `plan` and `audit` |
| Accepted parent lock | `86b3f4bb0ef55fe658f1294de38bca85118d7b6c` |
| Observed parent target | `9ab06004ed129d0d27e4a1876aa03b04d067cc71` on local `../ai-dev-foundation` `origin/main` |
| Next parent commit | `9411ad67e2e5254c18cc1480da2db64d812c9ab0` — deterministic apply-action planning |
| Open child issues | Issue #2 only |
| Cloud state | No GCP resource is required or was created by this inheritance work |

The baseline above was verified on 2026-07-16 after PR #10 merged. The child worktree
was clean before this document branch was created.

## Completed capability

- The manifest and lock implement one-first-parent-commit-at-a-time inheritance under
  [ADR-0003](adr/0003-adopt-direct-parent-template-inheritance.md).
- Governance policy resolves the child-owned Terraform profile: zero required approvals,
  Renovate, merged-branch deletion, and the foundation checks plus `scan`.
- `validate` is offline. `plan` and `audit` use GET-only GitHub discovery. Command and
  exit-code contracts are documented in
  [the governance policy README](../.github/governance/README.md).
- PR #10 CI completed successfully and GitHub reported the PR mergeable before merge.
- No policy-driven apply command has been inherited or executed in this child.

## Current external governance state

A GET-only `plan` against this repository on 2026-07-16 returned `status: drift` with no
`unknown` controls.

| State | Controls |
|-------|----------|
| Drift | The managed ruleset is absent, so pull-request, required-check, force-push, and admin-bypass controls have no current managed value |
| Drift | `scan` is required by child policy but was not observed on the current `main` head |
| Drift | `delete_branch_on_merge` is `false`; policy requires `true` |
| Compliant | Dependabot security updates are disabled because Renovate is selected |
| Compliant | Secret scanning and push protection are enabled |

The `scan` workflow currently has IaC path filters. A non-IaC merge such as PR #10 does
not produce a `scan` check on the new branch head. Resolve or explicitly model this
required-check behavior before any governance apply; otherwise non-IaC PRs may become
unmergeable after enforcement.

## Next recommended task

Create one PR for parent commit `9411ad67e2e5254c18cc1480da2db64d812c9ab0`, using a
branch such as `feat/2-inherit-governance-apply-plan`.

The verified inheritance plan reports:

| Classification | Paths |
|----------------|-------|
| Add | `scripts/tests/test_github_governance_apply_actions.py` |
| Modify | `.github/governance/README.md`, `scripts/github_governance.py`, `scripts/tests/test_github_governance_comparison.py`, `scripts/tests/test_github_governance_discovery.py` |
| Protected | `.ai/decision-log.md` |
| Candidate delete / unowned | None |

The parent slice builds ordered GitHub REST write requests as pure data. It does not
execute a request and does not expose public `apply`. Preserve inherited file content
and modes exactly. Do not overwrite the protected decision log; review the parent entry
and append a child-specific entry only if the decision applies here. Advance the lock to
`9411ad67...` only in the same reviewed PR as the accepted inherited files.

### Acceptance checks

1. Confirm `main` is clean and current, then run the inheritance validator and planner
   from [the inheritance guide](troubleshooting/template-inheritance.md).
2. Confirm the planner still selects `9411ad67...`. Stop if the lock, origin identity,
   or first-parent result differs from this document.
3. Verify inherited blobs and executable modes against that parent commit.
4. Run `make format`, `make lint`, `make doctor`, `make test-unit`, `make test`,
   `make security-scan`, and `make build`; report unavailable local scanners honestly.
5. Run governance `validate`. A live `plan` is permitted only as GET-only evidence and
   must leave the worktree and GitHub settings unchanged.
6. Open a complete Issue #2 PR, wait for green CI, and stop before the next parent commit.

## Parent queue after the next task

Process each row as a separate reviewed PR in first-parent order. Re-run the planner
after every lock advance; this table is orientation, not authority.

| Order | Parent commit | Parent change | Child review focus |
|-------|---------------|---------------|--------------------|
| 2 | `64f6fc8` | Preserve stricter ruleset constraints | Prove updates cannot weaken unmanaged constraints |
| 3 | `67d1596` | Add verified apply execution boundary | Execution exists internally; keep it unreachable without the intended confirmation boundary |
| 4 | `70ea07a` | Expose confirmed apply command | Requires a reviewed live plan and separate explicit human approval before any GitHub write |
| 5 | `d4c284c` | Enforce vulnerability intake controls | Re-check repository security visibility and permissions |
| 6 | `cce70e4` | Model repository collaboration settings | Preserve the child solo-development defaults |
| 7 | `91276b9` | Migrate legacy setup to the policy wrapper | Breaking parent change; update child usage and migration guidance |
| 8 | `32c1f29` | Propose hardened template inheritance | Parent architecture is protected child content; evaluate against child ADR-0003 rather than copying it |
| 9 | `5632f8d` | Adopt solo-friendly defaults | Compare with the existing child override; do not erase Terraform-required checks |
| 10 | `4035dbd` | Add inheritance contract validation | The child bootstrap may already match; trust planner classification |
| 11 | `1e99d39` | Add next-parent planner | The child bootstrap may already match; trust planner classification |
| 12 | `9ab0600` | Add governance template profile chain | Verify direct-parent ownership and downstream `secure-ga4-bq-template` effects |

## Approval boundaries and open decisions

- Continue read-only inheritance PRs without GitHub setting writes or GCP operations.
- Do not execute governance `apply` merely because the command becomes available. First
  present its target, ordered actions, side effects, and the `scan` resolution; obtain
  explicit human approval for that specific write execution.
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
branch was created; `git pull` fast-forwarded main to PR #10. The three Python commands
were also verified against the merged content. The inheritance planner performs no
fetch, so refreshing the parent repository is a separate deliberate action.

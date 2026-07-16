---
id: project-handoff
title: Template Inheritance Handoff
status: active
updated: 2026-07-16
---

# Template Inheritance Handoff

This mutable document records the verified restart point for Issue
[#2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/2). Update it
when the accepted parent lock, workflow proof, next task, or external governance state
changes. Architectural decisions remain in ADRs and the append-only decision log.

## Restart point

| Item | Verified state |
|------|----------------|
| Child repository | `Yukihide-Mitsuoka/terraform-gcp-template` |
| Child baseline | `main` at merge commit `d789accc55d71e69ae0d668efa069b9ef956a320` |
| Last completed change | [PR #27](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/pull/27), inherited the governance profile-chain resolver |
| Accepted parent lock | `9ab06004ed129d0d27e4a1876aa03b04d067cc71` |
| Parent target | Same commit; the read-only planner reports `up_to_date` |
| Work in progress | Add a unique, always-reported `iac-scan` workflow context without changing live governance |
| Open child issues | Issue #2 only |
| Cloud state | No GCP resource is required or was created by this work |

The baseline was verified after PR #27 merged. The current branch changes only the
child-owned IaC workflow, its local contract test, canonical test targets, and status
documentation. It does not change repository settings or run Terraform against GCP.

## Completed capability

- The direct-parent inheritance contract and lock implement the accepted one-first-parent-
  commit-at-a-time process in
  [ADR-0003](adr/0003-adopt-direct-parent-template-inheritance.md).
- The child is synchronized through the current parent target `9ab0600`; there is no
  remaining parent queue at this checkpoint.
- Governance policy resolves foundation, profile, and repository required checks with
  stable deduplication. No Terraform profile is selected yet.
- `validate` is offline. Governance `plan` and `audit` use GET-only GitHub discovery.
  The public `apply` boundary requires exact repository confirmation, one action at a
  time, read-back verification, and fresh replanning.
- Live governance `apply` has never been authorized or invoked for this repository.
- The existing path-filtered `scan` policy value remains unresolved and must not be
  enforced. ADR-0003 requires a unique always-reported context first.

## Current workflow candidate

The current branch introduces job ID and display name `iac-scan` with these contracts:

- the job runs for every pull request and every push to `main`;
- checkout includes full history, and event base/head SHAs define the changed range;
- Terraform, `infra/`, `k8s/`, or `helm/` changes run both Trivy and Checkov;
- a proven non-IaC range reports success without invoking the scanners;
- an absent, zero, or unavailable range fails safe by running the full scan;
- Trivy still fails on MEDIUM or higher findings, and Checkov remains strict.

The historical Trivy finding GCP-0076 in external module version `v0.1.0` is not
suppressed. An IaC-changing PR will continue to fail until that module enables subnet
flow logs or the dependency is upgraded to a compliant version. This workflow PR has no
IaC diff, so its scanner steps should skip while the `iac-scan` context succeeds.

Local contract tests first failed against the old workflow, then passed after the change.
GitHub Actions is still the authority for workflow syntax and context naming. Do not use
`iac-scan` in enforced policy until the PR and the resulting `main` push both show that
exact successful context.

## Current external governance state

A GET-only `plan` on 2026-07-16 returned `status: drift` and no `unknown` controls:

| State | Controls |
|-------|----------|
| Drift | The managed ruleset is absent; pull-request, required-check, force-push, and admin-bypass controls have no managed value |
| Drift | Policy requests legacy `scan`, but current `main` observed only the nine foundation checks |
| Drift | Merged-branch deletion, squash-only strategy, and squash commit formatting differ |
| Drift | Vulnerability alerts and private vulnerability reporting are disabled |
| Compliant | Discussions are disabled and Dependabot security updates are disabled because Renovate is selected |
| Compliant | Secret scanning and push protection are enabled |

This is evidence only. No write action from the plan is authorized by this document.

## Next recommended task

After the current workflow PR merges:

1. Verify the merged PR and subsequent `main` push both report successful `iac-scan`.
2. In a separate PR, change the child repository policy from legacy `scan` to
   `iac-scan`.
3. Add `.github/governance/profiles/terraform-gcp.json` with parent
   `ai-dev-foundation` and required check `iac-scan`.
4. Extend child inheritance ownership so the profile directory can propagate safely to
   downstream `secure-ga4-bq-template`; review that child separately before inheritance.
5. Run inheritance and governance validation plus a GET-only governance plan. Do not
   execute `apply`.

Keeping workflow proof and policy selection in separate PRs prevents a required context
from being named before GitHub has observed it. The profile should add only the
Terraform-specific check; the foundation's nine checks remain inherited automatically.

### Acceptance checks for the current workflow PR

1. Run `make format`, `make lint`, `make doctor`, `make test-unit`, `make test`,
   `make security-scan`, and `make build`; report unavailable local scanners honestly.
2. Run inheritance `validate` and `plan`; they must remain `up_to_date` at `9ab0600`.
3. Run governance `validate`; it should still resolve legacy `scan`, because policy
   migration is intentionally deferred.
4. Confirm the PR reports successful `iac-scan` plus the existing required checks.
5. Merge, then verify `iac-scan` on the new `main` head before starting the policy PR.

## Remaining parent queue

None at the recorded checkpoint. Re-run the read-only planner after refreshing the parent
checkout; do not infer future parent commits from this document.

## Approval boundaries and open decisions

- Read-only validation, planning, and GitHub discovery are allowed.
- Do not execute governance `apply` without a separately presented target, ordered
  actions, side effects, and explicit owner approval for that exact write.
- Do not run Terraform `apply`, create a bucket, or create any GCP resource for this work.
- Do not suppress GCP-0076 merely to make an IaC-changing PR green.
- Update or close Issue #2 only after the accepted workflow/profile sequence and any
  separately approved live reconciliation are verified, or after the owner narrows scope.

## Verified restart commands

```bash
git switch main
git pull --ff-only origin main
python3 scripts/template_inheritance.py validate --root .
python3 scripts/template_inheritance.py plan --root . --parent-root ../ai-dev-foundation
python3 scripts/github_governance.py validate --root .
python3 scripts/github_governance.py plan --root . \
  --repo Yukihide-Mitsuoka/terraform-gcp-template
```

The inheritance commands and governance validation were verified on 2026-07-16 after
PR #27. The GET-only governance plan produced the external state recorded above. The
inheritance planner performs no fetch; refreshing the parent checkout is a separate
deliberate action.

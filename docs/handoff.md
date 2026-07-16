---
id: project-handoff
title: Template Inheritance Handoff
status: active
updated: 2026-07-16
---

# Template Inheritance Handoff

This mutable document records the verified restart point for Issue
[#2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/2). Update it
when the accepted parent lock, profile state, next task, or external governance state
changes. Architectural decisions remain in ADRs and the append-only decision log.

## Restart point

| Item | Verified state |
|------|----------------|
| Child repository | `Yukihide-Mitsuoka/terraform-gcp-template` |
| Child baseline | `main` at PR #28 merge commit `bbbeee0c99e2da3f60b58c9fe43f87150cbfab12` |
| Last completed change | [PR #28](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/pull/28), added the always-reported `iac-scan` context |
| Accepted parent lock | `9ab06004ed129d0d27e4a1876aa03b04d067cc71` |
| Parent target | Same commit; the read-only planner reports `up_to_date` |
| Work in progress | Add the child-owned `terraform-gcp` governance profile and remove legacy `scan` policy duplication |
| Open child issues | Issue #2 only |
| Cloud state | No GCP resource is required or was created by this work |

The `main` baseline and profile precondition were verified on 2026-07-16. The current
branch changes policy files and local contract tests only. It makes no GitHub repository
setting change and does not run Terraform against GCP.

## Completed capability

- The direct-parent inheritance contract is synchronized through parent commit
  `9ab0600`; there is no remaining parent queue at this checkpoint.
- The governance resolver composes foundation, profile-chain, and repository checks in
  monotonic order with stable deduplication.
- PR #28 and its resulting `main` push both reported a successful job named exactly
  `iac-scan`. On the `main` push, the non-IaC path succeeded and both scanners skipped.
- IaC changes still invoke strict Trivy and Checkov. The historical GCP-0076 finding in
  external module `v0.1.0` remains unsuppressed.
- Governance `validate` is offline. `plan` and `audit` use GET-only GitHub discovery.
  Live governance `apply` has never been authorized or invoked for this repository.

## Current profile candidate

The current branch declares `.github/governance/profiles/terraform-gcp.json` with parent
`ai-dev-foundation` and required check `iac-scan`. The resolved check ownership is:

| Layer | Required checks |
|-------|-----------------|
| Foundation | `lint`, `test`, `build`, `doctor`, `link-check`, `pr-quality`, `secret-scan`, `dependency-scan`, `license-check` |
| Terraform profile | `iac-scan` |
| Repository override | None |

The repository policy retains only its repository-specific solo values: zero approvals
and automatic merged-branch deletion. Removing its duplicated foundation checks does not
remove them from the resolved policy.

The profile directory is protected from `ai-dev-foundation` inheritance and legacy
template sync because it is declared by this Terraform template family. When
`secure-ga4-bq-template` migrates to this repository as its direct parent, that
downstream manifest must classify the same directory as inherited. The profile does not
exist in or propagate to `nextjs-saas-template`.

## Current external governance state

A GET-only `plan` using the candidate policy on 2026-07-16 returned `status: drift` and
no `unknown` controls:

| State | Controls |
|-------|----------|
| Compliant | All ten desired check names, including `iac-scan`, are observed on current `main` |
| Drift | The managed ruleset is absent; pull-request, required-check, force-push, and admin-bypass controls have no managed value |
| Drift | Merged-branch deletion, squash-only strategy, and squash commit formatting differ |
| Drift | Vulnerability alerts and private vulnerability reporting are disabled |
| Compliant | Discussions and Dependabot security updates are disabled as selected |
| Compliant | Secret scanning and push protection are enabled |

This is evidence only. No write action from the plan is authorized by this document.

## Next recommended task

After the current profile PR merges:

1. Verify the PR and resulting `main` push still report all ten checks, including
   `iac-scan`.
2. Re-run governance `validate` and the GET-only `plan` from merged `main` and preserve
   the evidence in this handoff.
3. Treat the local Issue #2 migration implementation as complete; keep any live
   governance reconciliation as a separately presented and explicitly approved action.
4. Migrate `secure-ga4-bq-template` to this repository as its direct parent in small,
   reviewed PRs. Inspect its protected paths before inheriting the Terraform profile.

Do not change `nextjs-saas-template` as part of the Terraform downstream migration. It
remains a separate direct child of `ai-dev-foundation` and resolves no Terraform profile.

### Acceptance checks for the current profile PR

1. The failing-first child contract tests must pass and resolve exactly the foundation
   checks plus `iac-scan`, with no legacy `scan`.
2. Run `make format`, `make lint`, `make doctor`, `make test-unit`, `make test`,
   `make security-scan`, and `make build`; report unavailable local scanners honestly.
3. Inheritance `validate` and `plan` must remain `up_to_date` at `9ab0600`.
4. Governance `validate` must load exactly one `terraform-gcp` profile. A GET-only plan
   must report `branch.required_status_checks_observed` compliant.
5. Confirm the PR reports successful `iac-scan` plus the nine foundation checks.

## Remaining parent queue

None at the recorded checkpoint. Re-run the read-only planner after refreshing the parent
checkout; do not infer future parent commits from this document.

## Approval boundaries and open decisions

- Read-only validation, planning, and GitHub discovery are allowed.
- Do not execute governance `apply` without a separately presented target, ordered
  actions, side effects, and explicit owner approval for that exact write.
- Do not run Terraform `apply`, create a bucket, or create any GCP resource for this work.
- Do not suppress GCP-0076 merely to make an IaC-changing PR green.
- Update or close Issue #2 after the profile PR and merged-main evidence are complete;
  do not imply that live GitHub drift was reconciled.

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

The inheritance commands, profile validation, and GET-only governance plan were verified
on 2026-07-16. The inheritance planner performs no fetch; refreshing the parent checkout
is a separate deliberate action.

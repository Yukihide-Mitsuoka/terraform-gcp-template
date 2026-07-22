---
id: project-handoff
title: Template Inheritance Handoff
status: active
updated: 2026-07-23
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
| Child baseline | `main` at PR #57 merge commit `de7df1b760534644eb97b9bdd10ab72adb5f665c` |
| Last completed change | [PR #57](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/pull/57), adopted ruleset-only governance discovery |
| Accepted parent lock | `01eb97c6a7fd8106bada2be835803b49f56dce10` |
| Parent target | `937baa4e04d0bbe451c8bf04f5619db8bd3f5db0`; the next reviewed candidate is `f21dd13ae2a39210f4cbdc407dbcd323d2bd1ff1` |
| Work in progress | Repository-maintenance PRs are review-gated; no cloud work is active |
| Open child issues | See GitHub Issues; completed governance migration Issue #2 is closed |
| Cloud state | No GCP resource is required or was created by this work |

The merged `main` baseline and read-only inheritance plan were verified on 2026-07-23.
No GitHub repository setting was changed, and Terraform was not run against GCP.

## Completed capability

- The direct-parent inheritance contract is accepted through parent commit
  `01eb97c`; later parent commits remain a reviewed queue starting at `f21dd13a`.
- The governance resolver composes foundation, profile-chain, and repository checks in
  monotonic order with stable deduplication.
- PR #28 and its resulting `main` push both reported a successful job named exactly
  `iac-scan`. On the `main` push, the non-IaC path succeeded and both scanners skipped.
- PR #29 and its resulting
  [`main` push](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/actions/runs/29497973295)
  also reported successful `iac-scan`; merged policy validation resolves the nine
  foundation checks plus that Terraform check and no legacy `scan`.
- IaC changes still invoke strict Trivy and Checkov. The historical GCP-0076 finding in
  external module `v0.1.0` remains unsuppressed.
- Governance `validate` is offline. `plan` and `audit` use GET-only GitHub discovery.
  Live governance `apply` has never been authorized or invoked for this repository.

## Accepted profile state

Merged `main` declares `.github/governance/profiles/terraform-gcp.json` with parent
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
template sync because it is declared by this Terraform template family. Downstream
direct children classify the same directory as inherited. The profile does not exist in
or propagate to `nextjs-saas-template`.

## Last recorded external governance evidence

A GET-only `plan` from merged `main` on 2026-07-16 returned `status: drift` and
no `unknown` controls. This is historical evidence, not a current-state assertion;
run a fresh GET-only plan before making a governance decision:

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

The governance migration and downstream direct-parent migration are complete. Next:

1. Review the parent candidate `f21dd13a` independently. The read-only planner reports
   one foundation ADR addition and one ADR index update; do not jump directly to the
   later parent target.
2. After each accepted parent checkpoint, propagate reviewed changes to
   `secure-ga4-bq-template` and `secure-ai-controls` through their own PRs.
3. Keep protected workflows repository-owned and keep any live governance
   reconciliation as a separately presented, explicitly approved action with target,
   ordered writes, and side effects.

`nextjs-saas-template` remains a separate direct child of `ai-dev-foundation` and
resolves no Terraform profile.

### Merged-main evidence

- `make test-unit`: three governance tests and four workflow tests passed.
- On 2026-07-23, inheritance `plan` selected `f21dd13a` as the next candidate from
  lock `01eb97c` toward parent target `937baa4`.
- Governance `validate` loaded exactly one `terraform-gcp` profile.
- The GET-only plan reported `branch.required_status_checks_observed` compliant for all
  ten resolved checks and returned no `unknown` controls.
- PR #57 and its resulting `main` baseline completed the ruleset-only discovery
  migration at merge commit `de7df1b`.

## Remaining parent queue

The read-only planner reports candidate `f21dd13a` between accepted lock `01eb97c` and
target `937baa4`. Re-run the planner after every reviewed merge; do not infer or skip
future parent commits from this document.

## Approval boundaries and open decisions

- Read-only validation, planning, and GitHub discovery are allowed.
- Do not execute governance `apply` without a separately presented target, ordered
  actions, side effects, and explicit owner approval for that exact write.
- Do not run Terraform `apply`, create a bucket, or create any GCP resource for this work.
- Do not suppress GCP-0076 merely to make an IaC-changing PR green.
- Closing Issue #2 represents implementation completion only; it does not imply that
  live GitHub drift was reconciled.

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

The inheritance planner was verified on 2026-07-23 at merge commit `de7df1b` against
parent target `937baa4`. The planner performs no fetch; refreshing the parent checkout
is a separate deliberate action.

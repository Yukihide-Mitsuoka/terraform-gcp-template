# ADR-0003: Adopt manifest-driven direct-parent template inheritance

| Field | Value |
|-------|-------|
| Status | accepted |
| Date | 2026-07-16 |
| Deciders | repository owner |
| Author | Codex (AI agent) |
| Supersedes / Superseded by | Supersedes local application of LOG-0004 |

## Context

This repository is the direct Terraform child of `ai-dev-foundation` and the direct
parent of `secure-ga4-bq-template`. Its governance files currently match foundation
commit `8035bbbf28c2ea1f84e7e5bfe90fb858c5370daf` from upstream PR #21, but later
foundation changes are not represented locally.

The scheduled Template Sync workflow cannot push inherited workflow changes with its
standard token. Its denylist also cannot prove that newly added parent paths will avoid
Terraform-owned files such as `.gitignore`, `infra/`, the stack CI workflow, and local
governance policy. The repository owner accepted the replacement architecture in
[ai-dev-foundation ADR-0004](https://github.com/Yukihide-Mitsuoka/ai-dev-foundation/blob/main/docs/adr/0004-harden-multi-level-template-inheritance.md)
through upstream PR #33.

Constraints are: keep direct-parent topology; preserve all Terraform and repository
local files; keep every intermediate `main` green; add no repository-administration
credential to Actions; make no live GitHub setting change during migration; and keep
each PR within GR-020.

## Options considered

### Option 1: Do nothing

Keep the current denylist sync and stale governance resolver. This has no migration
cost, but workflow sync remains unreliable, new parent paths are not fail-closed, and a
Terraform-family policy cannot pass safely to the secure GA4 child. Rejected.

### Option 2: Add a privileged Template Sync credential

A PAT or GitHub App could write workflow files without changing the transport. It would
not fix ownership ambiguity, accumulated multi-commit diffs, or governance profile
composition, and it would add a credential boundary. Rejected.

### Option 3: Port foundation changes manually without a contract

Small reviewed PRs would preserve local authentication and allow workflow changes, but
reviewers could not prove the accepted parent commit or path ownership. Rejected.

### Option 4: Adopt the upstream manifest-driven reconciler

Record the direct parent and accepted commit, declare inherited and protected paths,
and advance one first-parent commit per reviewed PR. Add a Terraform governance profile
only after its required check always reports. This adds bootstrap and migration work but
is fail-closed, reversible, and consistent with the accepted template graph.

## Decision

Adopt Option 4 and the constraints of upstream ADR-0004. This repository MUST name
`Yukihide-Mitsuoka/ai-dev-foundation` as its only direct parent and MUST bootstrap its
lock at `8035bbbf28c2ea1f84e7e5bfe90fb858c5370daf`, whose inherited governance blobs were
verified equal on 2026-07-16.

The child-owned manifest, lock, `.gitignore`, `.templatesyncignore`, repository policy,
Terraform CI workflow, and `infra/` MUST be protected. Parent changes MUST advance one
first-parent commit at a time through reviewed PRs; candidate deletions remain disabled.
The Terraform family profile MUST be inherited by `secure-ga4-bq-template` through this
repository, never directly from the foundation.

The current path-filtered `scan` workflow MUST NOT become a required profile check. It
must first expose a unique, always-reported context such as `iac-scan`. No governance
apply or repository-setting mutation is authorized by this ADR.

## Consequences

**Positive:** Parent provenance and ownership become reviewable; Terraform-local paths
remain protected; multi-level governance can add Terraform checks without replacing
foundation checks; and no privileged Actions credential is introduced.

**Negative:** Bootstrap requires several small PRs; each parent hop adds merge latency;
and the secure GA4 child cannot migrate until the Terraform parent is green.

Migration is expand-only: add the manifest and lock; bootstrap validation and planning;
advance foundation commits in order; make the Terraform check always report; add the
family profile; then migrate `secure-ga4-bq-template`. The scheduled writer remains
non-authoritative and is removed only after equivalent read-only drift visibility exists.

Rollback is a reviewed PR restoring the previous lock or removing an unconsumed
bootstrap component. Existing GitHub settings and GCP resources are unchanged.

**Follow-ups:** Continue terraform-gcp-template Issue #2, then migrate the secure GA4
child through this repository.

---
id: decision-log
title: Decision Log
authority: 4
read_when: [architecture-change, planning, onboarding]
---

# Decision Log

Append-only index of decisions. Newest first. Two kinds of entries:

- **ADR-linked**: architectural decisions — full context lives in `docs/adr/`.
- **Lightweight**: decisions too small for an ADR but worth remembering (COD-052).

Rules: never edit or delete past entries; supersede with a new entry that references the
old one. One line per entry. AI agents append entries in the same PR as the change.

| Date | ID | Decision | Link |
|------|----|----------|------|
| 2026-07-16 | LOG-0020 | Advance the accepted parent lock to validator checkpoint `4035dbd`; retain the exact already-bootstrapped planner blob from next parent `1e99d395` rather than regress it to validator-only code, keep the candidate validator tests already current, adapt the protected governance troubleshooting text to the approved exact-confirmation flow, and leave the unowned parent inheritance README uncopied; no GitHub setting or GCP resource changes are authorized | [ADR-0003](../docs/adr/0003-adopt-direct-parent-template-inheritance.md) |
| 2026-07-16 | LOG-0019 | Advance the accepted parent lock to `5632f8d`; adopt solo-friendly defaults so Discussions resolve disabled while zero approvals, automatic merged-branch deletion, child Terraform checks, and repository overrides remain intact; protected parent ADR paths are not copied and live governance `apply` remains separately unauthorized | [.github/governance/README.md](../.github/governance/README.md) |
| 2026-07-16 | LOG-0018 | Advance the accepted parent lock to architecture checkpoint `32c1f29`; its ADR and index paths remain protected and are not copied because accepted child ADR-0003 already adopts the owner-approved upstream ADR-0004, so this checkpoint changes no inherited blob, runtime behavior, GitHub setting, or GCP resource | [ADR-0003](../docs/adr/0003-adopt-direct-parent-template-inheritance.md) |
| 2026-07-16 | LOG-0017 | Advance the accepted parent lock to `91276b9`, superseding local LOG-0003 and completing LOG-0015's migration condition; `scripts/setup-github.sh` is now a no-policy compatibility wrapper whose dry-run delegates to `plan`, whose apply requires exact repeated target confirmation, and whose failures and exit codes come from the reconciler; live `apply` remains separately unauthorized | [.github/governance/README.md](../.github/governance/README.md) |
| 2026-07-16 | LOG-0016 | Advance the accepted parent lock to `cce70e4`; squash-only merging is an immutable WF-030 minimum, repository collaboration settings share one verified PATCH before linear-history enforcement, child solo approvals and Terraform checks remain unchanged, and live `apply` remains separately unauthorized | [.github/governance/README.md](../.github/governance/README.md) |
| 2026-07-16 | LOG-0015 | Advance the accepted parent lock to `d4c284c`; `SEC-003` makes vulnerability alerts and private vulnerability reporting immutable foundation minimums, permission-limited reads remain `unknown`, only confirmed disabled controls produce enable actions, and live `apply` remains separately unauthorized | [.github/governance/README.md](../.github/governance/README.md) |
| 2026-07-16 | LOG-0014 | Advance the accepted parent lock to `70ea07a`; public governance `apply` requires an exact `--repo` and `--confirm-repo` match before GitHub discovery, emits redacted partial evidence on failure, and remains unexecuted and separately unauthorized for live repository changes in this child | [.github/governance/README.md](../.github/governance/README.md) |
| 2026-07-16 | LOG-0013 | Advance the accepted parent lock to `67d1596`; the internal governance executor requires exact repository confirmation, makes at most one planned write then reads back, verifies, and replans from fresh state, and stops with redacted evidence on any failure without exposing a public `apply` command | [.github/governance/README.md](../.github/governance/README.md) |
| 2026-07-16 | LOG-0012 | Advance the accepted parent lock to `64f6fc8`; existing managed-ruleset update actions are planned only when branch conditions and rule inventory are supported, while stricter review, merge-method, and check-integration constraints are preserved and unknown constraints fail closed | [.github/governance/README.md](../.github/governance/README.md) |
| 2026-07-16 | LOG-0011 | Advance the accepted parent lock to `9411ad67`; governance apply-action planning remains internal pure data, executes no request, exposes no public `apply`, and fails closed on unknown state, unobserved checks, or unsafe ruleset updates | [.github/governance/README.md](../.github/governance/README.md) |
| 2026-07-16 | LOG-0010 | Bootstrap the read-only one-first-parent planner and tests as exact blobs from parent commit `1e99d395` without advancing lock `8035bbbf`; planning uses only an existing identity-checked local parent checkout and cannot fetch, materialize, or delete | [ADR-0003](../docs/adr/0003-adopt-direct-parent-template-inheritance.md) |
| 2026-07-16 | LOG-0009 | Bootstrap the offline inheritance validator and tests as exact blobs from parent commit `4035dbd0` without advancing lock `8035bbbf`; the bootstrap tool validates only the child-owned contract and does not imply acceptance of intervening parent history | [ADR-0003](../docs/adr/0003-adopt-direct-parent-template-inheritance.md) |
| 2026-07-16 | LOG-0008 | Bootstrap inheritance at verified parent commit `8035bbbf`; classify only byte-and-mode-identical foundation paths as inherited, keep divergent or absent paths protected until reviewed migration, and mirror all protected roots in the legacy sync ignore | [ADR-0003](../docs/adr/0003-adopt-direct-parent-template-inheritance.md) |
| 2026-07-16 | ADR-0003 | Adopt the accepted ai-dev-foundation manifest-driven direct-parent inheritance architecture; bootstrap from verified parent commit `8035bbbf` before advancing one first-parent commit per PR | [ADR-0003](../docs/adr/0003-adopt-direct-parent-template-inheritance.md) |
| 2026-07-03 | LOG-0007 | Markdown formatting MUST be frontmatter-aware: mdformat pinned via pre-commit with `mdformat-frontmatter` + `mdformat-gfm`, config in `.mdformat.toml` (`wrap=keep`, `number=true`). A naive run once collapsed all YAML frontmatter into headings — never use a formatter without these plugins | [.mdformat.toml](../.mdformat.toml) |
| 2026-07-02 | ADR-0002 | AI-facing docs are written in English | [ADR-0002](../docs/adr/0002-ai-facing-docs-in-english.md) |
| 2026-07-02 | ADR-0001 | Record architecture decisions as ADRs | [ADR-0001](../docs/adr/0001-record-architecture-decisions.md) |
| 2026-07-02 | LOG-0006 | `guard-bash.sh` must work when `jq` is absent (the `\|\| cat` fallback greps raw hook JSON); GR-010/011 patterns therefore treat `"` as a token terminator. Do not "simplify" that away. Verified by a matrix test on both paths | — |
| 2026-07-02 | LOG-0005 | AI PR review runs via `ai-review.yml`, disabled by default (repo var `ENABLE_AI_REVIEW`); supplements, never replaces, human review | — |
| 2026-07-02 | LOG-0004 | Template updates distribute via actions-template-sync PRs; downstream-customized files protected by `.templatesyncignore` | — |
| 2026-07-02 | LOG-0003 | GitHub governance (branch protection etc.) bootstrapped by `scripts/setup-github.sh` (gh CLI, idempotent) instead of a Probot app — no extra runtime dependency | — |
| 2026-07-02 | LOG-0002 | Canonical make targets are a binding contract (check-only lint, no `%:` catch-all, GR-031-guarded destructive targets); stack examples live in `profiles/` | [profiles/README.md](../profiles/README.md) |
| 2026-07-02 | LOG-0001 | Skills are vendor-neutral files in `.skills/`, routed via CLAUDE.md table instead of duplicated `.claude/skills/` wrappers | — |

---
id: terraform-gcp-template-adr-index
title: Terraform GCP Template Architecture Decision Records
---

# Terraform GCP Template Architecture Decision Records

This directory contains decisions owned by `terraform-gcp-template`. Inherited foundation
decisions from `ai-dev-foundation` are synchronized under
[`docs/foundation/adr/`](../foundation/adr/).

## Rules

- Numbered sequentially: `NNNN-kebab-case-title.md`. Copy the
  [foundation ADR template](../foundation/templates/adr.md).
- Status flow: `proposed → accepted | rejected`; later `deprecated` or
  `superseded by ADR-NNNN`. **Accepted ADRs are never edited** — supersede them.
- One decision per ADR. Keep it under ~2 pages.
- The ADR PR is approved by a human before implementation starts (GR-022).
- Every ADR gets a line in [.ai/decision-log.md](../../.ai/decision-log.md).

## Index

| # | Title | Status | Date |
|---|-------|--------|------|
| [0003](0003-adopt-direct-parent-template-inheritance.md) | Adopt manifest-driven direct-parent template inheritance | accepted | 2026-07-16 |

<!-- Append new Terraform-template ADRs to this table (newest last). -->

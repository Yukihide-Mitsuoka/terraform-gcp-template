---
id: template-inheritance-validation
title: Template Inheritance Validation and Planning
---

# Template inheritance validation and planning

This guide defines the side-effect-free commands adopted by
[ADR-0003](../adr/0003-adopt-direct-parent-template-inheritance.md).

## Validate the contract

```bash
python3 scripts/template_inheritance.py validate --root .
```

A successful command exits with status 0 and prints normalized JSON. Invalid schema,
unsafe paths, ownership overlap, missing mandatory protected paths, symlinks, repository
mismatch, and invalid commit IDs fail closed with status 2.

## Plan one parent commit

```bash
python3 scripts/template_inheritance.py plan \
  --root . \
  --parent-root ../ai-dev-foundation
```

The parent root must be a local Git worktree whose credential-free GitHub origin matches
the direct parent in the manifest. The command reads the existing local
`origin/<branch>` ref and does not fetch or update it.

The lock must be on that ref's first-parent history. The planner selects only the commit
immediately after the lock and reports its paths:

| Field | Meaning |
|-------|---------|
| `add` | An inherited parent file is absent in the child |
| `modify` | Inherited content or executable mode differs |
| `candidate_delete` | The parent removed an inherited file; no deletion occurs |
| `already_current` | The child already matches the candidate state |
| `protected` | A child-owned path is reported and skipped |
| `unowned` | A path outside both ownership lists is reported and skipped |

An origin mismatch, missing first-parent history, invalid Git state, unsafe path, or
symlink exits with status 2. Refreshing the parent checkout or changing the lock is a
separate reviewed action; do not change the lock only to silence an error.

## Side effects and provenance

Validation and planning perform no network request, fetch, checkout, file write,
materialization, deletion, GitHub API call, Terraform command, or GCP operation. The
planner script and tests are exact blobs from parent commit
`1e99d395ff949a40d45d888f59a6da41fc86e502`. Importing this bootstrap tool does not
advance the accepted parent lock.

---
id: template-inheritance-validation
title: Template Inheritance Validation
---

# Template inheritance validation

This repository adopts the direct-parent inheritance contract defined by
[ADR-0003](../adr/0003-adopt-direct-parent-template-inheritance.md).

Validate the child-owned manifest and lock without network or GitHub access:

```bash
python3 scripts/template_inheritance.py validate --root .
```

A successful command exits with status 0 and prints normalized JSON. Invalid schema,
unsafe paths, ownership overlap, missing mandatory protected paths, symlinks, repository
mismatch, and invalid commit IDs fail closed with status 2.

The validator performs no Git operation, network request, file write, deletion, GitHub
API call, Terraform command, or GCP operation. The script and its unit tests are exact
blobs from parent commit `4035dbd0e3e7cca1300f1c2f8e49967e60940022`; importing this
bootstrap tool does not advance the accepted parent lock.

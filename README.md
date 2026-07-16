# terraform-gcp-template

**GCP Terraform starter on the ai-dev-foundation base** — a template repository for
infrastructure projects where AI agents are the primary developers. It layers a Terraform
setup on top of everything [ai-dev-foundation](https://github.com/Yukihide-Mitsuoka/ai-dev-foundation)
provides (rules, guardrails, skills, hooks, CI).

> **AI agents:** stop reading this file. Your entry point is [CLAUDE.md](CLAUDE.md)
> (Claude Code) or [AGENTS.md](AGENTS.md) (everyone else).

## Position in the template chain

```
ai-dev-foundation ──sync──▶ terraform-gcp-template ──sync──▶ your infra project
   (base template)              (this repo)                       │ source=?ref
                                     │ source=?ref                ▼
                                     └──────────▶ terraform-gcp-modules (tagged library)
```

| Decision | Rule |
|----------|------|
| Need Terraform/GCP? | "Use this template" **here** |
| No Terraform? | Use [ai-dev-foundation](https://github.com/Yukihide-Mitsuoka/ai-dev-foundation) directly |
| Reusable building blocks | Live in [terraform-gcp-modules](https://github.com/Yukihide-Mitsuoka/terraform-gcp-modules), **referenced by tag, never copied** |
| Base updates | ai-dev-foundation changes arrive here as sync PRs ([template-sync.yml](.github/workflows/template-sync.yml), manual trigger any time); downstream repos repoint their sync source to THIS repo |

## What this adds on top of ai-dev-foundation

| Addition | Location |
|----------|----------|
| Terraform root-config layout (per-env) | [`infra/envs/`](infra/) with a worked `dev` example referencing the module library pinned at `?ref=v0.1.0` |
| Canonical Makefile wired for this layout | [`Makefile`](Makefile) — fmt/lint/validate/test over `infra/`; `plan ENV=<env>`; heavier layered-foundations reference remains in [`profiles/terraform-gcp/`](profiles/terraform-gcp/) |
| Terraform gitignore/state hygiene | `.gitignore` |

Everything else (`.ai/` rules, `.skills/`, `.claude/` hooks and skills, `.github/`
workflows, docs skeleton) comes from the base — see its
[README](https://github.com/Yukihide-Mitsuoka/ai-dev-foundation#readme).

## Using this template

1. **Create the repo**: GitHub → "Use this template".
2. **Repoint template sync**: in `.github/workflows/template-sync.yml`, change
   `source_repo_path` to `Yukihide-Mitsuoka/terraform-gcp-template`; set the repo variable
   `TEMPLATE_SYNC_ENABLED=true` to receive updates.
3. **Replace placeholders**: `grep -rn "{{" . --exclude-dir=.git` — mission, project name,
   state bucket in `infra/envs/*/versions.tf`.
4. **Inspect GitHub governance**: run `python3 scripts/github_governance.py plan --root .
   --repo OWNER/REPOSITORY` after `gh auth login`. It reports policy drift without
   changing settings. Use `audit` for a CI-suitable nonzero drift result. After reviewing
   the plan and obtaining the repository owner's explicit approval for that target, use
   `apply` with an exact `--confirm-repo OWNER/REPOSITORY`; it changes settings.
   `scripts/setup-github.sh` remains temporarily for legacy repository settings not
   represented in policy, such as squash-only merges and Discussions.
5. **Install local gates**: `make setup`.
6. **Verify**: `make doctor && make build` (build = credential-free validate of every env).
7. Point your agent at the repo and assign it an issue.

## License

MIT — see [LICENSE](LICENSE).

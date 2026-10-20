# UX Companion Cube

A skill family for the part of product work that happens **before anything is built**: finding
the real problem, knowing who it is for, and writing a design spec you can defend.

It sits upstream of the existing `ux-review` heuristic family, which evaluates interfaces that
already exist.

```
ux-companion (router)
      │
      ├─ ux-user-context   who is this for?        → .ux/USERS.md
      ├─ ux-research       is this assumption true? → .ux/research/<topic>.md
      ├─ ux-discover       what is the problem?     → .ux/briefs/<feature>.md
      └─ ux-design-spec    how should it work?      → .ux/specs/<feature>.md
                                 │
                                 └─→ /to-spec, /to-tickets → (built) → ux-review
```

## Why

Two failure modes this is built to prevent:

- **Building the wrong thing well.** Nobody wrote down who the user is or what problem this
  solves, so the team optimises a solution to a problem that was never stated.
- **Overengineering.** The spec grows a settings page, an admin view and analytics before
  anyone has used version one.

Against both, the family holds four lines:

1. **Evidence or Assumption, never neither.** Every claim is tagged. Assumptions that drive
   decisions are flagged. A thin-but-honest brief tells the team to go get evidence; a brief
   padded with confident guesses tells them to go build.
2. **Records decisions, does not invent them.** Nothing is written as a decision unless you
   confirmed it.
3. **One question at a time.** Like an interview, not a form. Stops when the answer is clear.
4. **Smallest version first.** The spec states the minimum that solves the problem; anything
   larger is justified against the brief or cut, with the reason.

## Install

Vendor-neutral `.agents/skills/` layout — works in Claude Code, Codex, Cursor and Rovo Dev.
Copy or symlink into the repo you are working in:

```bash
git clone <this repo> ~/dev/ux-companion
ln -s ~/dev/ux-companion/.agents/skills/ux-companion     <your-repo>/.agents/skills/ux-companion
ln -s ~/dev/ux-companion/.agents/skills/ux-discover      <your-repo>/.agents/skills/ux-discover
ln -s ~/dev/ux-companion/.agents/skills/ux-user-context  <your-repo>/.agents/skills/ux-user-context
ln -s ~/dev/ux-companion/.agents/skills/ux-research      <your-repo>/.agents/skills/ux-research
ln -s ~/dev/ux-companion/.agents/skills/ux-design-spec   <your-repo>/.agents/skills/ux-design-spec
```

If your agent only discovers `.claude/skills/`, symlink that to the same place —
`ln -s ../.agents/skills .claude/skills`, as this repo does for its own dogfooding.

## Use

Start with the router and let it pick:

> "Help me design a way to re-run a failed job."

Or call a skill directly when you already know which one you need:

| You have | Use |
|---|---|
| A vague idea or a feature request | `ux-discover` |
| No idea who the users are | `ux-user-context` |
| An assumption that needs testing, or raw interview notes | `ux-research` |
| A brief, and you want a design direction | `ux-design-spec` |
| "I'm about to build X, am I missing something?" | `ux-design-spec` — developer mode, returns a risk list |
| A built UI | `ux-review` — different family |

## What lands in your repo

```
.ux/
  USERS.md              # personas / JTBD, context of use, skill level
  surface-map.md        # product areas, navigation, patterns, vocabulary
  briefs/<feature>.md   # Problem Briefs
  specs/<feature>.md    # Design specs
  research/<topic>.md   # research plans, discussion guides, insights
```

Markdown in the repo, so it is diffable, reviewable, and readable by the next skill. The
second feature starts with what the first one learned instead of a blank page.

## Not built yet

`ux-evidence` (transcripts and support tickets into a tagged evidence log) and `ux-competitor`
(how adjacent products solve this). The skills say so rather than improvising a thin version.

Also deliberately absent: Confluence publishing, direct Jira work-item creation, and a
generated or crawled surface map. See [`plans/poc-plan.md`](plans/poc-plan.md) for what each is
waiting on.

## Repo

```
.agents/skills/<skill>/SKILL.md   the skills — one self-contained file each
plans/poc-plan.md                 decisions, contracts, build order, deferred work
evals/golden-scenarios.md         five scenarios, run by hand
evals/check_skills.py             frontmatter validation — run after editing any skill
```

```bash
python3 evals/check_skills.py
```

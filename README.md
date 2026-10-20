# UX Companion

A skill family for the part of product work that happens **before anything is built**: finding
the real problem, knowing who it is for, and writing a design spec you can defend.

It sits upstream of the existing `ux-review` heuristic family, which evaluates interfaces that
already exist.

```
ux-companion (router)
      │
      ├─ ux-user-context   who is this for?         → .ux/USERS.md
      ├─ ux-evidence       what do we already know?  → .ux/evidence/<batch>.md
      ├─ ux-research       is this assumption true?  → .ux/research/<topic>.md
      ├─ ux-discover       what is the problem?      → .ux/briefs/<feature>.md
      ├─ ux-competitor     how do others solve it?   → .ux/LANDSCAPE.md
      ├─ ux-concepts       how else could we do it?  → .ux/concepts/<feature>.md
      │                                                .ux/PRINCIPLES.md
      ├─ ux-design-spec    how should it work?       → .ux/specs/<feature>.md
      └─ ux-prototype      can I see it?             → .ux/prototypes/<feature>.html
                                 │
                                 ├─→ ux-review
                                 └─→ to-tickets (optional, own schedule)
```

`ux-evidence` and `ux-competitor` are **standing**, not per-feature: a log and a landscape that
every later feature reads and every later feature adds to.

The shape of the practice, not just the file list: **know → discover → diverge → converge →
make it touchable → evaluate.** The middle two are where most teams skip straight from a
problem to a specification of the first idea anyone said; the first is what most teams never
accumulate at all, so every feature starts from nothing and the same question gets researched
twice.

## Why

Five failure modes this is built to prevent:

- **Building the wrong thing well.** Nobody wrote down who the user is or what problem this
  solves, so the team optimises a solution to a problem that was never stated.
- **Overengineering.** The spec grows a settings page, an admin view and analytics before
  anyone has used version one.
- **Building the first thing anyone said.** No alternative was ever on the table, so the
  direction was chosen by whoever spoke first rather than by anyone deciding.
- **Shipping the unobjectionable.** Every heuristic passes, nothing is wrong with it, and
  nobody mentions it to a colleague.

- **Learning nothing twice.** Each feature starts from a blank page, so the same question gets
  researched again, the same competitor gets looked up again, and what the last feature found
  is in somebody's head or a closed tab.

Against all five, the family holds eight lines:

1. **Evidence or Assumption, never neither.** Every claim is tagged. Assumptions that drive
   decisions are flagged. A thin-but-honest brief tells the team to go get evidence; a brief
   padded with confident guesses tells them to go build.
2. **Records decisions, does not invent them.** Nothing is written as a decision unless you
   confirmed it.
3. **Reason first, ask last.** It works the answer out from your request, your repo and
   published research before it asks you anything — then asks only what you alone can supply,
   one question at a time. Answering a questionnaire leaves you with the gaps you started
   with, itemised.
4. **Smallest version first.** The spec states the minimum that solves the problem; anything
   larger is justified against the brief or cut, with the reason.
5. **Both lenses.** Every criterion is applied twice: to a person operating an interface, and
   to an agent calling a tool. Findability for an agent is the tool description it reads
   before acting, not a menu it can see.
6. **Diverge once, then narrow.** `ux-concepts` is the only place the work gets wider — prior
   art, a reframe, five directions that differ in approach rather than in degree. It ends with
   one choice, so nothing downstream gets bigger. The spec then minimises the best of five
   instead of the first of one.
7. **The floor is not the ceiling.** Themes B–J are satisfied by the absence of problems.
   Theme L asks what is actually good here — the one moment someone would screenshot, and the
   honest answer when there isn't one.
8. **Cheapest source first, and keep what it cost you.** Read the evidence log before planning
   a study, and the landscape before sweeping prior art — then write back what you learned, so
   the next feature inherits it. `ux-evidence` and `ux-competitor` exist to be the place it
   goes; an atom cited as `EV-0042` is what makes line 1's `**Evidence:**` tag checkable rather
   than decorative.

## Install

```bash
npx skills add juhovainio/ux-companion
```

Picks up your existing GitHub auth (works for this private repo), lets you choose which
skills and which agent (Claude Code, Codex, Cursor, …) to install to, and symlinks them in so
updates here show up without reinstalling. Add `--all` to skip the prompts, or `-g` to install
once for every project. See the [`skills` CLI docs](https://github.com/vercel-labs/skills) for
all options.

### Manual install

Vendor-neutral `.agents/skills/` layout — works in Claude Code, Codex, Cursor and Rovo Dev.
Copy or symlink into the repo you are working in:

```bash
git clone <this repo> ~/dev/ux-companion
cd <your-repo> && ln -s ~/dev/ux-companion/.agents/skills .agents/skills
```

Symlink the directory, not each skill — then a new skill in this repo appears in yours without
a second install step.

If your agent only discovers `.claude/skills/`, symlink that to the same place —
`ln -s ../.agents/skills .claude/skills`, as this repo does for its own dogfooding.

## Use

Say what you want. `ux-companion` is the only entry point — the sub-skills are internal
dispatch targets, so you never need to know their names:

> "Help me design a way to re-run a failed job."

Where that lands:

| You have | Routes to |
|---|---|
| A vague idea or a feature request | `ux-discover` |
| No idea who the users are | `ux-user-context` |
| A pile of support tickets, reviews or transcripts nobody has read | `ux-evidence` |
| An assumption that needs testing, or raw interview notes | `ux-research` |
| "How do others solve this?", or a landscape that has gone stale | `ux-competitor` |
| A problem, and one obvious solution everyone has already assumed | `ux-concepts` |
| A chosen direction, and you want flows, states and copy | `ux-design-spec` |
| A spec, and someone who needs to see it to react to it | `ux-prototype` |
| "I'm about to build X, am I missing something?" | `ux-design-spec` — developer mode, returns a risk list |
| A finished spec, ready to file as Jira tickets | `to-tickets` |
| A built UI | `ux-review` — different family |

## What lands in your repo

```
.ux/
  USERS.md                # personas / JTBD, context of use, skill level
  PRINCIPLES.md           # the product's design stance, as trade-offs
  LANDSCAPE.md            # the competition set, table stakes, where we differ, last verified
  surface-map.md          # product areas, navigation, patterns, vocabulary
  jira-project.md         # the Jira project this repo files tickets to (to-tickets)
  briefs/<feature>.md     # Problem Briefs
  competitors/<product>.md # one teardown each, by flow rather than feature matrix
  concepts/<feature>.md   # directions explored, one chosen, the rest and what they were better at
  evidence/INDEX.md       # the standing evidence log, and what it cannot speak for
  evidence/<batch>.md     # citable atoms — one observation, one source, one date
  specs/<feature>.md      # Design specs (gains "## Jira tickets" once filed)
  prototypes/<feature>.*  # one self-contained HTML file, or an exact session transcript
  research/<topic>.md     # research plans, discussion guides, insights
```

Markdown in the repo, so it is diffable, reviewable, and readable by the next skill. The
second feature starts with what the first one learned instead of a blank page.

## Not built yet

Deliberately absent: Confluence publishing and a generated or crawled surface map. Direct Jira
ticket creation is handled by `to-tickets`, behind a mandatory dry-run confirmation gate. See
[`plans/poc-plan.md`](plans/poc-plan.md) for what the remaining gaps are waiting on.

Each skill also states its own cuts rather than improvising a thin version — `ux-evidence` does
not pull from ticket APIs or score sentiment, `ux-competitor` does not do pricing, market share
or win/loss, `ux-research` does not do surveys or journey maps.

## Repo

```
.agents/skills/<skill>/SKILL.md   the skills — one self-contained file each
.agents/skills/ux-companion/
  references/design-questions.md  Themes A–M — the shared criteria, read by five skills
plans/poc-plan.md                 decisions, contracts, build order, deferred work
plans/reconciliation.md           comparison with the parallel jussi-exploration branch
evals/golden-scenarios.md         eight scenarios, run by hand
evals/check_skills.py             frontmatter validation — run after editing any skill
```

Themes A–J generalise the `ux-review` heuristics to the pre-build stage and form a floor: pass
them all and nothing is wrong with the design. K originates adjacent value; L asks what is
actually good here, and is the only theme that can fail a design for being merely correct; M
(privacy & data handling) was added later, reasoned the same way as B–J. They live in one file
because five skills read them — edit there, never restate a theme inside a skill.

```bash
python3 evals/check_skills.py
```

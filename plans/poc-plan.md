# UX Companion — POC plan

Source: [AI Hackathon Ideation Doc](https://amd.atlassian.net/wiki/spaces/AIG/pages/2079603339/AI+Hackathon+Ideation+Doc)

A skill family that covers the path from "I have an idea" to "I have a design spec I can
defend." It sits upstream of the existing `ux-review` heuristic family, which reviews a UI
that already exists.

```
ux-companion (router)
      │
      ├─ ux-user-context ──┐
      ├─ ux-research ──────┤
      ├─ ux-discover ──────┴──→ ux-concepts ──→ ux-design-spec ──→ ux-prototype ──→ ux-review
                                                       │
                                                       └──→ to-tickets (optional, own schedule)
```

`ux-concepts` and `ux-prototype` are post-POC additions — see *Beyond the POC* below for what
they fix. The five-skill POC shape is what the Decisions table and Build order describe.

## Decisions

| # | Question | Decision | Why |
|---|---|---|---|
| 1 | Packaging | Plain `.agents/skills/` layout | Portable to Claude Code, Codex, Cursor, Rovo Dev with no manifest. No install step to demo. |
| 2 | POC scope | Router, `ux-user-context`, `ux-research`, `ux-discover`, `ux-design-spec` | Per the POC scope column in the ideation doc table. `ux-competitor` and `ux-evidence` are out. |
| 3 | Output destination | Repo markdown under `.ux/` only | Diffable, no external dependency, and the next skill can read it back. Confluence publishing can be its own skill later. |
| 4 | Surface map origin | Template, with an agent-assisted first draft the user confirms | No crawling infrastructure; works on CLIs and web apps alike. The user owns the truth. |
| 5 | `USERS.md` location | Per repo, at `.ux/USERS.md` | Zero config. Duplication across repos of one product is accepted for the POC. |
| 6 | Jira handoff | ~~Hand off to `/to-spec` and `/to-tickets`~~ Superseded — `to-tickets` now writes real Jira tickets behind a mandatory dry-run confirmation gate | Originally deferred so nothing could write junk to a live project on stage. Built once the confirmation gate made that risk acceptable; see `to-tickets`'s SKILL.md. |

### Drift noted in the source doc

The "Hackathon MVP" section lists three skills (router, `ux-discover`, `ux-design-spec`);
the skills table's POC scope column lists five, adding `ux-user-context` and `ux-research`.
**The table is authoritative** — it is the more recent edit. The MVP section should be
updated or deleted so the doc stops contradicting itself.

## Architecture

### One self-contained `SKILL.md` per skill, plus one shared reference

Each `SKILL.md` embeds its own templates and conventions. No `scripts/`, no shared
`templates/` directory.

The original plan had no `references/` at all. The existing `ux-review` family splits long
content into `references/` and resolves the path at runtime with a `find $HOME/.claude/skills/…`
shell fallback — worth it there because the content is long and the family is Claude Code
only. Here it looked like it would buy duplication of ten lines of shared convention in
exchange for a path resolution step Codex and Cursor handle differently.

**That trigger has since been tripped**, not by length but by sharing. Reconciling with
`jussi-exploration` brought in a 190-line themes file (A–K, each with a Human lens and an
Agent lens) that three skills read. Inlining it would mean three copies that drift, which is
exactly the failure the "no duplication" argument was protecting against. It lives at
`.agents/skills/ux-companion/references/design-questions.md` — under the router because it
belongs to the family rather than to any one member.

Path resolution is kept deliberately dumb: skills read the sibling relative path
`../ux-companion/references/design-questions.md`, and fall back to a Glob if it does not
resolve. No shell, so it works in every host.

**Upgrade trigger, revised:** add a `references/` file when content is shared by more than one
skill, or when a `SKILL.md` passes ~300 lines.

### Shared repo files the skills read and write

```
.ux/
  USERS.md              # personas / JTBD, context of use, skill level
  surface-map.md        # product areas, navigation, key patterns and terms
  briefs/<feature>.md   # Problem Briefs      (ux-discover)
  specs/<feature>.md    # Design specs        (ux-design-spec)
  research/<topic>.md   # plans, guides, insight summaries (ux-research)
```

`evidence/` from the source doc is omitted — `ux-evidence` is out of POC scope, so nothing
would write it.

Every skill reads `.ux/` before asking the user anything, so the second feature starts with
the knowledge from the first instead of a blank page.

### Conventions every skill follows

1. **Evidence or Assumption, never neither.** Each claim is tagged `**Evidence:**` with a
   source link or `**Assumption:**`. Assumptions that drive a decision carry `⚠️ drives a
   decision`.
2. **Records decisions, does not invent them.** Nothing is written as a decision unless the
   user confirmed it. Unresolved items go to Open questions.
3. **Reason first, ask last.** Reason the answer out from context; research it where a
   published finding would sharpen it; state an assumption where neither settles it; ask only
   for what the user alone can supply. Those surviving questions are asked one at a time,
   stopping when the answer is clear enough rather than after a fixed count.
4. **Existing context first.** Read `.ux/` before asking what is already written down.
5. **Both lenses.** A consumer is a person operating an interface or an agent calling a tool,
   and most products have both. Apply both unless the consumer is clearly one.

## Skill contracts

### `ux-companion` — router

| | |
|---|---|
| Triggers | "Help me design…", "is this worth building?", "who is this for?", "I'm about to build X" |
| Input | Free text |
| Output | A route announcement, then the chosen sub-skill |

Reads `.ux/` to see what already exists, asks at most one clarifying question, announces the
route and the reason in one sentence, then hands off. **It never does the downstream work
itself.**

Routing:

| Situation | Route to |
|---|---|
| No `.ux/USERS.md`, and the request is about who the user is | `ux-user-context` |
| Idea or request with no clear problem statement | `ux-discover` |
| Needs to plan or synthesise research, or validate with real users | `ux-research` |
| A brief exists and the user wants a design direction | `ux-design-spec` |
| "I'm about to build X, am I missing something?" | `ux-design-spec` in developer mode — risk list, not a full spec |
| A UI already exists and needs reviewing | Out of family — point at `ux-review` |

### `ux-discover` — Problem Brief

| | |
|---|---|
| Triggers | An idea or feature request with no clear problem statement |
| Input | Idea, Jira ticket, Confluence page, or free text |
| Output | `.ux/briefs/<feature>.md` |

Interviews the user one question at a time. Brief sections: Problem, Who has it, Evidence,
Why now, Success criteria, Assumptions to validate, Open questions.

Modes: **PM/PO** (evidence and success metrics first), **feature lead** (product fit and edge
cases), **developer** (short risk list, no full brief), **live interview** (produces probe
questions during a real interview: warm-up, context, deep dive, reaction, wrap-up).

### `ux-user-context` — USERS.md

| | |
|---|---|
| Triggers | "Who is the user?", or another skill needs reusable user context |
| Input | Cold start: questions to the caller. Expanding: existing docs and briefs |
| Output | `.ux/USERS.md` |

Personas or jobs-to-be-done, context of use, skill level. **Never invents a persona** — what
is not known is written as `Unknown` with the question that would resolve it. Appends to an
existing `USERS.md` rather than overwriting.

### `ux-research` — research plans and synthesis

| | |
|---|---|
| Triggers | "How do we validate this?", "help me plan research", "here are my interview notes" |
| Input | A question to answer, or raw notes |
| Output | `.ux/research/<topic>.md` |

**Deliberately cut for POC** to three outputs: a research plan (question, method, participants,
what would change our mind), a discussion guide, and synthesis of supplied notes into tagged
insights. The ideation doc lists nine more deliverables — usability test reports, surveys,
recruitment, journey maps, opportunity maps, personas, prioritised recommendations. Personas
belong to `ux-user-context`; the rest are listed as out of scope inside the skill so it says
so rather than improvising a thin version.

This is the skill most at risk of becoming a kitchen sink. If it feels thin at demo time, cut
it from the POC rather than widening it.

### `ux-design-spec` — Design spec

| | |
|---|---|
| Triggers | A Problem Brief exists and the user wants a design direction |
| Input | `.ux/briefs/<feature>.md`, `.ux/USERS.md`, `.ux/surface-map.md` |
| Output | `.ux/specs/<feature>.md` |

Three phases, in order:

1. **Overengineering gate.** Describe the smallest version that solves the brief's problem.
   Anything larger must be justified against the brief; unjustified scope goes to
   **Out of scope** with the reason it was cut.
2. **Spec.** Flows, entry points, placement in the existing navigation, states, copy, the
   simplest alternative considered, out of scope, product opportunities (Theme K).
3. **Pre-build heuristic check.** Themes B–J and M from
   `.agents/skills/ux-companion/references/design-questions.md`, each applied through both the
   Human lens and the Agent lens. Theme A was settled by the brief. Visual criteria —
   affordance rendering, visual hierarchy, loading-state styling — wait for `ux-review` on a
   real UI.

Theme K is the family's only generative step: it originates adjacent value rather than
extracting what was stated. It sits in the spec rather than the brief because it needs both
the problem (Theme A, from the brief) and the flow and consumer (Theme B, decided here). It is
explicitly not a way to reopen Phase 1's cuts — an opportunity must extend something already
decided, and anything needing its own problem statement is a separate idea.

The heuristic check is a **phase of this skill, not a separate skill**. The ideation doc's MVP
list implies a fourth skill; a skill that only ever runs on this skill's output, at one point
in its flow, is a section.

If `.ux/surface-map.md` is missing, offer to draft one from the repo and have the user confirm
it before using it.

Ends by naming the handoff: `to-tickets`, whenever the user wants to file it — it does not run
automatically. `ux-design-spec` itself still does not write to Jira; `to-tickets` does, behind
a confirmation gate.

## Build order

1. `ux-discover` — the demo centrepiece, and it defines the brief format everything downstream reads.
2. `ux-design-spec` — consumes the brief; proves the end-to-end path.
3. `ux-user-context` — unblocks "who is the user?", the doc's headline question.
4. `ux-companion` router — written last of the four so it routes to skills whose shapes are settled.
5. `ux-research` — broadest, cut hardest, least load-bearing for the demo.
6. `README.md` + golden scenarios.

## How we will know it worked

`evals/golden-scenarios.md`, run by hand — no eval harness for a POC. Five scenarios:

1. **Vague idea** → router picks `ux-discover`; brief has a real problem statement, not a restatement of the idea.
2. **Feature that is too large** → `ux-design-spec` cuts something real into Out of scope, with a reason.
3. **"Who is this for?" with no `.ux/`** → router picks `ux-user-context`; unknowns stay marked `Unknown`.
4. **Developer quick-check** → a short risk list, no full spec, no file.
5. **Existing `.ux/` context** → skills read it and do not re-ask what is already written down.

Pass criteria across all five: nothing is invented, every key decision is Evidence or flagged
Assumption, Out of scope contains real cuts rather than things nobody proposed, and nothing is
asked that the request, the repo or `.ux/` already answers.

## Risks

| Risk | Mitigation |
|---|---|
| Five skills is more than the original MVP's three, in a hackathon timebox | Build order is value-ordered. If time runs out, stop after step 4 — the router plus three skills is still a complete demo. |
| `ux-research` is broad enough to swallow the timebox | Cut to three outputs, everything else explicitly listed as out of scope. Drop the skill entirely if it is thin at demo time. |
| Skills ask too many questions and the demo drags | "Stop when clear enough" is a stated behaviour, and the demo uses a prepared scenario. |
| `.agents/skills/` discovery differs per agent | Verify discovery in Claude Code before building further; document the fallback in the README. |

## Deferred

| Thing | Add when |
|---|---|
| `ux-evidence` | Marked NO in the POC scope column. After the POC lands. |
| `ux-competitor` as a standing landscape | `ux-concepts` Phase 1 covers the per-decision sweep. Build this when someone needs the market view to persist between decisions. |
| Confluence publishing | Someone outside a repo needs to read the output. |
| ~~Direct Jira work-item creation~~ | Done — see `to-tickets`. |
| Shared product-level `USERS.md` | A second repo in the same product needs the same personas. |
| Generated or crawled surface map | The hand-written map is measurably the bottleneck. |
| Eval harness | Golden scenarios get run often enough that by hand hurts. |
| Merging the `jussi-exploration` branch structurally | Jussi has weighed in. See [`reconciliation.md`](reconciliation.md) — the strict improvements are already folded in; the structural call is open. |

## Beyond the POC: what the five skills could not do

The POC family is a reduction machine — find the problem, cut the scope, check the result. Run
end to end, it reliably produces a competent version of **whatever idea was mentioned first**,
and it has no way to tell a design that merely passes from one anyone would care about. Three
structural gaps, and what was added for each:

| Gap | Why it mattered | Added |
|---|---|---|
| No divergence anywhere | Brief → spec means the direction was chosen by whoever spoke first. Theme K is the only generative beat and is deliberately scope-bound, so it cannot propose a different approach. | `ux-concepts` — prior art, reframe, five directions that differ in approach, converge on one. Divergence in thinking; the overengineering gate still runs downstream, so nothing gets bigger. |
| No stated point of view | With no stance, choosing between directions is arbitrary and every spec re-derives taste from zero. | `.ux/PRINCIPLES.md`, drafted and confirmed once by `ux-concepts`, read by everything after. Trade-off shaped ("rather X than Y") — a principle that rules nothing out does no work. |
| B–J is a floor with no ceiling | Every theme is satisfied by the *absence* of a problem. A design can pass all nine and be unmemorable, and nothing in the family notices. | Theme L — craft and the signature moment — as a spec section alongside K, with "it does not have one" as a valid and useful answer. |

And one practical gap: `ux-review` evaluates built interfaces, so every criterion needing a
real surface waited on engineering. `ux-prototype` closes it — one self-contained HTML file, or
an exact session transcript for a CLI or agent-facing feature. Nobody has ever decided they
loved a product by reading a spec; a prototype moves the disagreement forward by a month, while
changing it still costs an afternoon.

Phase 3 of `ux-design-spec` also now requires a stance change before the check, and says so in
the report when it ran single-context. Checking your own spec in the frame you wrote it in
finds typography, not flaws.

**Not added, deliberately:** a crit skill (the stance change plus `ux-prototype`'s reaction loop
covers it), a design-system or token skill (nothing in `.ux/` is visual yet), and narrative or
presentation output (that is downstream of whether the design is any good).

## Reconciled with `jussi-exploration`

A parallel independent build of the same ideation doc exists on `origin/jussi-exploration`.
The strict improvements from it are folded into `main` — themes A–K as the shared criteria
asset, reason-first in place of interview-first, the premise-mismatch rule, research grounding,
and the Human/Agent lens throughout. The structural question (one skill or five) is deliberately
left open for Jussi. Nothing on his branch was changed or deleted. Full comparison in
[`reconciliation.md`](reconciliation.md).

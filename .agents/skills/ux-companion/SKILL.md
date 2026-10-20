---
name: ux-companion
description: Entry point for product and UX work before or during building — reads `.ux/` context and routes internally to the right companion skill, so the user never needs to know any of their names. Use when someone asks "help me design…", "is this worth building?", "who is this for?", "do we have personas", "can you scope this feature", "how should this work", "write the spec", "this feels too big", "what are our options" or "is there a better way to do this", "can I see it", "make me a prototype", "how do we find out if this is true", "help me plan some research", "write me a discussion guide", "what do we actually know about this", "what's in these support tickets", "how do other products solve this", "who are our competitors", "publish this to Confluence", "where should these docs live", "I'm about to build X, am I missing something?", or hands over a vague idea, feature request, Jira ticket, Confluence page, or a pile of tickets, reviews or transcripts with no clear problem statement. Do NOT use when a built UI needs reviewing (use ux-review).
allowed-tools: Read, Glob, Grep, Skill
---

# UX Companion

You are a router. Your job is to pick the right skill and hand
over — **not to do the downstream work yourself.**

**Artefact root.** Resolve it per `references/artefact-store.md` before reading context, and
state it in one line when it is not the default. Then **substitute it for the literal `.ux/`
prefix in every path below** — they are written as `.ux/…` shorthand, and once a non-default root
is resolved, reading a path that still begins `.ux/` is a bug. Getting this wrong here is the
most expensive place to do so: you read ten paths to pick a route, you write nothing that would
leave a trace, and a root resolved wrongly sends every route after it to the wrong skill.

The family covers the path from "I have an idea" to "here is a prototype of the direction we
chose, and the reasons we rejected the others". It sits upstream of `ux-review`, which reviews
interfaces that already exist — and now feeds it a prototype to review before anyone builds.

```
ux-evidence ─────┐
ux-user-context ─┤
ux-research ─────┤
ux-discover ─────┴─→ ux-concepts ─→ ux-design-spec ─→ ux-prototype ─→ ux-review
                      (diverge)  ↑    (converge)       (make it real)
                   ux-competitor ┘            └─→ to-tickets (optional, own schedule)
```

`ux-evidence` and `ux-competitor` are **standing** rather than per-feature: they maintain a log
and a landscape that every later feature reads, so the second feature starts from what the
first one learned.

## Step 1 — Read the context

Check what already exists before deciding anything:

- `.ux/USERS.md` — is there user context?
- `.ux/PRINCIPLES.md` — does the product have a stated design stance?
- `.ux/briefs/` — is there a brief for this feature already?
- `.ux/concepts/` — have directions been explored and one chosen?
- `.ux/specs/` — is there a spec already?
- `.ux/prototypes/` — is there something touchable already?
- `.ux/surface-map.md` — is the product surface mapped?
- `.ux/research/` — is there research on this?
- `.ux/evidence/INDEX.md` — is there already logged evidence that speaks to this?
- `.ux/LANDSCAPE.md` — is there a standing view of how others solve this, and is it still fresh?

What exists changes the route more than how the request was phrased. Someone saying "help me
design this" with no brief needs `ux-discover` first, whatever they asked for.

## Step 2 — Route

| Situation | Route to |
|---|---|
| An idea, feature request or ticket with no clear problem statement | `ux-discover` |
| "Who is the user?" / "who are we building for?", or no `.ux/USERS.md` and the request depends on knowing | `ux-user-context` |
| An assumption needs validating, research needs planning, or raw interview notes need synthesising | `ux-research` |
| The user has support tickets, reviews, transcripts or forum threads and wants to know what is in them | `ux-evidence` |
| "What do we actually know?" / "is there evidence for this?" and `.ux/evidence/` is empty but material exists | `ux-evidence` |
| "How do others solve this?", "who are our competitors?", or the landscape is missing or stale | `ux-competitor` |
| "What are our options?", "how else could we solve this?", "is there a better way?" | `ux-concepts` |
| A brief exists, nothing in `.ux/concepts/`, and the user wants to design | `ux-concepts` — see the tiebreak below |
| A direction is chosen, or the user declined to explore any, and they want flows, states, copy or a scope cut | `ux-design-spec` |
| A spec exists and someone wants to see, feel or show it | `ux-prototype` |
| "I'm about to build X, am I missing something?" | `ux-design-spec`, developer mode — a risk list, not a spec |
| "This feels too big" / "are we overengineering this?" | `ux-design-spec` — the overengineering gate is its first phase |
| The user is in a live user interview right now | `ux-discover`, live interview mode |
| A spec exists and the user wants it filed as Jira tickets | `to-tickets` |
| An artefact needs to reach people who will not clone the repo — "publish this", "put it on Confluence" | `ux-publish` |
| "Where should these live?", "move our docs", or artefacts should not be in this repo | No skill needed — set the root per `references/artefact-store.md`, in whichever skill is in hand |
| A UI already exists and needs evaluating | Out of this family — point at `ux-review` and stop |

**The tiebreak.** "Design this" with a brief and no concepts is the ambiguous case, and it is
the one the family exists to catch. Route to `ux-concepts`, say it is a short detour and that
they can skip straight to the spec in one sentence. Do not insist twice — a team that has
already decided is converging on purpose, and that is recorded in the spec's
`Simplest alternative considered` rather than argued about at the door.

**Evidence or research?** The other confusable pair. `ux-evidence` reads material that already
exists; `ux-research` goes and gets material that does not. When both apply, route to
`ux-evidence` first — the cheapest study is the one you do not have to run, and what the log
turns up changes what is worth asking real people.

**Ask at most one clarifying question**, and only when two routes are genuinely plausible and
would produce different work. Ask it as a specific binary choice, never as an open "what would
you like to do?". When the request is ambiguous but one route dominates, take it and say so —
the user can redirect in one sentence, which is cheaper than being interrogated at the door.

## Step 3 — Hand over

Announce the route in one sentence, with the reason, then hand over:

> Routing to **ux-discover** — there's no brief for this yet, so let's find the problem before
> designing anything.

To hand over: invoke the named skill with the Skill tool and follow its directives in full —
do not summarise them or improvise a shortened version. This is a required dependency: if the
host has no skill-invocation mechanism, stop and report that routing cannot complete rather
than improvising the downstream skill's work from memory.

## Chaining

When a skill finishes, suggest the natural next step and stop. Do not chain automatically —
each of these produces a document someone needs to agree with before the next one builds on
it.

| Just finished | Usually next |
|---|---|
| `ux-evidence` | `ux-discover` — a brief citing the atoms, or `ux-research` if themes are forming |
| `ux-competitor` | `ux-discover` on a gap worth closing, or `ux-concepts` if a decision is already waiting |
| `ux-user-context` | `ux-discover` — now scope the problem |
| `ux-discover` | `ux-concepts`, or `ux-research` first if the brief's decision-driving assumptions are unvalidated |
| `ux-research` | `ux-user-context` to fold findings into `USERS.md`, then `ux-discover` or `ux-concepts` |
| `ux-concepts` | `ux-design-spec` on the chosen direction — once the user has chosen it |
| `ux-design-spec` | `ux-prototype` to make it touchable, and `to-tickets` to file it in Jira — independent next steps, each on its own schedule |
| `ux-prototype` | `ux-review` on the prototype, then back to `ux-design-spec` with what it revealed |
| Any artefact, once it is agreed | `ux-publish`, if people outside the repo need to read it — optional, on its own schedule |

## Family conventions

Every skill here follows a fuller set of conventions than this (evidence tagging, smallest
version first, both lenses, the floor-vs-ceiling split) — each enforces its own concretely, and
`README.md` summarises the set for humans. The two below are the ones this router itself acts
on, so they live here rather than only downstream:

- **Reason first, ask last.** Each skill works the answer out from context before asking — this
  is why Step 2 allows at most one clarifying question, asked only when two routes would
  produce genuinely different work.
- **Diverge before converging, once.** `ux-concepts` is the one place the work gets wider;
  everything after it narrows. This is why the tiebreak above sends an ambiguous "design this"
  through `ux-concepts` rather than straight to `ux-design-spec` — a team that goes from brief
  straight to spec has chosen a direction without noticing it chose.

## Shared references

Two assets live under this skill because they belong to the family rather than to any one
member. Edit them there — restated inside a skill, either becomes a second copy that drifts.

`references/artefact-store.md` holds where artefacts live: how the root resolves, that `.ux/` is
shorthand for it, and the publish contract. Every skill that reads or writes an artefact reads
this first.

`references/design-questions.md` holds Themes A–L, the family's single criteria asset.
`ux-discover` reasons through Theme A, `ux-concepts` works the solution space between A and B,
`ux-design-spec` reasons through B–J and M in its heuristic check and K and L in its spec,
`ux-user-context` uses the Human/Agent lens distinction. It lives under this skill because it
belongs to the family, not to any one member. Edit it there — a theme restated inside a skill
becomes a second copy that drifts.

## Scope

In this family: `ux-discover`, `ux-user-context`, `ux-research`, `ux-evidence`,
`ux-competitor`, `ux-concepts`, `ux-design-spec`, `ux-prototype`, `to-tickets`, `ux-publish`.
Unlike the rest, `to-tickets` and `ux-publish` are also meant to be invoked directly — their own
descriptions say so, rather than marking themselves internal.

Not built, and the skills say so rather than improvising a thin version: publishing to anything
other than Confluence, and a generated or crawled surface map.

## Do not

- Do not write a brief, spec or `USERS.md` yourself. Route.

---
name: ux-companion
description: Entry point for turning rough input into a properly structured document and narrative (problem brief, user context, research plan, concepts, design spec, prototype). Shows what is missing, which claims lack evidence, and which named owner can answer each open question. Reads `.ux/` context, runs a first-run owners onboarding when `.ux/OWNERS.md` is missing, and routes internally to the right companion skill, so the user never needs to know any of their names. Use when someone asks "help me write this up", "turn these notes into a doc", "what's missing from this", "who should answer this", "help me design…", "is this worth building?", "who is this for?", "do we have personas", "can you scope this feature", "how should this work", "write the spec", "this feels too big", "what are our options", "how else could we solve this", "is there a better way to do this", "can I see it", "make me a prototype", "how do we find out if this is true", "help me plan some research", "write me a discussion guide", "I'm about to build X, am I missing something?", or hands over a vague idea, feature request, Jira ticket or Confluence page with no clear problem statement. Do NOT use when a built UI needs reviewing (use ux-review).
allowed-tools: Read, Glob, Grep, Skill
---

# UX Companion

You are a router. Your job is to pick the right skill and hand
over — **not to do the downstream work yourself.**

The family turns rough input (an idea, notes, a ticket) into a properly structured document
with a clear narrative. For each document it reasons out what it can, says what is missing,
tags every claim as Evidence or Assumption, and names the person who can close each gap. The
documents run from "I have an idea" to "here is a prototype of the direction we chose, and the
reasons we rejected the others". The family sits upstream of `ux-review`, which reviews
interfaces that already exist, and feeds it a prototype to review before anyone builds.

```
ux-owners ───→ .ux/OWNERS.md (first run, read by everything below)

ux-user-context ─┐
ux-research ─────┤
ux-discover ─────┴─→ ux-concepts ─→ ux-design-spec ─→ ux-prototype ─→ ux-review
                      (diverge)       (converge)       (make it real)
                                            └─→ /to-spec, /to-tickets
```

## Step 1 — Read the context

Check what already exists before deciding anything:

- `.ux/OWNERS.md` — does the team have owners per topic?
- `.ux/USERS.md` — is there user context?
- `.ux/PRINCIPLES.md` — does the product have a stated design stance?
- `.ux/briefs/` — is there a brief for this feature already?
- `.ux/concepts/` — have directions been explored and one chosen?
- `.ux/specs/` — is there a spec already?
- `.ux/prototypes/` — is there something touchable already?
- `.ux/surface-map.md` — is the product surface mapped?
- `.ux/research/` — is there research on this?

What exists changes the route more than how the request was phrased. Someone saying "help me
design this" with no brief needs `ux-discover` first, whatever they asked for.

## Step 2 — Route

**First run comes first.** If `.ux/OWNERS.md` does not exist, route to `ux-owners` before
anything else and say so in one sentence: "Routing to **ux-owners** first. I need to know who
owns which topic so open questions can name a person." Then continue with what the user asked.
The user can say "later" in one word. Skip onboarding, and the documents tag gaps `Owner:
unassigned`. Do not insist twice. Skip it without asking in developer mode and live interview
mode, which write no file. Offer it once, at the end, when a document finishes with open
questions and no owners file.

If the user asks to change who owns a topic, route to `ux-owners` whatever else exists.

| Situation | Route to |
|---|---|
| No `.ux/OWNERS.md`, and the user has not said "later" | `ux-owners`, then the row that fits the request |
| "Who owns X?", "X now owns security", "add an owner for legal" | `ux-owners`, update path |
| An idea, feature request or ticket with no clear problem statement | `ux-discover` |
| "Who is the user?" / "who are we building for?", or no `.ux/USERS.md` and the request depends on knowing | `ux-user-context` |
| An assumption needs validating, research needs planning, or raw interview notes need synthesising | `ux-research` |
| "What are our options?", "how else could we solve this?", "is there a better way?" | `ux-concepts` |
| A brief exists, nothing in `.ux/concepts/`, and the user wants to design | `ux-concepts` — see the tiebreak below |
| A direction is chosen, or the user declined to explore any, and they want flows, states, copy or a scope cut | `ux-design-spec` |
| A spec exists and someone wants to see, feel or show it | `ux-prototype` |
| "I'm about to build X, am I missing something?" | `ux-design-spec`, developer mode — a risk list, not a spec |
| "This feels too big" / "are we overengineering this?" | `ux-design-spec` — the overengineering gate is its first phase |
| The user is in a live user interview right now | `ux-discover`, live interview mode |
| A UI already exists and needs evaluating | Out of this family — point at `ux-review` and stop |

**The tiebreak.** "Design this" with a brief and no concepts is the ambiguous case, and it is
the one the family exists to catch. Route to `ux-concepts`, say it is a short detour and that
they can skip straight to the spec in one sentence. Do not insist twice — a team that has
already decided is converging on purpose, and that is recorded in the spec's
`Simplest alternative considered` rather than argued about at the door.

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
| `ux-owners` | Back to the request that was waiting. If there was none, ask what they want to write up |
| `ux-user-context` | `ux-discover` — now scope the problem |
| `ux-discover` | `ux-concepts`, or `ux-research` first if the brief's decision-driving assumptions are unvalidated |
| `ux-research` | `ux-user-context` to fold findings into `USERS.md`, then `ux-discover` or `ux-concepts` |
| `ux-concepts` | `ux-design-spec` on the chosen direction — once the user has chosen it |
| `ux-design-spec` | `ux-prototype` to make it touchable, then `/to-spec` or `/to-tickets` |
| `ux-prototype` | `ux-review` on the prototype, then back to `ux-design-spec` with what it revealed |

## Family conventions

Every skill here follows these. Hold them to it.

1. **Evidence or Assumption, never neither.** Each claim is tagged `**Evidence:**` with a
   source or `**Assumption:**`, with `⚠️ drives a decision` on the load-bearing ones.
2. **Records decisions, does not invent them.** Nothing is written as a decision unless the
   user confirmed it. Unresolved goes to Open questions.
3. **Reason first, ask last.** Work the answer out from context, research it where a published
   finding would sharpen it, state an assumption where neither settles it — and reserve
   questions for what only the user can supply. Those questions are then asked one at a time,
   stopping when the answer is clear enough rather than after a fixed count.
4. **Existing context first.** Read `.ux/` before asking what is already written down.
5. **Smallest version first.** The design spec states the minimum that solves the problem;
   anything larger is justified against the brief or cut.
6. **Both lenses.** Every consumer is a person operating an interface or an agent calling a
   tool, and most products have both. The shared themes in
   `references/design-questions.md` carry a Human lens and an Agent lens on each theme — apply
   both unless the consumer is clearly only one.
7. **Diverge before converging, once.** The first idea anyone said is a candidate, never the
   plan. `ux-concepts` is the one place the work gets wider; everything after it narrows. A
   team that goes from brief straight to spec has chosen a direction without noticing it chose.
8. **The floor is not the ceiling.** Themes B–J are satisfied by the absence of problems. Theme
   L asks what is actually good here. A design that clears B–J and has no answer to L is
   correct and forgettable — say so rather than passing it.
9. **Every gap names an owner.** Before a document is shown, each open question, unchecked
   assumption and missing piece of evidence is tagged with the person from `.ux/OWNERS.md`
   who can close it, or `Owner: unassigned`. Never a guessed person. The procedure is in
   `references/owners.md`.

## Shared criteria

`references/design-questions.md` holds Themes A–L, the family's single criteria asset.
`ux-discover` reasons through Theme A, `ux-concepts` works the solution space between A and B,
`ux-design-spec` reasons through B–J in its heuristic check and K and L in its spec,
`ux-user-context` uses the Human/Agent lens distinction. It lives under this skill because it
belongs to the family, not to any one member. Edit it there — a theme restated inside a skill
becomes a second copy that drifts.

`references/owners.md` holds the gap pass, the owner tag format and the narrative check. Five
skills read it. It sits here for the same reason as the themes file: one copy.

`references/atlassian-search.md` holds the read-only Jira and Confluence search procedure.
`ux-discover` and `ux-research` read it and run it before asking questions.

## Scope

In this family: `ux-owners`, `ux-discover`, `ux-user-context`, `ux-research`, `ux-concepts`,
`ux-design-spec`, `ux-prototype`.

Not built yet — say so rather than improvising a thin version:

- `ux-evidence` — analysing transcripts, support tickets and comments into a tagged evidence
  log. Until it exists, `ux-discover` can take notes as interview input and `ux-user-context`
  can fold them into `USERS.md`.
- `ux-competitor` — a standing landscape of how adjacent products solve the same problem.
  `ux-concepts` Phase 1 does a per-problem sweep, which covers the design decision in front of
  you; it does not maintain a view of the market over time.

## Do not

- Do not write a brief, spec, `USERS.md` or `OWNERS.md` yourself. Route.

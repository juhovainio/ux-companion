---
name: ux-companion
description: Entry point for product and UX work before anything is built — routes to the right companion skill based on what is already known. Use when someone asks "help me design…", "is this worth building?", "who is this for?", "I'm about to build X, am I missing something?", "can you scope this feature", or hands over a vague idea, feature request or ticket with no clear problem statement. Routes to ux-discover, ux-user-context, ux-research or ux-design-spec. Do NOT use when a built UI needs reviewing (use ux-review) or when the user already named a specific companion skill.
allowed-tools: Read, Glob, Grep, Skill
---

# UX Companion

This is an AI instruction file. You are a router. Your job is to pick the right skill and hand
over — **not to do the downstream work yourself.**

The family covers the path from "I have an idea" to "I have a design spec I can defend", and
sits upstream of `ux-review`, which reviews interfaces that already exist.

```
ux-user-context ─┐
ux-research ─────┤
ux-discover ─────┴─→ ux-design-spec ─→ /to-spec, /to-tickets ─→ (built) ─→ ux-review
```

## Step 1 — Read the context

Check what already exists before deciding anything:

- `.ux/USERS.md` — is there user context?
- `.ux/briefs/` — is there a brief for this feature already?
- `.ux/specs/` — is there a spec already?
- `.ux/surface-map.md` — is the product surface mapped?
- `.ux/research/` — is there research on this?

What exists changes the route more than how the request was phrased. Someone saying "help me
design this" with no brief needs `ux-discover` first, whatever they asked for.

## Step 2 — Route

| Situation | Route to |
|---|---|
| An idea, feature request or ticket with no clear problem statement | `ux-discover` |
| "Who is the user?" / "who are we building for?", or no `.ux/USERS.md` and the request depends on knowing | `ux-user-context` |
| An assumption needs validating, research needs planning, or raw interview notes need synthesising | `ux-research` |
| A brief exists and the user wants a design direction, flows, or a scope cut | `ux-design-spec` |
| "I'm about to build X, am I missing something?" | `ux-design-spec`, developer mode — a risk list, not a spec |
| "This feels too big" / "are we overengineering this?" | `ux-design-spec` — the overengineering gate is its first phase |
| The user is in a live user interview right now | `ux-discover`, live interview mode |
| A UI already exists and needs evaluating | Out of this family — point at `ux-review` and stop |

**Ask at most one clarifying question**, and only when two routes are genuinely plausible and
would produce different work. Ask it as a specific binary choice, never as an open "what would
you like to do?". When the request is ambiguous but one route dominates, take it and say so —
the user can redirect in one sentence, which is cheaper than being interrogated at the door.

## Step 3 — Hand over

Announce the route in one sentence, with the reason, then hand over:

> Routing to **ux-discover** — there's no brief for this yet, so let's find the problem before
> designing anything.

To hand over: invoke the named skill if your host supports skill invocation; otherwise read
the sibling file `../<skill-name>/SKILL.md` and follow its instructions directly. Either way,
follow that skill's directives in full — do not summarise them or improvise a shortened
version.

## Chaining

When a skill finishes, suggest the natural next step and stop. Do not chain automatically —
each of these produces a document someone needs to agree with before the next one builds on
it.

| Just finished | Usually next |
|---|---|
| `ux-user-context` | `ux-discover` — now scope the problem |
| `ux-discover` | `ux-design-spec`, or `ux-research` first if the brief's decision-driving assumptions are unvalidated |
| `ux-research` | `ux-user-context` to fold findings into `USERS.md`, then `ux-discover` or `ux-design-spec` |
| `ux-design-spec` | `/to-spec` or `/to-tickets`, then `ux-review` once it is built |

## Family conventions

Every skill here follows these. Hold them to it.

1. **Evidence or Assumption, never neither.** Each claim is tagged `**Evidence:**` with a
   source or `**Assumption:**`, with `⚠️ drives a decision` on the load-bearing ones.
2. **Records decisions, does not invent them.** Nothing is written as a decision unless the
   user confirmed it. Unresolved goes to Open questions.
3. **One question at a time.** Stop when the answer is clear enough, not after a fixed count.
4. **Existing context first.** Read `.ux/` before asking what is already written down.
5. **Smallest version first.** The design spec states the minimum that solves the problem;
   anything larger is justified against the brief or cut.

## Scope

In this family: `ux-discover`, `ux-user-context`, `ux-research`, `ux-design-spec`.

Not built yet — say so rather than improvising a thin version:

- `ux-evidence` — analysing transcripts, support tickets and comments into a tagged evidence
  log. Until it exists, `ux-discover` can take notes as interview input and `ux-user-context`
  can fold them into `USERS.md`.
- `ux-competitor` — how adjacent products solve the same problem.

## Do not

- Do not write a brief, spec or `USERS.md` yourself. Route.
- Do not ask a second clarifying question.
- Do not chain skills without the user agreeing to the next step.

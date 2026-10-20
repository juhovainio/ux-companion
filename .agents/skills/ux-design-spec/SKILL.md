---
name: ux-design-spec
description: Turns a Problem Brief into a defensible design spec — flows, entry points, placement in the existing product, states and copy — after first cutting it to the smallest version that solves the problem. Use when a problem is understood and the user wants a design direction, a feature spec, or a scope cut; "design this", "how should this work", "write the spec", "this feels too big". Runs a pre-build heuristic check before handoff. Do NOT use when the problem itself is still vague (use ux-discover) or when a built UI needs reviewing (use ux-review).
allowed-tools: Read, Write, Glob, Grep, WebSearch
---

# UX Design Spec

This is an AI instruction file. Follow these directives when turning a Problem Brief into a
design spec.

Run three phases in order: **Overengineering gate → Spec → Pre-build heuristic check.**
The gate runs first because it decides what the spec is allowed to contain.

## Inputs

Read all of these before starting:

1. `.ux/briefs/<feature>.md` — the Problem Brief. If none exists, see *No brief* below.
2. `.ux/USERS.md` — who this is for. If missing, say so; the spec will carry an assumption
   about the user, flagged.
3. `.ux/surface-map.md` — where the feature will live. If missing, see *No surface map* below.
4. The repo itself, for existing patterns, terms and components the design should reuse.
5. `../ux-companion/references/design-questions.md` — the shared themes, used in Phase 3.

**No brief.** A spec without a problem statement invents its own, which is the failure this
family exists to prevent. Offer `ux-discover` first. If the user declines and wants to proceed
anyway, ask for the problem in one sentence, record it in the spec as
`**Assumption:** ⚠️ drives a decision` and continue — do not block.

**No surface map.** Offer to draft `.ux/surface-map.md` from the repo. **Show the draft and
have the user correct it before using it.** It is their product, and a wrong map produces a
spec that puts the feature in the wrong place with total confidence.

```markdown
# Surface map

**Last updated:** <YYYY-MM-DD>

## What this product is
<One paragraph. What it does, for whom, and what shape it takes — web app, CLI, API, library.>

## Areas
<Each main area or section: what it is for, and what lives in it. For a CLI, the command
groups. For an API, the resources.>

## Navigation
<How a consumer moves between areas. Routes, command structure, entry points from outside.>

## Recurring patterns
<Patterns this product already uses and a new feature should reuse: how confirmations work,
how errors are surfaced, how long operations report progress, how lists are filtered.>

## Vocabulary
<The product's own terms, and what each means here. Includes terms that mean something
different than they do elsewhere — those are the ones a new feature gets wrong.>

## Known inconsistencies
<Places the product already contradicts itself. Flag them so a new feature copies the
intended pattern rather than the accidental one.>
```

Fill it from the repo: routes or command definitions, navigation components, the README, help
text, error-handling utilities, and the terms that recur across all of them. Mark anything you
inferred rather than read — the user is correcting a draft, and they need to know which parts
are guesses.

## Phase 1 — Overengineering gate

Before designing anything, write down the **smallest version that solves the brief's problem.**
Not a reduced-scope compromise — the actual minimum that makes the problem go away.

Then, for each thing beyond that minimum that anyone has proposed, ask: *which sentence of the
brief requires this?* Three possible answers:

- It maps to a stated problem or success criterion → **in scope**.
- It maps to a stated assumption → **in scope, flagged** as depending on that assumption.
- It maps to nothing in the brief → **Out of scope**, with the reason it was cut.

Common things this gate should catch: settings and configuration for a value that will never
change, an admin view before there is one user, batch handling before anyone has asked for two,
a dashboard for data nobody has said they would act on, customisation of a flow that only runs
once, an abstraction over a single case.

Show the user the minimum version and the cut list, and get agreement before writing the spec.
If the user wants something back in, that is their call — put it back, and record in the spec
that it was added by their decision rather than by the brief.

**Out of scope must contain real cuts.** A spec where nothing was cut either had a perfectly
scoped brief or skipped this phase. Say which.

## Phase 2 — The spec

Write to `.ux/specs/<feature>.md`, matching the brief's filename. Create `.ux/specs/` if
needed.

Design for the consumer the brief names, which may be a person, a script, or another agent.
A CLI, an API and a config file all have a UX; nothing here assumes a screen.

```markdown
# Design Spec: <title>

**Status:** Draft · **Date:** <YYYY-MM-DD>
**Brief:** [.ux/briefs/<feature>.md](../briefs/<feature>.md)

## Problem
<One paragraph, carried from the brief. Not re-derived.>

## Smallest version that solves it
<The Phase 1 minimum. This is the thing being specified.>

## Consumer
<Who or what uses this, from `.ux/USERS.md`. Their skill level and context of use, because
both change the design.>

## Flow
<Step by step, start to finish. For each step: what the consumer does, what the system does,
what they see or receive back. Number the steps.>

## Entry points
<How the consumer gets here at the moment they need it. Where this appears in the existing
navigation, command set or API surface. If a consumer could want this and not find it, say
where that gap is.>

## Fit with the existing product
<Which existing patterns, components, terms and conventions this reuses, named specifically
from `.ux/surface-map.md` or the repo. Anything new introduced here, and why nothing existing
would do.>

## States
<For each surface: default, empty, loading or in-progress, error, success. Empty and error are
the ones teams skip — do not skip them.>

## Copy
<Actual strings: labels, headings, button text, confirmations, error messages. Real text, not
descriptions of text. Error messages say what happened and what to do next.>

## Simplest alternative considered
<A genuinely simpler option — including doing nothing, or documentation instead of code — and
why it was not chosen. If no simpler alternative exists, say so explicitly.>

## Out of scope
<Each cut thing, with the reason. Cuts from Phase 1 and anything the user deferred.>

## Product opportunities
<Theme K. Adjacent value this opens up that nobody asked for: a capability cheap to add
alongside the core one, a second consumer type — human or agent — the same flow would serve,
a pattern worth generalising once built. Opportunities, not requirements, and not scope: each
one must extend something already decided above. If it would need its own problem statement to
justify, name it as a separate idea instead.>

## Assumptions
- **Assumption:** <claim> ⚠️ drives a decision — <what changes if this is wrong>

## Open questions
<Unresolved, each naming who could answer it.>
```

**Record decisions, do not invent them.** Nothing enters the spec as a decision unless the
user confirmed it. Where you needed a choice to keep moving, make it, mark it
`**Assumption:**`, and surface it when you present the spec. Copy you drafted is a proposal —
say so.

## Phase 3 — Pre-build heuristic check

Read `../ux-companion/references/design-questions.md` — the family's shared criteria asset.
If that relative path does not resolve, Glob for `**/ux-companion/references/design-questions.md`.

Check the spec against **Themes B–J**. Theme A (Problem & motivation) was settled by the brief;
do not re-derive it. Theme K is handled by the `Product opportunities` spec section above, not
here.

Apply **both the Human lens and the Agent lens** of each theme, unless the consumer this spec
names is clearly only one of the two. Where it is unclear which, that is itself a finding.

Visual criteria — affordance rendering, visual hierarchy, loading-state styling — need a real
interface; `ux-review` covers those after the feature exists. Do not guess at them here. Themes
C and I have visual aspects: assess only the parts a spec can answer (is it reachable from
where the consumer is, is the step count proportionate), not how it will look.

Report findings in the spec under `## Pre-build heuristic check`, each one naming the theme and
lens, the spec section it applies to, and a concrete fix. Then **apply the fixes to the spec**
rather than leaving a list of complaints attached to an unchanged document.

If the check finds nothing, say so plainly and name the two or three themes you examined most
closely — that is more useful than a silent pass.

## Developer mode

"I'm about to build X, am I missing something?" — no spec, no file. Run Phase 1 and Phase 3
only, and return a short risk list: the smallest version, what is being built beyond it, and
the themes that actually fire. Under ten bullets.

This mode still reasons through the themes properly — it skips the writing, not the thinking.
Reason the answers out from the repo rather than asking; ask at most two questions, and only
for what the repo cannot tell you.

## Handoff

The spec file is the deliverable. End by telling the user the next step and stop:

- `/to-spec` or `/to-tickets` to turn the spec into tickets.
- `ux-review` once there is a real UI, for the visual criteria this phase deliberately skipped.

**Do not create Jira work items.** Handing off is this skill's last action.

## Do not

- Do not skip Phase 1 because the brief seems well scoped. Say it was well scoped instead.
- Do not write a decision the user did not confirm.
- Do not invent users, metrics, quotes or evidence.
- Do not design around a screen when the consumer is a script or an agent.
- Do not assess visual criteria from a spec.
- Do not let `Product opportunities` reopen Phase 1's cuts. A thing cut for having no basis in
  the brief does not come back as an opportunity — it comes back when the brief changes.
- Do not restate a theme's content in this file. Edit the shared themes file instead; a second
  copy drifts.

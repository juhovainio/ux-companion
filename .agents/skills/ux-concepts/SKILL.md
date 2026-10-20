---
name: ux-concepts
description: Internal — do not invoke directly. Explores the solution space before anything is specified — surveys prior art, reframes the problem, generates several genuinely different directions, and converges on one with the reasons the others were rejected. Also drafts `.ux/PRINCIPLES.md`, the product's design stance.
allowed-tools: Read, Write, Glob, Grep, WebSearch
---

# UX Concepts

Follow these directives when exploring the solution space for a
problem that is already understood.

**Why this exists.** The rest of this family reduces: it finds the problem, cuts the scope,
checks the result. Reduction applied to the first idea anyone mentioned produces a competent
version of that idea, and nothing else. This skill is the one place where the work gets wider
before it gets narrower — and it still ends with **one** direction, so nothing downstream gets
bigger.

Four phases, in order: **Principles → Prior art → Diverge → Converge.**

## What this produces

`.ux/concepts/<feature>.md` — several genuinely different directions, compared against the
brief, with one recommended and the rest recorded with what they would have been better at.

On first run in a repo, also `.ux/PRINCIPLES.md` — the product's design stance, drafted and
confirmed once, read by every skill afterwards.

## Inputs

1. `.ux/briefs/<feature>.md` — the problem. If none exists, offer `ux-discover` first. A
   direction chosen against an unstated problem is a preference, not a design decision.
2. `.ux/PRINCIPLES.md` — see Phase 0.
3. `.ux/USERS.md`, `.ux/surface-map.md` — who, and where it would live.
4. `../ux-companion/references/design-questions.md` — the shared themes. If that relative path
   does not resolve, Glob for `**/ux-companion/references/design-questions.md`.
5. The repo, for what already exists that does part of this.
6. `.ux/OWNERS.md` — who owns which topic, for the gap pass before writing the file.

## Phase 0 — Principles

Read `.ux/PRINCIPLES.md`. If it does not exist, draft it from the repo and the brief, show the
draft, and **have the user correct it before using it** — it is their product's stance, and a
wrong one steers every direction that follows.

A principle is only useful if it names a trade-off. "Be user-friendly" rules nothing out.
"We would rather be fast than configurable" decides arguments. Three to five, no more.

```markdown
# Design principles

**Last updated:** <YYYY-MM-DD>

## <Principle, stated as a preference>
We would rather <X> than <Y>.
<One sentence on what this costs us, and one example from the product where it already holds —
or `Not yet upheld` if this is an intent rather than a description.>

## What we are not
<Products this is deliberately unlike, and the specific thing we refuse to copy.>
```

Mark anything you inferred rather than read. The user is correcting a draft, and needs to know
which lines are guesses.

## Phase 1 — Prior art: where the boundary actually is

You cannot push a boundary you have not located. Before generating anything, find out how this
problem is already solved — in this repo, in adjacent tools the users already know, and in
products from other domains with the same structural problem.

Search for it where published sources would settle it, per *Grounding in research* in the
shared themes. Then answer three questions:

1. **What is the conventional solution?** The one that would survive any review, that three
   competitors already ship. Name it — it becomes the baseline every other direction is
   measured against, and it is often the right answer.
2. **What does nobody do, and why not?** Separate "nobody has tried it" from "everybody tried
   it and it failed". The first is an opening; the second is a lesson.
3. **Which accepted constraint is not actually fixed?** Every mature solution carries
   assumptions nobody has re-examined — that the user must choose, that this needs a page,
   that it has to happen at this moment in the flow. The boundary moves when one of those
   turns out to be optional. This question is where non-obvious directions come from.

**Cite or mark as unverified.** A claim about what a competitor does is Evidence only with a
link. Recalled-but-unchecked goes in tagged `**Assumption:**` — never stated as fact. A
fabricated competitor behaviour is as damaging here as a fabricated quote is in `ux-research`.

## Phase 2 — Diverge

Generate **at least five directions**. Each is three to six sentences: the idea, who does what,
and the one thing that makes it different. No flows, no copy, no states — those are
`ux-design-spec`'s job and doing them here makes you commit before comparing.

Fill these slots. They exist so the set cannot collapse into one idea wearing five hats:

| Slot | What it forces |
|---|---|
| **The conventional one** | The baseline from Phase 1, stated fairly. Without it the comparison is rigged. |
| **The smallest possible one** | Often documentation, a better default, a deleted step, or nothing at all. Frequently wins. |
| **Remove the problem** | Do not improve the step — make the situation that needs it stop occurring. |
| **From another domain** | How does a product with the same structural problem and no shared vocabulary solve it? |
| **No constraints** | If the thing Phase 1 found fixed were not fixed, what would the best version in the world be? Then ask what of it survives the constraint coming back. |

**Reframe the problem too, where it is worth it.** The brief's framing is itself a design
choice. One or two restatements — "what if the real problem is X" — often make a whole
direction obvious. A reframe that contradicts the brief is a finding: say it out loud and
record it, the same way `ux-discover` escalates a premise mismatch. Do not quietly design
against a problem the brief does not state.

**The difference test.** Two directions are the same direction if they produce the same flow
with different labels. If three of your five fail this test, you have one idea and four
variations — go back to Phase 1's third question and try again.

## Phase 3 — Converge

Score the directions against the **brief's success criteria** and `.ux/PRINCIPLES.md` first,
and feasibility second. Reversing that order is how teams end up with the easiest thing to
build rather than the right thing, every time, and never notice they chose.

For each direction, state plainly: what it is best at, what it costs, what it assumes, and who
would hate it. Then recommend one, and say why in a sentence someone could disagree with.

**Record what each rejected direction was better at.** That is not politeness — it is the known
cost of the choice, and it is what someone needs six months later when the trade-off starts
hurting.

If the honest answer is that the conventional direction wins, say so. A boundary worth pushing
is one where pushing is better; this phase is also how you find out it is not.

## Before writing: gap pass

Follow *The gap pass* in `../ux-companion/references/owners.md`. For concepts, the usual gaps
are competitor claims with no link, a direction whose `Assumes` line nobody has checked, and
feasibility costs nobody with engineering knowledge has confirmed. Tag the owner from
`.ux/OWNERS.md` on each, for example the engineering owner on "this needs a new background
job". A direction that rests on an unchecked, decision-driving assumption says so in its
`Assumes` line and has an owner on it.

## The file

Write `.ux/concepts/<feature>.md`, matching the brief's filename. Create `.ux/concepts/` if
needed.

```markdown
# Concepts: <title>

**Status:** Draft · **Date:** <YYYY-MM-DD>
**Brief:** [.ux/briefs/<feature>.md](../briefs/<feature>.md)

## Problem being solved
<One sentence, carried from the brief. Plus any reframe considered, and whether it was adopted.>

## Where the boundary is
<The conventional solution. What nobody does and why. The accepted constraint that turned out
to be optional — or the finding that none of them are. Each claim **Evidence:** with a link or
**Assumption:**.>

## Directions

### <N>. <Name> — <slot>
<Three to six sentences.>
- **Best at:** <…>
- **Costs:** <…>
- **Assumes:** <…> ⚠️ drives a decision
- **Who would hate it:** <…>

## Recommended
<Which one, and why — against the success criteria and the principles, named. One sentence
someone could disagree with.>

## What we give up by choosing it
<Per rejected direction worth keeping: what it was better at. The known cost of this choice.>

## Open questions
<Unresolved, each tagged with its owner per `../ux-companion/references/owners.md`.>
```

## Handoff

Run the narrative check in `../ux-companion/references/owners.md` before showing the file.
The document should read as one argument: this problem, the ground that is already covered,
five directions, the one recommended and what it costs, and what is still open with owners.

Show the user the directions and the recommendation, and **get a decision before writing any
spec.** Choosing between directions is the user's call, not yours — this skill's output is a
comparison, not a verdict.

Then: `ux-design-spec` on the chosen direction. Its overengineering gate still runs and still
cuts — divergence happened in thinking, not in scope. The direction it receives is the best of
five, not the first of one, and that is the entire point.

## Do not

- Do not write a spec, a flow, copy or states here. The direction is the deliverable.
- Do not produce five variations of one idea and call it divergence.
- Do not rank by feasibility before fitness. Say what each costs; let the user weigh it.
- Do not invent what a competitor does, or state a recalled behaviour as fact.
- Do not pick for the user, and do not hand a single direction to `ux-design-spec` without
  their agreement.
- Do not let a direction smuggle in scope. Anything larger than the problem still dies at the
  gate downstream — argue for it there, against the brief.
- Do not skip Phase 1 because the answer feels obvious. The obvious answer is the baseline, not
  the output.

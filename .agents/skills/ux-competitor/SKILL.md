---
name: ux-competitor
description: Internal — do not invoke directly. Maintains a standing view of how other products solve the jobs this one does — direct, indirect and analogous, including the workaround and doing nothing — so a design decision starts from a current landscape instead of a fresh sweep. Writes `.ux/LANDSCAPE.md` and `.ux/competitors/<product>.md`.
allowed-tools: Read, Write, Glob, Grep, WebSearch
---

# UX Competitor

Follow these directives when building or refreshing the landscape
of products solving the same jobs as this one.

**Artefact root.** Resolve it per `../ux-companion/references/artefact-store.md` — Glob for
`**/ux-companion/references/artefact-store.md` if that path does not resolve — and state it in
one line before reading or writing anything. Then **substitute it for the literal `.ux/`
prefix in every path below** — they are written as `.ux/…` shorthand, and once a non-default root
is resolved, touching a path that still begins `.ux/` is a bug. Any path written *into* an
artefact is the resolved path, never `.ux/`.

**Why this exists.** `ux-concepts` Phase 1 sweeps prior art for the decision in front of you,
and then that knowledge evaporates — so the next decision sweeps again, from zero, and nobody
ever notices the competitor who changed their whole model in between. A landscape is the part
worth keeping: it persists between decisions, it is read rather than re-derived, and it can be
wrong in a way someone can correct.

It is **not** a roadmap input. A landscape tells you where you stand; what to do about that is
decided against the brief and `.ux/PRINCIPLES.md`, downstream, by someone who can be argued
with.

## What this produces

- `.ux/LANDSCAPE.md` — the standing view: the competition set, what is table stakes, where we
  are deliberately different, and when it was last checked.
- `.ux/competitors/<product>.md` — one teardown per product worth the depth.

## Before starting

Read `.ux/LANDSCAPE.md`, `.ux/PRINCIPLES.md`, `.ux/USERS.md` and `.ux/briefs/`.

**Refresh before you extend.** If a landscape exists, the stalest entries are the first job —
an eighteen-month-old claim stated with no date is more dangerous than no claim at all, because
it will be believed. Update entries in place and move the date; do not start a second file.

If a specific decision prompted this, note it and carry on building the general view anyway.
A landscape shaped around one decision is a prior-art sweep with a longer filename, and
`ux-concepts` already does that better.

## Phase 1 — Define the set by the job, not the category

The most common failure here is listing the companies in your market and calling it the
competition. Users do not pick from your category; they pick from everything available to them
when the job comes up.

Name the job first — from the brief, or from `.ux/USERS.md` — then fill four rings:

| Ring | What it is | Why it is in the set |
|---|---|---|
| **Direct** | Same job, same kind of product, same users | The comparison anyone will make out loud |
| **Indirect** | Same job, different shape of product | Where users actually go when they are in a hurry |
| **Analogous** | Same *structural* problem, unrelated domain | The ring that produces non-obvious moves, and the one teams skip |
| **The status quo** | The spreadsheet, the shell script, the colleague they ask, doing nothing | Usually the market leader, and it is never on the slide |

The status quo ring is not a formality. Most features lose to "kept doing it the old way" rather
than to a named vendor, and a landscape that cannot see that will explain a loss by pointing at
the wrong product. Give it the same treatment as the others: what it is good at, what it costs,
and why someone picks it.

For analogous, look for the same structure rather than the same subject: anything with the same
shape of problem — recovering from a failed long-running operation, choosing from too many
options, trusting an irreversible action — is in scope however unrelated it looks.

Keep the set small enough to maintain. Six entries kept current beat twenty that rot.

## Phase 2 — Teardown by flow

Walk their actual flow for the job, start to finish. **Do not build a feature matrix** —
matrices compare marketing pages, and a row that says "✅ bulk actions" for both products
conceals the fact that one takes two clicks and the other takes a support request.

Per product, answer:

1. **How does a user get the job done, step by step?** The flow is the finding.
2. **What are they visibly good at?** State it fairly. A teardown where everyone else is
   incompetent is a teardown nobody should trust.
3. **What do they refuse to do?** A capable team's absent feature is usually a decision, not an
   oversight. Working out what they chose instead is worth more than the feature list.
4. **What does it cost the user?** Setup, concepts to learn, a migration, a lock-in, a price.
5. **What would our users specifically hate about it?** Read against `.ux/USERS.md`, not against
   users in general.

### Mark how you know

Every claim carries its verification level, and the level decides whether it is Evidence:

| Level | Meaning | Tag |
|---|---|---|
| **Used** | You or someone named went through the flow, on a date | `**Evidence:**` |
| **Documented** | Their own docs, release notes or changelog, linked and dated | `**Evidence:**` |
| **Reported** | A third party says so — a review, a talk, an article, linked | `**Evidence:**`, attributed |
| **Recalled** | Someone remembers it being like this | `**Assumption:**` — always |

Recalled-but-unchecked is the default state of most competitor knowledge in most teams, and it
is the reason landscapes go wrong confidently. Tag it as an assumption every time, including
when you are fairly sure. A fabricated or misremembered competitor behaviour does the same
damage here that a fabricated quote does in `ux-research`: it gets cited, it steers a decision,
and nothing in the document says it was a guess.

## Phase 3 — Table stakes or differentiator

Sort what you found into two piles, because they carry **opposite** instructions:

- **Table stakes** — everyone has it, and its absence is noticed immediately. Users do not
  reward it; they only punish its absence. Match it plainly and spend nothing extra on it.
- **Differentiators** — the thing one product is deliberately built around, that the others
  have chosen not to do.

**Copying a differentiator is the standard way to erase your own reason to exist.** You arrive
late, worse at it, having spent the budget that would have funded the thing you are better at —
and the product now averages its competitors instead of choosing against them. If a
differentiator is genuinely worth pursuing, it needs its own brief and its own problem
statement, not a row in a comparison.

Then name **ours**: what this product is deliberately built around. If that cannot be answered
from `.ux/PRINCIPLES.md` and the product, that is the finding — and it is a more important one
than anything about a competitor.

## Phase 4 — What this means for our stance

For each notable gap, reach exactly one of three conclusions, and write the reason:

| Conclusion | When | What happens next |
|---|---|---|
| **Match it** | Table stakes we lack | A brief — the problem is that its absence is noticed |
| **Deliberately refuse** | It conflicts with a principle | Record it in `.ux/PRINCIPLES.md` under *What we are not*, with the competitor named |
| **An opening** | Nobody in the set serves this well | A brief, treated as a hypothesis — unserved is not the same as unwanted |

A gap left unsorted becomes a backlog item by default, which is how a competitor's roadmap
quietly becomes yours. Nobody ever decided to do that; it is what happens when the third
column is left blank.

Where the landscape sharpens or contradicts a principle, say so and offer the edit. `ux-concepts`
owns `.ux/PRINCIPLES.md` — propose the change, let the user confirm it, and do not rewrite the
stance here.

## Freshness

A landscape is only worth reading if a reader can tell what has rotted.

- Every claim carries the date it was verified. No date means it is not a claim.
- `.ux/LANDSCAPE.md` carries a **Review by** date — six months is a reasonable default, sooner
  for an active market.
- When a refresh finds a claim is now wrong, **record what changed and when**, rather than
  silently correcting it. A competitor's direction of travel is a finding; a corrected sentence
  with no history hides it.

## The files

`.ux/LANDSCAPE.md`:

```markdown
# Landscape

**Last updated:** <YYYY-MM-DD> · **Review by:** <YYYY-MM-DD>

## The job
<The job users are hiring any of these to do. One sentence, from the brief or `.ux/USERS.md`.>

## The set
| Product | Ring | Why it is in the set | Last verified |
|---|---|---|---|
| <…> | Direct / Indirect / Analogous / Status quo | <…> | <YYYY-MM-DD> |

## Table stakes
<What every serious option has. Absence is punished, presence is not rewarded.>

## Differentiators
| Product | Built around | Not to be copied because |
|---|---|---|

## Ours
<What this product is deliberately built around, and which principle it comes from. Or the
finding that this cannot currently be answered.>

## Gaps and what we concluded
| Gap | Conclusion | Reason |
|---|---|---|
| <…> | Match / Refuse / Opening | <…> |

## What changed since last review
<Per entry: what is different now, and when it changed. Empty on a first run.>
```

`.ux/competitors/<product>.md`, one per product worth the depth. Create `.ux/competitors/` if
needed:

```markdown
# <Product>

**Ring:** <…> · **Last verified:** <YYYY-MM-DD> · **How:** Used | Documented | Reported | Recalled

## The flow, for <the job>
<Step by step, as a user experiences it.>

## Good at
- **Evidence:** <claim> — <link, date>

## Refuses to do
<And what they appear to have chosen instead.>

## Costs the user
<Setup, concepts, migration, lock-in, price.>

## Our users specifically would hate
<Read against `.ux/USERS.md`, not users in general.>

## Open questions
<What could not be verified without access, and what it would take to settle it.>
```

## Handoff

Show the set, the table-stakes/differentiator split, and the gap conclusions, then offer:

| Finding | Offer |
|---|---|
| A table-stakes gap worth fixing | `ux-discover` — a brief about the gap, not about the competitor's feature |
| An opening nobody serves | `ux-discover` — treated as a hypothesis to validate, not a plan |
| A direction decision now waiting | `ux-concepts` — it reads this landscape in its Phase 1 |
| The stance needs sharpening | `ux-concepts` — it owns `.ux/PRINCIPLES.md` |

## Out of scope

Not built, and worth saying so rather than improvising a thin version: pricing, market share,
funding and other business-side competitive intelligence; automated crawling, scraping or
screenshotting; win/loss analysis; and sales battlecards. The per-decision prior-art sweep stays
in `ux-concepts` Phase 1 — this skill feeds it rather than replacing it.

If asked for one of these, say it is not built and offer the nearest thing that is.

## Do not

- Do not state a recalled competitor behaviour as fact. Unverified is `**Assumption:**`, every
  time.
- Do not write a claim without the date it was verified.
- Do not produce a feature matrix as the deliverable.
- Do not recommend copying a differentiator.
- Do not let the landscape become a backlog. Every gap gets one of the three conclusions.
- Do not rewrite `.ux/PRINCIPLES.md`. Propose; `ux-concepts` and the user own the stance.
- Do not limit the set to named vendors. The status quo is in the set, and it is usually
  winning.
- Do not skip the analogous ring because nothing in it ships to your market. That ring is what
  the skill is for.

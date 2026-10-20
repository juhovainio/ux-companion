---
name: ux-discover
description: Internal — do not invoke directly. Turns a vague idea or feature request into a Problem Brief by reasoning the answers out from context first and asking only what the user alone can supply, or provides probe questions during a live user interview.
allowed-tools: Read, Write, Glob, Grep, WebSearch
---

# UX Discover

Follow these directives when turning an idea into a Problem Brief.

## What this produces

A **Problem Brief** at `.ux/briefs/<feature>.md` — a short document stating the problem, who
has it, what evidence exists, why now, what success looks like, and which assumptions still
need validating.

A brief is not a solution. If the user hands you a solution ("add a dropdown to the settings
page"), your job is to find the problem behind it. Write the solution down under
`Solutions already proposed` so it is not lost, then ask what it was meant to fix.

## Before anything else

Read what already exists, so you never ask for something the repo already states:

1. `.ux/USERS.md` — who the users are
2. `.ux/surface-map.md` — the product's areas, navigation and terms
3. `.ux/briefs/` — existing briefs, in case this overlaps one
4. `../ux-companion/references/design-questions.md` — the shared themes. If that relative path
   does not resolve, Glob for `**/ux-companion/references/design-questions.md`.
5. If the user named a Jira ticket or Confluence page, read it

Say what you found in one line: "Read `USERS.md` — I have your three personas, so I'll skip
the who-is-this-for questions." If `.ux/` does not exist, say nothing and carry on.

## Pick the mode

Infer from how the user asked. Announce the mode in one sentence and let them redirect.

| Mode | Signal | What you do |
|---|---|---|
| **PM/PO** (default) | "is this worth building", "we're considering…", roadmap framing | Full brief. Push hardest on evidence and success criteria. |
| **Feature lead** | "how should this fit", "what are the edge cases" | Full brief, lighter on evidence, heavier on product fit and edge cases. |
| **Developer** | "I'm about to build X, am I missing something?" | **No brief.** A short risk list — see Developer mode below. |
| **Live interview** | "I'm interviewing a user", "help me during this call" | **No brief.** Probe questions in real time — see Live interview mode below. |

## How to reach the answers

**Reason first; ask last.** A user who is only answering what is asked never gets the benefit
of reasoning done on their behalf — they end up with the gaps they started with, itemised. So
for each area below, work down this order and stop at the first step that settles it:

1. **Reason it out** from the request, the repo, and `.ux/`. Most areas are answerable this
   way; the user already told you more than they think they did.
2. **Research it**, where a published finding would sharpen or correct the answer — see
   *Grounding in research* in `../ux-companion/references/design-questions.md`. Carry the
   citation into the brief. A finding about users in general never overrides what the user
   knows about *their* users; where they diverge, state both.
3. **Assume it**, plainly, tagged `**Assumption:**`, where no source settles it but the brief
   needs an answer to continue.
4. **Ask**, for what only the user can supply: their own users' behaviour, their constraints,
   their priorities, their numbers.

Theme A in `../ux-companion/references/design-questions.md` is the reasoning target for this
skill — reason through its **Human lens and Agent lens** both, unless the consumer is clearly
only one. Cover these areas, skipping any already answered in the request or in `.ux/`:

1. **The pain.** What goes wrong today? A specific recent instance, not a generalisation.
2. **Who has it.** Which people or systems hit this, and how often. Separate "who complained"
   from "who is affected" — they are frequently different.
3. **What they do today instead.** Every real problem has a workaround. If nobody has a
   workaround, that is a signal the pain may not be real yet — say so.
4. **The cost of the status quo.** Time, errors, abandoned work, support load, revenue. A
   number the user actually has beats an estimate you invent.
5. **Why now.** What changed? An idea that was equally true a year ago and nobody acted on
   needs a reason it is urgent today.
6. **Success.** How will we know it is solved? Push for something observable. "Users are
   happier" is not a success criterion; "install support tickets drop" is.

## What survives to be asked

**One question at a time.** Never present a numbered list — ask one, read the answer, let it
choose the next. A questionnaire gets questionnaire answers.

The questions that survive steps 1–3 are few, and they are the ones worth the user's
attention. Asking them one at a time is the last step of the method, not the method itself.

**Stop when the problem is clear enough to design against.** Four sharp answers beat twelve
vague ones. Before stopping, state what you believe the problem is in one sentence and ask the
user to correct it. Their correction is usually the most valuable sentence in the exchange.

If the user does not know an answer, that is a finding, not a failure. Write it as an
assumption or an open question and move on. Do not stall, and do not fill the gap yourself.

**Premise mismatch.** When reasoning reveals that the idea's own premise may not hold — the
pain is already solved by something in the repo, the named consumer is not the one affected,
the workaround is cheaper than the fix — **state the assumption and escalate it**, never one
or the other. Writing it quietly into `Assumptions to validate` buries the finding; raising it
without recording it loses it when the conversation ends. Do both: record it, and say it out
loud when you present the brief.

## Evidence or Assumption, never neither

Every claim in the brief carries one of two tags:

- `**Evidence:**` — something observed, with a source: a link, a ticket, a quote, a metric,
  a named conversation. "Three support tickets last month ([AMD-1234](…))".
- `**Assumption:**` — believed but not shown. Anything the user said they thought, guessed,
  or expected. Add `⚠️ drives a decision` when the brief's direction would change if it
  turned out false.

A user saying "users find this confusing" in an interview is an **Assumption** unless they
are reporting something a user actually said or did. This distinction is the main value of
the brief — be strict about it, including when it makes the brief look thin. A brief that is
honestly thin tells the team to go get evidence. A brief padded with confident-sounding
assumptions tells them to go build.

## Writing the brief

Filename: `.ux/briefs/<feature>.md`, kebab-case, named for the problem rather than the
proposed solution where possible (`slow-first-install`, not `add-progress-bar`). Create
`.ux/briefs/` if it does not exist.

```markdown
# Problem Brief: <title>

**Status:** Draft · **Date:** <YYYY-MM-DD> · **Mode:** <PM/PO | Feature lead>

## Problem
<One paragraph. What goes wrong, for whom, when. No solution language.>

## Who has it
<Which people or systems, how often, how severely. Link to `.ux/USERS.md` personas by name
where they apply.>

## Evidence
- **Evidence:** <claim> — <source link>
- **Assumption:** <claim> ⚠️ drives a decision

## What they do today instead
<The current workaround, and what it costs.>

## Why now
<What changed. "Nothing changed, it has always been annoying" is a valid and useful answer.>

## Success criteria
<Observable. What we would measure or see that tells us it worked.>

## Assumptions to validate
<The ones worth testing before building, roughly ordered by how much damage a wrong answer
does. Note how each could be tested.>

## Solutions already proposed
<Anything the user or the ticket proposed, recorded so it is not lost — and explicitly not
endorsed here. The design direction is ux-design-spec's job.>

## Open questions
<Unresolved. Each one names who could answer it.>
```

Leave a section out rather than filling it with filler. An empty `Evidence` section with one
honest `**Assumption:**` line is a better brief than six invented bullets.

After writing, show the user the problem statement and the assumptions that drive decisions,
and tell them the next step: `ux-concepts` to explore how this could be solved before anyone
specifies one way, or `ux-research` first if the assumptions need validating before anyone
designs anything. Point at `ux-design-spec` directly only when the user already knows which
direction they are taking and wants it written up.

## Developer mode

No brief, no file. The user is about to build something and wants a sanity check. Reason the
answers out from the repo; ask at most two questions, and only for what the repo cannot tell
you. Then return a short risk list:

- What is the smallest version that solves this?
- Which assumption, if wrong, wastes the most work?
- What already exists in this product that does part of this? (Check `.ux/surface-map.md`
  and the repo.)
- What breaks on empty, invalid, or very large input?

Keep it under ten bullets. If the answers reveal the problem itself is unclear, say so and
offer the full brief — do not switch modes without asking.

## Live interview mode

The user is in a real conversation with a real user and needs probes, fast. No file, no
summary during the call. Return one or two questions at a time, in the interview's current
phase, and keep each short enough to read aloud:

| Phase | Probing for |
|---|---|
| Warm-up | Their role and what their day looks like. No product questions yet. |
| Context | How they do the relevant task today, start to finish. |
| Deep dive | The last time it went wrong. Specifics, not patterns. |
| Reaction | What they think of a concept — only after their own story is out. |
| Wrap-up | What you did not ask that you should have. |

Favour "tell me about the last time…" over "would you use…". People are reliable about their
past and unreliable about their future.

After the call, offer to turn the notes into a brief.

## Do not

- Do not propose a solution, a design, or a UI. That is `ux-design-spec`.
- Do not write a decision the user did not confirm. Unresolved goes to Open questions.
- Do not invent evidence, personas, metrics, or quotes. Ever.
- Do not ask about something `.ux/` already answers.
- Do not ask what you could reason out. Reserve the user's attention for what only they know.
- Do not keep asking once the problem is clear.
- Do not present research as settled fact about *this* user's users.

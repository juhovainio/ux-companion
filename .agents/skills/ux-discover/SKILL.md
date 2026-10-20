---
name: ux-discover
description: Turns a vague idea or feature request into a Problem Brief by interviewing the user one question at a time. Use when someone has an idea, a feature request, a Jira ticket or a Confluence page but no clear problem statement — "we should build X", "can you help me scope this", "is this worth building", "write up this feature request". Also provides probe questions during a live user interview. Do NOT use when a Problem Brief already exists and the user wants a design direction (use ux-design-spec), or when a UI already exists and needs reviewing (use ux-review).
allowed-tools: Read, Write, Glob, Grep
---

# UX Discover

This is an AI instruction file. Follow these directives when turning an idea into a Problem Brief.

## What this produces

A **Problem Brief** at `.ux/briefs/<feature>.md` — a short document stating the problem, who
has it, what evidence exists, why now, what success looks like, and which assumptions still
need validating.

A brief is not a solution. If the user hands you a solution ("add a dropdown to the settings
page"), your job is to find the problem behind it. Write the solution down under
`Solutions already proposed` so it is not lost, then ask what it was meant to fix.

## Before asking anything

Read what already exists, so you never ask for something the repo already states:

1. `.ux/USERS.md` — who the users are
2. `.ux/surface-map.md` — the product's areas, navigation and terms
3. `.ux/briefs/` — existing briefs, in case this overlaps one
4. If the user named a Jira ticket or Confluence page, read it

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

## The interview

**One question at a time.** Never present a numbered list of questions — ask one, read the
answer, let it choose the next question. This is the whole point of the skill; a questionnaire
gets questionnaire answers.

Cover these areas, in roughly this order. Skip any the user has already answered, in their
request or in `.ux/`:

1. **The pain.** What goes wrong today? Ask for a specific recent instance, not a
   generalisation. "When did this last happen?" beats "how often does this happen?"
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

**Stop when the problem is clear enough to design against — not after a fixed number of
questions.** Four sharp answers beat twelve vague ones. Before you stop, state what you
believe the problem is in one sentence and ask the user to correct it. Their correction is
usually the most valuable sentence in the interview.

If the user does not know an answer, that is a finding, not a failure. Write it as an
assumption or an open question and move on. Do not stall, and do not fill the gap yourself.

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
and tell them the next step: `ux-design-spec` for a design direction, or `ux-research` if the
assumptions need validating before anyone designs anything.

## Developer mode

No brief, no interview, no file. The user is about to build something and wants a sanity
check. Ask at most two questions, then return a short risk list:

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
- Do not keep interviewing once the problem is clear.

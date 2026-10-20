---
name: ux-evidence
description: Internal — do not invoke directly. Turns signal the product already generates — support tickets, session transcripts, reviews, forum threads, sales and success notes — into a tagged log of individually citable evidence atoms in `.ux/evidence/`, so a brief can cite a source instead of asserting one.
allowed-tools: Read, Write, Glob, Grep
---

# UX Evidence

Follow these directives when turning raw material the product
already generates into a tagged evidence log.

**Why this exists.** This family's first rule is *Evidence or Assumption, never neither* — but
`**Evidence:**` is only worth more than `**Assumption:**` if the source can be checked. Without
somewhere for sources to live, every brief either links out to a ticket nobody opens or quietly
degrades into confident paraphrase. This skill gives evidence an address: a stable ID a brief
cites, that someone can follow back to the thing that was actually observed.

The unit is the **atom** — one observation, one source, one date, tagged. A study report
answers the question it was commissioned for and then dies; an atom answers questions nobody
had asked yet. That is the whole reason for the format.

## Boundary with `ux-research`

These look adjacent and are not interchangeable. Get this wrong and you build a second,
competing store of the same material.

| | `ux-evidence` | `ux-research` |
|---|---|---|
| Input | **Unsolicited** signal that already exists | **Solicited** sessions you planned and ran |
| Unit | The atom — one observation | The theme — a pattern across a study |
| Lifetime | Standing; grows, is never rewritten | Per-study; finished when the study is |
| Question | Asked later, by someone else | Asked up front, in the research plan |

Atoms are an input to synthesis, not a replacement for it. When a batch of atoms is clearly
about to become themes, hand to `ux-research` rather than growing a second synthesis step here.

## What this produces

- `.ux/evidence/<batch>.md` — the atoms from one intake, with the frame they came from.
- `.ux/evidence/INDEX.md` — the standing index: what has been logged, what the next ID is, and
  who is structurally missing from the log.

## Before starting

Read `.ux/evidence/INDEX.md`, `.ux/USERS.md`, `.ux/surface-map.md`, and `.ux/briefs/`.

**Check the batch is not already logged** against the index's source column. Logging the same
tickets twice inflates every count drawn from the log afterwards, and the inflation is
invisible once it is in there.

If a brief prompted this, read it first and note its assumptions that drive decisions — those
are what someone will come looking for in the log. Do not let them narrow what you extract: an
atom only usable for today's question is a quote, not evidence.

## Phase 1 — Frame the intake before reading it

This phase is the one that makes the log honest, and it is the one that gets skipped. Write the
frame down **before** extracting anything, so the extraction cannot quietly define it.

1. **What is the source**, exactly? "Support tickets" is not a frame. "Tickets tagged
   `installer` in Q3 FY26, 320 of them" is.
2. **How was this material selected**, and by whom? Material someone pre-filtered as
   "interesting" is a sample of their judgement as much as of your users.
3. **Who is structurally absent?** Every source has a shape, and the shape is not the user
   base:
   - **Support tickets** record people who hit a problem *and* had the energy and standing to
     report it. Users who hit it and gave up leave no ticket and are usually the larger group.
   - **Reviews and forum threads** over-represent the extremes at both ends.
   - **Sales and success notes** are filtered through what the person in the room wanted to
     hear, and often describe non-customers' stated reasons rather than their behaviour.
   - **Session transcripts** record people who agreed to be recorded.
4. **What is the denominator?** The total the material was drawn from. Record it even when it
   is unknown — `Denominator: unknown` is a usable warning; a count with no denominator reads
   as a proportion and is not one.

A frame that cannot be written down honestly means the batch is not loggable yet. Say so rather
than logging it with a vague frame; a vague frame is how a biased sample becomes a fact.

## Phase 2 — Extract atoms

One observation per atom. If an atom needs the word "and", it is two atoms.

- **Verbatim where there was language.** The quote is the evidence; a paraphrase is already
  analysis, and the analysis is the part that should stay reversible.
- **What they did beats what they said**, and when both exist, record both — the gap between
  them is frequently the most valuable thing in the batch.
- **No conclusions in the atom.** "Users find the install confusing" is a conclusion. "Ran
  `install.sh` three times in four minutes, each time from a different directory" is an atom.
  The first cannot be checked; the second can.
- **Tag confidence per atom** as **Observed** (you have the behaviour), **Reported** (they
  described it), or **Inferred** (you concluded it from surrounding material — allowed, but
  never later cited as Evidence without something Observed behind it).

This is a different axis from `ux-research`'s Strong/Moderate/Weak, which rates a theme by how
many participants showed it. One atom has one source, so participant count says nothing; how
directly you saw it says everything. Do not mix the two scales.

## Phase 3 — A request is not a problem

The most expensive error available here, and it is one line from happening in every batch.

A ticket saying *"add a bulk delete button"* is a **Request** atom. The **Problem** atom is
whatever that person was doing when they wanted it — and it is often absent from the ticket
entirely, because people report their proposed solution and not their situation.

- Log the request as `Kind: Request`. Never as evidence of the problem it implies.
- Log the problem separately, as its own atom, and link the two.
- Where the material does not say what the problem was, **record that it does not.** An
  unexplained request is a real finding: it tells `ux-discover` what to go ask about.

Counting requests is counting how many people guessed the same solution. That is a fact about
the discourse, not about the product.

## Phase 4 — Count honestly

- Always give the denominator: "14 of 320 tickets", never "a number of users".
- **Never add counts across sources with different frames.** Nine tickets plus four reviews is
  not thirteen of anything; the two were drawn from different populations by different
  mechanisms.
- One person appearing in six tickets is one person. Deduplicate by human, not by document.
- Where the count is of documents rather than people, say which: "14 tickets, from at least 9
  distinct accounts" — and `unknown accounts` where the material does not let you tell.

## Privacy

Source material of this kind carries real customer identities, and the log lands in a git
repository that may be shared more widely than the ticket system was. Theme M in
`../ux-companion/references/design-questions.md` applies to what this skill writes, not just to
what the product ships.

- **Pseudonymise people.** `P3`, `Account A`. Never names, email addresses, usernames, account
  IDs or phone numbers in an atom — including inside a verbatim quote, where they are easiest
  to miss.
- **Link, do not transcribe.** Cite the ticket by its key and quote only the line carrying the
  observation. The access control on the source system is doing work you should not undo.
- **Quote only what was observed.** Surrounding material in a transcript or a ticket often has
  nothing to do with the point and everything to do with someone's bad week.
- Redact secrets, tokens, internal hostnames and file paths that appear in pasted logs.
- If material was given under a consent that did not cover this, say so and stop. That is a
  question for the person who collected it, not a judgement call to make here.

## The files

Write atoms to `.ux/evidence/<batch>.md`, named for the source and period
(`support-tickets-2026-q3.md`). Create `.ux/evidence/` if needed.

```markdown
# Evidence: <batch>

**Date logged:** <YYYY-MM-DD> · **Atoms:** EV-00NN–EV-00NN

## Frame
**Source:** <exactly what this material is>
**Period:** <…> · **Denominator:** <n, or `unknown`>
**Selected by:** <how this material was chosen, and by whom>
**Structurally absent:** <who this source cannot contain, and what that biases>

## Atoms

### EV-0042 — <one-line observation, no conclusion>
**Kind:** Problem | Workaround | Request | Context | Praise
**Confidence:** Observed | Reported | Inferred
**Source:** <AMD-1234 | session 2026-03-04 | review, 2026-02-11> · **Who:** <P3, role>
**Area:** <product area, matching `.ux/surface-map.md` where one exists>

> "<verbatim, where there was language>"

<What they were observed to do, where that differs from what they said. One sentence.>

**Related:** EV-0038 — <the problem behind this request, or the atom this contradicts>
```

Then update `.ux/evidence/INDEX.md`:

```markdown
# Evidence log

**Last updated:** <YYYY-MM-DD> · **Atoms:** <n> · **Next ID:** EV-00NN

## Batches logged
| Batch | Source | Period | Denominator | Atoms |
|---|---|---|---|---|

## Known gaps
<Who the log structurally cannot speak for, and which question it therefore cannot settle.
This section is what stops the log being mistaken for the user base.>
```

**IDs are permanent.** Take the next from the index and never renumber, reuse or compact them —
a brief that cites `EV-0042` must keep meaning the same observation a year later. If an atom
turns out to be wrong, mark it `**Superseded by:** EV-00NN` in place rather than deleting it.

## Handoff

Report what the batch actually showed, including when that is less than the person hoping for
it wanted, then offer — do not run — the next step:

| What the batch produced | Offer |
|---|---|
| A pattern worth a problem statement | `ux-discover` — a brief, citing these atoms by ID |
| Atoms about who the users are and how they work | `ux-user-context` — fold into `.ux/USERS.md` |
| Enough atoms that themes are forming | `ux-research` — synthesis, with these as input |
| A question the material cannot answer | `ux-research` — a plan to go ask it properly |

When atoms contradict an existing brief's assumption, **say so out loud** rather than only
logging it. A contradiction found in material already sitting on disk is the cheapest finding
this family can produce, and it is worthless if nobody is told.

## Out of scope

Not built, and worth saying so rather than improvising a thin version: pulling from ticket,
review or CRM APIs (paste the material, or point at files in the repo), sentiment scoring,
automated clustering, dashboards or trend charts over time, and prioritisation. Personas belong
to `ux-user-context`; themes and study design belong to `ux-research`.

If asked for one of these, say it is not built and offer the nearest thing that is.

## Do not

- Do not invent an atom, a quote, a ticket reference or a count. A fabricated atom is worse
  than a fabricated quote in a report, because it will be cited as a source by name.
- Do not write a count without its denominator, and do not sum counts across frames.
- Do not log a request as evidence of the problem it proposes a solution to.
- Do not put a conclusion in an atom. The log holds what happened; conclusions are drawn later,
  by someone who can be disagreed with.
- Do not record names, emails, account IDs or secrets, including inside quotes.
- Do not renumber, reuse or delete an ID.
- Do not extract only the atoms that support the brief that prompted the batch.

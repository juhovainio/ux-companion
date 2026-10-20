---
name: ux-research
description: Internal — do not invoke directly. Plans user research and synthesises raw interview or usability-session notes into tagged insights. Reads published findings before proposing a study. Produces research plans, discussion guides and insight summaries in `.ux/research/`.
allowed-tools: Read, Write, Glob, Grep, WebSearch
---

# UX Research

Follow these directives when planning research or synthesising
notes.

## Scope

This skill does three things:

1. **Research plan** — what question, which method, who to talk to, what would change our mind.
2. **Discussion guide** — the questions to actually ask, in order.
3. **Synthesis** — raw notes in, tagged insights out.

**Out of scope for now**, and worth saying so rather than improvising a thin version: survey
design and analysis, usability test reports, participant recruitment and scheduling, journey
maps, opportunity-solution trees, and prioritised roadmap recommendations. Personas and
jobs-to-be-done belong to `ux-user-context` — when synthesis produces something about who the
users are, hand it there rather than writing a second description of the same people.

If asked for something out of scope, say it is not built yet and offer the nearest thing that
is. Do not produce a hollow version.

## Before starting

Read `.ux/USERS.md`, `.ux/briefs/`, and `.ux/research/`. Research that re-asks a question the
repo already answers wastes the scarcest resource here, which is a real user's half hour.

If a brief exists, start from its **assumptions that drive decisions** — those are, by
construction, the things most worth validating.

**Desk research before field research.** Where a published finding would already settle the
question — an established usability result, a study on the same interaction — search for it
first, per *Grounding in research* in `../ux-companion/references/design-questions.md`. If the
literature answers it, say so and do not run the study; spend the sessions on the part that is
specific to these users, which is the part nobody else can have answered. A general finding
never overrides what this team knows about *their* users — where they diverge, that divergence
is the thing worth researching.

## Research plan

The question comes first, and the method follows from it. Most "we should do some user
research" requests are really one specific uncertainty wearing a large coat — find it.

Ask, one at a time:

1. **What decision is waiting on this?** If no decision changes based on the answer, the
   research is not worth running. Say so — that is a legitimate and useful outcome.
2. **What do you believe the answer is?** Stating the expectation up front is what makes a
   surprise visible later.
3. **What would change your mind?** The most valuable question in the skill. If nothing would,
   stop; this is a decision already made, and the research is theatre.
4. **Who has the answer?** Real, reachable people, named where possible. "Users" is not a
   recruitment plan.

Pick the lightest method that can answer the question:

| Question | Method |
|---|---|
| Do people have this problem at all? | 3–5 interviews about their last real instance of it |
| How do they do it today? | Watch them do it — contextual observation beats description |
| Can they use what we built? | Usability session, task-based, no leading |
| Which of two directions? | Show both, ask about their last relevant experience, not their preference |
| How often / how many? | Not interviews — usage data, support tickets, logs |

Five interviews that change a decision beat twenty that confirm what everyone already thought.

Write to `.ux/research/<topic>.md`:

```markdown
# Research plan: <topic>

**Date:** <YYYY-MM-DD> · **Status:** Planned

## Decision waiting on this
<What we will do differently depending on the answer.>

## Question
<One sentence, answerable.>

## Current belief
<What we think the answer is, and whether that is Evidence or Assumption today.>

## What would change our mind
<Specific and observable. "If three of five participants do X.">

## Method
<What we will do, and why it is the lightest thing that answers the question.>

## Participants
<Who, how many, how reached. Note anyone we want but cannot get, and what that biases.>

## Risks to validity
<Leading questions, wrong participants, asking about the future, sample too small to carry
the weight we will put on it.>
```

## Discussion guide

Structure: warm-up, context, deep dive, reaction, wrap-up.

Rules that matter more than the questions themselves:

- **Ask about the past, not the future.** "Tell me about the last time…" is reliable; "would
  you use…" is not.
- **Never name the feature before they describe their own problem.** Once a participant knows
  what you are hoping to hear, they will help you hear it.
- **Ask what they did, then why.** Not whether they liked it.
- **Silence is a question.** Note where to stop talking and wait.
- **Keep the concept until after their own story is out**, in the reaction phase.

Write the guide with the questions in order, a time budget per phase, and the probes to use
when an answer is thin. Mark which question maps to which assumption from the brief — if a
question maps to nothing, cut it.

## Synthesis

Input: raw notes, transcripts, session recordings as text, support threads. Output: tagged
insights.

1. **Quote first.** Pull what people actually said or did, verbatim, with who and when. Never
   paraphrase into the insight — the quote is the evidence; paraphrase is already analysis.
2. **Group by what people are doing**, not by which question you asked. The real themes cross
   question boundaries.
3. **Tag confidence per theme** by how many participants showed it and how directly:
   - **Strong** — most participants, observed behaviour.
   - **Moderate** — several participants, or reported rather than observed.
   - **Weak** — one participant, or inferred. Keep it; one person can name a real problem.
     Just do not let it carry a decision alone.
4. **Record what contradicted the expectation**, in its own section. This is the part teams
   skip and the part most worth the money.
5. **Separate what they said from what you concluded.** Implications are yours; label them.

```markdown
# Insights: <topic>

**Date:** <YYYY-MM-DD> · **Sessions:** <n> · **Method:** <…>

## Headline
<The one thing someone should know if they read no further.>

## Themes
### <Theme> — Confidence: Strong | Moderate | Weak
<What people did or said.>
- > "<verbatim quote>" — <participant>, <date>

## What surprised us
<Where findings contradicted the stated belief in the plan.>

## What this changes
<The decision from the plan, and what the answer means for it. Labelled as our conclusion,
not the participants'.>

## Still unknown
<What this did not answer, and whether it needs another round.>
```

Then offer the follow-ups rather than doing them unasked: fold user findings into
`.ux/USERS.md` via `ux-user-context`, or update the brief's assumptions — promoting any that
are now backed by evidence.

## Do not

- Do not invent quotes, participants, sessions or numbers. Ever. A fabricated quote is the
  single most damaging thing this family could produce.
- Do not report "5 of 8 participants" unless there were eight participants.
- Do not present a one-participant finding as a theme.
- Do not run research on a decision that is already made.
- Do not write personas here.

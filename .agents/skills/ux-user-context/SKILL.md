---
name: ux-user-context
description: Internal — do not invoke directly. Builds and maintains `.ux/USERS.md` — personas or jobs-to-be-done, context of use, and skill level for a product. Works from questions to the caller on a cold start, or from existing docs, briefs and notes when expanding.
allowed-tools: Read, Write, Glob, Grep
---

# UX User Context

Follow these directives when building or expanding `USERS.md`.

## What this produces

`.ux/USERS.md` — a short, reusable description of who uses this product, what they are trying
to get done, the context they do it in, and how skilled they are. Every other skill in this
family reads it, so the next feature starts with this knowledge instead of a blank page.

It describes **real users as currently understood**, including the parts not yet understood.
It is not a marketing persona, and it does not contain a fictional name, a stock photo, or an
invented biography.

## Two entry paths

**Cold start** — no `.ux/USERS.md` exists. Build it by interviewing the caller.

**Expanding** — a `USERS.md` exists and new information has arrived: a brief, interview notes,
a research summary, a support thread. Read the existing file first, then **append and amend;
never overwrite.** Preserve what is there, mark what changed, and keep the date on each
change.

Before either path, gather what the repo already knows: `.ux/USERS.md`, `.ux/briefs/`,
`.ux/research/`, `.ux/OWNERS.md`, the README, any docs directory, and — if the product is a CLI or an API —
its help text and reference docs, which usually state who it is for. Tell the user in one line
what you found and start from there rather than from zero.

## The interview (cold start)

**One question at a time.** Stop when there is enough to design against, not after a fixed
count. Three users understood properly beats eight sketched.

Cover, in roughly this order:

1. **Who actually uses this?** Push past job titles to roles-in-context: "developers" is not a
   user, "a developer installing ROCm on a fresh machine for the first time" is. Ask who the
   caller has personally watched or talked to.
2. **What are they trying to get done?** Their goal, in their words — not the feature they
   use. The job, not the tool.
3. **What is the context?** Where, on what, under what pressure, how often, alongside what
   other work. Interruption, deadline, unfamiliar machine and shared environment all change a
   design.
4. **How skilled are they?** With this product, and with the domain around it. These differ:
   an expert kernel developer can be a complete novice at this product's CLI.
5. **What do they already know and expect?** Conventions from adjacent tools they use daily.
   Designing against those expectations is most of consistency.
6. **Who else is affected but is not the primary user?** The person who inherits the output,
   approves it, or supports it when it breaks.

If the caller does not know, that is the single most valuable output of this skill. Write
`Unknown` and the question that would resolve it. Do not fill the gap.

## Two lenses: human and agent

A product in this repository has two kinds of consumer, and they are not a primary and a
footnote — they are two populations with different needs for the same capability:

- **Human lens** — a person operating a UI, a CLI, or a config file.
- **Agent lens** — an AI agent calling a skill, an MCP tool or an API, or a script or CI job
  doing the same without one.

Ask which apply here; do not assume only the first. The signals differ:

| | Human consumer | Agent consumer |
|---|---|---|
| **Skill level** | Familiarity with this product and its domain | What it can be expected to know without being told — an agent reads literally and will not infer from context the way a person does |
| **Context of use** | Where, on what, under what pressure | Headless, unattended, mid-chain between two other calls; no one watching to notice a wrong turn |
| **Expectations** | Conventions from adjacent tools | Parameter names and result shapes that match sibling tools; no prompts, stable output, meaningful exit codes |
| **How they find it** | Where their eyes land | A tool name and description read before acting — never documentation it would have to already know it needs |
| **What "done" looks like** | A visible message or screen | A structured result it can act on; a silent success and a silent no-op must not look the same |

`../ux-companion/references/design-questions.md` carries both lenses on every theme; this file
is where the family records *which* of them this product actually has. Where it is genuinely
unclear whether a consumer is a person or an agent, that belongs under `What we do not know`
rather than being settled by a guess.

## Evidence or Assumption, never neither

Tag every characterisation:

- `**Evidence:**` — observed, with a source: an interview, a ticket, a metric, a named
  conversation, usage data.
- `**Assumption:**` — believed but not shown. Add `⚠️ drives a decision` where a design would
  change if it were false.

"Our users are mostly experienced with Linux" is an **Assumption** unless someone measured or
asked. A `USERS.md` that is honest about being mostly assumptions is useful — it tells the team
exactly which research would pay off. One that reads as fact is worse than having no file,
because every downstream spec inherits the invention.

## The file

```markdown
# Users

**Last updated:** <YYYY-MM-DD> · **Confidence:** <Mostly evidence | Mixed | Mostly assumption>

## <User or job name>
<A role in context, not a job title. "First-time installer on a fresh workstation".>

- **Lens:** <Human | Agent>
- **Goal:** <what they are trying to get done, in their words>
- **Context of use:** <where, on what, under what pressure, how often>
- **Skill level:** <with this product> / <with the domain>
- **Expectations:** <conventions from tools they already use>
- **Pain today:** <what goes wrong for them now>
- **Evidence:** <source> · **Assumption:** <claim> ⚠️ drives a decision

## <Next user or job>
…

## Also affected
<People who inherit, approve or support the output without being primary users.>

## What we do not know
<Each open question, tagged with its owner per `../ux-companion/references/owners.md`, or the
source that could answer it. This section is a feature. Do not leave it empty to make the
document look finished.>

## Changelog
- <YYYY-MM-DD> — <what changed and what prompted it>
```

Use as many user sections as the product genuinely has — typically two to four. If the caller
describes one user, write one.

**An agent consumer gets a full section with the same fields, not a footnote.** "Agent calling
this to decide whether a job can be submitted" is a user section; so is "CI job running this
unattended nightly". Do not demote them to a list at the bottom — a downstream spec reads this
file to find out who it is designing for, and a consumer in a footnote gets designed for like
one.

Personas or jobs-to-be-done is the caller's choice; default to **jobs-to-be-done** phrasing
("first-time installer", "release engineer verifying a build") because it stays accurate when
the same person wears two hats.

## Before writing: gap pass

Follow *The gap pass* in `../ux-companion/references/owners.md`. For `USERS.md`, the usual
gaps are user sections that are all assumption, a skill level nobody measured, and an agent
consumer nobody has confirmed exists. Tag the owner from `.ux/OWNERS.md` on each line of
`What we do not know`, typically the users and research owner. Run the narrative check from
the same file: someone reading the file cold should come away knowing who the users are, how
sure we are, and who to ask about the rest.

## Expanding an existing file

1. Read the current `USERS.md` in full.
2. Identify what the new source adds: a new user, a corrected assumption, an assumption now
   backed by evidence, a changed context.
3. **Promote assumptions to evidence when a source now supports them** — this is the most
   valuable edit this skill makes. Change the tag and add the source.
4. Contradiction between the file and the new source: do not silently pick a winner. Show the
   user both and ask. Record the resolution in the Changelog.
5. Add a dated Changelog line for every change.

## Do not

- Do not invent a user, a name, a demographic, a quote or a motivation.
- Do not convert an assumption into fact by rephrasing it confidently.
- Do not overwrite an existing `USERS.md`.
- Do not leave `What we do not know` empty to make the file look complete.
- Do not keep interviewing once there is enough to design against.

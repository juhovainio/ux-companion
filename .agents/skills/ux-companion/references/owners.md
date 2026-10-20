# Owners and gaps

The family's shared convention for finding what a document is missing and naming who can
close it. Read by `ux-discover`, `ux-concepts`, `ux-design-spec`, `ux-research` and
`ux-user-context`. Edit it here. A rule restated inside a skill becomes a second copy that
drifts.

`.ux/OWNERS.md` is written by `ux-owners`. This file says how to use it.

## The gap pass

Run it after drafting a document and before showing it. Four lists, in this order.

1. **Missing points.** Template sections that are empty, or filled only by assumptions. A
   brief with no success criteria has a missing point. So does a spec with no empty state.
2. **Missing evidence.** Claims that would need a source to become `**Evidence:**`. For each,
   name the kind of source that would do: a ticket, a metric, an interview, a log.
3. **Unchecked assumptions.** Every `**Assumption:** ... drives a decision`.
4. **Unanswered questions.** Everything going into `Open questions`.

Then work down each item in the same order the family always uses:

1. Can it be reasoned out from the request, the repo or `.ux/`? Do that and stop.
2. Does only the current user know it? Ask them, one question at a time.
3. Otherwise it needs someone else. Tag an owner.

Do not ask the user a question that an owner would answer better. "What is the p95 latency
today?" goes to whoever owns data and metrics, not to the person writing the brief.

## Matching a gap to a topic

Read `.ux/OWNERS.md`. Match on the `Covers` column first, then on the topic name. A gap about
"how long the install takes on a fresh machine" matches `Data and metrics` through its
`Covers` text, even though the words differ.

| Situation | What to write |
|---|---|
| One topic matches, owner assigned | The tag below |
| One topic matches, owner is `Unassigned` | `Owner: unassigned (<topic>)` |
| Two topics match | The one that can answer the question itself. Mention the second only if the answer needs both. |
| No topic matches | `Owner: unassigned` and add one line to the end of the gap list: "No topic covers <subject>. Add one with an owners update." |
| `.ux/OWNERS.md` does not exist | `Owner: unassigned`. Offer onboarding once, at the end, not during the work. |

Never guess a person. Never tag someone because they appear in the repo, the ticket or a
previous document. Only `.ux/OWNERS.md` assigns owners.

## Tag format

```markdown
[@Jane Doe](https://<site>.atlassian.net/jira/people/<accountId>)
```

It renders as a link in plain markdown, and the account ID survives if the text is later
pasted into Jira or Confluence, where it can become a real mention.

- Account ID is `unresolved`: write `@Jane Doe` with no link, and add "(no Atlassian ID)" once
  per document.
- Take `<site>` and `<accountId>` from `.ux/OWNERS.md`. Do not rebuild them from memory.

## Where tags go

Every item from the gap pass lands in the document with an owner on it. Use the section the
template already has, and keep the tag at the end of the line.

```markdown
## Open questions
- What is the install failure rate on fresh machines? Needs a number from the last 30 days.
  [@Jane Doe](https://acme.atlassian.net/jira/people/5b10ac8d82e05b22cc7d4ef5)
- Does the retry change the audit trail? Owner: unassigned (Security and legal)
```

- **Open questions.** One line each: the question, what answer would settle it, the owner.
- **Assumptions that drive a decision.** Tag the owner of the topic the assumption belongs
  to, at the end of the assumption line.
- **Missing evidence.** Goes into `Open questions` as a request: what source, from whom.
- **Missing points.** If the user can fill them now, ask. Otherwise they go into `Open
  questions` with an owner like everything else.

Do not add a section only for owners. The tags live in the sections that exist.

## The narrative check

A document is finished when it reads top to bottom as an argument, not as a form with every
field filled. Before showing it, read it once as the person who gets it cold:

- The first paragraph says what the document is about and what it asks of the reader.
- Each section follows from the one before. If a section could be moved without anyone
  noticing, it is a list entry, not part of the argument.
- What is unresolved is stated near the end with names on it, so the reader knows what to do
  next and who to talk to.

Fix what fails the read. Do not add a summary section to paper over it.

## Do not

- Do not tag an owner on a claim that is already `**Evidence:**` with a source. Tags mark
  what is still open.
- Do not tag more than one person per item. Pick the person who answers first.
- Do not message anyone or create Jira items. Tagging is text in the document.
- Do not invent a topic to have somewhere to put a tag. Unassigned is a true answer.

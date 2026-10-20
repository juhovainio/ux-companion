---
name: ux-owners
description: Internal, do not invoke directly. First-run onboarding that records who owns which topic (product, research, design, engineering, data, security, support) in `.ux/OWNERS.md`, with Atlassian account IDs, so every gap, missing piece of evidence and open question in a document can name the person who can close it. Also handles later updates to owners.
allowed-tools: Read, Write, Glob, Grep
---

# UX Owners

Follow these directives when setting up or updating `.ux/OWNERS.md`.

## What this produces

`.ux/OWNERS.md`: one table mapping topics to the person in charge of each, with their Atlassian
account ID. Every other skill in this family reads it. When a document has an open question or
an assumption nobody has checked, the skill looks up the topic here and tags the owner, so the
reader knows who to ask.

The file records who the user told you owns what. It does not record who you think should.

## Dependency

Resolving names needs the Atlassian tools of the host (`getAccessibleAtlassianResources` for
the site, `lookupJiraAccountId` for people). This is a required dependency. If the host has
no Atlassian access, say so, offer to record names without account IDs (`unresolved`), and let
the user choose. Do not invent account IDs, and do not construct them from names.

## Two entry paths

**First run.** No `.ux/OWNERS.md` exists. Run the onboarding below.

**Update.** The file exists and the user says "X now owns security", "add a legal topic",
"Jane left". Read the file, change only the rows involved, update the date, and show the
changed rows. Do not restart the interview.

## Onboarding

Reason first, ask last. A user who is asked eight questions about a team you could partly
read from the repo gets the gaps they started with, itemised.

### 1. Read what the repo already says

Read `CODEOWNERS` (also under `.github/` and `docs/`), `.ux/USERS.md`, `.ux/briefs/`,
`README.md` and any contributor or maintainer list. Names found there are **guesses**. Tell
the user in one line what you found: "`CODEOWNERS` names three people, I'll offer them as
starting points."

If the user linked a Confluence space or Jira project, read its team or contacts page too.

### 2. Propose the topics

Start from these. They match the sections the documents in this family contain.

| Topic | Covers |
|---|---|
| Product and priority | problem, why now, success criteria, scope cuts |
| Users and research | who the users are, interviews, support insight |
| Design | flows, copy, patterns, consistency with the product |
| Engineering feasibility | effort, architecture, dependencies, limits |
| Data and metrics | usage numbers, baselines, how success is measured |
| Security and legal | permissions, privacy, compliance, licences |
| Support and operations | what breaks in production, who answers the tickets |

Show the list once and ask whether to rename, add or drop any. Teams differ. A two-person
team may have three topics and a platform team may have a "Docs" topic. Keep the `Covers`
text, because other skills match gaps to topics through it.

### 3. Fill owners, one topic at a time

For each topic, ask one question: "Who owns engineering feasibility?" If step 1 produced a
guess, offer it: "`CODEOWNERS` lists Jane Doe for `/src`. Is she the one for engineering
feasibility?"

Accept "nobody yet", "me" and "skip". Record `Unassigned` for the first and the user's own
name for the second. Do not press. A topic with no owner is a true statement about the team.

Stop when every topic has an answer, including "unassigned".

### 4. Resolve each name

Get the Atlassian site from `getAccessibleAtlassianResources`. If there is more than one,
ask which. Then call `lookupJiraAccountId` for each name.

- **One match.** Use it.
- **Several matches.** Show names and emails if available and ask the user to pick. Never
  pick for them. Two people with the same name is the exact case this step exists for.
- **No match.** Ask once for a different spelling or an email. If that fails, record the
  name with account ID `unresolved` and move on.

### 5. Write and confirm

Write `.ux/OWNERS.md`, creating `.ux/` if needed, then show the table and ask the user to
correct it. Nothing is final until they confirm.

```markdown
# Owners

**Atlassian site:** <site>.atlassian.net · **Updated:** <YYYY-MM-DD>

| Topic | Owner | Atlassian account ID | Covers |
|---|---|---|---|
| Engineering feasibility | Jane Doe | 5b10ac8d82e05b22cc7d4ef5 | effort, architecture, dependencies |
| Security and legal | Unassigned | n/a | permissions, privacy, compliance, licences |
```

Rules for the table:

- One owner per topic. If the user names two, ask who answers first and put the other under
  `Covers` as backup, or split the topic.
- `Unassigned` rows stay in the table. They tell the other skills to write
  `Owner: unassigned` instead of guessing.
- `unresolved` account IDs stay visible so a later update can fix them.

## After writing

Say what is set up and what is not ("five topics have owners, two are unassigned, one name is
unresolved"). Then hand back to what the user originally asked for. Onboarding is a detour,
not the goal.

If the user says "later" or declines, do not write the file. The other skills carry on and
tag gaps `Owner: unassigned`. Offer again the next time a document ends with open questions.

## Do not

- Do not guess an owner from a git log, a commit count or a job title. A `CODEOWNERS` entry
  is a suggestion the user confirms, never a fact.
- Do not pick between several matching accounts.
- Do not invent or reconstruct an Atlassian account ID.
- Do not ask about a topic the user already declined to have.
- Do not post to Jira or Confluence, and do not message anyone. This skill only reads people
  and writes one file.
- Do not overwrite an existing `OWNERS.md` on update. Change the rows involved.

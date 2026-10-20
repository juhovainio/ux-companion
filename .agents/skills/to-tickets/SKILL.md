---
name: to-tickets
description: Turns a finished design spec into real Jira tickets. Use when the user says "create tickets for this spec", "turn this into tickets", "file this in Jira", "ticket this up", "make Jira issues for <feature>", "/to-tickets", or hands over a spec and asks for tickets, stories, or issues to track the build. Also use when picking up ticketing in a later session for a spec that was already written. Do NOT use to write or edit a design spec (use ux-design-spec) or to create ad hoc tickets unrelated to a `.ux/specs/` file.
allowed-tools: Read, Write, Glob, Grep, mcp__atlassian__jira_get_all_projects, mcp__atlassian__jira_create_issue, mcp__atlassian__jira_batch_create_issues, mcp__atlassian__jira_link_to_epic
---

# To Tickets

Follow these directives when turning a finished design spec into real Jira tickets.

This skill is independently invocable. It is not a phase of `ux-design-spec` and never runs
automatically when a spec is written — ticketing is a separate decision on its own schedule,
possibly in a different session, possibly never.

## Inputs

Read all of these before doing anything else:

1. The spec: `.ux/specs/<feature>.md`. If the user named a feature, read that file. If none is
   named, Glob `.ux/specs/*.md` — one match, use it and say so; more than one, list them and
   ask which; none, say there is no spec to ticket yet and stop (offer `ux-design-spec` first).
2. `.ux/jira-project.md` — a previously confirmed Jira project for this repo, if one exists.
3. The conversation itself — has the user already named a Jira project in this session?
4. `../ux-companion/references/design-questions.md` — Theme M only (Privacy & data handling),
   needed in Step 3. If that relative path does not resolve, Glob for
   `**/ux-companion/references/design-questions.md`.

## Already ticketed? Check first

If the spec already has a `## Jira tickets` section, show what is already recorded (keys and
dates) and ask whether this call is adding tickets for new work added to the spec since, or
something else — never silently re-run the full breakdown over work that is already filed.
Re-running blind is how a live project ends up with duplicate junk, which is exactly what this
skill's confirmation gate below exists to prevent.

## Still accurate? Check before filing

Compare the spec's `**Date:**` against `.ux/surface-map.md`'s `**Last updated:**`, if a surface
map exists. If the map was updated after the spec was written, say so in one line and ask
whether the spec still holds — a spec written against an older surface map may describe entry
points or patterns that have since moved. A yes is enough to proceed; this is a one-line check,
not a re-run of `ux-design-spec`.

## Step 1 — Determine the project

Never guess a project key. Resolve it in this order, stopping at the first that answers it:

1. **Already stated in this conversation** — use it, and say which earlier message it came from.
2. **`.ux/jira-project.md` exists** — read it, show the user the project it names, and get a
   one-line reconfirmation ("Still filing to `<KEY>`?"). That is a cheap confirmation, not a
   re-interview — do not ask it as an open question.
3. **Neither exists** — call `mcp__atlassian__jira_get_all_projects`, show the real list (key
   and name), and ask the user to choose. Never invent a key that merely looks plausible.

If the project just named differs from what `.ux/jira-project.md` currently records, confirm
before overwriting it — this file is a convenience cache, not a silent default. Once resolved,
write or update it:

```markdown
# Jira project

**Project key:** <KEY>
**Project name:** <Name>
**Set on:** <YYYY-MM-DD>
**Confirmed by:** user, via `to-tickets`
```

## Step 2 — Propose a breakdown

Granularity is not fixed. Always offer the choice, every time, even if an earlier feature in
this repo picked one already. Ground the options in this spec's actual content:

- **A — One ticket for the whole spec.** A single issue for the whole feature. Suits a small,
  one-sitting build.
- **B — One ticket per Flow step.** A parent ticket for the spec, plus one child ticket per
  numbered step in `## Flow`. Suits a build that ships or reviews step by step.
- **C — Something else.** Ask how the user wants it split — by surface, by state, by consumer
  (human vs. agent) — whatever seam fits this spec better than A or B.

Show what each option would actually produce before the user chooses. For B, list the real Flow
step titles from this spec as the candidate ticket summaries, not a generic placeholder.

## Step 3 — Draft the tickets

For each proposed ticket, draft real field values from the spec:

- **Project** — the key from Step 1.
- **Issue type** — ask once if not already known. No available Jira MCP tool enumerates a
  project's valid issue types, so this one question replaces what would otherwise be a wrong
  guess — it is not a shortcut taken for convenience.
- **Summary** — the feature title for a single ticket, or `<feature title>: <step title>` for a
  per-step ticket.
- **Description** — assembled from the relevant spec sections: `Problem`, the relevant part of
  `Flow`, `Entry points`, `Fit with the existing product`, `States`, `Copy`, and any bearing
  `Assumption:` lines. Always end with `Spec: .ux/specs/<feature>.md`, plus `Brief:
  <path>` (carried from the spec's own `**Brief:**` header line) and `Research: <path>` for any
  `.ux/research/<topic>.md` the spec's Assumptions cite as Evidence. A ticket that only points
  at the spec loses the trail back to why the work was proposed in the first place.
- **Check Evidence for Theme M before copying it in.** If the `Problem` or `Assumptions` text
  carries a named person, a direct quote, or another identifying detail, flag it — per Theme M
  (Privacy & data handling), a Jira ticket's audience is often wider than the interview or
  support conversation the evidence came from. Default to anonymising (a role or initials
  instead of a name) in the ticket description unless the user confirms the identifying detail
  should stay.
- **Parent link** (option B only) — ask once whether this project models parent/child as
  Epic → Story or Story → Subtask; do not assume a hierarchy scheme that may not exist in the
  chosen project. Once the parent ticket is created, link children via `additional_fields:
  {"parent": "<PARENT-KEY>"}` on `jira_create_issue`, or `jira_link_to_epic` if the project uses
  Epics.

## Step 4 — Confirmation gate (mandatory, before any write)

Creating a Jira ticket is a real, externally visible action in a live project. Show every
ticket's full preview and get explicit approval before calling `jira_create_issue` or
`jira_batch_create_issues` — no exceptions, and nothing is created while the user is still
asking for changes to another ticket in the same batch.

Print the dry run, numbered:

```
1. Project: <KEY>        Issue type: <Story>
   Summary: <...>
   Description:
   <...>

2. Project: <KEY>        Issue type: <Subtask> (parent: 1)
   Summary: <...>
   Description:
   <...>
```

Then ask: "Create these N tickets in `<KEY>`? (yes / edit one / cancel)". Loop on edits until
the full set is approved. Only an explicit yes creates anything. Cancelling ends the skill with
nothing written to Jira and nothing recorded in the spec.

## Step 5 — Create and record

1. Create the tickets. Use `jira_batch_create_issues` for a flat set with no parent/child links
   (option A, or option C without hierarchy); create sequentially via `jira_create_issue` —
   parent first — whenever a child ticket needs the parent's real key (option B), since the
   batch tool's schema has no parent-link field.
2. Append (or extend) a `## Jira tickets` section in `.ux/specs/<feature>.md`:

```markdown
## Jira tickets

| Ticket | Summary | Type | Created |
|---|---|---|---|
| [<KEY>](<url>) | <summary> | <type> | <YYYY-MM-DD> |
```

3. Tell the user the created keys and links. Stop — do not chain into anything further, the
   same as `ux-design-spec`'s handoff.

## Do not

- Do not call `jira_get_all_projects` or ask the user to choose a project when one is already
  known from this conversation or `.ux/jira-project.md` — re-asking what is already answered is
  the failure this family exists to avoid.
- Do not guess a project key, issue type, hierarchy scheme, or ticket breakdown. Ask, or read it
  from the spec.
- Do not call `jira_create_issue` or `jira_batch_create_issues` before the user has approved the
  full dry-run preview.
- Do not re-run the full breakdown over a spec that already has a `## Jira tickets` section
  without asking first.
- Do not file a spec written against a surface map that has since changed without a one-line
  reconfirmation that it still holds.
- Do not copy a named person, quote, or other identifying detail into a ticket description
  without checking it against Theme M first.
- Do not run as a phase of `ux-design-spec` or any other skill in this family.
- Do not leave created tickets unrecorded — the spec is this family's source of truth, and a
  spec that does not say what got filed drifts from reality immediately.

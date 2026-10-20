---
name: ux-publish
description: Publishes UX Companion artefacts to a place people who will never clone the repo can read — Confluence today. Use when the user says "publish this spec", "put the brief on Confluence", "share this with the wider team", "/ux-publish", or asks where artefacts are published and whether the published copy is current. Do NOT use to write or edit an artefact (use the skill that owns it), or to file Jira tickets (use to-tickets).
allowed-tools: Read, Write, Glob, Grep, mcp__plugin_atlassian_atlassian__getAccessibleAtlassianResources, mcp__plugin_atlassian_atlassian__searchConfluence, mcp__plugin_atlassian_atlassian__getConfluenceContent, mcp__plugin_atlassian_atlassian__createConfluenceContent, mcp__plugin_atlassian_atlassian__updateConfluenceContent
---

# UX Publish

Follow these directives when publishing artefacts out of the repo.

**Artefact root.** Resolve it per `../ux-companion/references/artefact-store.md` — Glob for
`**/ux-companion/references/artefact-store.md` if that path does not resolve — and state it in
one line before reading or writing anything. Then **substitute it for the literal `.ux/`
prefix in every path below** — they are written as `.ux/…` shorthand, and once a non-default root
is resolved, touching a path that still begins `.ux/` is a bug. `.ux/config.md` is the exception:
it is configuration and always resolves literally.

This skill is independently invocable. Publishing is a separate decision on its own schedule —
it never runs automatically because an artefact was written, the same way `to-tickets` never
files a spec just because one exists.

## What this is, and what it is not

**The local markdown is the source of truth. Always.** A published page is a *copy*, made for
people who will never clone the repo. Nothing is ever read back from it, nothing is synced in
reverse, and a page edited in Confluence does not update the repo.

If someone wants the published copy to be authoritative, that is a different product than this
one, and the honest answer is to say so rather than growing a sync engine one special case at a
time. What this skill can do about a page that was edited downstream is tell you it diverged.

## Before starting

1. Resolve the artefact root, and read `.ux/config.md`.
2. **Check a Confluence tool is actually available.** Tool names are host-specific — this skill
   names the ones it was built against, and another host's Confluence MCP server will name them
   differently. If none is present, **stop and say so.** Do not improvise, do not write the
   artefact somewhere else, and do not claim something was published.
3. Read the artefacts in scope, and their existing `## Published` blocks.

## Step 1 — Determine the target

Never guess a space. Resolve in this order, stopping at the first that answers it:

1. **Already stated in this conversation** — use it, and say which message it came from.
2. **`.ux/config.md` names a target** — use it, and say which space and parent page in the
   preview. The preview is the confirmation; do not ask a separate question first.
3. **Neither** — ask. Call `getAccessibleAtlassianResources` for the site, then
   `searchConfluence` to show real spaces, and have the user choose one and name a parent page.
   Never invent a space key that merely looks plausible.

Once resolved, record it in `.ux/config.md` — confirming first if it differs from what is
already there:

```markdown
**Publish to:** confluence
**Confluence space:** <KEY>
**Confluence parent page:** <page id>
**Set on:** <YYYY-MM-DD> · **Confirmed by:** user
```

The root in that file belongs to the family, not to this skill. Leave it alone unless the user
asks to change it, and follow the rules in the shared reference if they do.

## Step 2 — Decide what to publish

Ask what, if the user did not say. Default to the single artefact in front of you rather than
the whole tree — publishing everything is rarely what someone means and is expensive to undo.

**Markdown artefacts only.** `.ux/prototypes/<feature>.html` is a self-contained interactive
file, not a page: Confluence will not render it as one, and a flattened copy is worse than a
link. Say so and leave it in the repo.

For each artefact, work out which it is:

| State | What happens |
|---|---|
| No `## Published` block | **Create** a new page |
| Has one, local file changed since | **Update** that page |
| Has one, nothing changed since | **Skip**, and say it was already current |
| Has one, the remote page changed after we published | **Flag it.** Show that it diverged and ask before overwriting — someone edited it there, and a silent update destroys their work |

That last row is why the publish record stores a date rather than just a link. Read the page
with `getConfluenceContent` to compare before updating.

**Check what is being published before it leaves.** These artefacts can carry quotes, named
people and support-ticket detail, and a Confluence space is usually a wider audience than the
source material was collected for — per Theme M in `../ux-companion/references/design-questions.md`.
Flag any identifying detail and default to anonymising it in the published copy, unless the user
confirms it should stay. The repo copy is unaffected.

## Step 3 — Confirmation gate (mandatory, before any write)

Creating or updating a Confluence page is a real, externally visible action in a live space.
Show the full plan and get explicit approval before calling `createConfluenceContent` or
`updateConfluenceContent` — no exceptions, and nothing is published while the user is still
asking for changes to another item in the same batch.

Print the dry run, numbered:

```
Space: <KEY>   Parent: <page title> (<id>)

1. CREATE  "Problem Brief: slow first install"
           from .ux/briefs/slow-first-install.md
2. UPDATE  "Design spec: retry wrapper"          (page 12345, last published 2026-09-02)
           from .ux/specs/retry-wrapper.md
3. SKIP    "Users"                                already current
4. FLAG    "Concepts: retry wrapper"              page edited in Confluence on 2026-10-11,
           after we last published it — overwriting discards that edit
```

Then ask: "Publish these to `<KEY>`? (yes / edit one / cancel)". Loop on edits until the set is
approved. Only an explicit yes publishes anything. Cancelling ends the skill with nothing
written to Confluence and nothing recorded in the repo.

## Step 4 — Publish and record

1. Create or update each approved page. Pass the artefact body as markdown — these are markdown
   documents and converting them by hand loses structure. Title the page from the artefact's own
   H1, so a reader finds the same name in both places.
2. Append or update a `## Published` block at the end of each artefact that was published:

```markdown
## Published

| Target | Page | Last published |
|---|---|---|
| Confluence `<KEY>` | [<title>](<url>) | <YYYY-MM-DD> |
```

3. **Do not touch the artefact's `**Date:**` or `**Status:**` fields.** Those describe when the
   *content* was last worked on, and other skills compare them for staleness — `to-tickets`
   checks a spec's date against the surface map before filing. Publishing is not an edit to the
   document, and must not look like one.
4. Tell the user the page links. Stop — do not chain into anything further.

## Out of scope

Not built, and worth saying so rather than improvising a thin version: **GitHub wiki and any
other target** — Confluence is the only one implemented. Also absent: reading changes back from
a published page, bidirectional or scheduled sync, conflict resolution beyond flagging
divergence, publishing prototypes as pages, and page permissions or restrictions, which belong
to whoever owns the space.

If asked for one of these, say it is not built and offer the nearest thing that is.

## Do not

- Do not publish anything before the confirmation gate has been passed explicitly.
- Do not treat a published page as a source. Nothing is read back; the repo is the truth.
- Do not overwrite a page that changed after we last published it without asking.
- Do not claim a page was published when no Confluence tool was available. Stop and say so.
- Do not invent a space key or a parent page id.
- Do not publish an artefact you have not shown in the dry run.
- Do not edit the artefact beyond its `## Published` block, and never its `Date` or `Status`.
- Do not change the artefact root here. That is the family's setting, not this skill's.

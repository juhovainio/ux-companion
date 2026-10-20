# UX Companion — the artefact store

Where this family's artefacts live. Read by every skill that reads or writes one.

Skills in this family write paths as `.ux/briefs/<feature>.md`, `.ux/USERS.md` and so on.
**`.ux/` is shorthand for the configured artefact root**, not a literal directory — it only
happens to be literal by default.

## Resolving the root

Stop at the first that answers it:

1. **`.ux/config.md` exists** — use the `Root:` it names.
2. **It does not** — the root is `.ux/`. Say nothing about it and carry on; this is the default
   and the overwhelmingly common case.

`.ux/config.md` is **always resolved literally**, relative to the repository root, and is never
itself moved by the root it configures. Resolving the config through the root it defines is an
infinite regress. The same goes for `.ux/jira-project.md`: `.ux/` is where this family keeps its
*configuration*, the root is where it keeps its *artefacts*, and the two are deliberately
separate so that pointing the root elsewhere never orphans the settings that got you there.

**The config file wins over the conversation.** Unlike a Jira project key, a root has a tree of
existing files hanging off it — so a root mentioned in passing mid-session does not silently
override the recorded one. If the user asks to change it, change the config, then tell them the
existing artefacts are still at the old root and ask what to do about them. A skill cannot move
files it has not been asked to move.

## State the root before using it

**Say the resolved root out loud, in one line, before reading or writing anything:**

> Artefacts: `docs/ux/`.

This is not ceremony. Every `.ux/…` path in a skill is shorthand, and the single most likely
failure in this design is a skill resolving the root correctly and then writing to a literal
`.ux/` anyway — which succeeds, creates a second artefact tree, and is invisible until someone
goes looking for a brief that was written somewhere else. Stating the root first makes it a
fact in play rather than a rule to re-apply at every path; it also puts it in front of the user,
who can correct it in one sentence.

Skip the line when the root is the default `.ux/` and no config exists — there is nothing to
tell anyone.

## Paths written *into* an artefact are resolved paths

A skill's templates contain `.ux/…` paths that get copied into the artefact it writes — a spec's
`**Brief:**` header, for one, which `to-tickets` later pastes into a Jira description. Those are
read by people and by other tools, outside any skill that could resolve shorthand.

**Write the resolved path, never `.ux/`**, wherever a path lands inside an artefact.

Skills' frontmatter `description:` fields are the exception, and several mention `.ux/` paths.
Those are routing prose read by the host before any skill runs, not instructions — leave them
literal. They are not a thing to go and fix.

## The layout under the root is fixed

The root replaces `.ux` and nothing else. The subdirectory layout beneath it —
`briefs/`, `specs/`, `concepts/`, `evidence/`, `research/`, `competitors/`, `prototypes/`, and
the top-level `USERS.md`, `PRINCIPLES.md`, `LANDSCAPE.md`, `surface-map.md` — is not
configurable.

Artefacts cross-link each other relatively (`../briefs/<feature>.md`), which works at any root
and breaks if the layout under it is flattened or renamed.

## Never fall back silently

If the configured root cannot be read or written — it does not exist, or the host's file-access
permissions do not reach it — **stop and say so.** Do not write to `.ux/` instead.

A silent fallback splits a team's artefacts across two locations with no error, and the split is
only discovered later by someone who cannot find a document that was definitely written. Say
which root failed and why; let the user fix the path or the permission.

**Once a non-default root is resolved, reading or writing any path that still begins `.ux/` is
a bug** — not a fallback, not a reasonable default. It is the one error this design makes easy,
because such a path is syntactically fine and very nearly always correct for everyone else.

That matters most on **reads**, where it is otherwise silent. Skills are full of sensible
tolerances — "if none exists, offer `ux-discover` first", "if it does not exist, draft it", "if
missing, say so; the spec will carry an assumption". Every one of those assumes the root was
*reachable* and the file genuinely is not there. Resolve the root wrongly and they all fire at
once: a team with a full `USERS.md`, a stated set of principles and an evidence log gets
interviewed from a cold start, gets a spec carrying assumptions for facts they wrote down last
month, and gets `PRINCIPLES.md` redrafted over the top of the one they already agreed. Nothing
errors, and the output looks plausible.

So: when a config names a root and that root is missing or unreadable, **say so and stop**. Do
not fall through to the "if missing" branch. Those branches are correct only when there is no
config at all, or when the configured root is reachable and the file really is absent.

## Writing the config

Any skill in this family may write `.ux/config.md` — whichever one is in front of the user when
the question comes up, the same way `to-tickets` owns `.ux/jira-project.md` because it is the
skill that needs it. Do not route this through another skill; it is a one-time, three-field
answer.

Do not raise it unprompted. The default works, and asking where artefacts should live before
anyone has written one is exactly the door-step interrogation this family avoids.

Before recording a root, check two things and say what you found:

- **It is writable.** Verify now, so a bad path fails here rather than halfway through someone's
  first brief.
- **It is not gitignored, and it is in the repo.** These artefacts are meant to be committed —
  "the second feature starts with what the first one learned" depends on a teammate being able
  to read them. A root inside a build or temp directory silently un-commits the whole practice.
  A root *outside* the repo is allowed, since artefacts do not always belong next to code, but
  say plainly that it will not be versioned with the code and may sit outside what the host
  permits the agent to write.

```markdown
# UX artefact store

**Root:** docs/ux/
**Publish to:** confluence
**Confluence space:** PROD
**Confluence parent page:** 123456789
**Set on:** <YYYY-MM-DD> · **Confirmed by:** user
```

`Root:` is the only required field; omit the publish lines entirely when nothing is published.
The provenance line belongs to the publish target, which writes to a live external system — the
root needs none, since a directory either has your artefacts in it or does not.

## Publishing

Local markdown is **always** the source of truth. A publish target is a copy for people who will
never clone the repo — never read back from, never synced in reverse, never authoritative. This
family does not do bidirectional sync, and nothing here should grow into it.

`ux-publish` owns publishing, behind a mandatory confirmation gate. **Confluence is the only
target built.** GitHub wiki and anything else: not built — say so rather than improvising.

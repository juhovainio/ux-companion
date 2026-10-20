---
name: ux-prototype
description: Internal — do not invoke directly. Turns a design spec into something a person can actually touch — a single self-contained HTML file for a UI, or an exact session transcript for a CLI, API or agent-facing feature. Also returns what to ask the person looking at it.
allowed-tools: Read, Write, Glob, Grep
---

# UX Prototype

Follow these directives when turning a design spec into
something someone can react to.

**Artefact root.** Resolve it per `../ux-companion/references/artefact-store.md` — Glob for
`**/ux-companion/references/artefact-store.md` if that path does not resolve — and state it in
one line before reading or writing anything. Then **substitute it for the literal `.ux/`
prefix in every path below** — they are written as `.ux/…` shorthand, and once a non-default root
is resolved, touching a path that still begins `.ux/` is a bug. Any path written *into* an
artefact is the resolved path, never `.ux/`.

**Why this exists.** Nobody has ever decided they loved a product by reading a specification.
Agreement on a document is agreement on a document — it survives exactly until the first
person uses the thing. A prototype moves the disagreement forward by a month, while changing it
still costs an afternoon.

It also closes a gap in this family: `ux-review` evaluates built interfaces. Until there is a
prototype, nothing exists for it to evaluate, so every heuristic that needs a real surface
waits on engineering. It does not have to.

## What this produces

| Consumer | Artefact |
|---|---|
| A person using a UI | `.ux/prototypes/<feature>.html` — one self-contained file, opens in a browser |
| A person using a CLI | `.ux/prototypes/<feature>.md` — an exact session transcript |
| An agent or a script | `.ux/prototypes/<feature>.md` — the exact call and the exact result shape it receives |

Match the brief's and spec's filename. Create `.ux/prototypes/` if needed.

**The prototype is throwaway.** Put that in the file, at the top: this is a prototype, it has no
backend, it is not the implementation, do not extend it into one. A prototype that quietly
becomes production is how a week of exploratory HTML turns into three years of maintenance.

## Inputs

1. `.ux/specs/<feature>.md` — the spec. Its **Copy** section is the source of truth for every
   string. If no spec exists, offer `ux-design-spec` first; a prototype invented from scratch is
   a drawing of your own assumptions.
2. `.ux/USERS.md` — skill level and context of use decide how much explaining the interface
   does.
3. `.ux/surface-map.md` and the repo — existing patterns, terms and conventions to match.
4. `.ux/PRINCIPLES.md`, if it exists — it decides the details the spec does not state.

## The fidelity rule

**Real copy, real states, fake data, no backend.**

- **Real copy.** Every string comes from the spec, verbatim. If the spec is missing a string you
  need, write one, mark it in the handback as new, and offer to add it to the spec. Do not
  silently invent copy — the spec is the source of truth and this is how it quietly stops being
  one.
- **Real states.** Not only the happy path. See below.
- **Fake data.** Plausible, specific, and obviously fake on inspection. Never real user data,
  never real customer names.
- **No backend, no build step, no dependencies, no CDN.** One file, inline CSS and JS, works
  offline, opens by double-clicking. Anyone can open it; nobody has to install anything; it
  still works in six months.

Visual polish is the last thing to spend effort on and the first thing people comment on. Keep
it plain, legible and consistent, and say in the handback that the styling is not the proposal.

## Every state must be reachable

A prototype where you cannot reach the error state is a prototype of the happy path, and the
happy path is the part nobody needed to see.

Build every state the spec's **States** section names — default, empty, in-progress, error,
success — and make each one reachable by clicking. Add a small fixed **prototype controls**
strip, visibly not part of the design, that jumps straight to any state. People reviewing a
prototype will not find a state that takes four correct steps to produce.

The empty state and the error state are the two that decide whether a product feels considered.
Spend your time there, not on the dashboard.

## Accessibility is not fidelity

These are not polish and do not wait for the real build — they change the design, so they have
to be in the thing people react to:

- Semantic HTML: real `<button>`, real `<label>` tied to its input, headings in order.
- Keyboard reachable end to end, with visible focus.
- Text contrast that passes at normal size.

If the spec's design cannot be operated by keyboard, that is a finding about the spec. Report
it; do not quietly fix it in the prototype and leave the spec wrong.

## Non-GUI prototypes

A CLI, an API and an agent-facing tool all have a UX, and all can be prototyped — faster than a
UI, and with the same value. The artefact is a transcript, written exactly as it would appear:

- **CLI:** the command as typed, then the exact stdout, line for line, including spacing and
  the progress output. Then the same command failing, and the same command with nothing to
  report. Reading your own error message as a user would read it is most of the review.
- **API or agent tool:** the exact call, the exact result shape returned, with field names and
  realistic values. Then the empty result, and the failure — and check that an agent receiving
  each could tell them apart, which is Theme F's Agent lens made concrete.

Do not describe what the output would contain. Write the output.

## The reaction loop

The prototype is not the deliverable; what you learn from it is. End by telling the user how to
run it past someone, in three lines:

- **Ask them to do something, do not ask them what they think.** "Show me how you would re-run
  the failed job" beats "does this make sense?" — the second one gets you politeness.
- **Watch where they stop.** The pause before a click is the finding. Note it before they
  explain it away, and before you do.
- **Do not defend it.** Every sentence you spend explaining the prototype is a sentence of
  evidence you destroyed. If it needs narrating, that is the result.

When changes come back: **the spec is still the source of truth.** Update `.ux/specs/<feature>.md`
first, then regenerate the prototype from it. A prototype that has drifted ahead of its spec is
now the only record of the design, and it is a file nobody reads.

Notes from a real session with a real user go to `ux-research` for synthesis, not into your own
summary of what people seemed to think.

## Handoff

- `ux-review` on the prototype — it now has a real surface to evaluate, before engineering
  spent anything.
- `ux-design-spec` to fold back what the prototype revealed.
- `to-tickets` to file it in Jira, whenever the user is ready — on its own schedule, not
  automatically.

## Do not

- Do not invent copy the spec does not contain without flagging it.
- Do not build only the happy path.
- Do not use a component library, a framework, or a CDN link.
- Do not use real user data, real names, or a real customer's logo.
- Do not let the prototype become the implementation, or update it instead of the spec.
- Do not describe output where you could write it.
- Do not present a prototype as evidence that users want this. It is evidence of what the
  design is, not of whether anyone needs it.

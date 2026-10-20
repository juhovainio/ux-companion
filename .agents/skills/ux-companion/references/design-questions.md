# UX Companion — Themes

The shared criteria asset for this skill family. `ux-discover` reasons through Theme A;
`ux-concepts` works the solution space between A and B; `ux-design-spec` reasons through B–J in
its pre-build heuristic check, and through K and L in its spec (both need A and B settled, so
they land there rather than in the brief); `ux-user-context` uses the Human/Agent lens
distinction.

B–J are a **floor**: pass all of them and the result is unobjectionable, which is not the same
as good. L is the **ceiling**, and it is the one that decides whether anyone remembers this.

Authored on the `jussi-exploration` branch and vendored here unchanged. Themes A–J generalize
the `ux-review` / `cli-review` criteria to the pre-build stage; the theme-to-criterion mapping
is recorded in that branch's `design.md`. Edit this file rather than restating a theme inside
a skill — a second copy will drift from this one.

## Contents

- How to use these themes
- Grounding in research
- A — Problem & motivation
- B — Consumer(s) & flow
- C — Findability & affordance
- D — Language & clarity
- E — Consistency
- F — Feedback, trust & completion
- G — Error handling & prevention
- H — Operating context
- I — Complexity budget
- J — Empty & edge states
- K — Product opportunities
- L — Craft & the signature moment

## How to use these themes

Reason through each theme against the idea at hand — you are generating candidate answers,
not reading a questionnaire aloud to the user. A theme's questions are the thing to reason
about; they are rarely the thing to ask verbatim. For each theme, reach one of three outcomes:
an **answer** (reasoned from context, optionally backed by research), an **assumption**
(stated plainly, flagged as correctable later), or an **open question** (posed to the user,
reserved for what only they can supply).

Every theme carries a **Human lens** and an **Agent lens** — the two kinds of consumer a
feature in this repository might have: a person operating a UI or CLI, or an AI agent calling
a skill, MCP tool, or API. Apply both unless the consumer is clearly one or the other; where
it's unclear, that itself is worth a line in the brief rather than a silent guess.

## Grounding in research

Before settling an answer for a theme, judge whether a published finding would sharpen or
correct it — established usability/HCI research, prior art for the same kind of interaction,
or a domain-specific study on the stated pain point. Where it would, search for it before
reasoning alone. Prefer durable, authoritative sources (e.g. Nielsen Norman Group, Baymard
Institute, ACM/CHI publications) over a single blog post, and carry the citation into the
brief next to the answer it backs. Research grounds the *reasoning*, not the *user's own
knowledge* — a finding about users in general never overrides what the user knows about
*their* users; state both when they diverge, rather than silently preferring one.

Skip the search where the answer is settled by convention already established in this
repository, or where the question is too specific to this product for outside research to
speak to it (e.g. whether *this* team's users already do the workaround).

## A — Problem & motivation

Who has this pain point, and how do you know? What do they do today instead — a workaround, a
different tool, nothing? What does the status quo cost them (time, errors, abandoned tasks)?
How will anyone know the problem is actually solved, as opposed to merely addressed?

- **Human lens**: the "workaround" is often visible as a support ticket, a spreadsheet, or a
  manual process someone complains about.
- **Agent lens**: the "workaround" is often an agent guessing at a capability it was never
  given reliable knowledge of, or a human doing by hand what an agent could do directly —
  look for the step a human still has to perform between two automated ones.

## B — Consumer(s) & flow

Who or what initiates the flow, and who or what completes it — are they the same actor? Map
it step by step, including the steps *before* the first one anyone usually describes (how do
they arrive here at all?). At each step, will the consumer know where they are? Is the number
of steps or decisions proportionate to what's being accomplished, or could steps be combined?
How will the consumer know they succeeded, and is that signal different from "nothing went
wrong yet"?

- **Human lens**: location is reconstructible from a heading, breadcrumb, or prompt; a step
  count disproportionate to the task reads as friction even when each step is individually
  reasonable.
- **Agent lens**: "where it is in the flow" is whatever state a tool result or return value
  carries forward — if that's not in the response, the agent has no other way to know. Steps
  that could be combined often show up as two tool calls that are always made together.

## C — Findability & affordance

Will the consumer discover this at the moment they actually need it, from where they
naturally are — not from a path a determined explorer could eventually find? Does it read as
something that can be acted on at all?

- **Human lens**: assess from where a person's eyes land first — page placement, icon-only
  controls with no label, a feature buried three menu levels down.
- **Agent lens**: assess from the routing or trigger surface an agent actually reads before
  acting — a tool's name and description, the words a request would need to contain for this
  to surface at all — never from documentation an agent would have to go looking for on a
  hunch it already needs the capability to form.

## D — Language & clarity

Do names, labels, help text, and error copy say what they mean without requiring the reader
to already know the system? Is there a worked example for anything non-trivial?

- **Human lens**: a label needing re-reading, or jargon assumed without domain training.
- **Agent lens**: a parameter or field name literal enough that an agent won't guess its
  shape or meaning wrong and call it incorrectly — an agent reads what's there and acts on it
  sequentially, rather than skimming for the gist the way a person might.

## E — Consistency

Does this match the conventions already established elsewhere in the same product or tool
family — the same term for the same concept, the same interaction pattern for the same kind
of action?

- **Human lens**: a user who learned one part of the product should be able to guess how a
  new part behaves.
- **Agent lens**: an agent that has called one tool in a family should be able to guess a
  sibling tool's parameter names by pattern — inconsistency here breaks that pattern-matching
  outright, not just the look of the thing.

## F — Feedback, trust & completion

What tells the consumer this worked, partially worked, or failed — and roughly how quickly?
Before a consequential or hard-to-reverse action, is there enough information to commit with
confidence (what will happen, what's the scope of impact), or only a confirmation gate with
nothing behind it?

- **Human lens**: a visible message, spinner with context, or confirmation screen that states
  impact rather than just asking "are you sure?".
- **Agent lens**: a structured, parseable result the agent can act on next without a human in
  the loop — a silent success and a silent no-op must not look the same return value.

## G — Error handling & prevention

What are the foreseeable failure modes, and does the design prevent the ones with serious
consequences (data loss, irreversibility) before they happen, rather than only reporting them
after? When something does fail, is the message actionable, and is in-progress work
recoverable?

- **Human lens**: a confirmation step before a destructive action; an error message that says
  what to do next, not just that something went wrong.
- **Agent lens**: a message an agent can act on without a human translating it — and never a
  message that claims success while a fallback was silently substituted underneath, since an
  agent has no way to tell the difference and will report that false success onward as fact.

## H — Operating context

Does this work across every real context it will actually be used in, not only the one it was
designed against?

- **Human lens**: assistive technology, keyboard-only operation, degraded or small displays.
- **Agent lens**: headless, scripted, or automated use with no human watching — the agent
  equivalent of a CLI's `NO_COLOR` and non-terminal checks: does meaning survive when nobody
  is there to see a visual-only signal?

## I — Complexity budget

Is what's being proposed proportionate to the problem, or does it demand more from the
consumer than the task justifies? Is the most important thing the most prominent thing?

- **Human lens**: a form or screen with many competing decisions at equal visual weight; a
  one-shot action buried among administrative options.
- **Agent lens**: a tool with many required parameters and no sensible defaults forces an
  agent to guess values it has no way to determine — proportionate to an occasional power
  operation, disproportionate to a common one.

## J — Empty & edge states

What happens when there's nothing to show, or input is missing or invalid? Is the reason
given, along with what to do next?

- **Human lens**: a blank panel with no explanation reads as indistinguishable from a bug.
- **Agent lens**: an empty result with no indication of *why* (no matches vs. a failed query
  vs. not yet populated) gives an agent nothing to reason from about what to try next.

## K — Product opportunities

This is the one theme to originate rather than extract from the stated idea. Given the
problem and consumer(s) identified in Themes A and B: what adjacent value does solving this
open up that nobody asked for yet? A capability cheap to add alongside the core one. A second
consumer type — human or agent — who would benefit from the same flow with no extra design
work. A pattern here worth generalizing once it's built, so the next similar feature doesn't
start from zero. State these as opportunities, not requirements — the point is to surface them
for a decision, not to expand the scope on your own authority.

A test for "cheap enough to count as an opportunity" rather than scope creep: it extends
something the brief already decided — the same flow, the same consumer, data already being
produced — with no problem statement of its own. If stating it honestly would need its own
Theme A to justify why it matters, it's a separate idea; name it as one rather than folding it
in here.

## L — Craft & the signature moment

Themes B–J are satisfied by the absence of problems. Nothing in them is ever satisfied by the
presence of something good, which is why a design can pass all nine and still be the kind of
thing nobody mentions to a colleague. This theme is the only one that asks for a ceiling.

Which single moment in this flow would someone screenshot, quote, or still remember next week
— and does the design currently have one at all? What does it do at the point of highest
tension, which is almost always the long wait, the irreversible confirm, the first empty run,
or the failure? Where is a default chosen so well that the consumer never has to decide?

A signature moment is **cheap and specific**: one state, one transition, one sentence of copy,
one default. It is not a feature, and its cost is measured in minutes. If it would need its own
problem statement, it is Theme K or it is nothing — the ceiling is reached by doing the
existing thing unusually well, never by adding another thing.

- **Human lens**: the empty state that teaches the product instead of apologising for itself;
  the error written in plain words that names what to do next; the one transition that makes a
  wait feel handled rather than hung; the default so right that nobody opens settings. Also the
  inverse — the moment of friction you deliberately keep, because the destructive action
  *should* feel heavy.
- **Agent lens**: craft is measured in round trips avoided. A result shape complete enough that
  no second call is needed; an error naming the exact correction, so the retry is right the
  first time; a description precise enough that the right tool is picked without a guess. The
  signature moment for an agent is the chain that runs to completion without a human
  unsticking it.

Judge this one against the product's own `.ux/PRINCIPLES.md` where it exists. Craft without a
stance is decoration, and it shows: it reads as effort spent, not as a point being made.

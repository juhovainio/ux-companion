# Golden scenarios

Seven scenarios, run by hand. No eval harness for a POC — add one when running these manually
starts hurting.

Run each in a scratch directory so `.ux/` starts in a known state. Record pass/fail and what
actually happened, not what should have happened.

## Universal pass criteria

Every scenario fails if any of these is violated, regardless of its own criteria:

- **Nothing invented.** No fabricated quote, user, metric, persona or source.
- **Every claim tagged.** `**Evidence:**` with a source, or `**Assumption:**`.
- **No unconfirmed decisions.** Anything the user did not agree to is an assumption or an open
  question.
- **Nothing asked that could be reasoned.** A question the request, the repo or `.ux/` already
  answers is a failure even if the answer it gets is correct.
- **No questionnaires.** The questions that survive reasoning are asked one at a time.

---

## 1. Vague idea

**State:** empty `.ux/`.
**Input:** "I think we should add a progress bar to the installer."

**Expect**

- Router picks `ux-discover` and says why in one sentence.
- The progress bar is recorded under `Solutions already proposed`, not adopted as the goal.
- It reasons its way to the problem behind it — likely "users can't tell if a long install has
  hung" — and proposes that, rather than asking the user to supply it.
- The brief's problem statement is about the problem, not the proposed widget.
- Brief filename is named for the problem (`slow-install-no-feedback`), not the solution.

**Fails if** the brief's problem statement is "there is no progress bar", the file is called
`add-progress-bar.md`, or the first move is a question the installer's own code could answer.

---

## 2. Feature that is too large

**State:** a brief exists describing one narrow problem.
**Input:** "Design this — we'll want a settings page, admin controls, usage analytics and an
export."

**Expect**

- `ux-design-spec` runs Phase 1 before writing any spec.
- The smallest version is stated and is genuinely smaller than what was asked for.
- `Out of scope` contains real cuts with reasons — analytics and admin controls are likely
  candidates, each cut because no sentence of the brief requires it.
- Anything the user insists on keeping is recorded as added by their decision.
- `Product opportunities` does not quietly restore anything `Out of scope` just cut.

**Fails if** `Out of scope` is empty, contains only things nobody proposed, the spec silently
specifies all four additions, or a cut item reappears as an opportunity.

---

## 3. "Who is this for?" with no context

**State:** empty `.ux/`.
**Input:** "Who are the users of this tool?"

**Expect**

- Router picks `ux-user-context`.
- It reads the README and help text first, and says what it found.
- It asks rather than generating plausible personas — this is the one place asking is correct,
  because nothing in the repo can settle who the users actually are.
- Both lenses are considered: if the product exposes a CLI, an API or a skill, an agent
  consumer gets its own user section rather than a footnote.
- Unanswered questions appear as `Unknown` and under `What we do not know`.
- Confidence line reflects reality — `Mostly assumption` on a cold start is the honest answer.

**Fails if** a persona appears with an invented name, biography or demographic, if
`What we do not know` is empty, or if an obvious agent consumer is recorded only as a trailing
note.

---

## 4. Developer quick-check

**Input:** "I'm about to build a retry wrapper around our API client — am I missing anything?"

**Expect**

- Routed to `ux-design-spec` developer mode (or `ux-discover` developer mode).
- A risk list under ten bullets. **No brief, no spec, no file written.**
- At most two questions, and only for what the repo cannot answer.
- Covers the smallest version, what already exists in the repo that does part of this, and the
  themes that actually fire — likely G (error handling), F (feedback & trust), and the Agent
  lens of F, since a retry wrapper's caller is usually code.

**Fails if** it writes a file, asks its way through the themes instead of reasoning through
them, or returns a generic checklist that ignores the repo.

---

## 5. Existing context is reused

**State:** `.ux/USERS.md` with two users and `.ux/surface-map.md` both populated.
**Input:** "Help me design a way to re-run a failed job."

**Expect**

- The skill states what it read from `.ux/` in one line.
- It does **not** re-ask who the users are or how the product is structured.
- `Fit with the existing product` names specific patterns and terms from the surface map.
- The spec's consumer section references a user from `USERS.md` by name.

**Fails if** it asks a question `.ux/` already answers, or writes a spec that names no existing
pattern.

---

## 6. Divergence that actually diverges

**State:** a brief exists for a narrow problem. No `.ux/PRINCIPLES.md`.
**Input:** "What are our options here?"

**Expect**

- Router picks `ux-concepts`.
- It drafts `.ux/PRINCIPLES.md` and **shows it for correction** before using it. Each principle
  names a trade-off ("we would rather X than Y"), not a virtue.
- Prior art is searched, and every claim about another product is a link or is tagged
  `**Assumption:**`. Nothing is asserted about a competitor from memory as fact.
- At least five directions, filling the required slots — including the conventional baseline
  and the smallest possible one, which is sometimes documentation or a better default.
- The directions **differ in approach, not in degree.** Apply the difference test: two that
  would produce the same flow with different labels are one direction.
- One recommendation, scored against the brief's success criteria and the principles before
  feasibility, and **the user is asked to choose** rather than told.
- Each rejected direction records what it was better at.

**Fails if** the five directions are one idea in five sizes, a competitor behaviour is stated
without a source, feasibility decides the ranking, a spec or flow gets written here, or it
hands a direction to `ux-design-spec` without the user agreeing to it.

---

## 7. Prototype someone can react to

**State:** `.ux/specs/<feature>.md` exists with a populated Copy and States section.
**Input:** "Can I see this?"

**Expect**

- Router picks `ux-prototype`.
- One self-contained file. No build step, no npm, no framework, no CDN link — it opens by
  double-clicking and works offline.
- **Every string comes from the spec's Copy section, verbatim.** Anything new is flagged in the
  handback and offered back to the spec.
- Empty, in-progress, error and success states all exist and are **reachable by clicking**, via
  a visibly non-design prototype-controls strip.
- Semantic HTML, labelled inputs, keyboard-reachable with visible focus.
- The file says at the top that it is a prototype and not the implementation.
- The handback says what to ask the person looking at it — a task to perform, not an opinion to
  give.
- For a CLI or agent-facing feature, the artefact is an exact transcript — the real output text
  and the real result shape, including the failure and the empty case — not a description of
  what the output would contain.

**Fails if** only the happy path is built, the error state takes four correct steps to reach,
copy is invented without being flagged, it pulls in a library, it uses real user data, or it
asks "what do you think?" instead of giving the user a task to run.

---

## Scoring

A scenario passes only if its own expectations **and** all universal criteria hold. Note
near-misses verbatim — "it asked two clarifying questions instead of one" is the kind of drift
that only shows up by being written down.

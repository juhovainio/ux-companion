# Reconciling `main` and `jussi-exploration`

Two independent builds of UX Companion from the same ideation doc, neither aware of the
other. Both are on the remote; nothing is merged.

| | `jussi-exploration` (`3d92451`) | `main` (`f7b482d`) |
|---|---|---|
| Shape | One skill | Router + four skills |
| Method | Reason from context first; ask only what only the user can supply | Interview one question at a time |
| Criteria | Themes A–K, each with a **Human lens** and an **Agent lens** | Inline heuristic table in `ux-design-spec` Phase 3 |
| Research | `WebSearch`, with rules for citation and for research-vs-user-knowledge conflict | None |
| Output | One brief, **offered** for saving, not saved by default | Files always written to `.ux/` |
| Tools | `Read, WebSearch` — `Write` deliberately omitted | `Read, Write, Glob, Grep` |
| Validation | Run for real against an agent-facing idea; two gaps found and fixed | Five scenarios written, none run |
| Rationale | `design.md` — decisions recorded with what was rejected and why | `plans/poc-plan.md` |

## What each got right

**`jussi-exploration`:**

- **The Agent lens is the best idea in either branch.** "Findability for an agent is the tool
  name and description it reads before acting, never documentation it would have to already
  know it needs." Nothing on `main` approaches this, and the ideation doc's criterion H asks
  for exactly it.
- **Reason-first is better than interview-first**, and the critique in his SKILL.md lands on
  `main` directly: *"a user who is only answering what's asked never gets the benefit of
  reasoning done on their behalf, and ends up with the same gaps they started with, just
  itemized."* The four-step resolution order — reason, research, assume, ask — reserves the
  user's attention for what only they can supply.
- **Theme K (Product opportunities) is generative**, originated rather than waited for.
  `main` has no equivalent; every one of its skills is reactive.
- **The premise-mismatch rule** — when reasoning reveals the idea's own premise doesn't hold,
  state the assumption *and* escalate, never one or the other — came out of a real run.
- **`Write` omitted deliberately**, because saving is the occasional path, not the happy one.
- **It was actually run.** `main` has not been.

**`main`:**

- Persisted `.ux/` artifacts, so the second feature starts with what the first learned.
- The overengineering gate as an explicit phase with a forced cut list.
- Evidence/Assumption tagging as a hard rule on every claim.
- Separation of concerns across skills, so `USERS.md` is reusable across features rather than
  re-derived per idea.
- Router, which the ideation doc's table specifies and which `jussi-exploration` has no
  equivalent of.

## The overlap is not cosmetic

Jussi's single skill produces: Problem & motivation → Flow → Design considerations (C–J) →
Product opportunities → Open questions.

That is, section for section, `main`'s `ux-discover` brief **plus** `ux-design-spec`'s spec
and heuristic check — reached by reasoning instead of interviewing, and emitted as one
document instead of two files.

So this is not "two skills that happen to be adjacent." It is **two implementations of the
same pipeline** at different granularity. Shipping both unchanged is precisely the duplication
`ux-design-spec`'s own overengineering gate exists to catch.

Also: both are named `ux-companion`. Whichever is installed second silently shadows the other.

## Option 1 — Keep both, different granularity

Jussi's becomes the fast path (one-shot reasoning, nothing persisted); `main`'s pipeline
becomes the thorough path (artifacts in `.ux/`). The router picks between them.

- **For:** no authored work is discarded; the fast path genuinely suits a developer who wants
  a think, not a filing system.
- **Against:** two things answer "turn my idea into a brief," and a user has to understand the
  distinction before they can choose. Themes A–K would be maintained in one skill while
  `ux-design-spec` keeps a second, thinner criteria list — they will drift.

## Option 2 — Merge: his themes and stance become the engine inside the pipeline (recommended)

- `references/design-questions.md` moves to a shared location and becomes **the** criteria
  asset for the family. `ux-design-spec` Phase 3 reads it instead of its inline table.
- `ux-discover` adopts the **reason-first resolution order** and the premise-mismatch rule.
  Its interview stops being the method and becomes the last step of the method — which still
  satisfies the ideation doc's "one question at a time," because the questions that survive
  reasoning are asked one at a time. Live-interview mode is unaffected.
- The **Human/Agent lens** applies throughout: `ux-user-context` gains it properly rather than
  the thin `Non-human consumers` section it has now.
- **Theme K** becomes a required section of the design spec.
- `design.md`'s rationale merges into `plans/`.
- Jussi's SKILL.md stops being a separate skill. Its content survives; its identity as a
  standalone entry point does not.

- **For:** one pipeline, one criteria asset, no drift, no name collision, and the strongest
  ideas from both survive.
- **Against:** it deletes a colleague's skill as a skill — and that skill is the only part of
  either branch that has been tested against a real idea. The reasoning-only, nothing-written
  interaction is also genuinely different from a pipeline that always writes files, and
  Option 2 keeps the stance but loses that lightweight shape.

## Recommendation

**Option 2**, with one carve-out: keep the lightweight no-files path as `ux-design-spec`'s
existing developer mode, extended to run the full A–K reasoning and return a brief without
writing anything. That preserves what Jussi's skill actually feels like to use, without a
second entry point that competes with `ux-discover`.

Either way, two things should happen first:

1. **Jussi should have a say** — this restructures his work, and his branch is the one with a
   real run behind it.
2. **Run the golden scenarios** against whatever merges. Neither branch's combined form has
   been exercised, and `main` has never been run at all.

## Not in question — applied

These landed regardless of which option is chosen, because they are strict improvements to
`main`. All are now on `main`; `origin/jussi-exploration` is untouched.

- ✅ **Themes A–K with the Human/Agent lens** replace `ux-design-spec`'s inline heuristic
  table. Vendored unchanged to `.agents/skills/ux-companion/references/design-questions.md`,
  under the router because they belong to the family. Phase 3 reads B–J from there.
- ✅ **Reason-first resolution order** (reason → research → assume → ask) replaces
  interview-first as `ux-discover`'s default method. The interview is now the last step: the
  questions that survive reasoning are still asked one at a time.
- ✅ **The premise-mismatch rule** — state the assumption *and* escalate, never one or the
  other — in `ux-discover`.
- ✅ **Research grounding**, including the rule that a general finding never overrides the
  user's knowledge of their own users. `WebSearch` added to `ux-discover` and
  `ux-design-spec`.
- ✅ **Theme K (Product opportunities)** is a required section of the design spec — the
  family's only generative step. It sits in the spec rather than the brief because it needs
  both Theme A (the problem, from the brief) and Theme B (flow and consumer, decided in the
  spec). Guarded so it cannot reopen the overengineering gate's cuts.
- ✅ **The Human/Agent lens in `ux-user-context`**, replacing the thin `Non-human consumers`
  section. An agent consumer now gets a full user section with the same fields, not a footnote.

Also updated for consistency: the family conventions in the router and the plan, the golden
scenarios, and the `references/` upgrade trigger — which this tripped by sharing rather than
by length.

**Still open:** the structural call (Option 1 vs Option 2), and running the golden scenarios.
Both wait on Jussi.

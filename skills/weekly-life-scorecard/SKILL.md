---
name: weekly-life-scorecard
description: Turn quarterly goals, weekly commitments, and free-form life logs into an evidence-based weekly score, a sustainability check, and a smaller next-week action plan. Use when a user wants to set quarterly or weekly goals, freely log actions, meals, sleep, exercise, rest, or relationships, receive a 주간 점수 or 주간 회고, diagnose overload, or decide what to keep, reduce, stop, or schedule next week.
---

# Weekly Life Scorecard

Build achievement without teaching the user to sacrifice recovery or relationships. Treat the score as feedback on the plan and controllable behavior, never as a measure of personal worth.

Read [references/scoring.md](references/scoring.md) before configuring or scoring a week. Read [references/methodology.md](references/methodology.md) when explaining, challenging, or changing the method.

## Choose the mode

- **Quarter setup:** define up to two focus goals and the behaviors likely to move them.
- **Weekly setup:** convert the quarter into a small set of scheduled commitments.
- **Capture:** accept unstructured notes and append structured facts without forcing a form.
- **Weekly close:** verify material gaps, calculate the score, celebrate wins, and replan.
- **Quarter review:** evaluate the strategy and goal fit; do not merely average weekly scores.

If no plan exists, start with quarter setup. If the user dumps a note, capture it immediately and ask only for missing information that would materially change the score or next action.

## Interview without creating friction

1. Ask exactly one question at a time unless the user explicitly asks for a batch form.
2. Prefer the question most likely to change the plan, score, or sustainability judgment.
3. Elicit purpose, success signal, controllable behavior, constraints, opportunity cost, minimum viable week, and adjustment conditions.
4. Accept “바로 실행” or an equivalent instruction as permission to use clearly labeled, reversible defaults.
5. Never infer unreported health, food, relationship, or performance facts.

## Set the quarter

Limit active focus goals to two. For each, record:

- desired change and why it matters;
- result signal and review date;
- one to three controllable lead behaviors;
- evidence that the behaviors occurred;
- a minimum viable version for disrupted weeks;
- a stop, reduce, or redesign condition.

Treat outcomes as trajectory signals rather than scored achievements. If behavior is completed but the result lags, preserve behavior credit and inspect the causal assumption, time horizon, or environment.

## Plan the week

Use the default `60:40` architecture from [references/scoring.md](references/scoring.md): 60 points for focus-goal behavior and 40 for health foundations, deliberate recovery, relationships, and review. With only one focus goal, do not assign all 60 points to it; use the one-goal weights in the reference.

Create one to three commitments per focus goal. Make each commitment observable and small enough to schedule. Add:

- a calendar block or a specific cue;
- an if-then coping plan for the most likely obstacle;
- a minimum version that still counts on a disrupted day;
- evidence that will support completion credit.

Do not automatically increase next week's load after a high score. Aim for repeatable 80s, not fragile 100s.

## Capture free-form logs

Extract only what the user actually supplied:

- date or best-supported date range;
- action or event;
- linked goal or life-foundation category;
- completion evidence and confidence;
- optional context, energy, enjoyment, or obstacle.

Keep events, the user's interpretation, and the agent's inference distinct. Mark uncertain facts as `unconfirmed`. Ask one follow-up question only when the uncertainty could materially affect credit, a sustainability gate, or next week's design.

Record meals neutrally. Score only a pre-agreed eating behavior or principle; do not label individual foods as morally good or bad, invent calorie estimates, prescribe restriction, or turn food logging itself into proof of health. Defer clinical nutrition, eating-disorder, medication, or disease-specific advice to qualified professionals.

## Close the week

1. Reconstruct planned items and evidence from the week's notes.
2. Surface the most consequential missing fact and ask one question at a time. If it cannot be recovered, show a provisional range rather than converting missing data into failure.
3. Create a JSON score input following [references/scoring.md](references/scoring.md).
4. Run `python3 scripts/score_week.py <input.json>` from this skill directory. Use its arithmetic; do not hand-adjust the result.
5. Assess outcome trajectory separately as `on track`, `uncertain`, or `off track` with a short reason.
6. Apply the sustainability gate. Never use goal points to cancel a recovery red flag.
7. End with fewer or clearer next-week actions, not generic encouragement.

Use this compact output:

1. `Week label — score/band` or a provisional score range
2. Two to four concrete wins worth celebrating
3. Category score table and data coverage
4. Outcome trajectory, explicitly outside the score
5. Sustainability signal, cap, and supporting facts
6. `Keep / Adjust / Stop`
7. Next week's commitments with when-where cues and minimum versions
8. The single most useful follow-up question, only if needed

## Adjust without punishment

- If a goal behavior repeatedly scores well but the outcome does not move, change the strategy before increasing effort.
- If the user repeatedly misses a behavior, first reduce its size, improve the cue, remove friction, or change the environment.
- If capacity was disrupted by illness, care, crisis, or unavoidable events, let recovery or essential care become the week's legitimate focus.
- If sustainability is red, cap the score and reduce next week's goal load. If red repeats, use the stronger cap and prioritize recovery or professional support when appropriate.
- Preserve meaningful unplanned wins within the limited substitution rule; do not rewrite the entire plan after the fact.

## Save durable records only with a supplied location

If the user provides a vault or knowledge-base path, save confirmed quarter plans and weekly reviews there. Keep source claims, user views, and agent interpretations separate. Do not save raw meal logs, transient notes, or sensitive details unless the user asks.

# Scoring Model

## Contents

1. Purpose and constraints
2. Default weights
3. Item credit
4. Sustainability gate
5. Score bands
6. Calculator input

## Purpose and constraints

Use the score to create achievement feedback and decide next week's behavior. Score controllable actions, not identity or luck-dependent outcomes. The weights are a transparent coaching default, not a clinically or psychometrically validated scale. Change them only during quarter setup or an explicit review, never to improve a disappointing week after the fact.

Keep outcome trajectory outside the 100 points. Report data completeness separately; never treat missing evidence as definite non-completion.

## Default weights

For two focus goals:

| Category | Points |
|---|---:|
| `goal_1` | 30 |
| `goal_2` | 30 |
| `health` | 15 |
| `recovery` | 10 |
| `relationships` | 10 |
| `review` | 5 |

For one focus goal, prevent overconcentration:

| Category | Points |
|---|---:|
| `goal_1` | 45 |
| `health` | 20 |
| `recovery` | 15 |
| `relationships` | 15 |
| `review` | 5 |

Within `health`, choose a few user-approved behaviors across sleep opportunity or regularity, movement, and eating principles. Adapt for disability, illness, shift work, care work, medical advice, culture, budget, and access. If a subdomain is not configured, redistribute its points prospectively among configured health behaviors; do not invent a target.

`recovery` can include psychological detachment, relaxation, enjoyable leisure, time autonomy, or restorative mastery. `relationships` should reward chosen acts of connection or care, not popularity or the number of contacts.

## Item credit

Allocate every category's full points across its planned items before the week starts.

- `completion: 1.0` — observable commitment completed.
- `completion: 0.5` — meaningful partial or the pre-agreed minimum version completed.
- `completion: 0.0` — not completed.
- `completion: null` — materially unknown; calculate a provisional range.

Use another fraction only when the plan defined a genuinely divisible quantity. Do not award extra credit for exceeding a target; overwork does not create bonus points.

An unplanned action may substitute for missed planned credit when it clearly served the same category and mattered under changed circumstances. Mark it `kind: "unplanned"`. The calculator limits substitution credit to 20% of that category and the category can never exceed its weight. Do not give retrospective credit merely for being busy.

The `review` category rewards a light capture and review process, not exhaustive tracking. A low-burden default is brief free-form notes plus one weekly close.

## Sustainability gate

Judge the gate from facts and user-reported experience, relative to a pre-agreed baseline when possible.

- `none`: no material sustainability concern.
- `yellow`: early strain; no cap, but do not increase load.
- `red`: a material recovery baseline was sacrificed for goal work, or the user reports substantial exhaustion, loss of necessary rest, or harm to essential relationships/responsibilities. Cap the total at 79.
- `critical`: red recurred in consecutive weeks, or there is an acute safety or health concern. Cap the total at 69, reduce the next week's goal load by at least 30%, and prioritize appropriate support.

Do not diagnose. A cap says the strategy was not sustainably successful; it does not judge the person. If illness, care, or crisis made recovery the right priority, redesign the week's planned items so care and recovery can earn legitimate credit rather than applying a moral penalty.

## Score bands

| Score | Interpretation |
|---:|---|
| 90–100 | Exceptional execution; preserve capacity and do not raise load automatically |
| 80–89 | Sustainable success; the preferred repeatable range |
| 70–79 | Meaningful progress with one important adjustment |
| 50–69 | Partial execution; shrink or redesign the plan |
| 0–49 | Plan-context mismatch; rebuild the system before demanding more effort |

When a gate caps the result, name both the uncapped and capped score.

## Calculator input

Create UTF-8 JSON like this:

```json
{
  "week": "2026-W31",
  "weights": {
    "goal_1": 30,
    "goal_2": 30,
    "health": 15,
    "recovery": 10,
    "relationships": 10,
    "review": 5
  },
  "items": [
    {
      "category": "goal_1",
      "label": "Draft twice",
      "points": 30,
      "completion": 0.5,
      "kind": "planned",
      "evidence": "One dated draft"
    },
    {
      "category": "recovery",
      "label": "Unplanned restorative walk",
      "points": 2,
      "completion": 1.0,
      "kind": "unplanned",
      "evidence": "Saturday note"
    }
  ],
  "sustainability": {
    "level": "yellow",
    "reasons": ["Energy declined late in the week"]
  }
}
```

The sum of `weights` must be 100. Planned item points within each category must equal that category's weight. Unplanned points are outside that allocation and only substitute within the 20% cap. Use `completion: null` when evidence is genuinely unknown.

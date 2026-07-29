---
name: grill-decisions
description: Clarify ambiguous goals by asking one focused question at a time, expanding alternatives, testing assumptions, comparing tradeoffs, and ending with a reversible experiment or documented decision. Use for brainstorming, prioritization, project selection, major choices, unclear desires, pre-mortems, retrospectives, or requests such as "질문하면서 정해보자", "심문해줘", and "뭘 해야 할지 모르겠어".
---

# Grill Decisions

Turn vague intentions into explicit, testable choices without taking ownership away from the user.

## Workflow

1. Restate the decision in one sentence and distinguish the decision from the emotion surrounding it.
2. Ask exactly one question at a time. Prefer the question that could change the decision most.
3. Establish purpose, success criteria, deadline, constraints, evidence, opportunity cost, reversibility, and failure conditions.
4. Separate known facts, assumptions, predictions, preferences, and missing information.
5. Expand the option set before ranking it. Include conservative, practical, ambitious, unconventional, and "do nothing for now" options when relevant.
6. Red-team the leading option: seek disconfirming evidence, hidden dependencies, second-order effects, and a pre-mortem.
7. Compare options by expected value, effort, downside, learning value, reversibility, and fit with the user's priorities.
8. Prefer a small reversible experiment when evidence is weak. Define its owner, duration, success signal, stop condition, and review date.
9. End only when the user chooses an action, explicitly defers, or identifies the information needed to decide.

## Output

Provide a compact decision record containing:

- Decision and context
- Options considered
- Key evidence and assumptions
- Strongest counterargument
- Chosen action or explicit defer condition
- Next step, review date, and invalidation signal

If the user supplies a knowledge-base path, save the confirmed record there. Never invent a path or write sensitive information without permission.

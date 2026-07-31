#!/usr/bin/env python3
"""Deterministically calculate a Weekly Life Scorecard from JSON."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any


CAPS = {"none": 100.0, "yellow": 100.0, "red": 79.0, "critical": 69.0}


class ScoreInputError(ValueError):
    pass


def _number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ScoreInputError(f"{field} must be a number")
    value = float(value)
    if not math.isfinite(value):
        raise ScoreInputError(f"{field} must be finite")
    return value


def _band(score: float) -> str:
    if score >= 90:
        return "exceptional_execution"
    if score >= 80:
        return "sustainable_success"
    if score >= 70:
        return "meaningful_progress_adjust"
    if score >= 50:
        return "partial_execution_redesign"
    return "plan_context_mismatch"


def calculate(data: dict[str, Any]) -> dict[str, Any]:
    weights_raw = data.get("weights")
    if not isinstance(weights_raw, dict) or not weights_raw:
        raise ScoreInputError("weights must be a non-empty object")

    weights: dict[str, float] = {}
    for category, raw_weight in weights_raw.items():
        if not isinstance(category, str) or not category:
            raise ScoreInputError("weight category names must be non-empty strings")
        weight = _number(raw_weight, f"weights.{category}")
        if weight <= 0:
            raise ScoreInputError(f"weights.{category} must be greater than zero")
        weights[category] = weight

    if not math.isclose(sum(weights.values()), 100.0, abs_tol=1e-6):
        raise ScoreInputError("weights must sum to 100")

    items = data.get("items")
    if not isinstance(items, list) or not items:
        raise ScoreInputError("items must be a non-empty array")

    category_state = {
        name: {
            "weight": weight,
            "planned_allocated": 0.0,
            "planned_min": 0.0,
            "planned_max": 0.0,
            "unplanned_min": 0.0,
            "unplanned_max": 0.0,
            "known_items": 0,
            "total_items": 0,
        }
        for name, weight in weights.items()
    }

    unknown_items: list[str] = []
    for index, item in enumerate(items):
        prefix = f"items[{index}]"
        if not isinstance(item, dict):
            raise ScoreInputError(f"{prefix} must be an object")
        category = item.get("category")
        if category not in weights:
            raise ScoreInputError(f"{prefix}.category is not present in weights")
        label = item.get("label")
        if not isinstance(label, str) or not label.strip():
            raise ScoreInputError(f"{prefix}.label must be a non-empty string")
        points = _number(item.get("points"), f"{prefix}.points")
        if points <= 0:
            raise ScoreInputError(f"{prefix}.points must be greater than zero")
        kind = item.get("kind", "planned")
        if kind not in {"planned", "unplanned"}:
            raise ScoreInputError(f"{prefix}.kind must be planned or unplanned")

        completion_raw = item.get("completion")
        if completion_raw is None:
            completion_min, completion_max = 0.0, 1.0
            unknown_items.append(label.strip())
        else:
            completion = _number(completion_raw, f"{prefix}.completion")
            if not 0.0 <= completion <= 1.0:
                raise ScoreInputError(f"{prefix}.completion must be between 0 and 1 or null")
            completion_min = completion_max = completion

        state = category_state[category]
        state["total_items"] += 1
        if completion_raw is not None:
            state["known_items"] += 1
        if kind == "planned":
            state["planned_allocated"] += points
            state["planned_min"] += points * completion_min
            state["planned_max"] += points * completion_max
        else:
            state["unplanned_min"] += points * completion_min
            state["unplanned_max"] += points * completion_max

    for category, state in category_state.items():
        if not math.isclose(state["planned_allocated"], state["weight"], abs_tol=1e-6):
            raise ScoreInputError(
                f"planned points for {category} must equal its weight "
                f"({state['planned_allocated']:g} != {state['weight']:g})"
            )

    category_results: dict[str, Any] = {}
    uncapped_min = 0.0
    uncapped_max = 0.0
    known_count = 0
    item_count = 0
    for category, state in category_state.items():
        substitution_limit = state["weight"] * 0.20
        unplanned_min = min(state["unplanned_min"], substitution_limit)
        unplanned_max = min(state["unplanned_max"], substitution_limit)
        earned_min = min(state["weight"], state["planned_min"] + unplanned_min)
        earned_max = min(state["weight"], state["planned_max"] + unplanned_max)
        uncapped_min += earned_min
        uncapped_max += earned_max
        known_count += state["known_items"]
        item_count += state["total_items"]
        category_results[category] = {
            "earned_min": round(earned_min, 2),
            "earned_max": round(earned_max, 2),
            "weight": round(state["weight"], 2),
            "unplanned_credit_min": round(unplanned_min, 2),
            "unplanned_credit_max": round(unplanned_max, 2),
        }

    sustainability = data.get("sustainability", {})
    if not isinstance(sustainability, dict):
        raise ScoreInputError("sustainability must be an object")
    level = sustainability.get("level", "none")
    if level not in CAPS:
        raise ScoreInputError("sustainability.level must be none, yellow, red, or critical")
    reasons = sustainability.get("reasons", [])
    if not isinstance(reasons, list) or any(not isinstance(reason, str) for reason in reasons):
        raise ScoreInputError("sustainability.reasons must be an array of strings")

    cap = CAPS[level]
    capped_min = min(uncapped_min, cap)
    capped_max = min(uncapped_max, cap)
    provisional = bool(unknown_items)
    result: dict[str, Any] = {
        "week": data.get("week"),
        "provisional": provisional,
        "score_min": round(capped_min, 2),
        "score_max": round(capped_max, 2),
        "uncapped_score_min": round(uncapped_min, 2),
        "uncapped_score_max": round(uncapped_max, 2),
        "sustainability": {
            "level": level,
            "cap": int(cap),
            "cap_applied": uncapped_max > cap,
            "reasons": reasons,
        },
        "data_coverage": round(known_count / item_count, 3),
        "unknown_items": unknown_items,
        "categories": category_results,
    }
    if not provisional:
        result["score"] = round(capped_min, 2)
        result["uncapped_score"] = round(uncapped_min, 2)
        result["band"] = _band(capped_min)
    return result


def _read_input(path: str) -> dict[str, Any]:
    if path == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(path).read_text(encoding="utf-8")
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ScoreInputError("top-level JSON value must be an object")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Path to score JSON, or - for stdin")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    args = parser.parse_args()

    try:
        result = calculate(_read_input(args.input))
    except (OSError, json.JSONDecodeError, ScoreInputError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

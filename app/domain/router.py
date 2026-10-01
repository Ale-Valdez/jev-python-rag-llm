from app.domain.decisions import ChoiceDecision, DecisionResult, BooleanDecision


def route(decision: DecisionResult) -> str:
    intent = decision.answers["intent"]

    if not isinstance(intent, ChoiceDecision):
        raise ValueError("Expected intent to be a ChoiceDecision")

    if intent.choice == "billing":
        return "billing"

    if intent.choice == "technical_support":
        return "support"

    return "other"

HUMAN_ESCALATION_THRESHOLD = 0.80


def requires_human(decision: DecisionResult) -> bool:
    human = decision.answers["needsHuman"]

    if not isinstance(human, BooleanDecision):
        raise ValueError(
            "Expected needsHuman to be a BooleanDecision"
        )

    return human.probability >= HUMAN_ESCALATION_THRESHOLD

def decide_next_step(decision: DecisionResult) -> str:
    if requires_human(decision):
        return "human"

    return route(decision)


def route_next_action(decision: DecisionResult) -> str:
    result = decision.answers["next_action"]

    if not isinstance(result, ChoiceDecision):
        raise ValueError(
            "Expected next_action to be a ChoiceDecision"
        )

    if result.choice == "rag":
        return "rag"

    if result.choice == "llm":
        return "llm"

    if result.choice == "clarify":
        return "clarify"

    raise ValueError(
        f"Unknown next_action: {result.choice}"
    )
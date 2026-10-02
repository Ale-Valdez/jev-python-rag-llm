""" from app.domain.decisions import (
    BooleanDecision,
    ChoiceDecision,
    DecisionResult,
)
from app.domain.router import (
    HUMAN_ESCALATION_THRESHOLD,
    decide_next_step,
    route_next_action,
)


def make_decision(
    *,
    intent: str,
    needs_human: float,
) -> DecisionResult:
    return DecisionResult(
        answers={
            "intent": ChoiceDecision(
                choice=intent,
                probabilities={intent: 1.0},
                confidence=1.0,
            ),
            "needsHuman": BooleanDecision(
                probability=needs_human,
            ),
        }
    )



def test_route_next_action_to_rag():
    decision = DecisionResult(
        answers={
            "next_action": ChoiceDecision(
                choice="rag",
                probabilities={
                    "rag": 1.0,
                    "llm": 0.0,
                    "other": 0.0,
                },
                confidence=1.0,
            )
        }
    )

    assert route_next_action(decision) == "rag"


def test_route_next_action_to_llm():
    decision = DecisionResult(
        answers={
            "next_action": ChoiceDecision(
                choice="llm",
                probabilities={
                    "rag": 0.0,
                    "llm": 1.0,
                    "other": 0.0,
                },
                confidence=1.0,
            )
        }
    )

    assert route_next_action(decision) == "llm"


def test_route_next_action_to_other():
    decision = DecisionResult(
        answers={
            "next_action": ChoiceDecision(
                choice="other",
                probabilities={
                    "rag": 0.0,
                    "llm": 0.0,
                    "other": 1.0,
                },
                confidence=1.0,
            )
        }
    )

    assert route_next_action(decision) == "other" """
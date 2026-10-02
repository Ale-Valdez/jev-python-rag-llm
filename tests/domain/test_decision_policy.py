from app.domain.decisions import ChoiceDecision, DecisionResult
from app.domain.decision_policy import DecisionPolicy


def test_accepts_decision_when_margin_is_sufficient():
    decision = DecisionResult(
        answers={
            "next_action": ChoiceDecision(
                choice="rag",
                probabilities={
                    "rag": 0.80,
                    "llm": 0.15,
                    "clarify": 0.05,
                },
                confidence=0.90,
            )
        }
    )

    policy = DecisionPolicy(margin_threshold=0.30)

    resolved = policy.resolve(decision)

    assert resolved.action == "rag"
    assert resolved.accepted is True
    assert resolved.reason == "sufficient_margin"

def test_falls_back_when_margin_is_low():
    decision = DecisionResult(
        answers={
            "next_action": ChoiceDecision(
                choice="rag",
                probabilities={
                    "rag": 0.52,
                    "llm": 0.48,
                    "clarify": 0.00,
                },
                confidence=0.40,
            )
        }
    )

    policy = DecisionPolicy(
        margin_threshold=0.30,
        fallback_action="clarify",
    )

    resolved = policy.resolve(decision)

    assert resolved.action == "clarify"
    assert resolved.accepted is False
    assert resolved.reason == "low_margin"

def test_accepts_decision_at_exact_margin_threshold():
    decision = DecisionResult(
        answers={
            "next_action": ChoiceDecision(
                choice="rag",
                probabilities={
                    "rag": 0.60,
                    "llm": 0.30,
                    "clarify": 0.10,
                },
                confidence=0.80,
            )
        }
    )

    policy = DecisionPolicy(margin_threshold=0.30)

    resolved = policy.resolve(decision)

    assert resolved.action == "rag"
    assert resolved.accepted is True


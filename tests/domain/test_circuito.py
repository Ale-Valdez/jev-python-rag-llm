from app.domain.decision_policy import DecisionPolicy
from app.domain.decisions import ChoiceDecision, DecisionResult
from app.mock.decision_model import MockDecisionModel
from app.graph.graph import build_graph


def test_graph_falls_back_to_clarify_on_low_margin():
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

    model = MockDecisionModel(decision)

    policy = DecisionPolicy(
        margin_threshold=0.30,
        fallback_action="clarify",
    )

    graph = build_graph(
        decision_model=model,
        decision_policy=policy,
    )

    state = {
        "conversation": {
            "current_message": "¿Y el otro?",
        }
    }

    result = graph.invoke(state)

    assert result["resolved_decision"].action == "clarify"
    assert result["resolved_decision"].accepted is False
    assert result["resolved_decision"].reason == "low_margin"
    assert result["route"] == "clarify"

def test_graph_accepts_rag_when_margin_is_sufficient():
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

    model = MockDecisionModel(decision)

    policy = DecisionPolicy(
        margin_threshold=0.30,
        fallback_action="clarify",
    )

    graph = build_graph(
        decision_model=model,
        decision_policy=policy,
    )

    state = {
        "conversation": {
            "current_message": "¿Qué dice el documento sobre autenticación?",
        }
    }

    result = graph.invoke(state)

    assert result["resolved_decision"].action == "rag"
    assert result["resolved_decision"].accepted is True
    assert result["resolved_decision"].reason == "sufficient_margin"
    assert result["route"] == "rag"

def test_graph_uses_configured_fallback_action():
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

    model = MockDecisionModel(decision)

    policy = DecisionPolicy(
        margin_threshold=0.30,
        fallback_action="llm",
    )

    graph = build_graph(
        decision_model=model,
        decision_policy=policy,
    )

    state = {
        "conversation": {
            "current_message": "¿Y el otro?",
        }
    }

    result = graph.invoke(state)

    assert result["resolved_decision"].action == "llm"
    assert result["resolved_decision"].accepted is False
    assert result["resolved_decision"].reason == "low_margin"
    assert result["route"] == "llm"
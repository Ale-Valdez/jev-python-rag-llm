from app.graph.graph import build_graph
from app.mock.decision_model import MockDecisionModel


def test_graph_routes_to_rag():
    graph = build_graph(
        MockDecisionModel(next_action="rag")
    )

    result = graph.invoke(
        {
            "conversation": {
                "current_message": "What does chapter 4 say about ecosystems?"
            }
        }
    )

    assert result["route"] == "rag"


def test_graph_routes_to_llm():
    graph = build_graph(
        MockDecisionModel(next_action="llm")
    )

    result = graph.invoke(
        {
            "conversation": {
                "current_message": "Can you simplify the previous explanation?"
            }
        }
    )

    assert result["route"] == "llm"


def test_graph_routes_to_other():
    graph = build_graph(
        MockDecisionModel(next_action="other")
    )

    result = graph.invoke(
        {
            "conversation": {
                "current_message": "Hello!"
            }
        }
    )

    assert result["route"] == "other"
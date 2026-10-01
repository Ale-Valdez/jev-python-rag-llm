from langgraph.graph import END, START, StateGraph

from app.domain.decision_model import DecisionModel
from app.domain.router import route_next_action
from app.graph.nodes import (
    decision_node,
    llm_node,
    other_node,
    rag_node,
    clarify_node,
)
from app.graph.state import GraphState

def route_graph(state: GraphState) -> str:
    return route_next_action(state["decision"])


def build_graph(decision_model: DecisionModel):
    workflow = StateGraph(GraphState)

    workflow.add_node(
        "decision",
        lambda state: decision_node(
            state,
            decision_model,
        ),
    )

    workflow.add_node("rag", rag_node)
    workflow.add_node("llm", llm_node)
    workflow.add_node("other", other_node)
    workflow.add_node("clarify", clarify_node)

    workflow.add_edge(START, "decision")

    workflow.add_conditional_edges(
        "decision",
        route_graph,
        {
            "rag": "rag",
            "llm": "llm",
            "clarify": "clarify",
        },
    )

    workflow.add_edge("rag", END)
    workflow.add_edge("llm", END)
    workflow.add_edge("other", END)
    workflow.add_edge("clarify", END)

    return workflow.compile()
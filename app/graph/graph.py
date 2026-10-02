from langgraph.graph import END, START, StateGraph

from app.domain.decision_model import DecisionModel
from app.domain.decision_policy import DecisionPolicy
#from app.domain.router import route_next_action
from app.graph.nodes import (
    decision_node,
    llm_node,
    other_node,
    rag_node,
    clarify_node,
)
from app.graph.state import GraphState
from app.domain.actions import Action

def route_graph(state: GraphState) -> Action:
    resolved = state["resolved_decision"]
    return resolved.action


def tools_node(state: GraphState) -> dict:
    print("Executing tools node")
    return {"route": "tools"}

def build_graph(decision_model: DecisionModel, decision_policy: DecisionPolicy):
    workflow = StateGraph(GraphState)

    workflow.add_node(
        "decision",
        lambda state: decision_node(
            state,
            decision_model,
            decision_policy,
        ),
    )

    workflow.add_node("rag", rag_node)
    workflow.add_node("llm", llm_node)
    workflow.add_node("clarify", clarify_node)
    workflow.add_node("tools", tools_node)
    workflow.add_edge(START, "decision")

    workflow.add_conditional_edges(
        "decision",
        route_graph,
        {
            Action.RAG: "rag",
            Action.LLM: "llm",
            Action.CLARIFY: "clarify",
            Action.TOOLS: "tools",
        },
    )

    workflow.add_edge("rag", END)
    workflow.add_edge("llm", END)
    workflow.add_edge("clarify", END)
    workflow.add_edge("tools", END)

    return workflow.compile()
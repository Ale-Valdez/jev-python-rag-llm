from app.application.decision_context import DecisionContext
from app.application.decision_questions import DECISION_QUESTIONS
from app.domain.decision_model import DecisionModel
from app.graph.state import GraphState


def decision_node(
    state: GraphState,
    decision_model: DecisionModel,
) -> dict:
    conversation = state["conversation"]

    context = DecisionContext(
        current_message=conversation["current_message"],
        active_flow=conversation.get("active_flow"),
        last_action=conversation.get("last_action"),
        context=conversation.get("context", {}),
    )

    result = decision_model.evaluate(
        context=context,
        questions=DECISION_QUESTIONS,
    )

    return {"decision": result}


def rag_node(state: GraphState) -> dict:
    print("Executing RAG flow")
    return {"route": "rag"}


def llm_node(state: GraphState) -> dict:
    print("Executing LLM flow")
    return {"route": "llm"}


def other_node(state: GraphState) -> dict:
    print("Executing other flow")
    return {"route": "other"}

def clarify_node(state: GraphState) -> dict:
    print("Executing clarification flow")
    return {"route": "clarify"}
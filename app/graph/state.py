from typing import TypedDict

from app.domain.decisions import DecisionResult


class ConversationState(TypedDict, total=False):
    current_message: str
    active_flow: str
    last_action: str
    context: dict[str, str]


class GraphState(TypedDict, total=False):
    conversation: ConversationState
    decision: DecisionResult
    route: str
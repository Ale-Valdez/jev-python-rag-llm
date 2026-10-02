from typing import TypedDict

from app.domain.decisions import DecisionResult
from app.domain.resolved_decision import ResolvedDecision


class ConversationState(TypedDict, total=False):
    current_message: str
    active_flow: str
    last_action: str
    context: dict[str, str]


class GraphState(TypedDict, total=False):
    conversation: ConversationState
    decision: DecisionResult
    resolved_decision: ResolvedDecision
    route: str
from typing import Protocol

from app.domain.decisions import DecisionResult
from app.application.decision_context import DecisionContext


class DecisionModel(Protocol):

    def evaluate(
        self,
        *,
        context: DecisionContext,
        questions: dict,
    ) -> DecisionResult:
        ...
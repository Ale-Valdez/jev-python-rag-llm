from app.application.decision_context import DecisionContext
from app.domain.decisions import (
    ChoiceDecision,
    DecisionResult,
)


class MockDecisionModel:
    def __init__(self, result: DecisionResult):
        self.result = result

    def evaluate(
        self,
        *,
        context: DecisionContext,
        questions: dict,
    ) -> DecisionResult:
        return self.result
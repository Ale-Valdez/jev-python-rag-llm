from app.domain.decisions import DecisionResult
from app.domain.decision_model import DecisionModel
from app.jev.client import JevClient
from app.jev.mapper import map_decision_result
from app.application.decision_context import DecisionContext

class JevDecisionModel:
    def __init__(self, client: JevClient) -> None:
        self.client = client

    def evaluate(
        self,
        *,
        context: DecisionContext,
        questions: dict,
    ) -> DecisionResult:
        raw_result = self.client.evaluate(
            context=context,
            questions=questions,
        )

        return map_decision_result(raw_result)
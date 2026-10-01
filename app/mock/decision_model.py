from app.application.decision_context import DecisionContext
from app.domain.decisions import (
    ChoiceDecision,
    DecisionResult,
)


class MockDecisionModel:
    def __init__(self, next_action: str = "rag"):
        self.next_action = next_action

    def evaluate(
        self,
        *,
        context: DecisionContext,
        questions: dict,
    ) -> DecisionResult:
        return DecisionResult(
            answers={
                "next_action": ChoiceDecision(
                    choice=self.next_action,
                    probabilities={
                        "rag": 1.0 if self.next_action == "rag" else 0.0,
                        "llm": 1.0 if self.next_action == "llm" else 0.0,
                        "other": 1.0 if self.next_action == "other" else 0.0,
                    },
                    confidence=1.0,
                )
            }
        )
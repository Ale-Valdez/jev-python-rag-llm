from typesafe_sdk import ChoiceAnswer, NoulAnswer

from app.domain.decisions import (
    ChoiceDecision,
    DecisionResult,
    BooleanDecision,
)


def map_decision_result(response) -> DecisionResult:
    answers = {}

    for name, answer in response.answers.items():

        if isinstance(answer, ChoiceAnswer):
            answers[name] = ChoiceDecision(
                choice=answer.choice,
                probabilities=answer.probabilities,
                confidence=answer.confidence,
            )

        elif isinstance(answer, NoulAnswer):
            answers[name] = BooleanDecision(
                probability=answer.noul,
            )

        else:
            raise ValueError(
                f"Unsupported Jev answer type: {type(answer).__name__}"
            )

    return DecisionResult(answers=answers)
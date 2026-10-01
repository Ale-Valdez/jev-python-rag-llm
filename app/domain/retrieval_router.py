from app.domain.decisions import BooleanDecision, DecisionResult


def needs_retrieval(decision: DecisionResult) -> bool:
    result = decision.answers["needs_retrieval"]

    if not isinstance(result, BooleanDecision):
        raise ValueError(
            "Expected needs_retrieval to be a BooleanDecision"
        )

    return result.probability >= 0.5
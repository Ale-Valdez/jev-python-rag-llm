from dataclasses import dataclass

from app.domain.decisions import ChoiceDecision, DecisionResult
from app.domain.resolved_decision import ResolvedDecision
from app.domain.actions import Action


@dataclass(frozen=True)
class DecisionPolicy:
    margin_threshold: float = 0.30
    fallback_action: Action = Action.CLARIFY

    def resolve(self, decision: DecisionResult) -> ResolvedDecision:
        action = decision.answers["next_action"]

        if not isinstance(action, ChoiceDecision):
            raise ValueError(
                "Expected next_action to be a ChoiceDecision"
            )

        probabilities = action.probabilities

        selected_probability = probabilities[action.choice]

        other_probabilities = [
            probability
            for choice, probability in probabilities.items()
            if choice != action.choice
        ]

        if not other_probabilities:
            raise ValueError(
                "ChoiceDecision must contain at least two choices"
            )

        second_probability = max(other_probabilities)

        margin = selected_probability - second_probability

        if margin < self.margin_threshold:
            return ResolvedDecision(
                action=self.fallback_action,
                accepted=False,
                reason="low_margin",
            )

        return ResolvedDecision(
            action=Action(action.choice),
            accepted=True,
            reason="sufficient_margin",
        )
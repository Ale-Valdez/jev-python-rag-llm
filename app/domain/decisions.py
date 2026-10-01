from dataclasses import dataclass


@dataclass(frozen=True)
class BooleanDecision:
    probability: float


@dataclass(frozen=True)
class ChoiceDecision:
    choice: str
    probabilities: dict[str, float]
    confidence: float


@dataclass(frozen=True)
class ScoreDecision:
    score: float
    probabilities: dict[str, float]
    confidence: float


Decision = BooleanDecision | ChoiceDecision | ScoreDecision

@dataclass(frozen=True)
class DecisionResult:
    answers: dict[str, Decision]
from dataclasses import dataclass

from app.domain.actions import Action


@dataclass(frozen=True)
class ResolvedDecision:
    action: Action
    accepted: bool
    reason: str


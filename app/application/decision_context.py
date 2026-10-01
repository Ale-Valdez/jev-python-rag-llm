from dataclasses import dataclass, field


@dataclass(frozen=True)
class DecisionContext:
    current_message: str
    active_flow: str | None = None
    last_action: str | None = None
    context: dict[str, str] = field(default_factory=dict)
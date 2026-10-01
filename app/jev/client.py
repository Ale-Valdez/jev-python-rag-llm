from typesafe_sdk import TypeSafeClient
from dotenv import load_dotenv
from app.application.decision_context import DecisionContext

load_dotenv()

class JevClient:
    def __init__(self) -> None:
        self.client = TypeSafeClient()

    def _build_state(self, context: DecisionContext) -> dict:
        state = {
            "current_message": context.current_message,
        }

        if context.active_flow:
            state["active_flow"] = context.active_flow

        if context.last_action:
            state["last_action"] = context.last_action

        if context.context:
            state["context"] = context.context

        return state

    def evaluate(
        self,
        *,
        context: DecisionContext,
        questions: dict,
    ):
        state = self._build_state(context)

        return self.client.system_one(
            state=state,
            questions=questions,
        )
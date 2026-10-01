from app.domain.decisions import (
    BooleanDecision,
    ChoiceDecision,
    ScoreDecision,
)
from app.jev.client import JevClient
from app.jev.model import JevDecisionModel
from app.mock.decision_model import MockDecisionModel
from app.domain.router import route


def main() -> None:
    """ model = JevDecisionModel(
        client=JevClient(),
    ) """
    model = MockDecisionModel(intent="technical_support")
    result = model.evaluate(
        state=(
            "The customer was charged twice for their subscription. "
            "They need the problem resolved today because their "
            "account is currently blocked."
        ),
        questions={
            "intent": {
                "type": "choice",
                "criteria": {
                    "technical_support": (
                        "Problems with software functionality "
                        "or technical issues."
                    ),
                    "billing": (
                        "Questions or problems involving charges, "
                        "payments, invoices, or subscriptions."
                    ),
                    "sales": (
                        "Questions about purchasing products or services."
                    ),
                    "other": (
                        "Anything that does not fit the other categories."
                    ),
                },
                "instructions": (
                    "What is the customer's primary intent?"
                ),
            },
            "needsHuman": {
                "type": "boolean",
                "instructions": (
                    "Does this conversation require human intervention?"
                ),
            },
            "urgency": {
                "type": "score",
                "criteria": [
                    "Not urgent",
                    "Somewhat urgent",
                    "Urgent",
                    "Extremely urgent",
                ],
                "instructions": (
                    "How urgent is this customer request?"
                ),
            },
        },
    )


    next_step = route(result)
    print(f"Next step: {next_step}")
    if next_step == "billing":
        print("Executing billing flow")

    elif next_step == "support":
        print("Executing support flow")

    elif next_step == "other":
        print("Executing other flow")
    else:
        raise ValueError(f"Unknown next step: {next_step}")

    print("=== DOMAIN RESULT ===")

    for name, decision in result.answers.items():
        print(f"\n{name}:")
        print(f"  Python type: {type(decision).__name__}")
        print(f"  Value: {decision}")

    print("\n=== DOMAIN ACCESS ===")

    intent = result.answers["intent"]
    human = result.answers["needsHuman"]
    urgency = result.answers["urgency"]

    if isinstance(intent, ChoiceDecision):
        print(f"Intent: {intent.choice}")
        print(f"Intent confidence: {intent.confidence}")

    if isinstance(human, BooleanDecision):
        print(f"Human probability: {human.probability}")

    if isinstance(urgency, ScoreDecision):
        print(f"Urgency score: {urgency.score}")
        print(f"Urgency confidence: {urgency.confidence}")


if __name__ == "__main__":
    main()
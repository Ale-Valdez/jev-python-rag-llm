from app.jev.client import JevClient


def main() -> None:
    client = JevClient()

    result = client.evaluate(
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

    print("=== MULTI DECISION ===")

    for name, answer in result["answers"].items():
        print(f"\n{name}:")
        print(answer)


if __name__ == "__main__":
    main()
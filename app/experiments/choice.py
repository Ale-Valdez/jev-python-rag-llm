from app.jev.client import JevClient


def main() -> None:
    client = JevClient()

    result = client.evaluate(
        state=(
            "The customer says they were charged twice "
            "for the same subscription."
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
            }
        },
    )

    print("=== CHOICE ===")
    print(result)


if __name__ == "__main__":
    main()
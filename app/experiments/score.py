from app.jev.client import JevClient


def main() -> None:
    client = JevClient()

    result = client.evaluate(
        state=(
            "The customer has been unable to access their account "
            "for three days and says this is blocking their work."
        ),
        questions={
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
            }
        },
    )

    print("=== SCORE ===")
    print(result)


if __name__ == "__main__":
    main()
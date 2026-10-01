from app.jev.client import JevClient


def main() -> None:
    client = JevClient()

    result = client.evaluate(
        state=(
            "The support agent fixed the checkout problem "
            "and all tests are passing."
        ),
        questions={
            "continueWorking": {
                "type": "boolean",
                "instructions": "Should the agent take another step?",
            }
        },
    )

    answer = result["answers"]["continueWorking"]

    print("=== BOOLEAN ===")
    print(f"Type:        {answer['type']}")
    print(f"Probability: {answer['probability']}")


if __name__ == "__main__":
    main()
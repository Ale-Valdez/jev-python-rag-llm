import os

import requests


API_URL = "https://ai-gateway.vercel.sh/v1/evaluate"


def evaluate():
    api_key = os.environ["AI_GATEWAY_API_KEY"]
    print(api_key)
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "typesafe-ai/jev",
        "state": (
            "The support agent fixed the checkout problem "
            "and all tests are passing."
        ),
        "questions": {
            "continueWorking": {
                "type": "boolean",
                "instructions": (
                    "Should the agent take another step?"
                ),
            }
        },
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def main():
    result = evaluate()

    print("Jev response:")
    print(result)


if __name__ == "__main__":
    main()
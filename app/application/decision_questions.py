from typesafe_sdk import Choice, Noul

NEXT_ACTION = Choice(
    instructions=(
        "What should the system do next with the user's current request?"
    ),
    criteria={
        "rag": (
            "The user needs new information from the document knowledge base "
            "to answer the current request."
        ),
        "llm": (
            "The user's request can be answered using information already "
            "available in the conversation, without retrieving new document information."
        ),
        "clarify": (
            "The system cannot safely determine which action to take because "
            "the user's request lacks information needed to answer or retrieve "
            "the correct information. In this case, asking the user a clarification "
            "question is preferable to guessing."
        )
    },
)

NEEDS_RETRIEVAL = Noul(
    instructions=(
        "Does the user's current request require retrieving "
        "new information from the document knowledge base?"
    ),
)


DECISION_QUESTIONS = {
    "next_action": NEXT_ACTION,
}
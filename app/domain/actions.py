from enum import StrEnum


class Action(StrEnum):
    RAG = "rag"
    LLM = "llm"
    CLARIFY = "clarify"
    TOOLS = "tools"
PREVIOUS_ANSWERS = {
    # Explicit retrieval
    "A1": "El documento explica brevemente qué es RAG.",
    "A2": "El documento habla brevemente sobre desarrollo de software.",
    "A3": "El documento menciona algunos lenguajes de programación.",
    "A4": "El documento explica algunos conceptos generales de programación.",
    "A5": "El documento introduce el concepto de recuperación de información.",
    "A6": "El documento explica brevemente cómo funcionan los agentes.",

    # Transformation
    "B1": "RAG combina recuperación de información y generación de texto.",
    "B2": "RAG utiliza documentos relevantes para proporcionar contexto al modelo.",
    "B3": "RAG combina una etapa de recuperación con una etapa de generación.",
    "B4": "Un agente puede utilizar herramientas para obtener información.",
    "B5": "La recuperación permite encontrar información relevante.",
    "B6": "RAG recupera información relevante antes de generar una respuesta.",

    # Contextual
    "C1": "RAG primero recupera información relevante y después genera una respuesta.",
    "C2": "Después de recuperar los documentos, el sistema genera la respuesta.",
    "C3": "El primer paso es recuperar información relevante.",
    "C4": "RAG significa Retrieval-Augmented Generation.",
    "C5": "El sistema recupera fragmentos relevantes y los utiliza como contexto.",
    "C6": "La recuperación permite utilizar información procedente de los documentos.",

    # Ambiguous
    "D1": "El documento explica que RAG combina recuperación y generación.",
    "D2": "El documento presenta dos estrategias diferentes para recuperar información.",
    "D3": "La respuesta anterior explicó cómo funciona la recuperación.",
    "D4": "El documento habla sobre recuperación y generación.",
    "D5": "La respuesta anterior explicó los componentes principales de RAG.",
    "D6": "El documento contiene información sobre recuperación de documentos.",

    # Conversation
    "E1": "La explicación anterior describió cómo funciona RAG.",
    "E2": "La respuesta anterior explicó el concepto de RAG.",
    "E3": "Acabamos de revisar cómo funciona el sistema.",
    "E4": "La respuesta anterior explicó el concepto solicitado.",
    "E5": "La explicación anterior cubrió los puntos principales.",
    "E6": "La respuesta anterior explicó el funcionamiento general.",
}

CASES = [
    # ============================================================
    # RAG — requires new information
    # ============================================================

    {
        "name": "R1",
        "category": "rag",
        "previous_answer": (
            "El documento explica brevemente qué es RAG."
        ),
        "message": (
            "¿Qué dice sobre seguridad?"
        ),
        "expected": "rag",
    },
    {
        "name": "R2",
        "category": "rag",
        "previous_answer": (
            "El documento explica cómo funciona la recuperación."
        ),
        "message": (
            "¿Qué menciona sobre bases de datos?"
        ),
        "expected": "rag",
    },
    {
        "name": "R3",
        "category": "rag",
        "previous_answer": (
            "El documento introduce LangGraph."
        ),
        "message": (
            "¿Qué dice sobre los checkpoints?"
        ),
        "expected": "rag",
    },
    {
        "name": "R4",
        "category": "rag",
        "previous_answer": (
            "El documento explica los conceptos básicos de agentes."
        ),
        "message": (
            "¿Hay una sección sobre herramientas?"
        ),
        "expected": "rag",
    },
    {
        "name": "R5",
        "category": "rag",
        "previous_answer": (
            "El documento describe el funcionamiento general del sistema."
        ),
        "message": (
            "¿Qué menciona sobre autenticación?"
        ),
        "expected": "rag",
    },
    {
        "name": "R6",
        "category": "rag",
        "previous_answer": (
            "El documento explica qué es un modelo de lenguaje."
        ),
        "message": (
            "¿Habla también sobre embeddings?"
        ),
        "expected": "rag",
    },
    {
        "name": "R7",
        "category": "rag",
        "previous_answer": (
            "El documento presenta una introducción a RAG."
        ),
        "message": (
            "¿En qué parte explica Qdrant?"
        ),
        "expected": "rag",
    },
    {
        "name": "R8",
        "category": "rag",
        "previous_answer": (
            "El documento explica la arquitectura general."
        ),
        "message": (
            "¿Qué componentes menciona para almacenar los documentos?"
        ),
        "expected": "rag",
    },
    {
        "name": "R9",
        "category": "rag",
        "previous_answer": (
            "El documento explica cómo funciona el flujo de recuperación."
        ),
        "message": (
            "¿Qué dice sobre los permisos de los usuarios?"
        ),
        "expected": "rag",
    },
    {
        "name": "R10",
        "category": "rag",
        "previous_answer": (
            "El documento explica los conceptos principales."
        ),
        "message": (
            "Buscá qué dice sobre multitenancy."
        ),
        "expected": "rag",
    },

    # ============================================================
    # LLM — can answer from conversation
    # ============================================================

    {
        "name": "L1",
        "category": "llm",
        "previous_answer": (
            "RAG combina recuperación de información y generación de texto."
        ),
        "message": (
            "¿Podés explicarlo más fácil?"
        ),
        "expected": "llm",
    },
    {
        "name": "L2",
        "category": "llm",
        "previous_answer": (
            "RAG primero recupera información relevante y después genera una respuesta."
        ),
        "message": (
            "¿Podés resumirlo en una frase?"
        ),
        "expected": "llm",
    },
    {
        "name": "L3",
        "category": "llm",
        "previous_answer": (
            "Un agente puede utilizar herramientas para obtener información."
        ),
        "message": (
            "Dame un ejemplo."
        ),
        "expected": "llm",
    },
    {
        "name": "L4",
        "category": "llm",
        "previous_answer": (
            "La recuperación permite encontrar información relevante "
            "dentro de los documentos."
        ),
        "message": (
            "¿Podés explicarlo con palabras más simples?"
        ),
        "expected": "llm",
    },
    {
        "name": "L5",
        "category": "llm",
        "previous_answer": (
            "Qdrant almacena vectores que representan fragmentos de información."
        ),
        "message": (
            "¿Y para qué sirve eso?"
        ),
        "expected": "llm",
    },
    {
        "name": "L6",
        "category": "llm",
        "previous_answer": (
            "LangGraph permite representar un flujo como un grafo de estados."
        ),
        "message": (
            "¿Podés darme una explicación más corta?"
        ),
        "expected": "llm",
    },
    {
        "name": "L7",
        "category": "llm",
        "previous_answer": (
            "El sistema recupera documentos antes de generar la respuesta."
        ),
        "message": (
            "¿Por qué hace las dos cosas?"
        ),
        "expected": "llm",
    },
    {
        "name": "L8",
        "category": "llm",
        "previous_answer": (
            "El modelo utiliza el contexto recuperado para generar una respuesta."
        ),
        "message": (
            "Explicámelo como si fuera principiante."
        ),
        "expected": "llm",
    },
    {
        "name": "L9",
        "category": "llm",
        "previous_answer": (
            "Un embedding representa información como un vector numérico."
        ),
        "message": (
            "Dame una analogía."
        ),
        "expected": "llm",
    },
    {
        "name": "L10",
        "category": "llm",
        "previous_answer": (
            "El sistema divide los documentos en fragmentos antes de indexarlos."
        ),
        "message": (
            "¿Podés explicarme por qué?"
        ),
        "expected": "llm",
    },

    # ============================================================
    # CLARIFY — insufficient / ambiguous information
    # ============================================================

    {
        "name": "C1",
        "category": "clarify",
        "previous_answer": (
            "El documento presenta dos estrategias diferentes."
        ),
        "message": (
            "¿Y el otro?"
        ),
        "expected": "clarify",
    },
    {
        "name": "C2",
        "category": "clarify",
        "previous_answer": (
            "El documento contiene varios ejemplos."
        ),
        "message": (
            "¿Y ese?"
        ),
        "expected": "clarify",
    },
    {
        "name": "C3",
        "category": "clarify",
        "previous_answer": (
            "La respuesta anterior mencionó varias alternativas."
        ),
        "message": (
            "¿Cuál?"
        ),
        "expected": "clarify",
    },
    {
        "name": "C4",
        "category": "clarify",
        "previous_answer": (
            "Hay diferentes componentes involucrados en el sistema."
        ),
        "message": (
            "¿Y ese?"
        ),
        "expected": "clarify",
    },
    {
        "name": "C5",
        "category": "clarify",
        "previous_answer": (
            "La arquitectura utiliza diferentes servicios."
        ),
        "message": (
            "¿Cuál de los dos?"
        ),
        "expected": "clarify",
    },
    {
        "name": "C6",
        "category": "clarify",
        "previous_answer": (
            "La respuesta anterior mencionó varias opciones."
        ),
        "message": (
            "¿Y cuál?"
        ),
        "expected": "clarify",
    },
    {
        "name": "C7",
        "category": "clarify",
        "previous_answer": (
            "El documento habla de varios enfoques."
        ),
        "message": (
            "¿Cuál es mejor?"
        ),
        "expected": "clarify",
    },
    {
        "name": "C8",
        "category": "clarify",
        "previous_answer": (
            "La explicación anterior mencionó distintos componentes."
        ),
        "message": (
            "¿Ese?"
        ),
        "expected": "clarify",
    },
    {
        "name": "C9",
        "category": "clarify",
        "previous_answer": (
            "El documento presenta diferentes alternativas."
        ),
        "message": (
            "¿Cuál de ellos?"
        ),
        "expected": "clarify",
    },
    {
        "name": "C10",
        "category": "clarify",
        "previous_answer": (
            "La respuesta anterior mencionó dos posibilidades."
        ),
        "message": (
            "¿Y la otra?"
        ),
        "expected": "clarify",
    },
]

VARIANTS = {
    "A — message": {},
    "B — last_action": {
        "last_action": "rag_answer",
    },
    "C — active_flow": {
        "active_flow": "rag",
    },
    "D — both": {
        "active_flow": "rag",
        "last_action": "rag_answer",
    },
    "F — previous_answer": {
        "context": {
            "previous_answer": ...
        },
    },
}
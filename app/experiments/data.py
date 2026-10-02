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


CASE_2 =[ 
    # ============================================================
    # RAG
    # ============================================================

    {
        "name": "R1",
        "message": "¿Qué dice el documento sobre las vacaciones?",
        "expected": "rag",
    },
    {
        "name": "R2",
        "message": "Según el documento, ¿cuántos días de licencia corresponden?",
        "expected": "rag",
    },
    {
        "name": "R3",
        "message": "¿Qué requisitos establece el documento para solicitar una licencia?",
        "expected": "rag",
    },
    {
        "name": "R4",
        "message": "Compará lo que dice el documento sobre vacaciones y licencias.",
        "expected": "rag",
    },
    {
        "name": "R5",
        "message": "¿Qué dice el documento sobre los feriados?",
        "expected": "rag",
    },
    {
        "name": "R6",
        "message": "¿Cuál es el procedimiento descrito en el documento?",
        "expected": "rag",
    },
    {
        "name": "R7",
        "message": "Según el documento, ¿quién puede solicitar esta licencia?",
        "expected": "rag",
    },
    {
        "name": "R8",
        "message": "¿El documento menciona algún período de prueba?",
        "expected": "rag",
    },
    {
        "name": "R9",
        "message": "¿Qué condiciones establece el documento para trabajar desde casa?",
        "expected": "rag",
    },
    {
        "name": "R10",
        "message": "¿Podés buscar en el documento qué dice sobre horas extras?",
        "expected": "rag",
    },

    # ============================================================
    # LLM
    # ============================================================

    {
        "name": "L1",
        "message": "¿Qué significa la palabra resiliencia?",
        "expected": "llm",
    },
    {
        "name": "L2",
        "message": "Explicame qué es una API REST.",
        "expected": "llm",
    },
    {
        "name": "L3",
        "message": "Dame un ejemplo sencillo de una clase en Python.",
        "expected": "llm",
    },
    {
        "name": "L4",
        "message": "¿Qué diferencia hay entre una lista y una tupla en Python?",
        "expected": "llm",
    },
    {
        "name": "L5",
        "message": "¿Por qué usarías una cola de mensajes?",
        "expected": "llm",
    },
    {
        "name": "L6",
        "message": "¿Qué ventajas tiene usar Docker?",
        "expected": "llm",
    },
    {
        "name": "L7",
        "message": "¿Qué es una función pura?",
        "expected": "llm",
    },
    {
        "name": "L8",
        "message": "Explicame qué significa idempotencia.",
        "expected": "llm",
    },
    {
        "name": "L9",
        "message": "Resumí lo que acabás de explicarme.",
        "previous_answer": (
            "La idempotencia significa que realizar una misma operación "
            "varias veces produce el mismo efecto que realizarla una sola vez."
        ),
        "expected": "llm",
    },
    {
        "name": "L10",
        "message": "¿Por qué una arquitectura por capas puede ser útil?",
        "expected": "llm",
    },

    # ============================================================
    # TOOLS
    # ============================================================

    {
        "name": "T1",
        "message": "¿Qué temperatura hace actualmente en Buenos Aires?",
        "expected": "tools",
    },
    {
        "name": "T2",
        "message": "Reservame un turno para mañana a las 15.",
        "expected": "tools",
    },
    {
        "name": "T3",
        "message": "Cancelá mi último pedido.",
        "expected": "tools",
    },
    {
        "name": "T4",
        "message": "¿Cuánto dinero tengo disponible actualmente?",
        "expected": "tools",
    },
    {
        "name": "T5",
        "message": "Transferí $50.000 a Juan.",
        "expected": "tools",
    },
    {
        "name": "T6",
        "message": "¿Cuál es el estado de mi último pedido?",
        "expected": "tools",
    },
    {
        "name": "T7",
        "message": "¿Qué turnos hay disponibles para mañana?",
        "expected": "tools",
    },
    {
        "name": "T8",
        "message": "Cambiale la dirección de envío a mi último pedido.",
        "expected": "tools",
    },
    {
        "name": "T9",
        "message": "Mandale un mensaje a Juan avisándole que llego tarde.",
        "expected": "tools",
    },
    {
        "name": "T10",
        "message": "¿Qué hora es actualmente en Tokio?",
        "expected": "tools",
    },

    # ============================================================
    # AMBIGUOUS / CONTEXTUAL
    # ============================================================

    {
        "name": "A1",
        "message": "¿Y el otro?",
        "previous_answer": (
            "Hay dos alternativas disponibles, una para clientes nuevos "
            "y otra para clientes existentes."
        ),
        "expected": "llm",
    },
    {
        "name": "A2",
        "message": "Hacé eso.",
        "previous_answer": (
            "Podemos modificar el sistema o reemplazar completamente "
            "la implementación actual."
        ),
        "expected": "llm",
    },
    {
        "name": "A3",
        "message": "¿Cuál de los dos?",
        "previous_answer": (
            "Hay dos configuraciones posibles para el sistema."
        ),
        "expected": "llm",
    },
    {
        "name": "A4",
        "message": "Reservalo para mañana.",
        "previous_answer": (
            "Tenemos disponibles varios turnos para reservar."
        ),
        "expected": "tools",
    },
    {
        "name": "A5",
        "message": "Cancelalo.",
        "previous_answer": (
            "Tu último pedido es el número 4521 y figura como pendiente."
        ),
        "expected": "tools",
    },
]

    # ============================================================
    # TOOLS — requires external tools
    # ============================================================
CASES_TOOLS = [
    {
        "name": "T1",
        "message": "¿Qué temperatura hace actualmente en Buenos Aires?",
        "previous_answer": "",
        "expected": "tools",
    },
    {
        "name": "T2",
        "message": "Reservame un turno para mañana a las 15.",
        "previous_answer": "",
        "expected": "tools",
    },
    {
        "name": "T3",
        "message": "Cancelá mi último pedido.",
        "previous_answer": "",
        "expected": "tools",
    },
    {
        "name": "T4",
        "message": "¿Qué es una temperatura alta?",
        "previous_answer": "",
        "expected": "llm",
    },
    {
        "name": "T5",
        "message": "¿Qué dice el documento sobre las vacaciones?",
        "previous_answer": "",
        "expected": "rag",
    },
    {
        "name": "T6",
        "message": "Hacé lo del otro.",
        "previous_answer": (
            "Hay dos alternativas disponibles, una para clientes nuevos "
            "y otra para clientes existentes."
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
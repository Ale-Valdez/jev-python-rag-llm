from app.graph.graph import build_graph
from app.mock.decision_model import MockDecisionModel
from app.jev.model import JevDecisionModel
from app.jev.client import JevClient

model = MockDecisionModel(
    intent="sales",
    needs_human=0.20,
)

""" model =JevDecisionModel(
    client=JevClient(),
) """

graph = build_graph(model)

result = graph.invoke(
    {
        "message":(  
            "I was charged twice for my subscription " 
            "and my account is currently blocked.",
        ),
    }
)

print(result)
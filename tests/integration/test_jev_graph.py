from app.graph.graph import build_graph
from app.jev.client import JevClient
from app.jev.model import JevDecisionModel
import pytest
@pytest.mark.integration
def test_jev_drives_langgraph():
    decision_model = JevDecisionModel(
        JevClient()
    )

    graph = build_graph(decision_model)

    result = graph.invoke(
        {
            "conversation": {
                "current_message": (
                    "Can you explain what chapter 4 says about ecosystems?"
                )
            }
        }
    )

    print(result)

    assert "decision" in result
    assert "route" in result
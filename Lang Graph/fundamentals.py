from langgraph.graph import StateGraph
from typing import TypedDict

class State(TypedDict):
    text: str
    count: int


def node1(state):
    return {
        "text" : state["text"] + "Hello from First Node ",
        "count" : state["count"] + 1
    }

def node2(state):
    return {
        "text" : state["text"] + " Hello from Second Node",
        "count" : state["count"] + 1
    }

graph = StateGraph(State)

graph.add_node("First Node",node1)
graph.add_node("Second Node",node2)

graph.set_entry_point("First Node")

graph.add_edge("First Node","Second Node")

graph.set_finish_point("Second Node")

app = graph.compile()

result = app.invoke(
    {
        "text": "hello",
        "count" : 0
    }
)

print(result)

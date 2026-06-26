from langgraph.graph import StateGraph,END
from typing import TypedDict
from langchain_core.messages import HumanMessage
from langgraph.graph.message import add_messages
from typing import Annotated
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
# TASK 1 (Creating a simple 2 Node Graph)

# class State(TypedDict):
#     text: str
#     count: int


# def node1(state):
#     return {
#         "text" : state["text"] + "Hello from First Node ",
#         "count" : state["count"] + 1
#     }

# def node2(state):
#     return {
#         "text" : state["text"] + " Hello from Second Node",
#         "count" : state["count"] + 1
#     }

# graph = StateGraph(State)

# graph.add_node("First Node",node1)
# graph.add_node("Second Node",node2)

# graph.set_entry_point("First Node")

# graph.add_edge("First Node","Second Node")

# graph.set_finish_point("Second Node")

# app = graph.compile()

# result = app.invoke(
#     {
#         "text": "hello",
#         "count" : 0
#     }
# )

# print(result)

# TASK 2 (BUILDING AGENT USING LANGGRAPH)

class State(TypedDict):
    messages : Annotated[list, add_messages]

search = DuckDuckGoSearchRun()

@tool
def calculator(a: int,b: int) -> int:
    """Multiply two numbers"""
    return (a * b) 
@tool
def web_search(query: str) -> str:
    """Perform a web search for the given query"""
    return search.run(query)

@tool
def web_scraper(url: str) -> str:
    """Scrape the data of the website"""
    cleaned = ""
    if (url.startswith("http://") or url.startswith("https://")):
        try:
            r = requests.get(url,timeout=10)
            if r.status_code != 200:
                    return (f"Website {url} cannot be reached Error: {r.status_code}")

            
            soup = BeautifulSoup(r.text,"html.parser")

            data = soup.find_all(["h1","h2","h3","h4","h5","h6","p"])
                    
            for el in data:
                cleaned += el.text.strip() + "\n"

        except Exception as e:   
            return str(e)
    else:
         return ("Invalid URL Provided")
    return cleaned

def chatbot(state):
     response = model_with_tools.invoke(state["messages"])

     return {
          "messages" : [response]
     }

def should_continue(state):
     last_message = state["messages"][-1]

     if last_message.tool_calls:
          return "tool"
     
     return END
          
tools = [calculator,web_search,web_scraper]

model_with_tools = model.bind_tools(tools)

graph = StateGraph(State)

tools_node = ToolNode(tools)

graph.add_node("chatbot",chatbot)

graph.add_node("Tool_node",tools_node)

graph.set_entry_point("chatbot")

graph.add_conditional_edges(
     "chatbot",
     should_continue,
     {
        "tool" : "Tool_node",
        END : END
     }
)

graph.add_edge("Tool_node","chatbot")


app = graph.compile()

result = app.invoke(
     {
        "messages" : HumanMessage(content="Search What is Python?")
     }
)

print(result)
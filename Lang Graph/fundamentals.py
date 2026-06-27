from langgraph.graph import StateGraph,END
from typing import TypedDict
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage,AIMessage
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

memory = MemorySaver()

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

# search = DuckDuckGoSearchRun()

# @tool
# def calculator(a: int,b: int) -> int:
#     """Multiply two numbers"""
#     return (a * b) 
# @tool
# def web_search(query: str) -> str:
#     """Perform a web search for the given query"""
#     return {
#         "message" : [search.run(query)]
#     }

# @tool
# def web_scraper(url: str) -> str:
#     """Scrape the data of the website"""
#     cleaned = ""
#     if (url.startswith("http://") or url.startswith("https://")):
#         try:
#             r = requests.get(url,timeout=10)
#             if r.status_code != 200:
#                     return (f"Website {url} cannot be reached Error: {r.status_code}")

            
#             soup = BeautifulSoup(r.text,"html.parser")

#             data = soup.find_all(["h1","h2","h3","h4","h5","h6","p"])
                    
#             for el in data:
#                 cleaned += el.text.strip() + "\n"

#         except Exception as e:   
#             return str(e)
#     else:
#          return ("Invalid URL Provided")
#     return cleaned
def multiplication(state):
     return {
          "messages" : [AIMessage(content="Multiplication node reached")]
     }

def addition(state):
     return {
          "messages" : [AIMessage(content="Addition node reached")]
     }

def subtraction(state):
     return {
          "messages" : [AIMessage(content="Subtraction node reached")]
     }

def chatbot(state):
    #  response = model_with_tools.invoke(state["messages"])

     return {
          "messages" : state["messages"]
     }

def should_continue(state):
     last_message = state["messages"][-1].content.lower()

     if "multiply" in last_message:
          return "multiplication"
     
     if "addition" in last_message:
          return "addition"
     
     if "subtraction" in last_message:
          return "subtraction"
          
     return END
          
# tools = [calculator,web_search,web_scraper]

# tools = [multiply,add,subtract]

# model_with_tools = model.bind_tools(tools)

graph = StateGraph(State)

# ToolNode = worker who actually does the calculation and brings back the result
# tools_node = ToolNode(tools)

graph.add_node("chatbot",chatbot)


graph.add_node("Multiply_Node",multiplication)

graph.add_node("Addition_Node",addition)

graph.add_node("Subtraction_Node",subtraction)

graph.set_entry_point("chatbot")

graph.add_conditional_edges(
     "chatbot",
     should_continue,
     {
        "addition" : "Addition_Node",
        "multiplication" : "Multiply_Node",
        "subtraction" : "Subtraction_Node",
        END : END
     }
)

graph.add_edge("Addition_Node",END)
graph.add_edge("Multiply_Node",END)
graph.add_edge("Subtraction_Node",END)


app = graph.compile(
    #save everything to the memory
    checkpointer=memory
)

# result = app.invoke(
#     {
#         "messages" : [HumanMessage(content="Multiply 5 and 3")]
#     },
#     config={
#         "configurable": {
            #identifies the conversation
            # in next run if it is 1, it will remember all the previous conversation
            # if it changes to 2, a new conversation will start
#             "thread_id": "1"
#         }
#     }
     
# )

#  used for printing each and every step of the whole graph
for event in app.stream(
    {
        "messages":[
            HumanMessage(content="Multiply 5 and 6")
        ]
    },
    config={
        "configurable":{
            "thread_id":"1"
        }
    }
):
    print(event)

# print(result["messages"])
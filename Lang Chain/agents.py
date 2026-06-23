from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# @tool
# def add(a: int, b: int) -> int:
#     """Adds two numbers together"""
#     return a + b

# bind tools directly to the model
# model_with_tools = model.bind_tools([add])

# invoke with a question
# response = model_with_tools.invoke("What is 5 + 3?")

# the ai output
# print(response.content)

# will show you exactly which tool it called and with what arguments
# print(response.tool_calls)

# TASK 1 (Tool Calling Agent)
# @tool
# def calculator(a: int,b: int) -> int:
#     """Multiply two numbers"""
#     return (a * b) 

# @tool
# def formatted(name : str) -> str:
#     """Create a welcome message"""
#     return (f"Welcome Back, {name}")

# query = "What is 5 * 3"

# model_with_tools = model.bind_tools([calculator, formatted])

# response = model_with_tools.invoke(query)

# tool_calls = response.tool_calls[0]

# result = calculator.invoke(tool_calls["args"])

# prompt = ChatPromptTemplate.from_template("""
#         The calculator returned: {result}
#         Now give the final answer to the user question: {query}
# """)

# chain = prompt | model

# final_response = chain.invoke(
#     {
#         "result" : result,
#         "query" : query
#     }
# )

# print("Final Answer:", final_response.content)

# TASK 2 (Multiple Calls)
# @tool
# def calculator(a: int,b: int) -> int:
#     """Multiply two numbers"""
#     return (a * b) 

# @tool
# @tool
# def calculator(a: int,b: int) -> int:
#     """Multiply two numbers"""
#     return (a * b)

# @tool
# def formatted(name : str) -> str:
#     """Create a welcome message"""
#     return (f"Welcome Back, {name}")

# query = "What is 5 * 3"

# model_with_tools = model.bind_tools([calculator, formatted])

# response = model_with_tools.invoke(query)

# tools_map = {
#     "calculator": calculator,
#     "formatted": formatted
# }
# results = []

# for tool in response.tool_calls:
#     tools_name = tool["name"]
#     tools_arg = tool["args"]
#     result = tools_map[tools_name].invoke(tools_arg)
#     results.append(f"{tools_name} returned: {result}")

# results_text = "\n".join(results)

# prompt = ChatPromptTemplate.from_template("""
#         The calculator returned: {result}
#         Now give the final answer to the user question: {query}
# """)

# chain = prompt | model

# final_response = chain.invoke(
#     {
#         "result" : results_text,
#         "query" : query
#     }
# )

# print("Final Answer:", final_response.content)


# TASK 3 (BUILD AGENT THAT Can Search WEB)


search = DuckDuckGoSearchRun()

# Runs a search query and returns the results as a plain string
# result = search.run("latest AI news 2025")

@tool 
def web_search(query: str) -> str:
    """Perform a web search for the given query"""
    return search.run(query)

query = "What is the temprature in Thailand"

model_with_tools = model.bind_tools([web_search])

response = model_with_tools.invoke(query)

tools_map = {
    "web_search" : web_search
}
results = []
for tools_call in response.tool_calls:
    tool_name = tools_call["name"]
    tool_args = tools_call["args"]
    result = tools_map[tool_name].invoke(tool_args)

    results.append(f"{tool_name} returned: {result}")

result = "\n".join(results)

prompt = ChatPromptTemplate.from_template("""
    Here is the result of the web search : {result}
    Answer the following query of the User: {query}
""")

chain = prompt | model

final_result = chain.invoke(
    {
        "result" : results,
        "query" : query
    }
)

print("Final Result: ",final_result.content)
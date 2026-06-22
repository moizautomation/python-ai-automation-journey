# Learning the Basics of Langchain Agents

# this allow us to convert a normal function into an AI tool
from langchain_core.tools import tool
from langchain.agents import initialize_agent, AgentType
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Creating the tool that agent can use
@tool
# return integer
def add(a: int, b: int) -> int:
    # AI reads this to understand
    # wgat the tool does
    """Adds two numbers together"""
    return a + b

#making the AI agent
agent = initialize_agent(

    # give agent acess to the tool function
    tools = [add],

    # the brain of the agent
    llm = model,

    # tells the agent to
    # Use ReAct reasoning (Reason + Act + Observe)
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,

    # shows internal thinking process
    verbose=True
)

response = agent.invoke("What is 5 + 3?")

print(response)

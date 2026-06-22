# Learning different types of memory and comparing them.

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

n = 4
memory1 = InMemoryChatMessageHistory()

prompt1 = ChatPromptTemplate.from_template("""
        Conversation History:
        {history}
        Answer the user message below:
        {message}
""")

chain1 = prompt1 | model

prompt2 = ChatPromptTemplate.from_template("""
        I want you to summarize the following:
        {conversation}
""")

chain2 = prompt2 | model

history = ""

sum_history = ""

wind_memory = ""
for i in range (0,n):
    user_msg = input("Enter your Prompt: ")

    memory1.add_user_message(user_msg)
    
    response = chain1.invoke(
        {
            "history" : history,
            "message" : user_msg
        }
    )

    memory1.add_ai_message(response.content)
    
    history = ""
    for msg in memory1.messages:
        # msg.type returns 'human' or 'ai'
        speaker = "Human" if msg.type == "human" else "AI"
        history += f"{speaker}: {msg.content}\n"

    response2 = chain2.invoke(
        {
            "conversation" : history
        }
    )
    sum_history = response2.content

    wind_memory = memory1.messages[-3:]
    print(response.content)



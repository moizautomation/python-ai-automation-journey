# Fundamentals and Basic Syntax of Langchain
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory

load_dotenv()

#choosing the ai model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)


#used to start the workflow of ai agent response
# response = model.invoke(
#     "Explain what an API is"
# )


# print(response.content)


# prompt = ChatPromptTemplate.from_template(
#     """
# Explain this programming language:

# {language}
# """
# )


# the | operator is used to connect things
# here it is used to send the promp to model
# chain = prompt | model


# response = chain.invoke(
#     {
#         "language": "Python"
#     }
# )

# print(response.content)

# TASK 1 (CREATING A SIMPLE AI RESPONSE FROM INPUT)
# prompt = ChatPromptTemplate.from_template("""
#     Explain the following programming language
#     {language}
# """
# )
# chain = prompt | model

# response = chain.invoke(
#     {
#         "language" : "Python"
#     }
# )

# print(response.content)

# TASK 2 (MULTIPLE AI WORKING ON A SINGLE TASK)

#make the explanation prompt
# explain_prompt = ChatPromptTemplate.from_template("""
#     Explain the following topic in 5 lines

#     {topic}
# """
# )

#make the bullet points prompt
# bullet_prompt = ChatPromptTemplate.from_template("""
#     Make the following explanation into bullet points

#     {explanation}
# """
# )

#will send the input to the model for explanation
# explain_chain = explain_prompt | model

#will run the model
# response = explain_chain.invoke(
#     {
#         "topic" : "Python Language"
#     }
# )

# will send the input from the bullet prompt to the model which is the
# output from the previous prompt
# bullet_chain = bullet_prompt | model

# bullet_response = bullet_chain.invoke(
#     {
#         "explanation" : response.content
#     }
# )
# print(bullet_response.content)

# TASK 3 (Memory)

# prompt = ChatPromptTemplate.from_template(""""
#     Answer the following question:
#     {Input}
# """
# )

# memory = InMemoryChatMessageHistory()


# chain = prompt | model

# inputt = "My name is Abdul Moiz"
# response = chain.invoke(
#     {
#         "Input" : inputt
#     }
# )

# memory.add_user_message(inputt)
# memory.add_ai_message(response.content)

# history = memory.messages

# prompt1 = ChatPromptTemplate.from_template("""
#         Conversation history:
#         {history}
#         Answer the Question Below:
#         {question}
# """
# )

# chain1 = prompt1 | model

# response1 = chain1.invoke(
#     {
#         "history" : history,
#         "question" : "What is my Name?" 
#     }
# )
# print(response1.content)

# TASK 4 (Memory chatbot Loop)

n = 4
memory = InMemoryChatMessageHistory()

prompt = ChatPromptTemplate.from_template("""
        Conversation History:
        {history}
        Answer the user message below:
        {message}
""")

chain = prompt | model

history = ""

for i in range (0,n):
    user_msg = input("Enter your Prompt: ")

    memory.add_user_message(user_msg)
    
    response = chain.invoke(
        {
            "history" : history,
            "message" : user_msg
        }
    )

    memory.add_ai_message(response.content)
    
    history = ""
    for msg in memory.messages:
        # msg.type returns 'human' or 'ai'
        speaker = "Human" if msg.type == "human" else "AI"
        history += f"{speaker}: {msg.content}\n"

    print(response.content)

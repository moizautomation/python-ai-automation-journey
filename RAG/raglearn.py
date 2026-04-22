#Learning RAG Manually
# from openai import OpenAI
import google.generativeai as genai
import os                       # 1. Add this (helps Python talk to your system)
from dotenv import load_dotenv

#This line opens and reads your .env file
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')
# my_secret_key = os.getenv("OPENAI_API_KEY")

# #logging into OpenAI using secret key
# client = OpenAI(api_key=my_secret_key)


context = ""
highest = 0

#list of words to remove from question
ignore_words = ["for","what","is","why","when","how","?"]

with open("data.txt","r") as f:
    #reading all the lines
    data = f.readlines()

    question = input("Enter your Question: ").lower()
    tempq = question
    #splitting the question into a list of words
    question = question.split()
    
    
    for word in ignore_words:
            #if any word we want to ignore in the question
            if word in question:
                #remove that word
                question.remove(word)

    #reading each line            
    for line in data:
        match = 0
        lower_line = line.lower()
        for keyword in question:
            #if the whole keyword is in the line
            if keyword in lower_line.split():
                match += 1

        if(match > highest):
            highest = match
            context = line

if highest == 0: 
    print("I couldn't find that info") 
    exit()

#creating multi-line string prompt
prompt = f"""
Use ONLY the information below to answer.

Context:
{context}

Question:
{question}

Answer clearly:
"""

# asking ai to generate an answer
# response = client.chat.completions.create(
#     #choosing gpt model to use
#     model="gpt-4o-mini",
#     messages=[
#          #giving the role and prompt
#         {"role": "user", "content": prompt}
#     ]
# )
response = model.generate_content(prompt)

#select the first response and displays it
# print(response.choices[0].message.content)

print(response.text)

    

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
#Day 23
# model = genai.GenerativeModel('gemini-2.5-flash')
# prompt = f"""
# Question:
# "Explain what Python is in 2 simple lines"

# Answer:
# """

# response = model.generate_content(prompt)
# print(response.text)

#Day 24 Task 2 
# model = genai.GenerativeModel(
#     model_name="gemini-2.5-flash",
#     #to control what type of response ai give (eg: short,long etc)
#     system_instruction="You are a strict assistant. Give short answers only."
# )


# response = model.generate_content("Explain what machine learning is")
# print(response.text)

# model = genai.GenerativeModel(
#     model_name="gemini-2.5-flash",
#     #to control what type of response ai give (eg: short,long etc)
#     system_instruction="You are a Teacher. Explain like you are teaching a student."
# )


# response = model.generate_content("Explain what machine learning is")
# print(response.text)


# model = genai.GenerativeModel(
#     model_name="gemini-2.5-flash",
#     #to control what type of response ai give (eg: short,long etc)
#     system_instruction="You are a JSON only assistant. Give  answers in JSON only."
# )


# response = model.generate_content("Explain what machine learning is")
# print(response.text)

#Day 24 task 3 (Forcing ai output reliably)
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    #to control what type of response ai give (eg: short,long etc)
    system_instruction="You Must reply in bullet points only. Also the answer should never exceed 3 lines and you must always include one example"
)


response = model.generate_content("Explain what Artificial Intelligence is")
print(response.text)






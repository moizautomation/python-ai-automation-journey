import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-2.5-flash')
prompt = f"""
Question:
"Explain what Python is in 2 simple lines"

Answer:
"""

response = model.generate_content(prompt)

print(response.text)

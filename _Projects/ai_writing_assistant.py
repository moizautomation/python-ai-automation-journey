#AI Writing Assistant Tool
# User picks a task: write a product description, email, social post, or blog intro
# User fills in simple inputs (topic, tone, length)
# AI generates the content on click
# User can copy or download the result

import google.generativeai as genai
import time
import json
from dotenv import load_dotenv 
import os
import requests
from bs4 import BeautifulSoup
import streamlit as st

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="""
    You are a strict writing AI Assistant.
    You will recieve the task of writing something. eg: description,social post.
    You will also recieve the topic, text and length. Also the tone.
    You will strictly follow all of these things like especially the length and tone should
    be the same user asked for as well as the task you recieved.
    You are going to follow all the below rules striclty.
    Rules:
    - Never give extra text.
    - Stricly follow all the instructions given
    - If you have no information on topic, simply return no result found.
    """)

st.title("AI Writing Assistant")
st.divider()

st.header("Input")
st.divider()
task = st.selectbox("Task Selector",["Description","Email","Social Post","Blog Intro"])

topic = st.text_input("Enter the topic: ")

text = st.text_area("Enter your text: ")

length = st.text_input("Enter the length: ")

tone = st.selectbox("Tone",["Friendly","Professional","Casual"])

button = st.button("Enter")

if len(topic) == 0 or len(text) == 0 or len(length) == 0:
    st.error("Error! All fields are mandatory")

if "cache" not in st.session_state:
    st.session_state.cache = {}
# cleaned = text[:200]
key = topic + task
if(button):
    with st.spinner(f"Writing the {task}"):
        st.header("AI Result")
        st.divider() 
        prompt = f"""
        Task:
        {task}

        Topic:
        {topic}

        Text:
        {text}

        length:
        {length}

        Tone:
        {tone}
        """
        
        if key not in st.session_state.cache:
            response = model.generate_content(prompt)
            st.session_state.cache["key"] = response.text
            response_text = response.text
        else:
            response_text = st.session_state.cache["key"]

        st.write(response_text)

            







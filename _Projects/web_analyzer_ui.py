#Lead Generation Bot Project
# Goals:
# Extract structured data
# What it should do
# Scrape product/business data
# Store in JSON
# Handle multiple pages
#send description to ai to get summary

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

#Phase 4 - Control AI output and restrict it to only give in strict JSON format
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="""
    You must act like a strict assistant who only does what he is asked of. 
    You will receive text + mode.
    You should strictly output in the format defined below. The json format to follow is:

    If mode = Summary
    Format:
    {
    "mode": "only give mode",
    "summary": "you must give short explanation. no extra wordss"
    }

    If mode = Key Points
    Format:
    {
    "mode": "only give mode",
    "keypoints": ["Key point 1","Key Point 2", "Key Point 3"]
    }

    If mode = Sentiment
    Format:
    {
    "mode": "only give mode",
    "sentiment": "strictly give one of: positive / negative / neutral"
    } 
    """)

    
#make scraper look like a real browser instead of bot
headers = {
    "User-Agent": "Mozilla/5.0"
}

#Phase 1 - Input Validation and Mode setting
st.header("Web AI Analyzer")
st.divider()

st.subheader("Input")
st.divider()

url = st.text_area("Enter the Target URL: ")
mode = st.selectbox("Choose mode",["Summary","Key Points","Sentiment"])

button = st.button("Enter")

st.subheader("Output")
st.divider()

if(button):
    #check if url is empty
    #remove unnecesary characters from the url like \n
    url = url.strip()
    key = url + mode

    if(len(url) == 0):
        print("Input cannot be empty")
        st.stop()
    a = "http"
    b = "https"

    #check if url is valid
    if url.startswith("http"):
        #error handling
        try:
            with st.spinner("Processing"):
                #if user session cache not created
                if "cache" not in st.session_state:
                    #create an empty dict for it
                    st.session_state.cache = {}

                #if our key is in the cache
                if key in st.session_state.cache:
                    #reuse the old response
                    response_text = st.session_state.cache[key]
                #else call api again else
                else:
                    #send the request to the website
                    r = requests.get(url, headers = headers)
                    soup = BeautifulSoup(r.text,"html.parser")
                    #returns a list of all p tags
                    para = soup.find_all("p")

                    heading1 = soup.find_all("h1")
                    heading2 = soup.find_all("h2")
                    heading3 = soup.find_all("h3")

                    heading4 = soup.find_all("h4")
                    heading5 = soup.find_all("h5")
                    heading6 = soup.find_all("h6")

                    #merge all the headings text
                    headings = heading1 + heading2 + heading3 + heading4 + heading5 + heading6
                    #merge all the text
                    merge_data = para + headings

                    cleaned = ""
                    for data in merge_data:
                        cleaned += " " + data.text.strip() + " \n"
                    prompt = f"""

                    Text:
                    {cleaned}

                    Mode:
                    {mode}

                    IMPORTANT:
                    - If mode is keypoint, return ONLY meaningful points
                    - Do not return empty strings
                    - Each point must be based on actual text

                    """
                    

                    #Phase 3 - Sending cleaned data to AI
                    #cleaning the merged data by removing
                    #unnecassory characters and spaces
                    data_list = []
                    aires = "API Failed"

                    response = model.generate_content(
                        prompt,
                        generation_config={
                            "max_output_tokens" : 150,
                        })
                    #stores the response as a string
                    response_text = response.text
                    st.session_state.cache[key] = response_text

                    aires = response.text.strip()
                    st.success("Fetched From API")
                    st.header("AI Result")
                    st.divider()

                if(mode == "Summary"):
                    st.info("Cost per Request: 0.001$")

                    st.subheader(f"Mode: {mode}")
                    st.divider()

                    st.markdown("**Summary**")
                    st.write("Output")

                    st.write(response_text)
                elif(mode == "Key Points"):
                    st.info("Cost per Request: 0.002$")

                    st.subheader(f"Mode: {mode}")
                    st.divider()

                    st.markdown("**Key Points**")
                    st.write("Output")

                    st.write(response_text)
                elif(mode == "Sentiment"):
                    st.info("Cost per Request: 0.001$")

                    st.subheader(f"Mode: {mode}")
                    st.divider()

                    st.markdown("**Sentiment**")
                    st.write("Output")

                    st.write(response_text)

                    #add the result of that response in list
                data_list.append({
                "url" : url,
                "mode" : mode,
                "ai-result" : aires
                })
        except Exception as e:
            st.error("Website cannot be reached")
            st.write(e)
            st.stop()
    else:
        st.error("Invalid URL")
        st.stop()



# AI lead Intelligence Tool
# User pastes a list of company names or URLs
# Tool scrapes each company's website automatically
# AI analyzes each one: what they do, who they target, pain points
# Output: a clean report per company — ready to use for outreach
# Streamlit UI with download button for the full report

import google.generativeai as genai
import time
import json
from dotenv import load_dotenv 
import os
import requests
from bs4 import BeautifulSoup
import streamlit as st

header = {
    "User-Agent": "Mozilla/5.0"
}

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="""You are a strict business lead intelligence tool\
        You are going to recieve data about company.
        You will have to do the following:
        Format:
        What the company does (simple explanation of 2-3 lines)
        Target audience (two words only)
        Main product/service  (two words only)
        Customer pain points they solve (2 lines only)
        Possible sales/marketing angle (very important for outreach)"""
    )
choice = st.sidebar.selectbox("Navigation",["HomePage","AI Lead Intelligence Tool","Instructions"])

if(choice == "HomePage"):
    st.title("HomePage")
    st.header("AI Lead Intelligence Tool")
    st.divider()

    st.write("This is a Lead Intelligence AI Tool")
    st.write("You just need to paste the list of URL")
    st.write("It will tell you all the data about each url")

elif(choice == "AI Lead Intelligence Tool"):
    url_data = []
    #to store data of multiple comapnies
    all_reports = []

    st.title("AI Lead Intelligence Tool")

    st.header("Input")
    st.divider()

    urls = st.text_area("Paste the Companies URL Below:")

    button = st.button("Analyze Companies")

    st.header("Analyzed Results")
    st.divider()

    if "cache" not in st.session_state:
        st.session_state.cache = {}

    if button:
        if(len(urls) == 0):
            st.error("URL Field cannot be empty")
            st.stop()
            
        with st.spinner("Analyzing your Competitors"):
            urls = urls.split("\n")

            for url in urls:
                key = ""
                cleaned = ""

                url = url.strip()
                
                if(len(url) == 0):
                    continue
                
                if not url.startswith("http"):
                    st.error("Error! The URL is Invalid")
                    st.stop()
                
                try:
                    r = requests.get(url,headers=header)

                    info = BeautifulSoup(r.text,"html.parser")

                    data = info.find_all(["h1","h2","h3","h4","h5","h6","p"])
                    
                    for el in data:
                        cleaned += el.text.strip() + "\n"
                    
                    key = url + cleaned
                    url_data.append(cleaned)

                    if key in st.session_state.cache:
                        response_text = st.session_state.cache[key]
                    else:
                        prompt = f"""
                        Data:
                        {cleaned}
                        """
                        response = model.generate_content(prompt)
                        response_text = response.text
                        st.session_state.cache[key] = response_text
                    
                    #to store data of a single company
                    # st.write(response_text)
                    report = {}
                    report.update({"URL" : url, "AI Analysis" : response_text})
                    all_reports.append(report)
                    
                    st.download_button(
                        label = "Download Results",
                        data = all_reports,
                        file_name = "ai_result.json",
                        mime="text/plain"
                    )
                except:
                    st.error(f"Error! Website cannot be Reached{url}")
                    st.stop()

elif(choice == "Instructions"):
    st.title("Instructions")
    st.header("How to use the Tool")
    st.divider()

    st.write("1. User pastes a list of company names or URLs")
    st.write("2. Tool scrapes each company's website automatically")
    st.write("3. AI analyzes each one: what they do, who they target, pain points")
    st.write("4. Output: a clean report per company — ready to use for outreach")
    st.write("5. Streamlit UI with download button for the full report")




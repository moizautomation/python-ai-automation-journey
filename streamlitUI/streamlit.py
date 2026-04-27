#Day 29 Learning basics of Streamlit UI\
import streamlit as st

# #main heading
# st.title() 
# #display text,output
# st.write()
# #take input
# st.text_input()
# #trigger action
# st.button()
# #show success msg
# st.success()
# #show error message
# st.error()

# st.title("My First App")
# st.write("Hello World")

# st.title("Big Heading")
# st.header("Smaller Heading")
# st.text("Simple text")
# st.write("Auto-render smart output")

# url = st.text_input("Enter URL")
# if(st.button("submit")):
#     st.write("success")

# mode = st.selectbox("Choose Mode",["Summary","Key Points","Sentiments"])
# if(st.button("enter")):
#     st.header("Success")

# if st.button("Run"):
#     st.write("Button clicked")

# st.success("Success message")
# st.error("Error message")
# st.warning("Warning message")

# st.json({"name": "Ali", "mode": "summary"})

# st.title("Web Content Analyzer")
# url = st.text_input("Enter the URL: ")
# mode = st.selectbox("Choose Mode",["Summary","Key Points","Sentiment"])
# if(st.button("enter")):
#     st.text(url)
#     st.text(mode)
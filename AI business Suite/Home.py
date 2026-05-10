import streamlit as st

st.set_page_config(page_title="Abdul's AI Suite", layout="wide")

# Initialize the global usage counter
if "usage_count" not in st.session_state:
    st.session_state.usage_count = 0

st.title("🚀 Custom AI Business Solutions")
st.markdown(f"**Total Tools Used this Session: {st.session_state.usage_count}/3**")
st.divider()

st.header("Welcome to my AI Portfolio")
st.write("""
I build custom AI automation tools designed to save businesses time and money. 
This suite demonstrates three core capabilities:
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📊 Lead Intel")
    st.write("Scrapes company websites to find pain points and target audiences.")

with col2:
    st.subheader("🕵️ Web Analyzer")
    st.write("Analyzes sentiment and key points from URLs or text files.")

with col3:
    st.subheader("✍️ Writing Assistant")
    st.write("Generates high-quality professional copy in various tones.")

st.divider()
st.info("👈 Select a tool from the sidebar to get started!")
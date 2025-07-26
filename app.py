import streamlit as st
from utils import run_agent_sync

st.set_page_config(page_title="Common Medicine Suggestion App", page_icon="💊", layout="centered")

st.title("💊 Common Medicine Suggestion App")

st.markdown("""
This app provides **safe over-the-counter (OTC)** medicine suggestions for common ailments like cold, fever, headache, etc.

> ℹ️ This is **not** a medical diagnosis tool. Always consult a licensed doctor if symptoms persist or worsen.
""")

# Sidebar API setup
st.sidebar.header("Configuration")
google_api_key = st.sidebar.text_input("Google API Key", type="password")
youtube_pipedream_url = st.sidebar.text_input("Dummy YouTube Pipedream URL", placeholder="Enter a dummy Pipedream URL")

# User input form
with st.form("symptom_form"):
    symptom = st.text_input("What is your problem? (e.g., fever, headache)")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", 0, 120, 25)
        weight = st.number_input("Weight (kg)", 1.0, 200.0, 70.0)
    with col2:
        pregnant = st.checkbox("Pregnant / Lactating?")
        comorbid = st.multiselect("Comorbidities", ["liver_disease", "kidney_disease", "asthma", "ulcer", "diabetes"])
    submitted = st.form_submit_button("Suggest Safely")

if submitted:
    if not google_api_key or not youtube_pipedream_url:
        st.error("API Key and dummy YouTube URL are required.")
    else:
        st.info("🔄 Generating safe suggestion...")
        query = f"""
Symptom: {symptom}
Age: {age}
Weight: {weight} kg
Pregnant: {pregnant}
Comorbidities: {', '.join(comorbid)}
"""
        result = run_agent_sync(
            google_api_key=google_api_key,
            youtube_pipedream_url=youtube_pipedream_url,
            user_goal=query
        )
        if result and "messages" in result:
            for msg in result["messages"]:
                st.success(msg.content)
        else:
            st.warning("No result generated. Try again.")

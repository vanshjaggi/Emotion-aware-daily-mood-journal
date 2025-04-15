import streamlit as st
import requests
from database import fetch_entries

st.set_page_config(page_title="Emotion-Aware Mood Journal", layout="centered")

st.title("🧠 Emotion-Aware Daily Mood Journal")

journal = st.text_area("📝 Write about your day:")

if st.button("📸 Analyze Mood"):
    with st.spinner("Analyzing your face and journal..."):
        response = requests.post("http://localhost:5000/analyze", json={"journal": journal})
        if response.status_code == 200:
            result = response.json()
            st.success("✅ Analysis complete!")
            st.write(f"**Detected Emotion:** {result['emotion']}")
            st.write(f"**Sentiment from Text:** {result['sentiment']}")
        else:
            st.error("Error connecting to backend")

st.markdown("---")
st.subheader("📊 Previous Mood Logs")
entries = fetch_entries()
for e in entries:
    st.markdown(f"""
    - **Date:** {e[1]} **Time:** {e[2]}
    - **Emotion:** `{e[3]}` | **Sentiment:** `{e[4]}`
    - 📝 {e[5]}
    """)

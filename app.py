# app.py

import streamlit as st
from agents.research_agent import get_research_points, get_research_points_test
from agents.script_agent import generate_script, generate_script_test
from agents.voice_agent import generate_audio, generate_audio_test

st.set_page_config(page_title="Decibl Script Generator", page_icon="🎙️")

st.title("🎙️ Decibl: AI Podcast Script Generator")
st.write("Generate podcast scripts using AI agents — fast, personalized, and interactive-ready.")

# Sidebar for inputs
with st.sidebar:
    st.header("Customize Your Episode 🎧")
    topic = st.text_input("Topic", value="How Gen Z is reshaping the workplace")
    tone = st.selectbox("Tone", ["Calm", "Witty", "Motivational", "Professional"])
    duration = st.selectbox("Duration", ["2 minutes", "3 minutes", "5 minutes"])

if st.button("Generate Script"):
    with st.spinner("🔍 Researching and writing your script..."):
        research_points = get_research_points_test(topic)
        script = generate_script_test(topic, tone, duration, research_points)

        st.success("✅ Script generated successfully!")
        st.subheader("📜 Your Podcast Script:")
        st.text_area(label="", value=script, height=500)

        st.download_button(
            label="💾 Download Script",
            data=script,
            file_name="podcast_script.txt",
            mime="text/plain"
        )
    with st.spinner("🎧 Generating audio..."):
        audio_path = generate_audio_test(script)
        st.audio(audio_path, format="audio/mp3")


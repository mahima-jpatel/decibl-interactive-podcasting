# Decibl: Interactive AI Podcast Generator

**Decibl** is an AI-powered system that generates **personalized, interactive podcasts** on demand.  
With dynamic branching using LangGraph and realistic voice generation via ElevenLabs, users can customize their episode experience — from topic and tone to length and episode style — and even interact mid-listen.

---

## 🚀 Features

- Topic-driven podcast generation
- Script writing powered by GPT-4 / GPT-4o
- Research-based content enrichment (mock or API-connected)
- Branching storylines using LangGraph (Fast Facts, Deep Dive, Balanced)
- Realistic audio output with ElevenLabs
- User-friendly frontend via Streamlit
- Extensible for interactive Q&A or multi-voice storytelling

---

## How It Works


1. **User** selects a topic, tone, duration, and episode style
2. **Research Agent** collects bullet-point facts (from real or mock sources)
3. **Script Agent** generates a podcast-ready script based on tone and research
4. **Voice Agent** converts script to lifelike audio using ElevenLabs
5. **LangGraph** handles state transitions across the episode flow
6. **Streamlit App** presents the final script + audio to the user

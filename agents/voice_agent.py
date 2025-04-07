# agents/voice_agent.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Voice name to ID map (for API use)
VOICE_IDS = {
    "Rachel": "21m00Tcm4TlvDq8ikWAM",
    "Adam": "yoZ06aMxZJJ28mfd3POQ",
    "Bella": "EXAVITQu4vr4xnSDxMaL",
    "Antoni": "ErXwobaYiN019PkySvjV"
}

def generate_audio(script_text, voice_name="Rachel", output_path="outputs/podcast_audio.mp3"):
    voice_id = VOICE_IDS.get(voice_name)
    
    if not ELEVENLABS_API_KEY:
        raise ValueError("Missing ELEVENLABS_API_KEY in .env")
    
    if not voice_id:
        raise ValueError(f"Unknown voice name: {voice_name}")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": script_text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("❌ API Error:", response.text)
        raise RuntimeError(f"Audio generation failed: {e}")

    with open(output_path, "wb") as f:
        f.write(response.content)

    return output_path

def generate_audio_test(script_text, voice_name="Rachel", output_path="outputs/podcast_audio.mp3"):
    return "outputs/test_episode.mp3"
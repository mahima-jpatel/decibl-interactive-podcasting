# agents/script_agent.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get your LiteLLM key from the environment
LLM_1_API_KEY = os.getenv("OPENAI_API_KEY")

# Query GPT-4o via CMU LiteLLM
def generate_script(topic, tone, duration, research_points):
    formatted_points = "\n".join(f"- {point}" for point in research_points)

    prompt = f"""
You are a podcast scriptwriter for a cutting-edge AI content platform. Your job is to write a podcast script for the following:

Topic: {topic}
Tone: {tone}
Duration: {duration}

Structure the script as follows:
- Brief Introduction with a hook
- Main Content (built on the research points below)
- One actionable takeaway
- Thoughtful, soft closing

Add natural (pause), (breathe), or (smile) cues where appropriate for smooth audio delivery.

Here are the research points to incorporate:
{formatted_points}

Write in a natural, human tone as if you're speaking directly to the listener. Avoid listing — weave the research into a coherent, flowing story.
"""

    client = OpenAI(
        api_key=LLM_1_API_KEY,
        base_url="https://cmu.litellm.ai"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.85,
        max_tokens=1500
    )

    return response.choices[0].message.content.strip()


def generate_script_test(topic, tone, duration, research_points=None):
    return """
[INTRO]

(Softly) Welcome to today's episode of [Podcast Name], where we explore the transformative forces shaping our world. (Pause) Today, we’re diving into a topic that’s capturing headlines and redefining norms—how Gen Z is reshaping the workplace. (Breathe) Now, why does this matter in 2024? (Pause) Because, as we speak, a growing number of young creators and professionals are leading a quiet revolution in the way we work.

[MAIN CONTENT]

(Smile) Imagine a workplace that thrives on innovation and experimentation. This isn’t a distant dream—it’s happening right now. Recent publications and trending videos are buzzing with stories about Gen Z’s unique approach to work. They’re not just participants; they’re pioneers, blending cutting-edge AI tools with traditional methods to usher in more effective outcomes. (Pause)

Experts in various fields are noticing this shift. They recommend a synthesis of AI and human touch, a dance between new technologies and time-tested strategies, to unlock unprecedented potential. (Pause) It’s like conducting a symphony where every instrument, old and new, adds depth and harmony. (Breathe) And the results? Case studies reveal significant impacts when workplaces adopt practical strategies inspired by Gen Z’s ethos.

What makes this trend even more compelling is its alignment with today’s craving for personalized, interactive content. This generation’s appetite for innovation has made them adept at creating experiences that resonate with contemporary audiences, rooted deeply in current trends.

[TAKEAWAY]

(Pause, softly) So, what’s our actionable takeaway today? Whether you’re a leader, manager, or team member, start by embracing a mindset of openness and adaptability. Experiment with combining AI tools and traditional methods in your projects. (Pause) It’s about creating a workplace that’s not just ahead of the curve but one that shapes the curve.

[CLOSING]

As we wrap up, let us reflect on this: Gen Z is not just reshaping the workplace; they’re reshaping how we think about possibility and progress. (Pause, breathe) Thank you for joining us on this journey today. If you enjoyed this episode, consider sharing it with someone who might find it inspiring. Until next time, keep exploring and stay curious. (Smile, softly) Goodbye.
    """.strip()

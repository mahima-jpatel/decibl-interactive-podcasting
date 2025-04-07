from langgraph.graph import StateGraph, END
from typing import TypedDict, Literal
from agents.research_agent import get_research_points_test
from agents.script_agent import generate_script
from agents.voice_agent import generate_audio

class PodcastState(TypedDict):
    segment: str
    user_choice: str
    topic: str
    tone: str
    duration: str
    script: str
    audio_path: str

# Segment nodes
def intro_segment(state: PodcastState) -> PodcastState:
    return {**state, "segment": "intro"}

def ask_style_choice(state: PodcastState) -> PodcastState:
    return {**state, "segment": "ask_style"}

def fast_facts(state: PodcastState) -> PodcastState:
    research = get_research_points_test(state["topic"])
    script = generate_script(state["topic"], state["tone"], state["duration"], research)
    audio = generate_audio(script, voice_name="Rachel", output_path="outputs/fast_facts.mp3")
    return {**state, "segment": "fast_facts", "script": script, "audio_path": audio}

def deep_dive(state: PodcastState) -> PodcastState:
    research = get_research_points_test(state["topic"])
    script = generate_script(state["topic"], state["tone"], state["duration"], research)
    audio = generate_audio(script, voice_name="Rachel", output_path="outputs/deep_dive.mp3")
    return {**state, "segment": "deep_dive", "script": script, "audio_path": audio}

def balanced(state: PodcastState) -> PodcastState:
    research = get_research_points_test(state["topic"])
    script = generate_script(state["topic"], state["tone"], state["duration"], research)
    audio = generate_audio(script, voice_name="Rachel", output_path="outputs/balanced.mp3")
    return {**state, "segment": "balanced", "script": script, "audio_path": audio}

# Router for LangGraph
def route_from_style(state: PodcastState) -> Literal["fast_facts", "deep_dive", "balanced"]:
    return state["user_choice"]

# LangGraph flow
graph = StateGraph(PodcastState)

graph.add_node("intro", intro_segment)
graph.add_node("ask_style", ask_style_choice)
graph.add_node("fast_facts", fast_facts)
graph.add_node("deep_dive", deep_dive)
graph.add_node("balanced", balanced)

graph.set_entry_point("intro")
graph.add_edge("intro", "ask_style")
graph.add_conditional_edges("ask_style", route_from_style, {
    "fast_facts": "fast_facts",
    "deep_dive": "deep_dive",
    "balanced": "balanced"
})
graph.add_edge("fast_facts", END)
graph.add_edge("deep_dive", END)
graph.add_edge("balanced", END)

app = graph.compile()

# Entry function
def run_interactive_podcast(topic, tone, duration, user_choice):
    initial_state = {
        "segment": "",
        "user_choice": user_choice,
        "topic": topic,
        "tone": tone,
        "duration": duration,
        "script": "",
        "audio_path": ""
    }
    return app.invoke(initial_state)

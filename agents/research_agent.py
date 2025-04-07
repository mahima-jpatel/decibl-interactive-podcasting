# agents/research_agent.py

import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

def get_research_points(topic, num_results=5):
    if not SERPAPI_API_KEY:
        raise ValueError("SerpAPI key not found in environment variables.")

    search = GoogleSearch({
        "q": topic,
        "api_key": SERPAPI_API_KEY,
        "num": num_results
    })

    results = search.get_dict()
    organic_results = results.get("organic_results", [])

    research_points = []
    for result in organic_results[:num_results]:
        title = result.get("title", "")
        snippet = result.get("snippet", "")
        if snippet:
            research_points.append(f"{title}: {snippet}")

    if not research_points:
        research_points.append(f"No results found. Try a different topic.")

    return research_points


def get_research_points_test(topic):
    # Simulated high-quality mock research for testing
    return [
        f"Why '{topic}' matters in 2024: A growing number of creators and professionals are exploring this space.",
        "Recent publications and videos highlight a renewed focus on innovation and experimentation around this topic.",
        f"Experts suggest combining AI tools and traditional methods for better outcomes in areas related to '{topic}'.",
        "Case studies show significant impact when applying practical strategies tied to this theme.",
        "Audiences are increasingly drawn to content that’s personalized, interactive, and rooted in current trends."
    ]

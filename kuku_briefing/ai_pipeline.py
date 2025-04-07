import random
import datetime
from .models import User

def fetch_content(preferences: dict) -> dict:
    """
    Simulates fetching content based on user preferences.
    In reality, this would involve API calls, web scraping, DB queries.
    """
    content = {}
    if "News" in preferences.get("preferred_genres", []):
        content["news"] = [
            "Global markets see slight downturn.",
            "New breakthrough announced in renewable energy.",
            "Local government discusses infrastructure projects."
        ]
    if "Technology" in preferences.get("preferred_genres", []):
        content["tech"] = [
            "Latest smartphone model review is out.",
            "AI advancements continue to accelerate.",
        ]
    if "Fiction" in preferences.get("preferred_genres", []):
        content["fiction_updates"] = [
            f"New chapter released for 'The Astral Voyager'.",
            f"Top 10 trending fantasy audiobooks this week."
        ]
    if preferences.get("preferred_authors"):
        content["author_news"] = [f"Update from {author}: New book signing event announced." for author in preferences["preferred_authors"]]

    # Add a generic greeting
    content["greeting"] = ["Good morning! Here is your Kuku Daily Briefing."]

    # Add generic popular content if needed
    if not content or len(content) < 2:
         content["popular"] = ["Trending on Kuku FM: 'The Mind Architect' series.", "Don't miss the latest episode of 'History Uncovered'."]

    return content

def summarize_content(raw_content: dict) -> dict:
    """
    Simulates summarizing the fetched content using an LLM.
    Here, we'll just pick a random subset or slightly rephrase.
    """
    summaries = {}
    for category, items in raw_content.items():
        if items:
            # Simulate summarization - just take the first item or a random one
            summaries[category] = random.choice(items)
            # Simple modification to simulate summarization
            if category == "news":
                 summaries[category] = f"In world news: {summaries[category]}"
            elif category == "tech":
                 summaries[category] = f"Tech update: {summaries[category]}"

    return summaries


def generate_script(summarized_content: dict, user_name: str) -> list:
    """Generates the final script text."""
    script_parts = []
    now = datetime.datetime.now()
    time_of_day = "morning"
    if 12 <= now.hour < 17:
        time_of_day = "afternoon"
    elif now.hour >= 17:
        time_of_day = "evening"

    script_parts.append(f"Good {time_of_day}, {user_name}! Here's your Kuku Daily Briefing for {now.strftime('%A, %B %d')}.")

    # Order the script parts logically
    if "news" in summarized_content:
        script_parts.append(summarized_content["news"])
    if "tech" in summarized_content:
        script_parts.append(summarized_content["tech"])
    if "author_news" in summarized_content:
        script_parts.append(summarized_content["author_news"])
    if "fiction_updates" in summarized_content:
        script_parts.append(summarized_content["fiction_updates"])
    if "popular" in summarized_content:
         script_parts.append(f"Also trending: {summarized_content['popular']}")

    script_parts.append("That's all for your briefing today. Have a great day listening on Kuku FM!")
    return script_parts

def text_to_speech_simulation(script_parts: list, voice: str) -> str:
    """
    Simulates the Text-to-Speech generation.
    Returns the full script as a single string, indicating the voice.
    In reality, this would return an audio file path or stream.
    """
    full_script = " ".join(script_parts)
    return f"--- BEGIN AUDIO (Voice: {voice}) ---\n{full_script}\n--- END AUDIO ---"


def create_daily_briefing(user: User) -> str:
    """Runs the full pipeline to generate a personalized briefing."""
    print(f"Generating briefing for user: {user.name}")
    print(f"Preferences: {user.preferences}")

    # 1. Fetch content based on preferences
    raw_content = fetch_content(user.preferences)
    print(f"Fetched content categories: {list(raw_content.keys())}")

    # 2. Summarize content (Simulated)
    summarized_content = summarize_content(raw_content)
    print(f"Summarized content: {summarized_content}")

    # 3. Generate Script
    script = generate_script(summarized_content, user.name)
    print(f"Generated script parts: {len(script)}")

    # 4. Synthesize Audio (Simulated)
    audio_output = text_to_speech_simulation(script, user.preferences.get("preferred_voice", "Default"))
    print(f"Simulated audio generated with voice: {user.preferences.get('preferred_voice', 'Default')}")

    return audio_output

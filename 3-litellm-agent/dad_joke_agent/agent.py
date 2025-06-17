import os 
import random 

from google.adk.agents import Agent 
from google.adk.models.lite_llm import LiteLlm 

# model = LiteLlm(
#     model="openrouter/openai/gpt-4.1",
#     api_key = os.getenv("OPENROUTER_API_KEY")
# )

def get_dad_joke():
    jokes = [
        "Why did the chicken cross the road? to get to the other side!",
        "What do you call a belt made of watches?  A waist of time.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Becasue he was outstading in his field!"
    ]
    return random.choice(jokes)

root_agent = Agent(
    name="dad_joke_agent",
    model="gemini-2.0-flash",
    description="Dad joke agent",
    instruction="""
    You're a helpfull assistance that can tell jokes, 
    Only use the tool `get_dad_joke` to tell jokes.
    """,
    tools=[get_dad_joke]
)
"""
Before and After Calllbacks Example

This example demonstrates how to use both before_agent_callback and after_agent_callbacks
for logging purpose.

"""
from typing import Optional
from datetime import datetime

from google.genai import  types
from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext

# Create the Agent
root_agent = LlmAgent(
    name = "before_after_agent",
    model = "gemini-2.0-flash",
    description="A basic agent that demonstrates before and after agent callbacks",
    instruction="""
    You are a friendly greeting agent. Your name is {agent_name}.
    
    Your job is to:
    - Greet users politely
    - Respond to basic questions
    - Keep your responses friendly and concise
    """,
    # before_agent_callback=before_model_callback,
    # after_agent_callback=after_model_callback,
)
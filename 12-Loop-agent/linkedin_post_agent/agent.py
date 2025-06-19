"""
LindkedIn Post Generator Root Agent

This module defines the root agent for the LinkedIn post generation application.
It uses a sequential agent with an initial post generator followed by a refinement loop.
"""

from google.adk.agents import LoopAgent, SequentialAgent

from .subagents.post_refiner import post_refiner
from .subagents.post_reviewer import post_reviewer
from .subagents.post_generator import initial_post_generator

# Create the Refinement Loop Agent
refinement_loop = LoopAgent(
    name="PostRefinementLoop",
    max_iterations=10,
    sub_agents=[
        post_reviewer,
        post_refiner,
    ],
    description="Iteratively reviews and refines a linkedIn post until quality requirements are met",
)

# Create the Sequential Pipeline
root_agent = SequentialAgent(
    name="LinkedInPostGenerationPipeline",
    sub_agents=[
        initial_post_generator,  # Step 1: Generate initial post
        refinement_loop
    ],
    description="Generates and defines a LinkedIn post through an iterative review process"
)
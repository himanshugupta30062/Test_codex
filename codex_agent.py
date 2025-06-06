# codex_agent.py
"""Utility functions for sending prompts to the OpenAI API."""

import os
import openai

# Configure the OpenAI API key via environment variable when needed
openai.api_key = os.getenv("OPENAI_API_KEY", "")

def codex_agent(prompt):
    """Send a prompt to the OpenAI API and return the assistant's reply."""
    if not openai.api_key:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        openai.api_key = api_key

    try:
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )
        answer = response.choices[0].message.content.strip()
    except Exception as exc:
        print(f"OpenAI API request failed: {exc}")
        return ""

    print(f"Codex suggests: {answer}")
    return answer

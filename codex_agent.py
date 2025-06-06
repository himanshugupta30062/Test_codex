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
    except openai.OpenAIError as exc:
        print(f"OpenAI API request failed: {exc}")
        return ""

    print(f"Codex suggests: {answer}")
    return answer


def verify_openai_key() -> bool:
    """Check that the configured OpenAI API key is valid by making a tiny request."""
    if not openai.api_key:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("OPENAI_API_KEY environment variable is not set")
            return False
        openai.api_key = api_key

    try:
        # Perform a minimal request just to verify that authentication works
        openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": "ping"}],
            max_tokens=1,
        )
    except openai.AuthenticationError as exc:
        print(f"OpenAI API key authentication failed: {exc}")
        return False
    except openai.OpenAIError as exc:
        print(f"OpenAI API request failed: {exc}")
        return False

    print("OpenAI API key appears to be valid!")
    return True

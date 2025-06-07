# codex_agent.py
"""Utility functions for sending prompts to the OpenAI API."""

import os
import openai

# Lazily initialised OpenAI client
_client = None


def _get_client() -> openai.OpenAI:
    """Return a configured OpenAI client, creating it if necessary."""
    global _client
    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        _client = openai.OpenAI(api_key=api_key)
    return _client

def codex_agent(prompt: str) -> str:
    """Send a prompt to the OpenAI API and return the assistant's reply."""
    client = _get_client()
    try:
        response = client.chat.completions.create(
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
    try:
        client = _get_client()
    except ValueError:
        print("OPENAI_API_KEY environment variable is not set")
        return False

    try:
        # Perform a minimal request just to verify that authentication works
        client.chat.completions.create(
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

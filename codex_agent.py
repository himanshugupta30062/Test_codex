# codex_agent.py
"""Utility functions for sending prompts to the Gemini API."""

import os
import google.generativeai as genai

# Lazily initialised Gemini client
_client = None


def _get_client():
    """Return a configured Gemini client, creating it if necessary."""
    global _client
    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is not set")
        genai.configure(api_key=api_key)
        _client = genai
    return _client

def codex_agent(prompt: str) -> str:
    """Send a prompt to the Gemini API and return the assistant's reply."""
    client = _get_client()
    try:
        response = client.generate_text(
            model="models/text-bison-001",
            prompt=prompt,
            temperature=0.5,
        )
        answer = response.result.strip() if response.result else ""
    except Exception as exc:
        print(f"Gemini API request failed: {exc}")
        return ""

    print(f"Codex suggests: {answer}")
    return answer


def verify_gemini_key() -> bool:
    """Check that the configured Gemini API key is valid by making a tiny request."""
    try:
        client = _get_client()
    except ValueError:
        print("GEMINI_API_KEY environment variable is not set")
        return False

    try:
        # Perform a minimal request just to verify that authentication works
        client.generate_text(
            model="models/text-bison-001",
            prompt="ping",
            max_output_tokens=1,
        )
    except Exception as exc:
        print(f"Gemini API request failed: {exc}")
        return False

    print("Gemini API key appears to be valid!")
    return True

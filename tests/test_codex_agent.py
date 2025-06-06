import os
from unittest.mock import MagicMock, patch
import openai

from codex_agent import codex_agent, verify_openai_key


def test_codex_agent_returns_response(monkeypatch):
    os.environ['OPENAI_API_KEY'] = 'test'
    mock_resp = MagicMock()
    mock_choice = MagicMock()
    mock_choice.message.content = 'hello'
    mock_resp.choices = [mock_choice]
    with patch('openai.chat.completions.create', return_value=mock_resp) as mock_create:
        result = codex_agent('hi')
        assert result == 'hello'
        mock_create.assert_called_once()


def test_codex_agent_handles_openai_error(monkeypatch):
    os.environ['OPENAI_API_KEY'] = 'test'
    with patch('openai.chat.completions.create', side_effect=openai.OpenAIError('fail')) as mock_create:
        result = codex_agent('hi')
        assert result == ''
        mock_create.assert_called_once()


def test_verify_openai_key_success(monkeypatch):
    os.environ['OPENAI_API_KEY'] = 'test'
    with patch('openai.chat.completions.create', return_value=MagicMock()) as mock_create:
        assert verify_openai_key()
        mock_create.assert_called_once()


def test_verify_openai_key_failure(monkeypatch):
    os.environ['OPENAI_API_KEY'] = 'test'
    with patch('openai.chat.completions.create', side_effect=openai.OpenAIError('fail')) as mock_create:
        assert not verify_openai_key()
        mock_create.assert_called_once()

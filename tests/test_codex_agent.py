import os
from unittest.mock import MagicMock, patch
import openai

import codex_agent
from codex_agent import codex_agent, verify_openai_key


def test_codex_agent_returns_response(monkeypatch):
    os.environ['OPENAI_API_KEY'] = 'test'
    codex_agent._client = None
    mock_resp = MagicMock()
    mock_choice = MagicMock()
    mock_choice.message.content = 'hello'
    mock_resp.choices = [mock_choice]
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = mock_resp
    with patch('codex_agent._get_client', return_value=mock_client):
        result = codex_agent('hi')
        assert result == 'hello'
        mock_client.chat.completions.create.assert_called_once()


def test_codex_agent_handles_openai_error(monkeypatch):
    os.environ['OPENAI_API_KEY'] = 'test'
    codex_agent._client = None
    mock_client = MagicMock()
    mock_client.chat.completions.create.side_effect = openai.OpenAIError('fail')
    with patch('codex_agent._get_client', return_value=mock_client):
        result = codex_agent('hi')
        assert result == ''
        mock_client.chat.completions.create.assert_called_once()


def test_verify_openai_key_success(monkeypatch):
    os.environ['OPENAI_API_KEY'] = 'test'
    codex_agent._client = None
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = MagicMock()
    with patch('codex_agent._get_client', return_value=mock_client):
        assert verify_openai_key()
        mock_client.chat.completions.create.assert_called_once()


def test_verify_openai_key_failure(monkeypatch):
    os.environ['OPENAI_API_KEY'] = 'test'
    codex_agent._client = None
    mock_client = MagicMock()
    mock_client.chat.completions.create.side_effect = openai.OpenAIError('fail')
    with patch('codex_agent._get_client', return_value=mock_client):
        assert not verify_openai_key()
        mock_client.chat.completions.create.assert_called_once()

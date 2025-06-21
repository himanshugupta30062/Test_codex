import os
from unittest.mock import MagicMock, patch
from google.api_core.exceptions import GoogleAPIError

import codex_agent
from codex_agent import codex_agent, verify_gemini_key


def test_codex_agent_returns_response(monkeypatch):
    os.environ['GEMINI_API_KEY'] = 'test'
    codex_agent._client = None
    mock_client = MagicMock()
    mock_client.generate_text.return_value = MagicMock(result='hello')
    with patch('codex_agent._get_client', return_value=mock_client):
        result = codex_agent('hi')
        assert result == 'hello'
        mock_client.generate_text.assert_called_once()


def test_codex_agent_handles_gemini_error(monkeypatch):
    os.environ['GEMINI_API_KEY'] = 'test'
    codex_agent._client = None
    mock_client = MagicMock()
    mock_client.generate_text.side_effect = GoogleAPIError('fail')
    with patch('codex_agent._get_client', return_value=mock_client):
        result = codex_agent('hi')
        assert result == ''
        mock_client.generate_text.assert_called_once()


def test_verify_gemini_key_success(monkeypatch):
    os.environ['GEMINI_API_KEY'] = 'test'
    codex_agent._client = None
    mock_client = MagicMock()
    mock_client.generate_text.return_value = MagicMock(result='pong')
    with patch('codex_agent._get_client', return_value=mock_client):
        assert verify_gemini_key()
        mock_client.generate_text.assert_called_once()


def test_verify_gemini_key_failure(monkeypatch):
    os.environ['GEMINI_API_KEY'] = 'test'
    codex_agent._client = None
    mock_client = MagicMock()
    mock_client.generate_text.side_effect = GoogleAPIError('fail')
    with patch('codex_agent._get_client', return_value=mock_client):
        assert not verify_gemini_key()
        mock_client.generate_text.assert_called_once()

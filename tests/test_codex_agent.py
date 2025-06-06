import os
from unittest.mock import MagicMock, patch

from codex_agent import codex_agent


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

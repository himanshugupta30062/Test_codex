import json
import importlib

import pytest


def reload_app(monkeypatch):
    import app
    importlib.reload(app)
    return app


def test_app_loads_from_env(monkeypatch):
    monkeypatch.setenv("FLASK_SECRET_KEY", "envsecret")
    monkeypatch.setenv("FLASK_USERS_JSON", json.dumps({"u": "p"}))
    app = reload_app(monkeypatch)
    assert app.app.secret_key == "envsecret"
    assert app.USERS == {"u": "p"}


def test_app_loads_from_config(tmp_path, monkeypatch):
    cfg = tmp_path / "config.json"
    cfg.write_text(json.dumps({"secret_key": "cfgsecret", "users": {"a": "b"}}))
    monkeypatch.delenv("FLASK_SECRET_KEY", raising=False)
    monkeypatch.delenv("FLASK_USERS_JSON", raising=False)
    monkeypatch.setenv("APP_CONFIG_FILE", str(cfg))
    app = reload_app(monkeypatch)
    assert app.app.secret_key == "cfgsecret"
    assert app.USERS == {"a": "b"}

# Test_codex
This is a small demo showing how an environment can interact with the Gemini API. The project now relies on Google's `google-generativeai` package.

Set `GEMINI_API_KEY` in your environment before running `main.py` or the web demo.
You can copy `.env.example` to `.env` and update the key there:

```bash
export GEMINI_API_KEY=YOUR_KEY_HERE
```

### Application configuration

The Flask demo reads its configuration from environment variables or an optional
JSON file. The following variables can be set:

- `FLASK_SECRET_KEY` – value for `app.secret_key` used to sign sessions.
- `FLASK_USERS_JSON` – JSON object mapping usernames to passwords.
- `APP_CONFIG_FILE` – path to a JSON file containing `{"secret_key": "...", "users": {...}}`.
  Values from environment variables override the file.

If you encounter compatibility errors with the Gemini package, try upgrading or pinning the package version as specified in `requirements.txt`:

```bash
pip install --upgrade google-generativeai
```

## Setup

Install dependencies and run tests:

```bash
pip install -r requirements.txt
PYTHONPATH=. pytest -q
```

## Web Demo

To start a simple question-answer webpage, run:

```bash
python app.py
```

Then open <http://localhost:5000> in your browser.

## Verifying your API key

The `codex_agent` module exposes a helper function `verify_gemini_key` that makes
a tiny request to confirm your `GEMINI_API_KEY` is set correctly. Run the
following snippet to perform the check:

```python
from codex_agent import verify_gemini_key
verify_gemini_key()
```

If the API returns an authentication error, the function will print a message
indicating that the key may be incorrect.

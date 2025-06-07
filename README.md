# Test_codex
This is a small demo showing how an environment can interact with the OpenAI API. The project expects **OpenAI Python >=1.0** and uses the new chat completion API.

Set `OPENAI_API_KEY` in your environment before running `main.py` or the web demo:

```bash
export OPENAI_API_KEY=YOUR_KEY_HERE
```

## Clone the repository

Clone the project and enter the directory:

```bash
git clone https://github.com/himanshugupta30062/Test_codex.git
cd Test_codex
```

### Application configuration

The Flask demo reads its configuration from environment variables or an optional
JSON file. The following variables can be set:

- `FLASK_SECRET_KEY` – value for `app.secret_key` used to sign sessions.
- `FLASK_USERS_JSON` – JSON object mapping usernames to passwords.
- `APP_CONFIG_FILE` – path to a JSON file containing `{"secret_key": "...", "users": {...}}`.
  Values from environment variables override the file.

If you encounter compatibility errors with the OpenAI package, try upgrading or pinning the package version as specified in `requirements.txt`:

```bash
pip install --upgrade openai  # or `pip install openai==<version>`
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

The `codex_agent` module exposes a helper function `verify_openai_key` that makes
a tiny request to confirm your `OPENAI_API_KEY` is set correctly. Run the
following snippet to perform the check:

```python
from codex_agent import verify_openai_key
verify_openai_key()
```

If the API returns an authentication error, the function will print a message
indicating that the key may be incorrect.

### Changing the model

By default, `codex_agent.py` sends prompts to `gpt-3.5-turbo`. If you have access to GPT-4 or another model, open that file and replace the model name in the API calls.

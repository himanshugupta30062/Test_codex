# Test_codex
This is a small demo showing how an environment can interact with the OpenAI API. The project expects **OpenAI Python >=1.0** and uses the new chat completion API.

Set `OPENAI_API_KEY` in your environment before running `main.py` or the web demo:

```bash
export OPENAI_API_KEY=YOUR_KEY_HERE
```

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

# Test_codex
This is a small demo showing how an environment can interact with the OpenAI API. Set `OPENAI_API_KEY` in your environment before running `main.py` or the web demo.

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

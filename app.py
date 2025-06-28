"""Flask web application providing a simple interface to the Codex agent."""

from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    redirect,
    url_for,
    session,
)
from codex_agent import codex_agent


def load_settings():
    """Load the Flask secret key and user credentials."""
    import json
    import os

    config_path = os.getenv("APP_CONFIG_FILE")
    cfg = {}
    if config_path and os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
        except Exception:
            cfg = {}

    secret_key = os.getenv("FLASK_SECRET_KEY", cfg.get("secret_key", "change-me"))
    users_json = os.getenv("FLASK_USERS_JSON")
    if users_json:
        try:
            users = json.loads(users_json)
        except json.JSONDecodeError:
            users = {}
    else:
        users = cfg.get("users", {"admin": "password"})

    return secret_key, users


app = Flask(__name__)
app.secret_key, USERS = load_settings()

def login_required(func):
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return func(*args, **kwargs)

    return wrapper


@app.route('/')
@login_required
def index():
    username = session.get('username')
    return render_template('index.html', username=username)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json() or {}
    question = data.get('question', '')
    answer = codex_agent(question) if question else ''
    return jsonify({'answer': answer})


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if USERS.get(username) == password:
            session['username'] = username
            return redirect(url_for('index'))
        return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Simple sign-up page that stores new users in memory."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            return render_template('signup.html', error='Missing credentials')
        if username in USERS:
            return render_template('signup.html', error='User already exists')
        USERS[username] = password
        session['username'] = username
        return redirect(url_for('index'))
    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    import os
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 'yes']
    app.run(debug=debug_mode)

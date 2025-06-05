from flask import Flask, request, jsonify, render_template
from codex_agent import codex_agent

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json() or {}
    question = data.get('question', '')
    answer = codex_agent(question) if question else ''
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)

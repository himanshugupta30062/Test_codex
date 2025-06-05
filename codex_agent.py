# codex_agent.py

import openai

openai.api_key = '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'  # replace with your OpenAI API key

def codex_agent(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    answer = response.choices[0].message.content.strip()
    print(f"Codex suggests: {answer}")
    return answer

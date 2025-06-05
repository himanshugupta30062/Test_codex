# main.py

from environment import Environment
from codex_agent import codex_agent

env = Environment()
state = env.reset()

for _ in range(3):
    prompt = f"The current state is {state}. Suggest a helpful next action."
    action_str = codex_agent(prompt)
    action = {"suggested_action": action_str}

    state, reward, done = env.step(action)
    print(f"State after action: {state}, Reward: {reward}, Done: {done}\n")

    if done:
        print("Task completed!")
        break

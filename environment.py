# environment.py
"""Simple environment that counts steps and provides basic rewards."""

class Environment:
    """A small environment that tracks how many actions have been taken."""

    def __init__(self, max_steps: int = 3):
        self.max_steps = max_steps
        self.state = {}

    def reset(self):
        """Reset the environment state."""
        self.state = {"steps": 0, "history": []}
        print("Environment reset!")
        return self.state

    def step(self, action):
        """Apply an action and update the environment."""
        print(f"Performing action: {action}")
        self.state["steps"] += 1
        self.state["history"].append(action)
        reward = self.compute_reward()
        done = self.check_done()
        return self.state, reward, done

    def compute_reward(self):
        """Compute a simple reward based on the number of steps taken."""
        return self.state["steps"]

    def check_done(self):
        """Check if the maximum number of steps has been reached."""
        return self.state["steps"] >= self.max_steps

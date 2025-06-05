# environment.py

class Environment:
    def __init__(self):
        self.state = {}

    def reset(self):
        self.state = {}
        print("Environment reset!")
        return self.state

    def step(self, action):
        print(f"Performing action: {action}")
        self.state.update(action)
        reward = self.compute_reward()
        done = self.check_done()
        return self.state, reward, done

    def compute_reward(self):
        return 1

    def check_done(self):
        return False

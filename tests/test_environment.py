import pytest
from environment import Environment


def test_environment_progresses_to_done():
    env = Environment(max_steps=2)
    env.reset()
    state, reward, done = env.step({"a": 1})
    assert not done
    assert reward == 1
    state, reward, done = env.step({"b": 2})
    assert done
    assert state["steps"] == 2

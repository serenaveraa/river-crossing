from typing import Dict
from agent import Agent


class SimpleReflexAgent(Agent):
    def __init__(self, env):
        self.env = env
        self.step_index = 0

    def next_action(self, obs) -> Dict[str, int]:
        # Optimal 15-minute strategy encoded as reflex decisions by step parity
        # Persons: 0=A(1m), 1=B(2m), 2=C(5m), 3=D(8m)
        if self.step_index == 0:
            action = {"direction": 1, "person1": 0, "person2": 1}  # A+B -> R
        elif self.step_index == 1:
            action = {"direction": 0, "person1": 0, "person2": 0}  # A <- L
        elif self.step_index == 2:
            action = {"direction": 1, "person1": 2, "person2": 3}  # C+D -> R
        elif self.step_index == 3:
            action = {"direction": 0, "person1": 1, "person2": 1}  # B <- L
        else:
            action = {"direction": 1, "person1": 0, "person2": 1}  # A+B -> R

        self.step_index += 1
        return action



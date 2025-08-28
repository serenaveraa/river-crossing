from typing import List, Dict, Any, Optional
from agent import Agent


class ActionListAgent(Agent):
    def __init__(self, env, actions: List[Dict[str, int]]):
        self.env = env
        self.actions = actions
        self.current_index = 0

    def next_action(self, obs) -> Dict[str, int]:
        if self.current_index >= len(self.actions):
            # If actions are exhausted, repeat last action or raise
            # Here we raise to make error explicit to the caller
            raise IndexError("No more predefined actions available")

        action = self.actions[self.current_index]
        self.current_index += 1
        return action



## Practical 1 — River Crossing 🌉🔥

### Overview ✨
Educational Gymnasium environment modeling the classic River Crossing puzzle, plus multiple agents to interact with it: random, predefined action list, and a simple reflex strategy that solves it in exactly 15 minutes.

### The Puzzle 🧩
- **Friends**: Alberta (1m), Bernardo (2m), Carlos (5m), Diana (8m)
- **Rules**:
  - The bridge holds at most 2 people per crossing
  - There is a single torch that must be carried on every crossing
  - Someone must return with the torch when needed
  - Crossing time equals the slower person in the pair
- **Goal**: all four must cross in exactly 15 minutes

### Project Structure 📁
- `river_crossing_env.py`: Gymnasium `Env` (observation/action spaces, transitions, reward, render)
- `agent.py`: abstract agent interface (`next_action(obs)`) 
- `input_agent.py`: reads actions from the console
- `random_agent.py`: generates random actions (validated by the env)
- `action_list_agent.py`: executes a predefined list of actions in order
- `simple_reflex_agent.py`: fixed policy that achieves the 15-minute solution
- `river_crossing_utils.py`: small helpers (e.g., `finish`)
- `river_crossing.ipynb`: guided notebook to explore and run agents

### Action Format 🎮
Each action is a dictionary:
```python
{"direction": 0|1, "person1": 0..3, "person2": 0..3}
# direction: 0 = left, 1 = right
# persons: 0=A, 1=B, 2=C, 3=D
```

### How to Run ▶️
- Recommended: open `river_crossing.ipynb` and run cells in order.
  - Sections: “Input Agent”, “Random Agent”, “Action List Agent”, “Simple Reflex Agent”.

### Requirements 📦
- Python 3.11+
- Gymnasium
- (Optional) Poetry

Quick install with pip:
```bash
pip install gymnasium
```

### Included Agents 🤖
- **Random Agent**: explores by sampling actions at random.
- **Action List Agent**: consumes a predefined sequence of actions.
- **Simple Reflex Agent**: deterministic policy that reaches the 15-minute goal.

Minimal script example (similar to the notebook):
```python
from river_crossing_env import RiverCrossingEnv
from simple_reflex_agent import SimpleReflexAgent

env = RiverCrossingEnv()
agent = SimpleReflexAgent(env)
obs = env.reset()
done = False

while not done:
    action = agent.next_action(obs)
    obs, reward, done, info = env.step(action)

print("reward:", reward, "total_time:", info.get("time"))
```

### Recommended Reading 📚
Gym/Gymnasium basics: [Official docs](https://www.gymlibrary.dev/content/basic_usage/)



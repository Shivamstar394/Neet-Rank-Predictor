import pandas as pd

# Mock Data (Replace with actual API data)
historical_data = [
    {"quiz_id": 1, "user_id": 101, "score": 650, "responses": {1: "A", 2: "C", 3: "B"}},
    {"quiz_id": 2, "user_id": 101, "score": 670, "responses": {1: "B", 2: "C", 3: "A"}},
    {"quiz_id": 3, "user_id": 101, "score": 640, "responses": {1: "A", 2: "C", 3: "B"}},
]

df = pd.DataFrame(historical_data)
print(df.describe())  # Show statistical summary

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Mock Data (Replace with real NEET past results)
data = {
    "avg_quiz_score": [650, 670, 640, 700, 710, 720],
    "neet_rank": [10000, 9000, 11000, 5000, 4000, 3000]  # Lower rank is better
}

df = pd.DataFrame(data)

# Train Model
X = df[["avg_quiz_score"]]
y = df["neet_rank"]

model = LinearRegression()
model.fit(X, y)

# Predict rank for a new user
new_user_score = np.array([[680]])  # Example user
predicted_rank = model.predict(new_user_score)
print(f"Predicted NEET Rank: {predicted_rank[0]}")

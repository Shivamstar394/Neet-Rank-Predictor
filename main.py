from fastapi import FastAPI
import numpy as np
import pickle

app = FastAPI()

# Load trained model (for now, use the one in train_model.py)
def load_model():
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit([[650], [670], [640], [700], [710], [720]], [10000, 9000, 11000, 5000, 4000, 3000])
    return model

model = load_model()

@app.get("/predict-rank/")
def predict_rank(avg_quiz_score: float):
    predicted_rank = model.predict(np.array([[avg_quiz_score]]))[0]
    return {"predicted_rank": int(predicted_rank)}


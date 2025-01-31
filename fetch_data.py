import json

def fetch_quiz_data():
    current_quiz = {
        "user_id": 123,
        "score": 75,
        "questions": [
            {"id": 1, "topic": "Biology", "correct": True},
            {"id": 2, "topic": "Physics", "correct": False},
        ],
    }

    historical_quiz = {
        "user_id": 123,
        "history": [
            {"quiz_id": 1, "score": 60},
            {"quiz_id": 2, "score": 70},
            {"quiz_id": 3, "score": 80},
        ],
    }

    print("Current Quiz Data:", json.dumps(current_quiz, indent=2))
    print("Historical Quiz Data:", json.dumps(historical_quiz, indent=2))

fetch_quiz_data()

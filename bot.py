import json
import random

# Load intents from JSON
def load_data():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)

data = load_data()

import string

def normalize(text):
    return text.lower().translate(str.maketrans('', '', string.punctuation))

# Match user input to a pattern
def get_response(user_input):
    user_input_norm = normalize(user_input)
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern_norm = normalize(pattern)
            if pattern_norm in user_input_norm:
                return random.choice(intent["responses"])
    return "Sorry, I didn’t understand that. Could you rephrase?"


# Extract all patterns for dropdown
def get_all_questions():
    questions = []
    for intent in data["intents"]:
        questions.extend(intent["patterns"])
    return questions

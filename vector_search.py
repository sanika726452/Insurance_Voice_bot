from sentence_transformers import SentenceTransformer
import faiss
import json
import numpy as np

# Load data
with open("data.json", "r", encoding="utf-8") as f:
    intents = json.load(f)["intents"]

# Prepare data
all_patterns = []
tags = []
responses = {}

for intent in intents:
    tag = intent["tag"]
    for pattern in intent["patterns"]:
        all_patterns.append(pattern)
        tags.append(tag)
    responses[tag] = intent["responses"]

# Embed all patterns
model = SentenceTransformer("all-MiniLM-L6-v2")
pattern_embeddings = model.encode(all_patterns)

# Create FAISS index
dimension = pattern_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(pattern_embeddings))

# Function to get best response
def get_response_vector(user_input):
    user_embedding = model.encode([user_input])
    _, I = index.search(np.array(user_embedding), 1)
    best_match_idx = I[0][0]
    matched_tag = tags[best_match_idx]
    return responses[matched_tag][0]  # Pick first response

# 🎙️ Insurance Voice/Chat Bot

### AI-Powered Insurance Assistant using Vector Search (FAISS)

---

## 📌 Overview

The **Insurance Voice Bot** is an AI-powered assistant designed to answer insurance-related queries using semantic search and vector similarity.

Instead of traditional keyword matching, this system uses:

* Sentence embeddings
* FAISS vector database
* Intent-based response retrieval

This allows the bot to understand user queries based on meaning rather than exact words.

---

## 🧠 How It Works

1. **Intent Dataset (`data.json`)**

   * Contains tags, patterns (user queries), and responses.
   * Example:

     * Tag: `claim_process`
     * Patterns: "How to claim insurance?"
     * Responses: "To claim insurance, you must..."

2. **Sentence Embedding**

   * Uses `all-MiniLM-L6-v2` model from SentenceTransformers.
   * Converts text into numerical vectors.

3. **Vector Indexing (FAISS)**

   * All patterns are embedded.
   * Stored in a FAISS similarity index.
   * Enables fast nearest-neighbor search.

4. **Query Handling**

   * User input is converted into embedding.
   * FAISS finds closest matching intent.
   * Returns the corresponding response.

---

## ⚙️ Technologies Used

* Python
* SentenceTransformers (`all-MiniLM-L6-v2`)
* FAISS (Facebook AI Similarity Search)
* JSON-based intent dataset
* Streamlit (app.py used for UI)

---

## 📁 Project Structure

```
Insurance-Voice-Bot/
│
├── .devcontainer/
├── app.py
├── main.py
├── vector_search.py
├── data.json
├── requirements.txt
└── README.md
```

---

## 📂 File Explanation

### `data.json`

Contains intents dataset with:

* `tag`
* `patterns`
* `responses`

### `vector_search.py`

* Loads dataset
* Converts patterns into embeddings
* Creates FAISS index
* Retrieves best response using similarity search

### `main.py`

* Backend logic execution
* Connects vector search with application

### `app.py`

* User interface (Streamlit based)

### `requirements.txt`

Lists all required Python dependencies.

---

## 🚀 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Insurance-Voice-Bot.git
cd Insurance-Voice-Bot
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

If using Streamlit:

```bash
streamlit run app.py
```

If using terminal version:

```bash
python main.py
```

---

## 🧪 Example Queries

* What is term insurance?
* How to claim insurance?
* What documents are required for claim?
* What is premium payment process?

---

## 🔍 Core Feature

* Semantic understanding using embeddings
* Fast vector similarity search using FAISS
* Intent-based structured responses
* Lightweight and scalable architecture

---

## 🎯 Project Objective

To build an intelligent insurance assistant that can understand natural language queries and provide relevant responses using vector-based semantic matching.

---

## 🔮 Future Improvements

* Add voice input using SpeechRecognition
* Add text-to-speech output
* Integrate LLM for dynamic response generation
* Add web deployment
* Improve dataset size for better accuracy


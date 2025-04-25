from flask import Flask, render_template, request
import requests
from sentence_transformers import SentenceTransformer
import chromadb
import os

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Set up ChromaDB
client = chromadb.Client()
collection = client.get_or_create_collection("university")

# Load data if not already added
if collection.count() == 0:
    with open("context_data/university_facts.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    embeddings = model.encode(lines).tolist()
    collection.add(
        documents=lines,
        embeddings=embeddings,
        ids=[f"doc{i}" for i in range(len(lines))]
    )

app = Flask(__name__)
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral:7b-instruct"

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        user_question = request.form["question"]

        # Embed user question and search context
        question_embedding = model.encode(user_question).tolist()
        results = collection.query(query_embeddings=[question_embedding], n_results=3)
        context = "\n".join(results['documents'][0])

        # Construct enhanced prompt
        full_prompt = f"""
        You are a university assistant. Use the context below to answer the question.

        Context:
        {context}

        Question: {user_question}
        """

        response = requests.post(OLLAMA_URL, json={
            "model": MODEL_NAME,
            "prompt": full_prompt,
            "stream": False
        })

        if response.ok:
            result = response.json()
            answer = result.get("response", "No response from Ollama.")
        else:
            answer = "Error contacting Ollama."

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)

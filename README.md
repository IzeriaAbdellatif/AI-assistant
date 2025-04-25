# 🧠 University Chatbot with Flask + Ollama (RAG)

This project is a simple AI-powered chatbot designed for a university platform. It uses [Ollama](https://ollama.com/) to run large language models (LLMs) locally and integrates Retrieval-Augmented Generation (RAG) to answer user questions based on university-specific information.

---

## 🚀 Features

- 🗣️ Conversational chatbot powered by **Mistral 7B** or **LLaMA 3 8B**
- 🔎 Uses **RAG** to retrieve relevant answers from custom knowledge
- 🧠 Built with **Flask** (Python) and a simple HTML frontend
- 🧾 Answers questions about university courses, exams, and services
- 💾 Supports local context storage (e.g. `university_facts.txt`)

---

## ⚙️ Technologies Used

- Python 3.10+
- Flask
- Ollama (for LLM inference)
- Sentence Transformers (`all-MiniLM-L6-v2`)
- Vector database: FAISS or ChromaDB (optional, depending on version)

---

## 📁 Project Structure

```
ollama-rag-flask/
├── app.py                     # Flask backend
├── context_data/
│   └── university_facts.txt  # Custom knowledge base
├── templates/
│   └── index.html            # Frontend chat interface
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 🧪 How It Works

1. The user enters a question via a simple web interface.
2. Flask encodes the question using sentence-transformers.
3. A vector database searches for the most relevant pieces of context.
4. The context + question are sent to the LLM running via Ollama.
5. The model generates a natural language answer shown on the webpage.

---

## 📦 Setup Instructions

1. **Install Ollama**  
   Follow the instructions at [ollama.com](https://ollama.com/) to install and run Ollama.

2. **Pull a lightweight model**  
   Recommended:  
   `mistral:7b-instruct` or `llama3:8b`

3. **Clone this project**  
   Make sure you have Python 3.10+ installed.

4. **Install dependencies**  
   Use the command:  
   `pip install -r requirements.txt`

5. **Run the Flask server**  
   Start Ollama first:  
   `ollama run mistral:7b-instruct`  
   Then in another terminal:  
   `python app.py`

6. **Open the app in your browser**  
   Go to [http://localhost:5000](http://localhost:5000)

---

## 📚 Custom Knowledge Base

All university-specific data is stored in `context_data/university_facts.txt`. You can edit this file with facts like:

- Exam dates  
- Course instructors  
- Submission procedures  
- Contact methods  
- Password reset steps

The model will search this file to answer user questions.

---

## 🛠️ Troubleshooting

- If `chromadb` fails to install, switch to `faiss-cpu` as an alternative.
- Make sure Ollama is running before launching Flask.
- If RAM is limited, use smaller models like `mistral:7b`.

---

## 📌 To Do (Ideas)

- Use real-time university data from Cassandra and MinIO
- Add role-based answers (students vs teachers)
- Deploy with Docker or on a VM (e.g. VMware at EST Salé)
- Add multilingual support (Arabic, French)

---

## 📄 License

MIT License. You are free to use, adapt, and distribute this project.


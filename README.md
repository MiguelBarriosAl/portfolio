# 🧠 AI Portfolio CV

This project is an interactive AI-powered portfolio designed to showcase my profile as an **AI / Machine Learning Engineer**, built using a modern RAG (Retrieval-Augmented Generation) architecture.

It leverages:

- **FastAPI** for the API layer
- **LangChain** with **Ollama** as a local LLM
- **Qdrant** as a vector database
- PDF and unstructured text embedding for intelligent query response

> Example question:  
> “What’s your experience with MLOps?” or  
> “What kind of AI projects have you worked on?”

---

## 🚀 What this project does

- Indexes my profile from PDF or plain text files (e.g., `Miguel_Barrios.pdf`)
- Lets users query my profile using natural language
- Uses vector similarity search and LLMs to generate contextual answers
- Supports real-time re-indexing of updated documents

---

## 🛠 Tech Stack

- **Python** · `FastAPI` · `LangChain` · `Qdrant` · `Ollama`
- **Document Parsing**: `unstructured`, `pdfminer.six`, `pytesseract`
- **Package Management**: `Poetry`
- **CI/CD**: GitHub Actions (in progress)

---

## 📂 Project Structure

     ──  api/ # FastAPI endpoints
    ├── services/ # Core logic (embedding, vectorstore, QA)
    ├── scripts/ # Indexing scripts
    ├── data/dev/ # Sample PDFs (e.g. Miguel_Barrios.pdf)
    ├── tests/ # Unit tests
    ├── main.py # FastAPI entrypoint
    └── pyproject.toml # Poetry configuration


---

## 🔄 Indexing a new document


    poetry run python scripts/index_profile.py --file data/dev/ <any_cv_document>.pdf


## 🧠 Ask questions via API

    curl -X POST http://localhost:8000/ask \
    -H "Content-Type: application/json" \
    -d '{"query": "What is Miguel’s experience with Python?"}'

✅ Running tests

    poetry run pytest

docker run --env-file .env -p 8000:8000   -v $(pwd)/data:/app/data   ai-portfolio-backend
poetry run streamlit run frontend/Home.py
docker run -d --name qdrant -p 6333:6333 qdrant/qdrant

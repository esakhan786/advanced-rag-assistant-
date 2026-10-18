# 📚 Advanced RAG Assistant

An end-to-end **Advanced RAG** (Retrieval-Augmented Generation) application built with **Python, LangChain, Google Gemini, FAISS, and Streamlit**.

Supports:
- **Google Gemini** (`gemini-2.5-flash` - 100% Free tier)
- **Groq** (`llama-3.3-70b-versatile` - 100% Free tier)
- **OpenAI** (`gpt-4o-mini`)
- **Local HuggingFace Embeddings** (`sentence-transformers/all-MiniLM-L6-v2` - runs locally on CPU with 0 API cost)
- **FAISS & BM25 Hybrid Retrieval** with Parent-Child chunking & Cross-Encoder Reranking

---

## 🚀 Quickstart

### 1. Installation
```bash
cd Advanced-RAG-Capstone
pip install -r requirements.txt
```

### 2. Environment Setup (.env)
Create a `.env` file in `Advanced-RAG-Capstone/`:
```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_CHAT_MODEL=gemini-2.5-flash
EMBEDDING_PROVIDER=huggingface
HUGGINGFACE_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
VECTOR_DB=faiss
```

### 3. Build Vector Database
```bash
python scripts/build_index.py
```

### 4. Run the Web Application
```bash
streamlit run app.py
```

---

## 🌐 Deploying to Streamlit Community Cloud

1. Push this repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and create a **New app**.
3. Select your repository and branch (`main`).
4. Set Main file path to: `Advanced-RAG-Capstone/app.py` (or `app.py` if deployed from the inner folder).
5. In **Advanced Settings > Secrets**, add:
   ```toml
   GEMINI_API_KEY = "your_key_here"
   LLM_PROVIDER = "gemini"
   ```
6. Click **Deploy**!

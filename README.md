# RAG Document Q&A

Ask questions about your own PDF documents using retrieval-augmented generation (RAG). Upload any PDFs, run the ingestion pipeline, and query them in plain English — answers are grounded in your documents, not the model's training data.

## How it works

1. **Ingest** — PDFs are loaded, split into overlapping chunks, converted to vectors using a local embedding model, and stored in ChromaDB
2. **Query** — your question is embedded with the same model, the most relevant chunks are retrieved, and Claude answers using only that context

## Setup

**1. Clone the repo**
```bash
git clone git@github.com:your-username/rag-doc-qa.git
cd rag-doc-qa
```

**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your Anthropic API key**

Create a `.env` file in the project root:
```
ANTHROPIC_API_KEY=your-key-here
```

Get a key at [console.anthropic.com](https://console.anthropic.com).

**5. Add your PDFs**

Drop any PDF files into the `data/pdfs/` folder.

## Usage

**Ingest your documents** (run once, or whenever you add new PDFs):
```bash
python main.py ingest
```

**Ask a question:**
```bash
python main.py ask "What are the key findings?"
python main.py ask "Who authored this document?"
python main.py ask "Summarize the main recommendations"
```

## Project structure

```
rag-doc-qa/
├── data/
│   └── pdfs/           # drop your PDFs here
├── src/
│   ├── loader.py       # PDF parsing with PyMuPDF
│   ├── chunker.py      # splits text into overlapping chunks
│   ├── embedder.py     # converts chunks to vectors, stores in ChromaDB
│   ├── retriever.py    # queries ChromaDB for relevant chunks
│   └── qa.py           # sends context + question to Claude
├── main.py             # CLI entrypoint
├── requirements.txt
└── .env                # not committed — add your API key here
```

## Stack

- [Claude](https://anthropic.com) — answer generation
- [ChromaDB](https://www.trychroma.com) — local vector database
- [sentence-transformers](https://www.sbert.net) — local embedding model (`all-MiniLM-L6-v2`)
- [PyMuPDF](https://pymupdf.readthedocs.io) — PDF parsing
- [python-dotenv](https://github.com/theskumar/python-dotenv) — environment variable loading

## Notes

- The `chroma_db/` folder is created automatically on first ingest and persists between runs
- The embedding model downloads automatically on first run (~80MB)
- Chunk size and overlap can be tuned in `src/chunker.py` (`chunk_size=500`, `overlap=100`)
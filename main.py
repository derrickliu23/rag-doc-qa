from dotenv import load_dotenv
load_dotenv()

from src.loader import load_pdfs
from src.chunker import chunk_documents
from src.embedder import embed_and_store
from src.qa import ask
import sys

def ingest():
    docs = load_pdfs("data/pdfs")
    chunks = chunk_documents(docs)
    embed_and_store(chunks)
    print("Ingestion complete.")

def query(question: str):
    answer = ask(question)
    print(f"\nAnswer: {answer}\n")

if __name__ == "__main__":
    if sys.argv[1] == "ingest":
        ingest()
    elif sys.argv[1] == "ask":
        question = " ".join(sys.argv[2:])
        query(question)
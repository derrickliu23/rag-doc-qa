import fitz  # PyMuPDF
from pathlib import Path

def load_pdfs(pdf_dir: str) -> list[dict]:
    docs = []
    for path in Path(pdf_dir).glob("*.pdf"):
        doc = fitz.open(path)
        text = "\n".join(page.get_text() for page in doc)
        docs.append({"filename": path.name, "text": text})
        print(f"Loaded: {path.name} ({len(doc)} pages)")
    return docs
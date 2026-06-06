from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./chroma_db")

def get_or_create_collection(name: str = "documents"):
    return client.get_or_create_collection(name)

def embed_and_store(chunks: list[dict], collection_name: str = "documents"):
    collection = get_or_create_collection(collection_name)

    texts = [c["text"] for c in chunks]
    ids = [f"{c['source']}-chunk-{c['chunk_index']}" for c in chunks]
    metadatas = [{"source": c["source"], "chunk_index": c["chunk_index"]} for c in chunks]

    print(f"Embedding {len(texts)} chunks...")
    embeddings = model.encode(texts).tolist()

    collection.add(
        documents=texts,
        embeddings=embeddings,
        ids=ids,
        metadatas=metadatas
    )
    print(f"Stored {len(texts)} chunks in ChromaDB")
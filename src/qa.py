import os
import anthropic
from src.retriever import retrieve

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

def ask(question: str) -> str:
    chunks = retrieve(question, n_results=3)

    context = "\n\n".join([
        f"[From {c['source']}]\n{c['text']}"
        for c in chunks
    ])

    prompt = f"""You are a helpful assistant. Answer the question using only the context below.
If the answer isn't in the context, say "I don't have enough information to answer that."

Context:
{context}

Question: {question}
"""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text
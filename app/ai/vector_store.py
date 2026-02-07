from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

class VectorStore:
    def __init__(self):
        self.vectors = []
        self.texts = []

    def add(self, text: str):
        emb = model.encode(text)
        self.vectors.append(emb)
        self.texts.append(text)

    def search(self, query: str, top_k: int = 3):
        q_emb = model.encode(query)
        scores = [np.dot(q_emb, v) for v in self.vectors]
        ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
        return [self.texts[i] for i, _ in ranked[:top_k]]

vector_store = VectorStore()

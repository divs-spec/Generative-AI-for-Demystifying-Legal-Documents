from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class DocQA:
def __init__(self, simplifier=None, embedding_model: str = 'all-MiniLM-L6-v2'):
self.embedder = SentenceTransformer(embedding_model)
self.index = None
self.chunks = []
self.simplifier = simplifier


def build_vector_store(self, chunks):
self.chunks = chunks
embeddings = self.embedder.encode(chunks, convert_to_numpy=True)
dim = embeddings.shape[1]
self.index = faiss.IndexFlatL2(dim)
self.index.add(embeddings)


def query(self, question: str, top_k: int = 3):
if self.index is None:
return "No index built yet", []
q_emb = self.embedder.encode([question], convert_to_numpy=True)
D, I = self.index.search(q_emb, top_k)
hits = [self.chunks[i] for i in I[0]]
context = "\n".join(hits)
if self.simplifier:
answer = self.simplifier.simplify(context, level="medium")
else:
answer = context
return answer, hits

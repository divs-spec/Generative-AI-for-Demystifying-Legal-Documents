import pdfplumber
import re


# Extract text from PDF file
def extract_text_from_pdf(path: str) -> str:
text = ""
with pdfplumber.open(path) as pdf:
for page in pdf.pages:
text += page.extract_text() + "\n"
return text


# Split text into clauses/sentences
def simple_clause_split(text: str):
clauses = re.split(r'(?<=[.;])\s+', text.strip())
return [c for c in clauses if len(c.strip()) > 0]


# Break text into chunks for embeddings
def chunk_text(text: str, chunk_size: int = 300):
words = text.split()
chunks = []
for i in range(0, len(words), chunk_size):
chunks.append(" ".join(words[i:i+chunk_size]))
return chunks

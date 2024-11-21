import os
import pdfplumber
from docx import Document
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model globally
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text(file_path):
    """Extract text from supported file formats."""
    try:
        if file_path.endswith(('.txt', '.js', '.ts', '.tsx', '.json', '.html', '.css')):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        elif file_path.endswith('.pdf'):
            with pdfplumber.open(file_path) as pdf:
                return " ".join([page.extract_text() or "" for page in pdf.pages])
        elif file_path.endswith('.docx'):
            doc = Document(file_path)
            return " ".join([p.text for p in doc.paragraphs])
        else:
            return None
    except Exception as e:
        return None

def search_files(base_dir, query):
    """Perform semantic search across files in the directory."""
    results = []
    supported_extensions = ('.txt', '.pdf', '.docx', '.js', '.ts', '.tsx', '.json', '.html', '.css')
    query_embedding = model.encode(query)
    file_embeddings, file_paths = [], []

    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(supported_extensions):
                file_path = os.path.join(root, file)
                content = extract_text(file_path)
                if content:
                    file_embeddings.append(model.encode(content))
                    file_paths.append(file_path)

    if file_embeddings:
        similarities = cosine_similarity([query_embedding], file_embeddings)[0]
        results = sorted(zip(file_paths, similarities), key=lambda x: x[1], reverse=True)

    return results[:10]  # Return top 10 results

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
        if file_path.endswith(('.txt', '.js', '.ts', '.tsx', '.json', '.html', '.css', '.py')):
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
        print(f"Error extracting text from {file_path}: {e}")
        return None


def search_files(base_dir, query):
    """
    Search for files matching the query in two ways:
    1. File name contains the query.
    2. Query found in file content.
    """
    results = []
    supported_extensions = ('.txt', '.pdf', '.docx', '.js', '.ts', '.tsx', '.json', '.html', '.css', '.py')
    query_embedding = model.encode(query)
    file_embeddings, file_paths = [], []

    # Search through files
    for root, _, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = file.lower()

            # Check if the file name contains the query
            if query.lower() in file_name:
                results.append((file_path, "File Name Match"))

            # Extract content for semantic search
            content = extract_text(file_path)
            if content:
                # Direct content match
                if query.lower() in content.lower():
                    results.append((file_path, "Exact Content Match"))
                else:
                    file_paths.append(file_path)
                    file_embeddings.append(model.encode(content))

    # Perform semantic similarity search
    if file_embeddings:
        similarities = cosine_similarity([query_embedding], file_embeddings)[0]
        for i, score in enumerate(similarities):
            if score > 0.5:  # Threshold for relevance
                results.append((file_paths[i], f"Content Match (Score: {score:.2f})"))

    # Deduplicate results
    seen = set()
    final_results = []
    for file_path, match_type in results:
        if file_path not in seen:
            seen.add(file_path)
            final_results.append((file_path, match_type))

    return final_results[:10]  # Return top 10 results


if __name__ == "__main__":
    base_dir = "C:\\Open WebUI\\searching-transformer"  # Replace with your directory path
    query = "base"
    results = search_files(base_dir, query)

    print(f"Search Results for \"{query}\":")
    for file_path, match_type in results:
        print(f"{file_path} ({match_type})")

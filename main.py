import os
import pdfplumber
from docx import Document
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm

# Load pre-trained model from Hugging Face
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text(file_path):
    """Extract text from various file formats."""
    print(f"Processing file: {file_path}")
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
            return None  # Unsupported file type
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
        return None

def search_files(base_dir, query, supported_extensions):
    """Search for files by name or content containing the query."""
    print(f"Scanning directory: {base_dir}")
    results = []

    # Step 1: Gather all files (recursively)
    all_files = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            all_files.append(os.path.join(root, file))

    if not all_files:
        print("No files found in the directory or its subdirectories.")
        return []

    print(f"Found {len(all_files)} files. Starting search...")

    # Step 2: Generate embeddings for the query
    query_embedding = model.encode(query)

    # Step 3: Process files with a progress bar
    file_embeddings = []
    file_paths = []
    for file_path in tqdm(all_files, desc="Processing files"):
        if file_path.endswith(supported_extensions):
            content = extract_text(file_path)
            if content:
                file_embedding = model.encode(content)
                file_embeddings.append(file_embedding)
                file_paths.append(file_path)

    # Step 4: Calculate cosine similarities between the query and all file contents
    similarities = cosine_similarity([query_embedding], file_embeddings)[0]

    # Step 5: Sort results by similarity score
    sorted_results = sorted(zip(file_paths, similarities), key=lambda x: x[1], reverse=True)

    # Step 6: Return the top results
    for file_path, similarity in sorted_results[:10]:  # Top 10 results
        results.append((file_path, similarity))

    return results

if __name__ == "__main__":
    # Input directory
    directory = input("Enter the directory path to search (e.g., '/content/my_files'): ")
    if not os.path.exists(directory):
        print("Directory not found. Please check the path.")
    else:
        # Debugging: Print directory contents
        print("Directory contents:", os.listdir(directory))

        # Supported extensions
        supported_extensions = ('.txt', '.pdf', '.docx', '.js', '.ts', '.tsx', '.json', '.html', '.css')

        # Input search query
        search_query = input("Enter your search query: ")
        search_results = search_files(directory, search_query, supported_extensions)

        # Display results
        if search_results:
            print("\nSearch Results:")
            for file_path, similarity in search_results:
                print(f"Similarity: {similarity:.4f} - {file_path}")
        else:
            print("No results found.")

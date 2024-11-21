# **File Search and Semantic Search Enhancement**

This project is a file search application that allows users to search for files within a specified directory based on a query. It includes advanced features like **semantic similarity search** using **Sentence Transformers**, file type filtering, sorting, and date range filtering.

---

## **Features**

### **1. Basic Search**
- Search for files in a directory by specifying:
  - **Directory Path**.
  - **Query**.
- Results are returned based on matching file names.

### **2. Semantic Search**
- Powered by **SentenceTransformer** for semantic similarity search.
- Matches the query against:
  - **File Names**.
  - **File Content**.
- Supports file formats like:
  - `.txt`, `.js`, `.ts`, `.html`, `.pdf`, `.docx`, and more.

### **3. Filters for Advanced Search**
- **File Type Filter**: Narrow results to specific file types (e.g., `.py`, `.html`, `.js`).
- **Sorting Options**:
  - **By Score**: Sort results by semantic similarity scores (Ascending/Descending).
  - **By Date**: Sort by file modification date (Ascending/Descending).
- **Date Range Filter**: Filter results to include files modified within a specific date range.

### **4. User Interface**
- A web interface built with **Flask**.
- Dynamically renders results, showing:
  - **File Names**.
  - **Similarity Scores**.
  - **Modification Dates**.

---

## **Project Structure**

```plaintext
file-search-project/
├── app/
│   ├── templates/
│   │   ├── base.html        # Common UI elements
│   │   ├── home.html        # Search form page
│   │   └── results.html     # Results display page
│   ├── routes/
│   │   └── main.py          # Routes for search logic
│   └── static/
│       └── style.css        # CSS file for styling
├── utils/
│   └── file_search.py       # Search logic using semantic search and filters
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container configuration
├── .gitignore               # Ignored files for Git
└── README.md                # Documentation


# **Installation**

Step 1: Clone the Repository

bash
git clone <repository_url>
cd file-search-project

Step 2: Create a Virtual Environment (Optional but Recommended)

bash
python3 -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`

Step 3: Install Dependencies
Install all required dependencies:

bash
pip install -r requirements.txt
Or install manually:

bash
pip install flask sentence-transformers pdfplumber python-docx scikit-learn

Step 4: Run the Application
Start the Flask app:

bash
python app/routes/main.py
The app will run locally at: http://127.0.0.1:5000/

Usage

Enter Search Parameters:

Open the home page at / to input:
A directory path.
A search query.
Optional filters (file type, sort order, date range).

View Results:

Results will display:
File name.
Semantic similarity score (if applicable).
File modification date.


## ** Features and Enhancements **

1. File Type Filter
Search for specific file types, e.g., .js, .html, etc.

2. Sorting and Ranking
Sort results by:
Semantic Similarity Score (ascending/descending).
Modification Date (ascending/descending).

3. Date Range Filtering
Specify a date range to filter files modified within that timeframe.

4. Semantic Search
Leverages SentenceTransformer to rank files based on semantic similarity.
Results are more accurate, even for non-exact matches.


Example Use Case
Scenario:
You have a directory with multiple JavaScript files.
Search Parameters:

Query: "base"
File Type: .js
Sort: "score_desc" (Sort by relevance)
Date Range: From 2024-01-01 to 2024-11-30
Outcome:
All .js files containing the word "base" are returned, sorted by relevance and filtered by the specified date range.

# **Contribution**
We welcome contributions!

Fork the repository.
Create a new branch for your changes.
Submit a pull request with proper documentation and testing.

# **License**
This project is licensed under the MIT License.

**Future Improvements -**

# User Authentication:

Implement user accounts and session management for saving preferences.

# Better UI:

Upgrade the front-end with frameworks like React or Vue.js.

# Advanced Filters:

Include filters for file size, creation date, etc.

# Search History:

Save search history for easy access to past searches and results.

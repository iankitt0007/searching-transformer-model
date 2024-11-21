File Search and Semantic Search Enhancement

This project is a file search application that allows users to search for files within a specified directory based on a given query. The project incorporates advanced features like semantic similarity search using Sentence Transformers and allows filtering by file type, sorting by relevance or modification date, and filtering by a date range.

Features

1. Basic Search
Users can perform a basic search within a directory by specifying a directory and a query.
File names that match the query are returned as search results.

2. Semantic Search
The project uses SentenceTransformer to compute sentence embeddings and perform semantic similarity search.
It matches the query not only by the file name but also by the content within the files.
Supports various file formats such as .txt, .js, .ts, .html, .pdf, and .docx.

3. Filters for Advanced Search
Users can refine their search using the following optional filters:
File Type Filter: Allows the user to search within specific file types (e.g., .py, .js, .html).
Sort Results: Provides multiple sorting options:
Sort by Score (Descending/Ascending): Based on semantic similarity scores of file content.
Sort by Date (Descending/Ascending): Based on the file’s last modification date.
Date Range Filter: Filters results based on a specified modification date range (date_from, date_to).

4. User Interface
A simple web interface built with Flask allows users to enter search queries and filter options.
The results are dynamically rendered, showing the file names, similarity scores, and file modification dates.

Project Structure

graphql

file-search-project/
├── app/
│   ├── templates/
│   │   ├── base.html        # Base HTML template for common UI elements
│   │   ├── home.html        # The main search form page
│   │   └── results.html     # The page displaying search results
│   ├── routes/
│   │   └── main.py          # Routes to handle search logic and rendering
│   └── static/
│       └── style.css        # (Optional) CSS file for styling
├── utils/
│   └── file_search.py       # File search logic using semantic search and filters
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker configuration file for containerization
├── .gitignore               # Git ignore file for excluding unnecessary files
└── README.md                # This file


Installation
Step 1: Clone the Repository
Clone the repository to your local machine.
bash
Copy code
git clone <repository_url>
cd file-search-project

Step 2: Create a Virtual Environment (Optional but Recommended)
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Step 3: Install Dependencies
Install the required dependencies using pip:
bash
Copy code
pip install -r requirements.txt

You can install the required dependencies manually as well:
bash
Copy code
pip install flask sentence-transformers pdfplumber python-docx scikit-learn

Step 4: Run the Application
You can run the Flask application locally by running the following command:
bash
Copy code
python app/routes/main.py

By default, the app will run on http://127.0.0.1:5000/.

Usage
Enter Search Parameters:
Open the home page (/) to enter a directory path and a query.
Optional filters are available for file type, sort order, and date range.
View Results:
After submitting the form, the results will be displayed based on the provided query and optional filters.
Results show the file name, semantic similarity score (if applicable), and file modification date.

Features and Enhancements
1. File Type Filter:
Allows users to search for specific file types. For example, if you're looking for .js or .html files, you can specify that filter to limit the search to those file extensions.
2. Sorting and Ranking:
Results can be sorted based on semantic similarity scores or file modification date, either ascending or descending. This allows users to prioritize the most relevant or recently modified files.
3. Date Range Filtering:
Users can filter the search results by a date range, providing additional control to find files modified within a specific timeframe.
4. Semantic Search:
Unlike traditional file search tools, this project uses semantic search with SentenceTransformer. It computes embeddings of both the query and file content and ranks the files based on semantic similarity, enabling more accurate search results even when file names don't exactly match the query.

Example Use Case
Assume you have a directory with several files related to JavaScript development. You can perform a search like:
Query: "base"
File Type: .js
Sort: "score_desc" (Sort by relevance score)
Date Range: From 2024-01-01 to 2024-11-30
This would return all .js files containing the word "base", sorted by semantic relevance and filtered by the specified date range.

Contribution
If you'd like to contribute to this project, feel free to fork the repository, create a branch, and submit a pull request. Ensure that your changes are well-documented and tested.

License
This project is licensed under the MIT License.

Future Improvements
User Authentication: Implement user accounts and session management for saving search preferences.
Better UI: Enhance the front-end interface with modern UI frameworks like React or Vue.js.
Advanced Filters: Add more advanced filtering options such as file size, creation date, etc.
Search History: Implement search history so users can view their previous searches and results.

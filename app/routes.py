from flask import Blueprint, render_template, request
from utils.file_search import search_files

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        directory = request.form.get('directory')
        query = request.form.get('query')
        if not directory or not query:
            return render_template('home.html', error="Both directory and query are required.")
        results = search_files(directory, query)
        return render_template('results.html', results=results, query=query)
    return render_template('home.html')

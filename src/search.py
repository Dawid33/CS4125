from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.db_manager import DBManager

search = Blueprint('search', __name__)

db_manager = DBManager()


@search.route('/search', methods=['GET'])
def search_books():
    # Get query parameters
    book_id = request.args.get('id')
    title = request.args.get('title', '').strip()
    author = request.args.get('author', '').strip()

    # Use the parameters to filter the book search
    if book_id or title or author:
        books = db_manager.filter_books(book_id=book_id, title=title, author=author)
    else:
        books = db_manager.get_default_catalog()

    # Render the template with the filtered books
    return render_template('search/search.html', books=books)

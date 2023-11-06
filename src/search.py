from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.db_manager import DBManager

search = Blueprint('search', __name__)

db_manager = DBManager()


@search.route('/search', methods=['GET'])
def search_books():
     
     """Allows a User to query the db for a book based on title, author and isbn"""
     # Get query parameters
     title = request.args.get('title', '').strip()
     author = request.args.get('author', '').strip()
     isbn = request.args.get('isbn', '').strip()

     # Use the parameters to filter the book search
     if title or author or isbn:
          books = db_manager.filter_books(title=title, author=author, isbn=isbn)
     else:
          books = db_manager.get_default_catalog()

     # Render the template with the filtered books
     return render_template('search/search.html', books=books)

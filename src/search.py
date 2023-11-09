from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.catalogue.catalogue_manager import Catalogue

search = Blueprint('search', __name__)

catalogue = Catalogue()


@search.route('/search', methods=['GET'])
def search_books():
     
     """Allows a User to query the db for a book based on title, author and isbn"""
     # Get query parameters
     title = request.args.get('title', '').strip().lower()
     author = request.args.get('author', '').strip().lower()
     isbn = request.args.get('isbn', '').strip().lower()
     
     books = 0

     # Use the parameters to filter the book search
     if title or author or isbn:
          books = catalogue.filter_books(title, author, isbn)

     # Render the template with the filtered books
     return render_template('search/search.html', books=books)

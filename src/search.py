# search.py
from flask import Blueprint, render_template, request
from models.catalogue.catalogue_manager import Catalogue
from models.catalogue.book_search_strategies import (
    SearchByTitleStrategy,
    SearchByAuthorStrategy,
    SearchByISBNStrategy
)

search = Blueprint('search', __name__)
catalogue = Catalogue()


@search.route('/search', methods=['GET'])
def search_books():
    """
    Handle book search requests and render search results.

    Retrieves search parameters from the query string, sets the corresponding search strategy based on the
    parameters provided (title, author, or ISBN), and executes the search. If no parameters are provided,
    an empty list is returned. The results are then displayed using the 'search/search.html' template.

    Returns:
    Rendered HTML template with search results.
    """
    # Get search parameters
    title = request.args.get('title')
    author = request.args.get('author')
    isbn = request.args.get('isbn')

    # Initialize an empty list for books
    books = []

    # Set the appropriate search strategy based off the provided search parameter string and execute the search
    if title:
        catalogue.set_search_strategy(SearchByTitleStrategy())
        books = catalogue.execute_search(title)
    elif author:
        catalogue.set_search_strategy(SearchByAuthorStrategy())
        books = catalogue.execute_search(author)
    elif isbn:
        catalogue.set_search_strategy(SearchByISBNStrategy())
        books = catalogue.execute_search(isbn)
    else:
        # Use the default strategy to get all books
        books = catalogue.execute_search()

    # Render the search results in the HTML template
    return render_template('search/search.html', books=books)

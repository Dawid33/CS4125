from models.catalogue.book_search_strategies import (
    SearchByTitleStrategy,
    SearchByAuthorStrategy,
    SearchByISBNStrategy
)
from models.database_manager.db_manager import DBManager


class Catalogue:
    """
    The Catalogue class is designed to manage book searches using different methods, such as by title, author,
    or ISBN. It does this by using a search_strategy that can be easily changed without modifying the class itself. This
    approach ensures that the Catalogue class works independently of the actual search logic, which is defined in
    separate strategy classes. The execute_search method in Catalogue simply calls the search method on whichever
    strategy is currently set, allowing for versatile and interchangeable search behaviors at any point during the
    application's operation.
    """

    def __init__(self):
        self.db_manager = DBManager()
        # No default strategy
        self.search_strategy = None

    def set_search_strategy(self, strategy):
        """
        Method for setting the search strategy attribute
        """
        self.search_strategy = strategy

    def execute_search(self, term):
        """
        Executes a search using the current search strategy.

        This method relies on a search strategy being set beforehand; if no strategy is set, it raises an exception.
        The search is performed by calling the search method of the strategy with the provided search term.

        Parameters:
        - term (str): The search term to be used by the strategy for finding books.

        Returns:
        - A list of books that match the search criteria of the current strategy.

        Raises:
        - Exception: If no search strategy has been set prior to calling this method.
        """
        if not self.search_strategy:
            raise Exception("No search strategy set")
        return self.search_strategy.search(term)
    
    # Adds or updates book with title and author
    def insert_book(self, title, author, isbn):
        self.db_manager.insert_book(title, author, isbn)
        
    def insert_book_item(self, book_id):
        self.db_manager.insert_book_item(book_id)

    def get_book(self, book_id):
        return self.db_manager.get_book_by_id(book_id)

    def get_book_items(self, book_id):
         return self.db_manager.get_book_items_by_book_id(book_id)
        
    
    def remove_book(self, book_id):
        pass
   

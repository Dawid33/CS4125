from abc import ABC, abstractmethod
from models.database_manager.db_manager import DBManager


# Contains the Strategy Pattern implementation

class BookSearchStrategy(ABC):
    """ABSTRACT CLASS: ~ Defined interface for all concrete search strategies.
    Each concrete strategy class will inherit from this and implement the 'search'
    method, providing the specific behavior for searching books based on different criteria."""

    @abstractmethod
    def search(self, term):
        # An abstract method that must be overridden by concrete strategy implementations.
        pass


class SearchByTitleStrategy(BookSearchStrategy):
    """Implements the search method in BookSearchStrategy to search by title"""

    def search(self, term):
        db_manager = DBManager()
        return db_manager.search_by_title(term)


class SearchByAuthorStrategy(BookSearchStrategy):
    """Implements the search method in BookSearchStrategy to search by author"""

    def search(self, term):
        db_manager = DBManager()
        return db_manager.search_by_author(term)


class SearchByISBNStrategy(BookSearchStrategy):
    """Implements the search method in BookSearchStrategy to search by isbn"""

    def search(self, term):
        db_manager = DBManager()
        return db_manager.search_by_isbn(term)
    
    
# class SearchAllBooksStrategy(BookSearchStrategy):
#     def search(self, term=None):
#         """
#         Retrieve all books from the database.

#         This strategy ignores the 'term' parameter and returns all book entries.
#         It's used as the default search strategy when no specific criteria are provided.

#         Returns:
#             List of all Book objects in the database.
#         """
#         db_manager = DBManager()
#         return db_manager.get_default_catalog()

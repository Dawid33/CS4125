from src.catalogue.book_search import BookSearch
from src.db_manager import DBManager

class Catalogue(BookSearch):
    def __init__(self):
        self.db_manager = DBManager()
        
    def search_by_title(self, title):
        # Implement search by title using the database manager
        pass

    def search_by_author(self, author):
        # Implement search by author using the database manager
        pass

    def search_by_genre(self, genre):
        # Implement search by genre using the database manager
        pass

    def search_by_year(self, year):
        # Implement search by year using the database manager
        pass
    
    def update_book(self, title, author):
        self.db_manager.insert_book(title, author)
    
    def remove_book(self, Book):
        pass
    
    
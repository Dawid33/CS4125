from models.catalogue.book_search import BookSearch
from models.database_manager.db_manager import DBManager

class Catalogue(BookSearch):
    def __init__(self):
        self.db_manager = DBManager()
            
    # Filters books by either title, author or isbn
    def filter_books(self, title, author, isbn):
        return self.db_manager.filter_books(title, author, isbn)
    
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
    
    def search_by_title(self, title):
        # Implement search by title using the database manager
        pass

    def search_by_author(self, author):
        # Implement search by author using the database manager
        pass

    def search_by_isbn(self, genre):
        # Implement search by isbn using the database manager
        pass
    
    

from models.database_manager.db_manager import DBManager

class LendingManager:
    def __init__(self, library_member=None):
        self.db_manager = DBManager()
        # self.user = library_member
        
    def get_borrowed_books(self):
        pass
    
    def borrow_book(self, book_item):
        pass
    
    def return_book(self, book_item):
        pass
    
    def calculate_fine(self):
        pass
    
    def can_borrow_book(self):
        pass
    
    def is_book_available(self):
        pass
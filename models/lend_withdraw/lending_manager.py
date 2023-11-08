from models.database_manager.db_manager import DBManager

class LendingManager:
    def __init__(self, library_member=None):
        self.db_manager = DBManager()
        
    def get_borrowed_books(self, user_id):
        return self.db_manager.get_borrowed_books(user_id)
    
    def borrow_book(self, user, book_item) -> bool:
        # TODO: Check if user is eligible to borrow book before actually borrowing it.
        return self.db_manager.insert_borrowed_book(user.user_id, book_item)
    
    def return_book(self, borrow_id):
        self.db_manager.return_book(borrow_id)
    
    def calculate_fine(self):
        pass
    
    def can_borrow_book(self):
        pass
    
    def is_book_available(self):
        pass

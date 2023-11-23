# pylint: disable=too-few-public-methods
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from models.database_manager.db_manager import DBManager

class LendingManager:
    def __init__(self):
        self.db_manager = DBManager()
        
    def get_borrowed_books(self, user_id):
        return self.db_manager.get_borrowed_books(user_id)
    
    def borrow_book(self, user_id, book_item, borrow_date, due_date) -> bool:
        return self.db_manager.insert_borrowed_book(user_id, book_item, borrow_date, due_date)
    
    def return_book(self, borrow_id):
        self.db_manager.return_book(borrow_id)
    
    def get_fines(self, user_id):
        return self.db_manager.get_fines(user_id)
    
    def set_balance(self, user_id, balance):
        self.db_manager.set_balance(user_id, balance)
    
    def calculate_total_fine(self, user_id):
        fines = self.get_fines(user_id)
        total = 0
        
        if(len(fines)):
            for fine in fines:
                total += fine.fine_amount
        
        return total
    
    def pay_fine(self, fine_id, new_balance):
        self.db_manager.pay_fine(fine_id, new_balance)
        
    def is_book_limit_reached(self, current_user):
        if len(current_user.get_borrowed_books()) >= current_user.get_book_limit():
            return True
        else:
            return False
    
    def is_book_already_borrowed(self, current_user, book_id):
        for borrowed_book in current_user.get_borrowed_books():
            if str(borrowed_book[0].book_id) == str(book_id):
                    return True
                
        return False
    
    def is_book_copy_available(self, book_id):
        books = self.db_manager.get_book_items_by_book_id(book_id)
        available = 0
        for book_item in books:
            if not book_item.is_borrowed:
                available += 1
                
        return available

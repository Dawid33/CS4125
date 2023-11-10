from models.database_manager.db_manager import DBManager

class LendingManager:
    def __init__(self):
        self.db_manager = DBManager()
        
    def get_borrowed_books(self, user_id):
        return self.db_manager.get_borrowed_books(user_id)
    
    def borrow_book(self, user, book_item) -> bool:
        # TODO: Check if user is eligible to borrow book before actually borrowing it.
        return self.db_manager.insert_borrowed_book(user.user_id, book_item)
    
    def return_book(self, borrow_id):
        self.db_manager.return_book(borrow_id)
    
    def get_user_fines(self, user_id):
        return self.db_manager.get_user_fines(user_id)
    
    def calculate_total_fine(self, user_id):
        fines = self.get_user_fines(user_id)
        total = 0
        
        if(len(fines)):
            for fine in fines:
                total += fine.fine_amount
        
        return total
    
    def pay_fine(self, fine_id, new_balance):
        self.db_manager.pay_fine(fine_id, new_balance)
        
    def can_borrow_book(self):
        pass
    
    def is_book_available(self):
        pass

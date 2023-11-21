from abc import ABC, abstractmethod
from datetime import timedelta
from models.users.user import User
from models.lend_withdraw.lending_manager import LendingManager

# Abstract class that extends the user class, defines the main functionality for library members
class LibraryMember(User, ABC):
    def __init__(self, user_id, username, email, password, balance):
        super().__init__(user_id, username, email, password, balance)
        
        self.lending_manager = LendingManager()
        self.fine_amount =self.lending_manager.calculate_total_fine(self.user_id)
        self.fines = self.lending_manager.get_fines(self.user_id)
    
    # Gets all borrowed books by library member    
    def get_borrowed_books(self):
        return self.lending_manager.get_borrowed_books(self.user_id)
    
    # Returns selected book back to the library  
    def return_book(self, borrow_id):
        self.lending_manager.return_book(borrow_id)

    # Gets the total amount the user is fined            
    def get_fine_amount(self):
        return self.fine_amount
    
    # Gets all fines that the user owes
    def get_fines(self):
        return self.fines
        
    # Gets user balance
    def get_balance(self):
        return self.balance

    # Sets new user balance
    def set_balance(self, new_balance):
        self.lending_manager.set_balance(self.user_id, self.get_balance() + new_balance)

    def pay_fine(self, fine_id):
        # Find the fine that corresponds to the fine id
        fine = None
        for fine_obj in self.get_fines():
            if fine_obj.fine_id == str(fine_id):
                fine = fine_obj
                break

        # Check if fine amount exceeds balance
        if(self.get_balance() >= fine.fine_amount):
            new_balance = self.get_balance() - fine.fine_amount
            self.lending_manager.pay_fine(fine_id, new_balance)
            return True
        else:
            return False

    @abstractmethod
    def borrow_book(self, book_item, borrow_date):
        pass

# Student class that extends library member, defines the book limit, student user type and
# functionality for borrowing books      
class Student(LibraryMember):
    def __init__(self, user_id, username, email, password, balance, user_type="Student"):
        super().__init__(user_id, username, email, password, balance)
        
        self.user_type = user_type
        self.book_limit = 5  # Define the book limit for students.

    # Gets type for this user
    def get_user_type(self):
        return self.user_type

    # Gets the book limit for this user
    def get_book_limit(self):
        return self.book_limit
    
    def borrow_book(self, book_item, borrow_date):
        # For students the due date is always a week after borrow date
        due_date = borrow_date + timedelta(days=7)
               
        # Convert dates to strings with day, month, and year
        borrow_date_str = borrow_date.strftime('%d-%m-%Y')
        due_date_str = due_date.strftime('%d-%m-%Y')
        
        return self.lending_manager.borrow_book(self.user_id, book_item, borrow_date_str, due_date_str)
    
# Faculty class that extends library member, defines the book limit, faculty user type and
# functionality for borrowing books
class Faculty(LibraryMember):
    def __init__(self, user_id, username, email, password, balance, user_type="Faculty"):
        super().__init__(user_id, username, email, password, balance)
        
        self.user_type = user_type
        self.book_limit = 10  # Define the book limit for faculty members.

    # Gets type for this user
    def get_user_type(self):
        return self.user_type

    # Gets the book limit for this user
    def get_book_limit(self):
        return self.book_limit
    
    def borrow_book(self, book_item, borrow_date):
        # For Faculty the due date is always 2 weeks after borrow date
        due_date = borrow_date + timedelta(days=14)
               
        # Convert dates to strings with day, month, and year
        borrow_date_str = borrow_date.strftime('%d-%m-%Y')
        due_date_str = due_date.strftime('%d-%m-%Y')
        
        return self.lending_manager.borrow_book(self.user_id, book_item, borrow_date_str, due_date_str)

    def change_state(self, state):
        self.state = state



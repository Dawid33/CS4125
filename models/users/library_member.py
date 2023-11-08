from abc import ABC, abstractmethod
from models.users.user import User
from models.lend_withdraw.lending_manager import LendingManager

# Abstract class that extends the user class, defines the main functionality for library members
class LibraryMember(User, ABC):
    def __init__(self, user_id, username, email, password, fine_amount=0):
        super().__init__(user_id, username, email, password)
        self.fine_amount = fine_amount
        self.lending_manager = LendingManager()
        
    def set_fine_amount(self, amount):
        pass
            
    def get_fine_amount(self):
        return self.fine_amount

    def pay_fine(self, fine_id):
        pass
  
    def get_borrowed_books(self):
        return self.lending_manager.get_borrowed_books(self.user_id)
    
    def return_book(self, borrow_id):
        self.lending_manager.return_book(borrow_id)

    @abstractmethod
    def borrow_book(self, book_item):
        pass

# Student class that extends library member, defines the book limit, student user type and
# functionality for borrowing books      
class Student(LibraryMember):
    def __init__(self, user_id, username, email, password, user_type="Student"):
        super().__init__(user_id, username, email, password)
        self.user_type = user_type
        self.book_limit = 5  # Define the book limit for students.

    def get_user_type(self):
        return self.user_type

    def get_book_limit(self):
        return self.book_limit
    
    def borrow_book(self, book_item):
        pass
    
# Faculty class that extends library member, defines the book limit, faculty user type and
# functionality for borrowing books
class Faculty(LibraryMember):
    def __init__(self, user_id, username, email, password, user_type="Faculty"):
        super().__init__(user_id, username, email, password)
        self.user_type = user_type
        self.book_limit = 10  # Define the book limit for faculty members.

    def get_user_type(self):
        return self.user_type

    def get_book_limit(self):
        return self.book_limit
    
    def borrow_book(self, book_item):
        pass



from abc import ABC, abstractmethod
from enum import Enum
from src.users.user import User

# Abstract class that extends the user class, defines the main functionality for library members
class LibraryMember(User, ABC):
    def __init__(self, Id, username, email, password, lending_manager=0, fine_amount=0):
        super().__init__(Id, username, email, password)
        self.fine_amount = fine_amount
        self.lending_manager = lending_manager
        
    def set_fine_amount(self, amount):
        self.fine_amount = amount
        
    def get_fine_amount(self):
        return self.fine_amount

    def pay_fine(self, fine_id):
        pass
  
    def get_borrowed_books(self):
        pass
    
    def return_book(self, book):
        pass

    @abstractmethod
    def borrow_book(self, book_title):
        pass

# Student class that extends library member, defines the book limit, student user type and
# functionality for borrowing books      
class Student(LibraryMember):
    def __init__(self, Id, username, email, password, user_type="Student"):
        super().__init__(Id, username, email, password)
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
    def __init__(self, Id, username, email, password, user_type="Faculty"):
        super().__init__(Id, username, email, password)
        self.user_type = user_type
        self.book_limit = 10  # Define the book limit for faculty members.

    def get_book_limit(self):
        return self.book_limit
    
    def borrow_book(self, book_item):
        pass
    
# Define an enum for user roles.
class UserRoles(Enum):
    STUDENT = Student
    FACULTY = Faculty



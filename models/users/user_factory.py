from models.users.library_member import *
from models.users.admin import Admin
    
class UserFactory:
    @staticmethod
    def create_user(Id, username, email, password, user_type):
        if user_type == "STUDENT":
            return Student(Id, username, email, password)
        elif user_type == "FACULTY":
            return Faculty(Id, username, email, password)
        elif user_type == "ADMIN":
            return Admin(Id, username, email, password)
        else:
            raise ValueError("Invalid user type")
    

    
    
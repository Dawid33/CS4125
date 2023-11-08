from models.users.library_member import *
from models.users.admin import Admin
    
class UserFactory:
    @staticmethod
    def create_user(user_id, username, email, password, user_type):
        if user_type == "STUDENT":
            return Student(user_id, username, email, password)
        elif user_type == "FACULTY":
            return Faculty(user_id, username, email, password)
        elif user_type == "ADMIN":
            return Admin(user_id, username, email, password)
        else:
            raise ValueError("Invalid user type")
    

    
    
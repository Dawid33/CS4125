# pylint: disable=too-few-public-methods
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from models.users.library_member import *
from models.users.admin import Admin
    
# Class that creates a user factory that decides which user type to create
class UserFactory:
    @staticmethod
    def create_user(user_id, username, email, password, user_type, balance=0,):
        if user_type == "STUDENT":
            return Student(user_id, username, email, password, balance)
        elif user_type == "FACULTY":
            return Faculty(user_id, username, email, password, balance)
        elif user_type == "ADMIN":
            return Admin(user_id, username, email, password)
        else:
            raise ValueError("Invalid user type")
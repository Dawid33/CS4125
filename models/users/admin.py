# pylint: disable=too-few-public-methods
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from models.users.user import User
from instance.db import *
from models.users.admin_command import *

# Admin user type controls the book catalogue, and can also block/unblock users and waive user fines
# Extends the User class
class Admin(User):
    def __init__(self, user_id, username, email, password):
        super().__init__(user_id=user_id, username=username, email=email, password=password)

        self.admin_commands = []
        self.user_type = 'ADMIN'

    def add_admin_command(self, command):
        self.admin_commands.append(command)
    
    def execute_admin_commands(self):
        for command in self.admin_commands:
            command.execute()

    def get_user_type(self):
        return self.user_type
    
    # def block_library_member(self, user_id):
    #     user_to_block = self.db_manager.get_user_by_id(user_id)
        
    #     if not user_to_block:
    #         return "User cannot be blocked"
        
    #     self.db_manager.block_user(user_id)
    
    # def unblock_library_member(self, user_id):
    #     user_to_unblock = self.db_manager.get_user_by_id(user_id)

    #     if not user_to_unblock:
    #         return "User cannot be unblocked"
        
    #     self.db_manager.unblock_user(user_id)
    
    # # Function for waving a specific user fine
    # def waive_fine(self, fine_id):
    #     self.db_manager.waive_user_fine(fine_id)

    # def insert_book(self, title, author):
    #     self.catalogue_manager.insert_book(title, author)

    # def insert_book_item(self, book_id):
    #     self.catalogue_manager.insert_book_item(book_id)

    # def remove_book(self, book_id):
    #     self.catalogue_manager.remove_book(book_id)

        





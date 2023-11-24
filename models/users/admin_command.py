# pylint: disable=too-few-public-methods
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from models.catalogue.catalogue_manager import Catalogue
from models.database_manager.db_manager import DBManager
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class AddBook(Command):
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.catalogue_manager = Catalogue()

    def execute(self):
        self.catalogue_manager.insert_book(self.title, self.author, self.isbn)

class AddBookItem(Command):
    def __init__(self, book_id):
        self.book_id = book_id
        self.catalogue_manager = Catalogue()

    def execute(self):
        self.catalogue_manager.insert_book_item(self.book_id)
    
class RemoveBook(Command):
    def __init__(self, book_id):
        self.book_id = book_id
        self.catalogue_manager = Catalogue()

    def execute(self):
        self.catalogue_manager.remove_book(self.book_id)

class WaiveFine(Command):
    def __init__(self, username):
        self.username = username
        self.db_manager = DBManager()

    def execute(self):
        user = self.db_manager.get_user_by_username(self.username)
        self.db_manager.waive_user_fine(user.user_id)

class BlockUser(Command):
    def __init__(self, user_name):
        self.user_name = user_name
        self.db_manager = DBManager()

    def execute(self):
        user = self.db_manager.get_user_by_username(self.user_name)
        self.db_manager.block_user(user.user_id)

class UnblockUser(Command):
    def __init__(self, user_name):
        self.user_name = user_name
        self.db_manager = DBManager()

    def execute(self):
        user = self.db_manager.get_user_by_username(self.user_name)
        self.db_manager.unblock_user(user.user_id)
    
from models.catalogue.catalogue_manager import Catalogue
from models.database_manager.db_manager import DBManager
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class AddBook(Command):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.catalogue_manager = Catalogue()

    def execute(self):
        self.catalogue_manager.insert_book(self.title, self.author)

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
    def __init__(self, fine_id):
        self.fine_id = fine_id
        self.db_manager = DBManager()

    def execute(self):
        self.db_manager.waive_user_fine(self.fine_id)

class BlockUser(Command):
    def __init__(self, user_id):
        self.user_id = user_id
        self.db_manager = DBManager()

    def execute(self):
        self.db_manager.block_user

class UnblockUser(Command):
    def __init__(self, user_id):
        self.user_id = user_id
        self.db_manager = DBManager()

    def execute(self):
        self.db_manager.unblock_user
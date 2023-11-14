from models.users.user import User
from models.catalogue.catalogue_manager import Catalogue
from models.database_manager.db_manager import DBManager

# Admin user type controls the book catalogue, and can also block/unblock users and waive user fines
# Extends the User class
class Admin(User):
    def __init__(self, user_id, username, email, password):
        super().__init__(user_id, username, email, password)

        self.catalogue_manager = Catalogue()
        self.db_manager = DBManager()
        self.user_type = 'ADMIN'

    def get_user_type(self):
        return self.user_type
    
    def block_library_member(self, user):
        block = DBManager.block_user(self, user)
        return
    
    
    def unblock_library_member(self, user):
        pass
    
    def waive_fine(self, user, fine_id):
        pass


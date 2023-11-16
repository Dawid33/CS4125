from models.users.user import User
from models.catalogue.catalogue_manager import Catalogue
from models.database_manager.db_manager import DBManager
from instance.db import *

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
    
    # Function for waving a specific user fine
    def waive_fine(self, user_id, fine_id):
        fine_to_waive = Fine.query.filter_by(user_id=user_id, fine_id=fine_id).first()

        if not fine_to_waive:
            return "No Fine To Waive"
        
        db.session.delete(fine_to_waive)

        db.session.commit()

        return "Fine Waived Successfully"





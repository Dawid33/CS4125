from models.users.user import User

# Admin user type controls the book catalogue, and can also block/unblock users and waive user fines
# Extends the User class
class Admin(User):
    def __init__(self, Id, username, email, password, catalogue_manager):
        super().__init__(Id, username, email, password)
        # self.catalogue_manager = catalogue_manager
    
    def block_library_member(self, user):
        pass
    
    def unblock_library_member(self, user):
        pass
    
    def waive_fine(self, user, fine_id):
        pass


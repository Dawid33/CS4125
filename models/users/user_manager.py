from flask import session
from models.database_manager.db_manager import DBManager
from models.users.user_factory import UserFactory

class UserManager():
    def __init__(self):
       self.user_factory = UserFactory()
       self.db_manager = DBManager()
       
    def get_current_user(self):
        db_user = self.db_manager.get_user_by_id(session['user'])
        return self.user_factory.create_user(db_user.user_id, db_user.username, db_user.email, db_user.password, db_user.user_type)
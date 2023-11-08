from models.users.user_factory import UserFactory

class UserController():
    def __init__(self):
       self.user_factory = UserFactory()
       
    def create_user(self, user_id, username, email, password, user_type):
        return self.user_factory.create_user(user_id, username, email, password, user_type)
from abc import ABC

class User(ABC):
    def __init__(self, user_id, username, email, password, balance=0):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.balance = balance

    def __str__(self):
        return f"User Details( Id: {self.user_id}, Username: {self.username}, Email: {self.email} )"

from flask_json import FlaskJSON
json = FlaskJSON()

class User():
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
    
    def logout():
        pass
    
    def notify_overdue_book(self, book):
        pass
    
    def notify_book_available(self, book):
        pass
    
    def __str__(self):
        return f"User Details( Id: {self.user_id}, Username: {self.username}, Email: {self.email} )"

    @json.encoder
    def encoder(o):
        if isinstance(o, User):
            return "user" 

    

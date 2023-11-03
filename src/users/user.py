from uuid import uuid4

class User():
    def __init__(self, Id, username, email, password):
        self.Id = Id
        self.username = username
        self.email = email
        self.password = password
        self.session_token = None
        self.logged_in = False
        
    def generate_session_token(self):
        # Generate a unique session token using UUID
        self.session_token = str(uuid4())
    
    def get_session_token(self):
        return self.session_token
    
    def login():
        pass
    
    def logout():
        pass
    
    def notify_overdue_book(self, book):
        pass
    
    def notify_book_available(self, book):
        pass
    
    def __str__(self):
        return f"User Details( Id: {self.Id}, Username: {self.username}, Email: {self.email} )"
    

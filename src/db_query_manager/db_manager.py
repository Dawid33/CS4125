from flask_sqlalchemy import SQLAlchemy
from model.db import *
from model.db import db
import uuid

class DBManager:
    # Function to add a user to db
    def create_user(self, username, email, password, user_type):
        student_id = str(uuid.uuid1())

        # Create a new user
        student_user = User(user_id=student_id, username=username, email=email, password=password, is_admin=0, user_type_id=user_type, is_blocked=0)
        
        db.session.add(student_user)
        db.session.commit()
        
    def get_user_by_id(self, user_id):
        # Query the database to get a user by their user_id
        user = User.query.filter_by(user_id=user_id).first()
        return user

    def get_user_by_username(self, username):
        # Query the database to get a user by their username
        user = User.query.filter_by(username=username).first()
        return user
    
    def get_user_by_email(self, email):
        # Query the database to get a user by their email
        user = User.query.filter_by(email=email).first()
        return user
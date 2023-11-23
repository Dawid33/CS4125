# pylint: disable=too-few-public-methods
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from models.database_manager.db_manager import DBManager
from flask import flash, session

class Authentication():
    def __init__(self):
        self.db_manager = DBManager()
    
    # Function that authenticates user login based on username and password
    # Creates a session with user id if user logs in successfully
    def authenticate_login(self, username, password):
        user = self.db_manager.get_user_by_username(username)
        if user:
            if user.password == password:
                if user.is_blocked:
                    flash('This account has been blocked')
                else:    
                    session['user'] = user.user_id
                    return True
            else:
                flash('Login failed. Password is incorrect')
        else:
            flash('Login failed, Username is incorrect')
        
        return False
    
    # Function that authenticates user registration and creates a new user in db if successful
    def authenticate_registration(self, username, email, password, user_type):
        existing_user = self.db_manager.get_user_by_username(username)
        
        if existing_user:
            flash('Username is already in use. Please choose a different one.')
        else:
            existing_email = self.db_manager.get_user_by_email(email)
            if existing_email:
                flash('Email is already registered. Please use a different email.')
            else:
                self.db_manager.create_user(username, email, password, user_type)
                flash('Registration successful! You can now log in')
                return True
            
        return False
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from models.db import *
from models.db import db
import uuid

class DBManager:
    # Function to add a user to db
    def create_user(self, username, email, password, user_type):
        student_id = str(uuid.uuid1())

        # Create a new user
        student_user = User(user_id=student_id, username=username, email=email, password=password, is_admin=0, user_type=user_type, is_blocked=0)
        
        db.session.add(student_user)
        db.session.commit()

    # Query the database to get a user by their user_id        
    def get_user_by_id(self, user_id):
        user = User.query.filter_by(user_id=user_id).first()
        return user

    # Query the database to get a user by their username
    def get_user_by_username(self, username):
        user = User.query.filter_by(username=username).first()
        return user

    # Query the database to get a user by their email    
    def get_user_by_email(self, email):
        user = User.query.filter_by(email=email).first()
        return user

    # Query the database to get a book by its' id    
    def get_book_by_id(self, book_id):
        book = Book.query.filter_by(book_id=str(book_id)).first()
        return book

    # Function to add book to database
    def insert_book(self, title, author):
        book = Book (
            book_id = str(uuid.uuid4()),
            isbn = 'lol',
            title = title,
            author = author,
            publisher = 'lol',
            num_of_pages = 'lol',
            pub_date = 'your mom'
        )
        db.session.add(book)
        db.session.commit()

    def get_default_catalog(self):
        return db.session.execute(select(Book)).all()

    def search_by_title(self, title):
        search = "%{}%".format(title)
        books = Book.query.filter(Book.title.like(search)).all()
        return books

# pylint: disable=too-few-public-methods

"""
Library Management System Database Models

Defines SQLAlchemy models for a Library Management System database.

Attributes:
- db: SQLAlchemy instance for database operations.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    """
    Represents a book in the library.
    """
    book_id = db.Column(db.String, primary_key=True)
    isbn = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    publisher = db.Column(db.String)
    num_of_pages = db.Column(db.String)
    pub_date = db.Column(db.String)

class BookItem(db.Model):
    """
    Represents an individual copy or item of a book in the library.
    """
    book_item_id = db.Column(db.String, primary_key=True)
    book_id = db.Column(db.String, db.ForeignKey('book.book_id'), nullable=False)
    is_borrowed = db.Column(db.Boolean, default=False)

class User(db.Model):
    """
    Represents a user of the library.
    """
    user_id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    user_type = db.Column(db.String, nullable=False)
    is_blocked = db.Column(db.Boolean)
    balance = db.Column(db.Float, default=0)

class BorrowedBook(db.Model):
    """
    Represents a record of a book being borrowed from the library.
    """
    borrow_id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'), nullable=False)
    book_item_id = db.Column(db.String, db.ForeignKey('book_item.book_item_id'), nullable=False)
    borrow_date = db.Column(db.String, nullable=False)
    due_date = db.Column(db.String)

class Fine(db.Model):
    """
    Represents a fine imposed on a user for overdue books.
    """
    fine_id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'), nullable=False)
    fine_amount = db.Column(db.Float, default=0)
    description = db.Column(db.String)

class Reservation(db.Model):
    """
    Represents a reservation made by a user for a specific book.
    """
    reservation_id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'), nullable=False)
    book_id = db.Column(db.String, db.ForeignKey('book.book_id'), nullable=False)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    book_id = db.Column(db.String, primary_key=True)
    isbn = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    publisher = db.Column(db.String)
    num_of_pages = db.Column(db.String)
    pub_date = db.Column(db.String)

class BookItem(db.Model):
    book_item_id = db.Column(db.String, primary_key=True)
    book_id = db.Column(db.String, db.ForeignKey('book.book_id'), nullable=False)
    is_borrowed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.String)

class User(db.Model):
    user_id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    user_type = db.Column(db.String, nullable=False)
    is_blocked = db.Column(db.Boolean)
    balance = db.Column(db.Float, default=0)

class BorrowedBook(db.Model):
    borrow_id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'), nullable=False)
    book_item_id = db.Column(db.String, db.ForeignKey('book_item.book_item_id'), nullable=False)
    borrow_date = db.Column(db.String, nullable=False)
    return_date = db.Column(db.String)

class Fine(db.Model):
    fine_id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'), nullable=False)
    fine_amount = db.Column(db.Float, default=0)
    description = db.Column(db.String)

class Reservation(db.Model):
    reservation_id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'), nullable=False)
    book_id = db.Column(db.String, db.ForeignKey('book.book_id'), nullable=False)

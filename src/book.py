from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.database_manager.db_manager import DBManager

book = Blueprint('book', __name__)

db_manager = DBManager()

@book.route('/book/<uuid:book_id>', methods=['GET'])
def register(book_id):
     book = db_manager.get_book_by_id(book_id)
     if book is None: 
          return render_template("book/book_not_found.html")
     return render_template("book/book.html", title=book.title, author=book.author)
     



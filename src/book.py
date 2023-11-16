from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.database_manager.db_manager import DBManager
from models.lend_withdraw.lending_manager import LendingManager
from models.users.user_manager import UserManager
from datetime import datetime, timedelta

book = Blueprint('book', __name__)

user_manager = UserManager()
db_manager = DBManager()
lending_manager = LendingManager()

@book.route('/book/<uuid:book_id>', methods=['GET'])
def book_details(book_id):
     current_user = user_manager.get_current_user()
     book = db_manager.get_book_by_id(book_id)
     if book is None: 
          return render_template("book/book_not_found.html")

     books = db_manager.get_book_items_by_book_id(book_id)
     available = 0
     for book_item in books:
          if not book_item.is_borrowed:
               available += 1
     
     book_limit_reached = False
     already_borrowed = False
     if len(current_user.get_borrowed_books()) >= current_user.get_book_limit():
          book_limit_reached = True
     else:  
          for borrowed_book in current_user.get_borrowed_books():
               if str(borrowed_book[0].book_id) == str(book_id):
                    already_borrowed = True
                    break
     
     return render_template("book/book.html", title=book.title, author=book.author, available_copies=available, total_copies=len(books), book_id=book_id, already_borrowed=already_borrowed, book_limit_reached=book_limit_reached, book_limit=current_user.get_book_limit())

@book.route('/book/<uuid:book_id>/borrow', methods=['GET'])
def borrow(book_id):
     result = {
          "success": False
     }

     books = db_manager.get_book_items_by_book_id(book_id)
     user = user_manager.get_current_user()
     for book_item in books:
          if not book_item.is_borrowed:
               # Get the current date
               borrow_date = datetime.now()

               # Calculate the date one week from now
               due_date = borrow_date + timedelta(days=7)
               
               # Convert dates to strings with day, month, and year
               borrow_date_str = borrow_date.strftime('%d-%m-%Y')
               due_date_str = due_date.strftime('%d-%m-%Y')

               if lending_manager.borrow_book(user, book_item, borrow_date_str, due_date_str):
                    print("OKAY")
                    result["success"] = True
                    break
     
     return result

     

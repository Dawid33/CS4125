# pylint: disable=too-few-public-methods
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from flask import Blueprint, render_template
from models.database_manager.db_manager import DBManager
from models.lend_withdraw.lending_manager import LendingManager
from models.users.user_manager import UserManager
from models.notifications.notification_manager import NotificationManager
from models.catalogue.catalogue_manager import Catalogue
from datetime import datetime

book = Blueprint('book', __name__)

user_manager = UserManager()
catalogue_manager = Catalogue()
db_manager = DBManager()
lending_manager = LendingManager()
notification_manager = NotificationManager()

@book.route('/book/<uuid:book_id>', methods=['GET'])
def book_details(book_id):
     current_user = user_manager.get_current_user()
     book = catalogue_manager.get_book(book_id)
     if book is None: 
          return render_template("book/book_not_found.html")
     
     books = catalogue_manager.get_book_items(book_id)
     available = lending_manager.is_book_copy_available(book_id)
     book_limit_reached = lending_manager.is_book_limit_reached(current_user)
     already_borrowed = lending_manager.is_book_already_borrowed(current_user, book_id)

     
     return render_template("book/book.html", title=book.title, author=book.author, available_copies=available, total_copies=len(books), book_id=book_id, already_borrowed=already_borrowed, book_limit_reached=book_limit_reached, book_limit=current_user.get_book_limit())

@book.route('/book/<uuid:book_id>/borrow', methods=['GET'])
def borrow(book_id):
     result = {
          "success": False
     }

     books = catalogue_manager.get_book_items(book_id)
     book = catalogue_manager.get_book(book_id)
     user = user_manager.get_current_user()
     for book_item in books:
          if not book_item.is_borrowed:
               # Get the current date
               borrow_date = datetime.now()

               if user.borrow_book(book_item, borrow_date):
                    print("OKAY")
                    result["success"] = True
                    notification_manager.send_book_borrow_confirmation(user.email, book.title)
                    break
     
     return result


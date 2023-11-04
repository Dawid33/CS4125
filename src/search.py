from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.db_manager import DBManager

search = Blueprint('search', __name__)

db_manager = DBManager()

@search.route('/search', methods=['GET'])
def register():
     results = ""

     if request.args.get("title") is not None:
          title = request.args["title"].replace("\"", '')
          print(title)
          books = db_manager.search_by_title(title)
          for book in books:
               results += render_template("search/book_card.html", title=book.title, author=book.author)

     return render_template("search/search.html", results=results)



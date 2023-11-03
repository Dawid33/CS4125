from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.db_manager import DBManager

search = Blueprint('search', __name__)

@search.route('/search', methods=['GET', 'POST'])
def register():
     return render_template("search/search.html")



from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.users.library_member import *
from src.db_manager import DBManager

profile = Blueprint('profile', __name__)

# API call that communicates with the database to register a user
@profile.route('/profile', methods=['GET', 'POST'])
def user_profile():
    return render_template('user_profile/user_profile.html')



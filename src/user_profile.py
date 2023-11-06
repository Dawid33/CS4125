from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.users.library_member import *
from src.authentication import db_manager

profile = Blueprint('profile', __name__)


@profile.route('/profile', methods=['GET', 'POST'])
def user_profile():
    current_user = db_manager.get_user_by_id(session["user_id"])
    return render_template('user_profile/user_profile.html', user=current_user)



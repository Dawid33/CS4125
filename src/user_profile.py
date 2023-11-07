from flask import Blueprint, redirect, render_template, session, url_for
from models.users.library_member import *
from models.users.admin import *
from models.database_manager.db_manager import DBManager

profile = Blueprint('profile', __name__)
admin_profile = Blueprint('admin_profile', __name__)

db_manager = DBManager()


@profile.route('/profile', methods=['GET', 'POST'])
def user_profile():
    if 'user_id' in session:
        # current_user = db_manager.get_user_by_id(session["user_id"])
        current_user = session['user_id']
        return render_template('user_profile/user_profile.html', user=current_user)
    else:
        return redirect(url_for('authentication.login'))
    


@profile.route('/admin_profile', methods=['GET', 'POST'])
def is_admin_profile():
    current_user = db_manager.get_user_by_id(session["user_id"])
    admin = db_manager.get_admin_id(session["is_admin"])
    if admin == 1:
        return render_template('user_profile/admin_profile.html', user=current_user)
    else:
        return render_template('user_profile/admin_profile.html', user=current_user)


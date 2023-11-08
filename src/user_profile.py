from flask import Blueprint, redirect, render_template, session, url_for
from models.users.user_manager import UserManager

user_manager = UserManager()

profile = Blueprint('profile', __name__)

@profile.route('/profile', methods=['GET', 'POST'])
def user_profile():
    if 'user' not in session:
        return redirect(url_for('authentication.login'))
    
    current_user = user_manager.get_current_user()
    
    if current_user.get_user_type() == "ADMIN":
        return redirect(url_for('profile.admin_profile'))
    else:      
        return render_template('user_profile/user_profile.html', user=current_user)

@profile.route('/admin_profile', methods=['GET', 'POST'])
def admin_profile():
    current_user = user_manager.get_current_user()
    return render_template('user_profile/admin_profile.html', user=current_user)

@profile.route('/fines', methods=['GET', 'POST'])
def fines():
    current_user = user_manager.get_current_user()
    return render_template('user_profile/fines.html', user=current_user)

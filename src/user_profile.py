# pylint: disable=too-few-public-methods
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from flask import Blueprint, jsonify, redirect, render_template, request, session, url_for, abort
from models.users.user_manager import UserManager
from src.forms import *
from models.users.admin_command import *
from models.notifications.notification import EmailDecorator, Notification
from models.notifications.notification_manager import NotificationManager

user_manager = UserManager()
notification_manager = NotificationManager()

profile = Blueprint('profile', __name__)

# API endpoint that loads the initial user profile page and passes in a user object
@profile.route('/profile', methods=['GET'])
def user_profile():
    if 'user' not in session:
        return redirect(url_for('authentication.login'))
    
    current_user = user_manager.get_current_user()
    
    if current_user.get_user_type() == "ADMIN":
        return redirect(url_for('profile.admin_profile'))
    else:
        return render_template('user_profile/user_profile.html', user=current_user)

# API endpoint that loads the admin profile page
@profile.route('/admin_profile', methods=['GET', 'POST'])
def admin_profile():
    admin_user = user_manager.get_current_user()
    form = AddBookForm()  # Create an instance of the form
    waive_fine_form = WaiveFineForm()
    block_user_form = BlockUserForm()
    remove_book_form = RemoveBookForm()
    unblock_user_form = UnblockUserForm()

    # Pass the form to the template
    return render_template('user_profile/admin_profile.html', user=admin_user, form=form, waive_fine_form=waive_fine_form, 
                            block_user_form=block_user_form, remove_book_form=remove_book_form, unblock_user_form=unblock_user_form)

# API endpoint that triggeres return book on the user object
@profile.route('/return_book/<uuid:borrow_id>', methods=['GET'])
def return_book(borrow_id):
    current_user = user_manager.get_current_user()
    current_user.return_book(borrow_id)

    notification_manager.send_book_return_confirmation(current_user.email, "DEFAULT")
    return redirect(url_for('profile.user_profile'))

# API endpoint that triggers the top up fuctionality
@profile.route('/add_to_balance', methods=['GET', 'POST'])
def add_to_balance():
    current_user = user_manager.get_current_user()
    if request.method == 'POST':
        amount = request.form.get('amount')
        current_user.set_balance(float(amount))
        return redirect(url_for('profile.user_profile'))
    else:
        return render_template('user_profile/top_up_page.html', user=current_user)

# API endpoint that pays fine
@profile.route('/pay_fine/<uuid:fine_id>', methods=['GET', 'POST'])
def pay_fine(fine_id):
    current_user = user_manager.get_current_user()
    
    if(current_user.pay_fine(fine_id)):
        return redirect(url_for('profile.user_profile'))
    else:
        return redirect(url_for('profile.add_to_balance'))

@profile.route('/add_book', methods=['GET', 'POST'])
def add_book():
    add_book_form = AddBookForm()
    
    # Add the insert book command to the admin user using the command design pattern
    admin_user = user_manager.get_current_user()
    insert_book = AddBook(add_book_form.title.data, add_book_form.author.data, add_book_form.isbn.data)
    
    admin_user.add_admin_command(insert_book)

    if add_book_form.validate_on_submit():
        admin_user.execute_admin_commands()

    return redirect(url_for('profile.admin_profile'))  # Redirect back to the admin profile

@profile.route('/remove_book', methods=['POST'])
def remove_book():
    remove_book_form = RemoveBookForm()

    admin_user = user_manager.get_current_user()
    remove_book = RemoveBook(remove_book_form.isbn.data)
    
    admin_user.add_admin_command(remove_book)

    if remove_book_form.validate_on_submit():
        admin_user.execute_admin_commands()
    
    return redirect(url_for('profile.admin_profile'))

@profile.route('/waive_fine', methods=['GET', 'POST'])
def waive_fine():
    waive_fine_form = WaiveFineForm()
    admin_user = user_manager.get_current_user()
    waive_fine = WaiveFine(waive_fine_form.user.data)
    admin_user.add_admin_command(waive_fine)

    if waive_fine_form.validate_on_submit():
        admin_user.execute_admin_commands()
    
    return redirect(url_for('profile.admin_profile'))

@profile.route('/block_user', methods=['GET', 'POST'])
def block_user():
    block_user_form = BlockUserForm()
    admin_user = user_manager.get_current_user()
    block_user = BlockUser(block_user_form.user.data)
    admin_user.add_admin_command(block_user)

    if block_user_form.validate_on_submit():
        admin_user.execute_admin_commands()

    return redirect(url_for('profile.admin_profile'))

@profile.route('/unblock_user', methods=['GET', 'POST'])
def unblock_user():
    unblock_user_form = UnblockUserForm()
    admin_user = user_manager.get_current_user()
    unblock_user = UnblockUser(unblock_user_form.user.data)
    admin_user.add_admin_command(unblock_user)

    if unblock_user_form.validate_on_submit():
        admin_user.execute_admin_commands()

    return redirect(url_for('profile.admin_profile'))
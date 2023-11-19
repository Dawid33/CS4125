from flask import Blueprint, redirect, render_template, session, url_for, abort
from models.users.user_manager import UserManager
from models.catalogue.book import Book
from forms.book_form import AddBook
from instance.db import db

user_manager = UserManager()

profile = Blueprint('profile', __name__)

# API endpoint that loads the initial user profile page and passes in a user object
@profile.route('/profile', methods=['GET', 'POST'])
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
    current_user = user_manager.get_current_user()
    form = AddBook()  # Create an instance of the form

    if form.validate_on_submit():
        # If the form is submitted and valid, process the form data
        new_book_entry = Book(author=form.author.data, title=form.title.data, isbn=form.isbn.data)
        db.session.add(new_book_entry)
        db.session.commit()
        return redirect(url_for('profile.admin_profile'))  # Redirect back to the admin profile

    # Pass the form to the template
    return render_template('user_profile/admin_profile.html', user=current_user, form=form)

# API endpoint that triggeres return book on the user object
@profile.route('/return_book/<uuid:borrow_id>', methods=['GET'])
def return_book(borrow_id):
    current_user = user_manager.get_current_user()
    current_user.return_book(borrow_id)
    
    return redirect(url_for('profile.user_profile'))

# API endpoint that triggers the top up fuctionality
@profile.route('/top_up', methods=['GET', 'POST'])
def top_up_balance():
    current_user = user_manager.get_current_user()
    return render_template('user_profile/top_up.html', user=current_user)

# API endpoint that pays fine
@profile.route('/pay_fine/<uuid:fine_id>', methods=['GET', 'POST'])
def pay_fine(fine_id):
    current_user = user_manager.get_current_user()
    
    if(current_user.pay_fine(fine_id)):
        return redirect(url_for('profile.user_profile'))
    else:
        return redirect(url_for('profile.top_up_balance'))
    
@profile.route('/add_book', methods=['GET', 'POST'])
def add_book():
     form = AddBook()
     user = user_manager.get_current_user()

     if not user.is_admin:
          abort(403)

     if form.validate_on_submit():
          new_book_entry = Book(author=form.author.data, title=form.title.data, isbn=form.isbn.data)
          db.session.add(new_book_entry)
          db.session.commit()
          return redirect(url_for('admin_profile'))
     return render_template('admin_profile.html', user=user, form=form)
    

# # API endpoint that loads the fines page and passes in a user object
# @profile.route('/fines', methods=['GET', 'POST'])
# def fines():
#     current_user = user_manager.get_current_user()
#     return render_template('user_profile/fines.html', user=current_user)
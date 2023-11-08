from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.database_manager.db_manager import DBManager
from models.users.user_controller import UserController
from flask import g


auth = Blueprint('authentication', __name__)

db_manager = DBManager()
user_controller = UserController()

# API call that communicates with the database to register a user
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user_type=request.form.get('role').upper()
                    
        existing_user = db_manager.get_user_by_username(username)
        
        if existing_user:
            flash('Username is already in use. Please choose a different one.')
        else:
            existing_email = db_manager.get_user_by_email(email)
            if existing_email:
                flash('Email is already registered. Please use a different email.')
            else:
                db_manager.create_user(username, email, password, user_type)
                flash('Registration successful! You can now log in')
                return redirect(url_for('authentication.login'))
            
    return render_template('authentication/register.html')
  
# API call that logs in the user and creates a session
@auth.route('/login', methods=['GET', 'POST'])
def login():
    global current_user  # Access the global current_user variable
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = db_manager.get_user_by_username(username)
        if user:
            if user.password == password:
                session['user_id'] = user.user_id
                # current_user = user_controller.create_user(user.user_id, user.username, user.email, user.password, user.user_type)
                # session['user'] = current_user
                return redirect(url_for('authentication.home'))
            else:
                flash('Login failed. Password is incorrect')
        else:
            flash('Login failed, Username is incorrect')
        
    return render_template('authentication/login.html')

# API call that logs out the user and deletes session
@auth.route('/logout', methods=['GET'])
def logout():     
    if 'user_id' in session:
        del session['user_id']
    else:
        flash('Already logged out')
    return redirect(url_for('authentication.login'))

#API call that loads the home page when a user logs in successfuly
@auth.route('/', methods=['GET', 'POST'])
def home():
    if 'user_id' in session:
        return render_template("home/home.html")  
    else:
        return redirect(url_for('authentication.login'))

    
 
                



        


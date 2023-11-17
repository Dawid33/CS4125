from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.auth_manager.auth_manager import Authentication

auth = Blueprint('authentication', __name__)

# Creates authentication manager objects that deals with user authentication
auth_manager = Authentication()

# API call that communicates with the database to register a user
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user_type=request.form.get('role').upper()
        
        # Function inside auth_manager that authenticates user registration         
        if auth_manager.authenticate_registration(username, email, password, user_type):
            return redirect(url_for('authentication.login'))
            
    return render_template('authentication/register.html')
  
# API call that logs in the user and creates a session
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Function inside auth_manager that authenticates user login          
        if auth_manager.authenticate_login(username, password):
            return redirect(url_for('authentication.home'))
        
    return render_template('authentication/login.html')

# API call that logs out the user and deletes session
@auth.route('/logout', methods=['GET'])
def logout():     
    if 'user' in session:
        del session['user']
    else:
        flash('Already logged out')
    return redirect(url_for('authentication.login'))

# API call that loads the home page when a user logs in successfuly
@auth.route('/', methods=['GET', 'POST'])
def home():
    if 'user' in session:
        return render_template("home/home.html")  
    else:
        return redirect(url_for('authentication.login'))

    
 
                



        


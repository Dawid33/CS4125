from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.db import User
from src.db_query_manager import create_user

auth = Blueprint('authentication', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user_type_id=request.form.get('role')
        
        if(request.form.get('Student')):
            user_type_id = 0
        else:
            user_type_id = 1
            
        existing_user = User.query.filter_by(username=username).first()
        
        if existing_user:
            flash('Username is already in use. Please choose a different one.')
        else:
            existing_email = User.query.filter_by(email=email).first()
            if existing_email:
                flash('Email is already registered. Please use a different email.')
            else:
                create_user(username, email, password, user_type_id)
                flash('Registration successful! You can now log in.')
                return redirect(url_for('authentication.login'))
            
    return render_template('authentication/register.html')
    
@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                session['user_id'] = user.user_id
                return redirect(url_for("home_page.load"))
            else:
                flash('Login failed. Password is incorrect')
        else:
            flash('Login failed, Username is incorrect')
        
    return render_template('authentication/login.html')
                
                



        


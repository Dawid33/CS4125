from flask_sqlalchemy import SQLAlchemy
from src.db import *

db = SQLAlchemy()

# Function to create a new user type "student"
def create_student_user_type():
    student_type = UserType(user_type_id=0, type_name='student')
    db.session.add(student_type)
    db.session.commit()
    
# Function to create a new user type "student"
def create_faculty_user_type():
    faculty_type = UserType(user_type_id=1, type_name='faculty')
    db.session.add(faculty_type)
    db.session.commit()
    
# Function to add a user with the "student" user type
def create_student_user(username, email, password):
    # Retrieve the user type "student"
    student_user_type = UserType.query.filter_by(type_name='student').first()

    # Check if the user type "student" exists
    if student_user_type is None:
        # If it doesn't exist, create the "student" user type
        create_student_user_type()
        student_user_type = UserType.query.filter_by(type_name='student').first()
        
    student_id = str(uuid.uuid1())

    # Create a new user with the "student" user type
    student_user = User(user_id=student_id, username=username, email=email, password=password, is_admin=0, user_type_id=student_user_type.user_type_id, is_blocked=0)
    
    db.session.add(student_user)
    db.session.commit()
    
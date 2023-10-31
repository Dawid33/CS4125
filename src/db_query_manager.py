from flask_sqlalchemy import SQLAlchemy
from src.db import *
from src.db import db
import uuid

# Function to add a user with the "student" user type
def create_user(username, email, password, user_type):
    student_id = str(uuid.uuid1())

    # Create a new user with the "student" user type
    student_user = User(user_id=student_id, username=username, email=email, password=password, is_admin=0, user_type_id=user_type, is_blocked=0)
    
    db.session.add(student_user)
    db.session.commit()
    
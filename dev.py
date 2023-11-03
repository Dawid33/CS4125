from flask import Flask
from models.db import db
from src.authentication import auth
from src.user_profile import profile

app = Flask(__name__, static_url_path='/static')

app.secret_key = 'cs4125'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cs4125_database.db'

db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(profile)

with app.app_context():
    db.create_all()
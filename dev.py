from flask import Flask, render_template
from models.db import db
from src.authentication import auth
from src.user_profile import profile
from src.search import search
from src.book import book

app = Flask(__name__, static_url_path='/static')

app.secret_key = 'cs4125'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cs4125_database.db'

db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(profile)
app.register_blueprint(search)
app.register_blueprint(book)

@app.route("/")
def health_check():
    return render_template("home/home.html")

with app.app_context():
    db.create_all()

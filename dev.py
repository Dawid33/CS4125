from flask import Flask, render_template
from instance.db import db
from src.authentication import auth
from src.user_profile import profile
from src.search import search
from src.book import book
from src.notification import notify, EmailNotification
from models.users.user import json
from flask_json import FlaskJSON

app = Flask(__name__, static_url_path='/static')
json.init_app(app)


app.secret_key = 'cs4125'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cs4125_database.db'

db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(profile)
app.register_blueprint(search)
app.register_blueprint(book)
app.register_blueprint(notify)

# @app.route("/")
# def health_check():
#     return render_template("home/home.html")

@app.route('/test_email', methods=['GET'])
def test_email():
    notification = EmailNotification("My Message")
    return notification.send("dawidsobczak@fastmail.com")

with app.app_context():
    db.create_all()

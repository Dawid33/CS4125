from flask import Flask, render_template
from src.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cs4125_database.db'
db.init_app(app)

with app.app_context():
    db.create_all()
    
@app.route("/")
def login():
    return render_template("authentication/login.html")

@app.route("/register")
def register():
    return render_template("authentication/register.html")
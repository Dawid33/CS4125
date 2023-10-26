from flask import Flask, render_template
from src import authentication

app = Flask(__name__)
app.register_blueprint(authentication.bp)

@app.route("/")
def index():
    return render_template("authentication/login.html")


@app.route("/register")
def register():
    return render_template("authentication/register.html")


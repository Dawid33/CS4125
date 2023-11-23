# pylint: disable=too-few-public-methods
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from flask import Flask, render_template
import multiprocessing
from instance.db import db
from src.authentication import auth
from src.user_profile import profile
from src.search import search
from src.book import book
import gunicorn.app.base
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(profile)
app.register_blueprint(search)
app.register_blueprint(book)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

app.secret_key = 'cs4125'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cs4125_database.db'

@app.route("/health_check")
def health_check():
    return "FANTASTIC"

@app.route("/")
def index():
    return render_template("home/home.html")


class StandaloneApplication(gunicorn.app.base.BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == '__main__':
    with app.app_context():
        db.init_app(app)
        db.create_all()
    options = {
        'bind': '%s:%s' % ('0.0.0.0', '8080'),
        'workers': (multiprocessing.cpu_count() * 2) + 1,
    }
    StandaloneApplication(app, options).run()

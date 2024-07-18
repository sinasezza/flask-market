from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from configuration import DevelopmentConfig, config_class


def init_db(app: Flask):
    db.init_app(app)
    with app.app_context():
        db.create_all()


app = Flask(
    __name__,
    static_url_path="/static",
    static_folder="staticfiles",
    template_folder="templates",
)

db = SQLAlchemy()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Load default config and override config from an environment variable
app.config.from_object(DevelopmentConfig)
if config_class is not None:
    app.config.from_object(config_class)

with app.app_context():
    # Initialize the database
    init_db(app)
    
    # Import views
    from . import views

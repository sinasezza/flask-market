from flask import Flask

from configuration import DevelopmentConfig

from .models import init_db  # Import db and init_db


def create_app(config_class=None) -> Flask:
    app = Flask(
        __name__,
        static_url_path="/static",
        static_folder="staticfiles",
        template_folder="templates",
    )

    # Load default config and override config from an environment variable
    app.config.from_object(DevelopmentConfig)
    if config_class is not None:
        app.config.from_object(config_class)

    with app.app_context():
        # Initialize the database
        init_db(app)

        # Import views
        from . import views

    return app

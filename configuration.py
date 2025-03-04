import os
import pathlib

from dotenv import load_dotenv

# Define base directory
BASEDIR = pathlib.Path(__file__).resolve().parent

load_dotenv(BASEDIR / ".env")


class Config(object):
    """Base config."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")
    DEBUG = os.environ.get("DEBUG", False)
    TESTING = False
    DB_SERVER = "localhost"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI", "sqlite:///./database.db"
    )


class ProductionConfig(Config):
    """Uses production database server."""

    DB_SERVER = os.getenv("DB_SERVER_PRODUCTION", None)


class DevelopmentConfig(Config):
    DB_SERVER = os.getenv("DB_SERVER_DEVELOPMENT", "localhost")
    DEBUG = True


class TestingConfig(Config):
    DB_SERVER = os.getenv("DB_SERVER_DEVELOPMENT", "localhost")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_TEST_DATABASE_URI", "sqlite:///./test_database.db"
    )
    DEBUG = True
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}


port = int(os.environ.get("PORT", 5000))

config_name = os.environ.get("FLASK_CONFIGURATION", "default")
config_class = config[config_name]

import os
import pathlib
from dotenv import load_dotenv


# Define base directory
BASEDIR = pathlib.Path(__file__).resolve().parent

load_dotenv(BASEDIR / ".env")


class Config(object):
    """Base config."""

    DEBUG = os.environ.get('DEBUG', False)
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
    DEBUG = True
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}

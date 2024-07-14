import os
import pathlib

from dotenv import load_dotenv

from app import create_app
from configuration import BASEDIR, config

# Load environment variables from .env file
load_dotenv(BASEDIR / ".env")

config_name = os.environ.get("FLASK_CONFIGURATION", "development")
config_class = config[config_name]

# Create Flask app instance with the selected configuration
app = create_app(config_class=config_class)

port = int(os.environ.get("PORT", 5000))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)

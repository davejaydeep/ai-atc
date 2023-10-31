"""Factory Module to create standard flask rest app"""
from flask import Flask
from flask_cors import CORS
from application.api import status, atc


def create_app():
    """Function to Create App"""
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.register_blueprint(status, url_prefix=status.url_prefix)
    app.register_blueprint(atc, url_prefix=atc.url_prefix)

    return app

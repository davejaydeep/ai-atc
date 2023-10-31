"""Factory Module to create standard flask rest app"""
import os
import pinecone
from flask import Flask
from flask_cors import CORS
from application.api import status, train, question, chat


def create_app():
    """Function to Create App"""
    app = Flask(__name__)
    # TODO: make it configurable with '.env'
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.register_blueprint(status, url_prefix=status.url_prefix)
    app.register_blueprint(train, url_prefix=train.url_prefix)
    app.register_blueprint(question, url_prefix=question.url_prefix)
    app.register_blueprint(chat, url_prefix=chat.url_prefix)

    # Initialize Pinecone
    pinecone.init(api_key=os.environ.get("PINECONE_API_KEY"),
                  environment=os.environ.get("PINECONE_ENVIRONMENT"))
    return app
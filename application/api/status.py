"""
Status API
"""
import json
from flask import Blueprint, Response
from application.constants import APPLICATION_JSON

status = Blueprint('status', __name__)
status.url_prefix = '/status'


@status.route('/')
def index():
    """
    Status API endpoint
    """
    return Response(json.dumps("OK"), mimetype=APPLICATION_JSON)

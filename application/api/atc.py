"""
ATC API
"""
import json
from flask import Blueprint, Response
from application.constants import APPLICATION_JSON

atc = Blueprint('atc', __name__)
atc.url_prefix = '/atc'


@atc.route('/')
def index():
    """
    ATC API endpoint
    """
    return Response(json.dumps("OK"), mimetype=APPLICATION_JSON)

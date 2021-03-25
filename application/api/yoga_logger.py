from flask import Blueprint
from .. import json, as_json, JsonError

yoga_logger_api = Blueprint("yoga_logger_api", __name__)

@as_json
@yoga_logger_api.route('/', methods=['GET'])
def submit_report():
    words = {}
    words['moga'] = 'my yoga logger'
    return words
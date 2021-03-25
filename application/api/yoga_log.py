from flask import Blueprint, jsonify, request
from .. import json, as_json, JsonError
from ..model.YogaSessionModel import YogaSessionModel, db
from flask import current_app
import requests

yoga_log_api = Blueprint("yoga_log_api", __name__)

@as_json
@yoga_log_api.route('/', methods=['GET'])
def submit_report():
    words = {}
    words['moga'] = 'my yoga logger'
    return words

@as_json
@yoga_log_api.route('/yoga_session', methods=['POST'])
def log_yoga_session():
    
    data = request.json
    yoga_session = YogaSessionModel()
    yoga_session.name = data['name']
    yoga_session.instructor = data['instructor']
    yoga_session.date = data['date']
    yoga_session.session_length = data['session_length']
    yoga_session.save()

    return dict(status=200)
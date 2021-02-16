from flask import Blueprint
from .. import json, as_json, JsonError

report_submission_api = Blueprint("report_submission_api", __name__)

@as_json
@report_submission_api.route('/', methods=['GET'])
def submit_report():
    words = {}
    words['greeting'] = 'hello world'
    return words
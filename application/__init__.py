from flask import Flask
from flask_json import FlaskJSON, JsonError, json_response, as_json

json = FlaskJSON()

def create_app():
    
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        api_prefix = "/gateway_service/api/v1.0/"
        from .api import report_submission
        app.register_blueprint(report_submission.report_submission_api, url_prefix=f'{api_prefix}/report_submission')
        return app
from flask import Flask
from flask_json import FlaskJSON, JsonError, json_response, as_json

json = FlaskJSON()

def create_app():
    
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        api_prefix = "/yoga_logger/api/v1.0/"
        from .api import yoga_logger
        app.register_blueprint(yoga_logger.yoga_logger_api, url_prefix=f'{api_prefix}/log_yoga')
        return app
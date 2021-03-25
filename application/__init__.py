from flask import Flask
from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask_mongoengine import MongoEngine


db = MongoEngine()
json = FlaskJSON()


def create_app():
    
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)
    json.init_app(app)

    with app.app_context():
        api_prefix = "/yoga_log/api/v1.0/"
        from .api import yoga_log
        app.register_blueprint(yoga_log.yoga_log_api, url_prefix=f'{api_prefix}/yoga_session_management')
        return app
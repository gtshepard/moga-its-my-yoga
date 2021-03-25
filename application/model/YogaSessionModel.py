
from .. import db

class YogaSessionModel(db.Document):
    name = db.StringField()
    instructor = db.StringField()
    date = db.StringField()
    session_length = db.StringField()
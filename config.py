
from os import environ, path
from dotenv import load_dotenv

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')

    db_name = environ.get('DB_NAME_DEV')
    db_host = environ.get('DB_HOST')
    db_username = environ.get('DB_USERNAME')
    db_password = environ.get('DB_PASSWORD')
    db_uri = f"mongodb+srv://{db_username}:{db_password}@{db_host}/{db_name}?retryWrites=true&w=majority"
    MONGODB_HOST = db_uri
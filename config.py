
from os import environ, path
from dotenv import load_dotenv

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
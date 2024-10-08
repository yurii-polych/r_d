import os
from dotenv import load_dotenv


load_dotenv()


class AppConfig:
    DEBUG = os.getenv('DEBUG')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

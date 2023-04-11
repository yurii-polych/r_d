from django.apps import AppConfig
import os
from dotenv import load_dotenv


load_dotenv()


class UserConfig(AppConfig):
    default_auto_field = os.getenv('DEFAULT_AUTO_FIELD')
    name = 'user'

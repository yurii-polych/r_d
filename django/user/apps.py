from django.apps import AppConfig
from dotenv import load_dotenv

load_dotenv()


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

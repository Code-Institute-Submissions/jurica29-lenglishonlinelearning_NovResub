""" System Module """
from django.apps import AppConfig


class BaseappConfig(AppConfig):
    """Base app configuration"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "baseapp"

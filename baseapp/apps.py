from django.apps import AppConfig


class BaseappConfig(AppConfig):
    """Main app configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'baseapp'

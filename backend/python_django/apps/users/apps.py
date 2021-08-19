"""Django app configuration.

for all availabe options refer to
https://docs.djangoproject.com/en/3.2/ref/applications/#application-configuration
"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Representing the users application and its configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users"

"""Apps."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """API App config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.api"

"""Routes for the users app."""

from .views import UserViewSet

urls = [
    (r"users", UserViewSet),
]

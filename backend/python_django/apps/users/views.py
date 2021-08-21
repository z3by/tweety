"""Users views."""

from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """API view set for the User model."""

    queryset = User.objects.exclude(is_staff=True).all()
    serializer_class = UserSerializer
    lookup_field = "username"

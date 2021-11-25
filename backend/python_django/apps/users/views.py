"""Users views."""

from django.contrib.auth import get_user_model
from oauth2_provider.contrib.rest_framework.permissions import TokenHasResourceScope, TokenHasScope
from rest_framework import permissions, viewsets

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """API view set for the User model."""

    permission_classes = [permissions.IsAdminUser | TokenHasResourceScope | TokenHasScope]
    queryset = User.objects.exclude(is_staff=True).all()
    serializer_class = UserSerializer
    lookup_field = "username"
    required_scopes = ["users"]

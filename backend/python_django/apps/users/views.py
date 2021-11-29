from django.contrib.auth import get_user_model
from oauth2_provider.contrib.rest_framework.permissions import TokenHasResourceScope, TokenHasScope
from rest_framework import permissions, viewsets

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser | TokenHasResourceScope | TokenHasScope]
    queryset = User.objects.exclude(is_staff=True).all()
    serializer_class = UserSerializer
    lookup_field = "username"
    required_scopes = ["users"]


class FollowersViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAdminUser | TokenHasResourceScope | TokenHasScope]
    serializer_class = UserSerializer
    lookup_field = "username"
    required_scopes = ["users"]

    def get_user(self):
        return User.objects.get(username=self.kwargs["user_username"])

    def get_queryset(self):
        user = self.get_user()
        return user.followers.all()


class FollowingViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAdminUser | TokenHasResourceScope | TokenHasScope]
    serializer_class = UserSerializer
    lookup_field = "username"
    required_scopes = ["users"]

    def get_user(self):
        return User.objects.get(username=self.kwargs["user_username"])

    def get_queryset(self):
        user = self.get_user()
        return user.following.all()

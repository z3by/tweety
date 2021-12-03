from http import HTTPStatus

from django.contrib.auth import get_user_model
from oauth2_provider.contrib.rest_framework.permissions import TokenHasResourceScope, TokenHasScope
from rest_framework import permissions, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .schema import FollowerSchema, FollowingSchema
from .serializers import UserSerializer

User = get_user_model()

DEFAULT_PERMISSION_CLASSES = [TokenHasResourceScope | TokenHasScope | permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = DEFAULT_PERMISSION_CLASSES
    queryset = User.objects.exclude(is_staff=True).all()
    serializer_class = UserSerializer
    lookup_field = "username"
    required_scopes = ["users"]


class FollowersViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = DEFAULT_PERMISSION_CLASSES
    serializer_class = UserSerializer
    lookup_field = "username"
    required_scopes = ["users"]
    schema = FollowerSchema()

    def get_user(self):
        return User.objects.get(username=self.kwargs["user_username"])

    def get_queryset(self):
        user = self.get_user()
        return user.followers.all()


class FollowingViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = DEFAULT_PERMISSION_CLASSES
    serializer_class = UserSerializer
    lookup_field = "username"
    required_scopes = ["users"]
    schema = FollowingSchema()

    def get_follower(self) -> User:
        user = get_object_or_404(User, username=self.kwargs["user_username"])
        return user

    def get_followed_user(self) -> User:
        user = get_object_or_404(User, username=self.kwargs["username"])
        return user

    def get_queryset(self):
        user = self.get_follower()
        return user.following.all()

    def update(self, request, *args, **kwargs):
        follower = self.get_follower()
        followed_user = self.get_followed_user()
        if follower != request.user:
            return Response({"detail": "Forbidden"}, status=HTTPStatus.FORBIDDEN)
        if follower == followed_user:
            return Response(
                {"detail": "You can not follow yourself, unless you are a shadow 🤷"},
                status=HTTPStatus.FORBIDDEN,
            )
        try:
            follower.following.get(username=followed_user.username)
            return Response(status=HTTPStatus.NOT_MODIFIED)
        except User.DoesNotExist:
            follower.following.add(followed_user)
            return Response(status=HTTPStatus.NO_CONTENT)

    def destroy(self, request, *args, **kwargs):
        follower = self.get_follower()
        followed_user = self.get_followed_user()
        if follower != request.user:
            return Response({"detail": "Forbidden"}, status=HTTPStatus.FORBIDDEN)
        follower.following.remove(followed_user)
        return Response(status=HTTPStatus.NO_CONTENT)

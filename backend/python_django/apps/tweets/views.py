from oauth2_provider.contrib.rest_framework.permissions import TokenHasResourceScope, TokenHasScope
from rest_framework import permissions, viewsets
from .serializers import TweetSerializer
from .models import Tweet


DEFAULT_PERMISSION_CLASSES = [TokenHasResourceScope | TokenHasScope | permissions.IsAuthenticated]


class TweetsViewSet(viewsets.ModelViewSet):
    permission_classes = DEFAULT_PERMISSION_CLASSES
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    required_scopes = ["tweets"]

    def perform_create(self, serializer: TweetSerializer):
        serializer.save(author=self.request.user)


class UserTweetsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = DEFAULT_PERMISSION_CLASSES
    serializer_class = TweetSerializer
    required_scopes = ["tweets"]

    def get_queryset(self):
        author_username = self.kwargs["author_username"]
        return Tweet.objects.filter(author__username=author_username).all()

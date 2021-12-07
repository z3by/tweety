from oauth2_provider.contrib.rest_framework.permissions import TokenHasResourceScope, TokenHasScope
from rest_framework import permissions, viewsets
from .serializers import TweetSerializer
from .models import Tweet


DEFAULT_PERMISSION_CLASSES = [TokenHasResourceScope | TokenHasScope | permissions.IsAuthenticated]


class TweetViewSet(viewsets.ModelViewSet):
    permission_classes = DEFAULT_PERMISSION_CLASSES
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    required_scopes = ["tweets"]

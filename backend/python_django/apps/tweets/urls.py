from rest_framework_nested import routers

from .views import TweetsViewSet, UserTweetsViewSet
from apps.users.urls import USERS_PREFIX, router as users_router

TWEETS_PREFIX = r"tweets"

tweets_router = routers.SimpleRouter()
user_tweets_router = routers.NestedSimpleRouter(users_router, USERS_PREFIX, lookup="author")

tweets_router.register(TWEETS_PREFIX, TweetsViewSet)
user_tweets_router.register(TWEETS_PREFIX, UserTweetsViewSet, basename="user-tweet")

urlpatterns = tweets_router.urls + user_tweets_router.urls

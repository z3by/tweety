from rest_framework_nested import routers

from .views import TweetViewSet

TWEETS_PREFIX = r"tweets"

router = routers.SimpleRouter()
router.register(TWEETS_PREFIX, TweetViewSet)

urlpatterns = router.urls

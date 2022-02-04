from rest_framework_nested import routers

from .views import FollowersViewSet, FollowingViewSet, UserViewSet

USERS_PREFIX = r"users"
FOLLOWERS_PREFIX = r"followers"
FOLLOWING_PREFIX = r"following"

router = routers.SimpleRouter()
router.register(USERS_PREFIX, UserViewSet)

followers_router = routers.NestedSimpleRouter(router, USERS_PREFIX, lookup="followed")
followers_router.register(FOLLOWERS_PREFIX, FollowersViewSet, basename=FOLLOWERS_PREFIX)

following_router = routers.NestedSimpleRouter(router, USERS_PREFIX, lookup="follower")
following_router.register(FOLLOWING_PREFIX, FollowingViewSet, basename=FOLLOWING_PREFIX)

urlpatterns = [*router.urls, *followers_router.urls, *following_router.urls]

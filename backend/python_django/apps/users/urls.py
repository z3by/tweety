from rest_framework_nested import routers

from .views import UserViewSet
from .views import FollowersViewSet
from .views import FollowingViewSet

USERS_PREFIX = r"users"
FOLLOWERS_PREFIX = r"followers"
FOLLOWING_PREFIX = r"following"

router = routers.DefaultRouter()
router.register(USERS_PREFIX, UserViewSet)

followers_router = routers.NestedSimpleRouter(router, USERS_PREFIX, lookup="user")
followers_router.register(FOLLOWERS_PREFIX, FollowersViewSet, basename=FOLLOWERS_PREFIX)

following_router = routers.NestedSimpleRouter(router, USERS_PREFIX, lookup="user")
following_router.register(FOLLOWING_PREFIX, FollowingViewSet, basename=FOLLOWING_PREFIX)

urlpatterns = [*router.urls, *followers_router.urls, *following_router.urls]

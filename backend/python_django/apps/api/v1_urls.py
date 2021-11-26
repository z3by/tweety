from rest_framework import routers

from apps.users.urls import urls as user_urls

router = routers.DefaultRouter()

for prefix, viewset in user_urls:
    router.register(prefix, viewset)

app_name = "api"
urlpatterns = router.get_urls()

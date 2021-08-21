"""The Default API router."""

from rest_framework import routers

from apps.users.urls import urls

router = routers.DefaultRouter()

for prefix, viewset in urls:
    router.register(prefix, viewset)

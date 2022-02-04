from http import HTTPStatus

import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http.response import JsonResponse
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from oauth2_provider.urls import base_urlpatterns, oidc_urlpatterns

from apps.tweets.urls import urlpatterns as tweets_urlpatterns
from apps.users.urls import urlpatterns as users_urlpatterns

admin.site.site_title = _("Tweety Admin Site")

admin.site.site_header = _("Tweety Administration")

admin.site.index_title = _("Tweety Administration")


class Oauth2Urls:
    urlpatterns = base_urlpatterns + oidc_urlpatterns
    app_name = "oauth2_provider"


class ApiVersionOneUrls:
    urlpatterns = users_urlpatterns + tweets_urlpatterns
    app_name = "api_v1"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/", include(ApiVersionOneUrls, namespace="api_v1")),
    path("api/v1/oauth2/", include(Oauth2Urls, namespace="oauth2_provider")),
]

media_patterns: list = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
dev_patterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    *media_patterns,
]


if settings.DEBUG:
    urlpatterns += dev_patterns


def handler404(request, exception=None):
    return JsonResponse({"detail": "Not Found"}, status=HTTPStatus.NOT_FOUND)


def handler500(request, exception=None):
    return JsonResponse(
        {"detail": "Internal Server Error "}, status=HTTPStatus.INTERNAL_SERVER_ERROR
    )

"""Main application urlconf."""

import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from oauth2_provider.urls import base_urlpatterns, oidc_urlpatterns

admin.site.site_title = _("Tweety Admin Site")

admin.site.site_header = _("Tweety Administration")

admin.site.index_title = _("Tweety Administration")


class Oauth2Urls:
    """Oauth2 Url config."""

    urlpatterns = base_urlpatterns + oidc_urlpatterns
    app_name = "oauth2_provider"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.api.v1_urls", namespace="api")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("oauth2/", include(Oauth2Urls, namespace="oauth2_provider")),
]

media_patterns: list = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
dev_patterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    *media_patterns,
]


if settings.DEBUG:
    urlpatterns += dev_patterns

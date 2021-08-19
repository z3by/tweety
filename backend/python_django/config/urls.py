"""Main application urlconf."""

import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _

admin.site.site_title = _("Tweety Admin Site")

admin.site.site_header = _("Tweety Administration")

admin.site.index_title = _("Tweety Administration")

urlpatterns = [
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    media_urlpatterns: list = static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    dev_urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        *media_urlpatterns,
    ]
    urlpatterns += dev_urlpatterns

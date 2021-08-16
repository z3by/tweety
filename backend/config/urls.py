import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _

admin.site.site_title = _("Tweety Admin Site")

admin.site.site_header = _("Tweety Administration")

admin.site.index_title = _("Tweety Administration")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
]

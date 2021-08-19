"""Admin site configuration for users app."""

from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    """Register User model in django admin site."""

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (_("Login info"), {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "full_name",
                    "short_name",
                    "email",
                    "bio",
                    "link",
                    "photo",
                    "cover",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "full_name", "is_superuser"]
    search_fields = ["full_name"]

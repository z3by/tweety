"""Django forms for users app."""

from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    """Subclass the UserChangeForm to update the model attribute."""

    class Meta(admin_forms.UserChangeForm.Meta):
        """Override the UserChangeForm to use the custom user model."""

        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    """Subclass the UserCreationForm to update the model attribute."""

    class Meta(admin_forms.UserCreationForm.Meta):
        """Override the UserCreationForm meta class.

        override the model attribute to use the custom User model,
        and customize the error messages.
        """

        model = User

        error_messages = {"username": {"unique": _("This username has already been taken.")}}

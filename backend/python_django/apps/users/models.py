"""Django user models."""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """A custom user model."""

    first_name = None  # type: ignore
    last_name = None  # type: ignore
    full_name = models.CharField(_("full name"), max_length=200)
    short_name = models.CharField(_("short name"), max_length=50, blank=True, null=True)
    bio = models.TextField(_("Bio"), blank=True, null=True)
    location = models.CharField(
        _("Location"),
        max_length=200,
        null=True,
        blank=True,
    )
    link = models.URLField(_("Link"), max_length=200, null=True, blank=True)
    photo = models.ImageField(
        _("User personal photo"),
        upload_to="img/profile/photos",
        blank=True,
    )
    cover = models.ImageField(
        _("Cover Photo"),
        upload_to="img/profile/covers",
        blank=True,
    )
    birth_date = models.DateField(_("Birth Date"), null=True, blank=True)

    def get_full_name(self) -> str:
        """Get the full name of the user.

        Returns
        -------
        str
            the full name of the user
        """
        return str(self.full_name)

    def get_short_name(self) -> str:
        """Get the short name of the user.

        Returns
        -------
        str
            the short name of the user
        """
        return str(self.short_name)

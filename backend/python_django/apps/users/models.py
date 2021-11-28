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
    following = models.ManyToManyField(
        to="self",
        through="Follow",
        related_name="followers",
        symmetrical=False,
    )

    def get_full_name(self) -> str:
        return str(self.full_name)

    def get_short_name(self) -> str:
        return str(self.short_name)


class Follow(models.Model):
    source = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)
    target = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["source", "target"], name="%(app_label)s_%(class)s_unique_followers"
            ),
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_prevent_self_follow",
                check=~models.Q(source=models.F("target")),
            ),
        ]

        ordering = ["-created"]

    def __str__(self):
        return f"{self.source} follows {self.target}"

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Tweet(models.Model):
    text = models.TextField(_("Full Text"), max_length=280)
    created_date = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_date = models.DateTimeField(_("Modified date"), auto_now=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_("Author"),
        related_name="tweets",
    )
    in_reply_to_status = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("In reply to status"),
    )

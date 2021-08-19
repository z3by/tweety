"""Factories for users.models."""
from typing import Any, Sequence

from django.contrib.auth import get_user_model
from factory import Faker, post_generation
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    """A factory for User model."""

    username = Faker("user_name")
    email = Faker("email")
    full_name = Faker("name")

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        """Set a password.

        Parameters
        ----------
        create : bool
        extracted : Sequence[Any]
        """
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)

    class Meta:
        """Model factory metadata."""

        model = get_user_model()
        django_get_or_create = ["username"]

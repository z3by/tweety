"""Test users models."""

import pytest

from ..models import User


@pytest.mark.django_db
def test_user_get_short_name(user: User):
    """Test gets the short name or an empty string."""
    assert user.get_short_name() == user.short_name


@pytest.mark.django_db
def test_user_get_full_name(user: User):
    """Test gets the full name or an empty string."""
    assert user.get_full_name() == user.full_name

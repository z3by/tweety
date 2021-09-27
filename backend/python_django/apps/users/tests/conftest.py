"""Pytest configuration file."""
import pytest
from rest_framework.test import APIClient

from ..models import User
from .factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    """Use the tmp directory as a MEDIA_ROOT."""
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    """Provide the UserFactory as a fixture."""
    return UserFactory()


@pytest.fixture
def api_client():
    """Provide django rest framework's test client as a fixture."""
    return APIClient()

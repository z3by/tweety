"""Pytest configuration file."""
import pytest
from rest_framework.test import APIClient

from ..models import User
from .factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def api_client(user: User) -> APIClient:
    user.is_superuser = True
    user.is_staff = True
    client = APIClient()
    client.force_authenticate(user=user)
    return client

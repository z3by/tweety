"""Test admin."""

import pytest
from django.test.client import Client
from django.urls import reverse

from ..models import User

pytestmark = pytest.mark.django_db


def test_changelist(admin_client: Client):
    """Test user changelist.

    Parameters
    ----------
    admin_client : Client
        Django test client with admin privleges.
    """
    url = reverse("admin:users_user_changelist")
    response = admin_client.get(url)
    assert response.status_code == 200


def test_search(admin_client: Client):
    """Test search users.

    Parameters
    ----------
    admin_client : Client
        Django test client with admin privleges.
    """
    url = reverse("admin:users_user_changelist")
    response = admin_client.get(url, data={"q": "test"})
    assert response.status_code == 200


def test_add(admin_client: Client):
    """Test add user.

    Parameters
    ----------
    admin_client : Client
        Django test client with admin privleges.
    """
    url = reverse("admin:users_user_add")
    response = admin_client.get(url)
    assert response.status_code == 200
    response = admin_client.post(
        url,
        data={
            "username": "test",
            "password1": "My_R@ndom-P@ssw0rd",
            "password2": "My_R@ndom-P@ssw0rd",
        },
    )
    assert response.status_code == 302
    assert User.objects.filter(username="test").exists()


def test_view_user(admin_client: Client):
    """Test view user.

    Parameters
    ----------
    admin_client : Client
        Django test client with admin privleges.
    """
    user = User.objects.get(username="admin")
    url = reverse("admin:users_user_change", kwargs={"object_id": user.pk})
    response = admin_client.get(url)
    assert response.status_code == 200

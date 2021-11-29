"""Test admin."""

import pytest
from django.test.client import Client
from django.urls import reverse

from ..models import Follow, User
from .factories import UserFactory

pytestmark = pytest.mark.django_db


def test_changelist(admin_client: Client):
    url = reverse("admin:users_user_changelist")
    response = admin_client.get(url)
    assert response.status_code == 200


def test_search(admin_client: Client):
    url = reverse("admin:users_user_changelist")
    response = admin_client.get(url, data={"q": "test"})
    assert response.status_code == 200


def test_add(admin_client: Client):
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
    user = User.objects.get(username="admin")
    url = reverse("admin:users_user_change", kwargs={"object_id": user.pk})
    response = admin_client.get(url)
    assert response.status_code == 200


def test_follow_changelist(admin_client: Client):
    url = reverse("admin:users_follow_changelist")
    response = admin_client.get(url)
    assert response.status_code == 200


def test_follow_add(admin_client: Client):
    url = reverse("admin:users_follow_add")
    first_user = UserFactory.create()
    second_user = UserFactory.create()
    response = admin_client.get(url)
    assert response.status_code == 200
    args = {
        "source": first_user.pk,
        "target": second_user.pk,
    }
    response = admin_client.post(
        url,
        data=args,
    )
    assert response.status_code == 302
    assert Follow.objects.filter(**args).exists()


def test_follow_view(admin_client: Client):
    first_user: User = UserFactory.create()
    second_user: User = UserFactory.create()
    first_user.following.add(second_user)
    follow = Follow.objects.first()
    url = reverse("admin:users_follow_change", kwargs={"object_id": follow.pk})
    response = admin_client.get(url)
    assert response.status_code == 200

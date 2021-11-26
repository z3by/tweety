"""Test users views."""

import pytest
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.test import APIClient

from apps.users.models import User

from .factories import UserFactory


@pytest.mark.django_db
def test_list_users_no_staff(api_client: APIClient):
    """Test that list users doesn't include staff."""
    url = reverse("api:user-list")
    UserFactory.create_batch(3)
    UserFactory.create_batch(2, is_staff=True)

    response: Response = api_client.get(url)
    assert response.status_code == 200
    for user in response.json():
        assert not User.objects.get(username=user["username"]).is_staff

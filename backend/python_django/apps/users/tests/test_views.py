"""Test users views."""

import pytest
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.test import APIClient

from apps.users.models import User

from .factories import UserFactory


@pytest.fixture
def user_with_one_follower():
    first_user: User = UserFactory.create()
    follower: User = UserFactory.create()
    follower.following.add(first_user)
    return first_user, follower


@pytest.mark.django_db
def test_list_users_no_staff(api_client: APIClient):
    """Test that list users doesn't include staff."""
    url = reverse("api_v1:user-list")

    response: Response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.json()) == 1
    UserFactory.create_batch(2, is_staff=True)
    UserFactory.create_batch(2)

    response: Response = api_client.get(url)
    assert len(response.json()) == 3
    for user in response.json():
        assert not User.objects.get(username=user["username"]).is_staff


@pytest.mark.django_db
def test_list_user_followers(api_client: APIClient, user_with_one_follower):
    first_user, follower = user_with_one_follower
    url = reverse("api_v1:followers-list", kwargs=dict(followed_username=first_user.username))
    response: Response = api_client.get(url)
    assert response.status_code == 200
    assert response.json()[0]["username"] == follower.username


@pytest.mark.django_db
def test_retreive_single_user_follower(api_client: APIClient, user_with_one_follower):
    first_user, follower = user_with_one_follower
    url = reverse(
        "api_v1:followers-detail",
        kwargs=dict(followed_username=first_user.username, username=follower.username),
    )
    response: Response = api_client.get(url)
    assert response.status_code == 200
    assert response.json()["username"] == follower.username


@pytest.mark.django_db
def test_list_users_followed_by_a_user(api_client: APIClient, user_with_one_follower):
    first_user, follower = user_with_one_follower
    url = reverse("api_v1:following-list", kwargs=dict(follower_username=follower.username))
    response: Response = api_client.get(url)
    assert response.status_code == 200
    assert response.json()[0]["username"] == first_user.username


@pytest.mark.django_db
def test_user_can_follow_or_unfollow_another_user(user: User, api_client: APIClient):
    second_user: User = UserFactory.create()

    url = reverse(
        "api_v1:following-detail",
        kwargs=dict(follower_username=user.username, username=second_user.username),
    )
    # before following
    response: Response = api_client.get(url)
    assert response.status_code == 404

    # follow
    response: Response = api_client.put(url)
    assert response.status_code == 204
    # after following
    response: Response = api_client.get(url)
    assert response.status_code == 200
    # already following
    response: Response = api_client.put(url)
    assert response.status_code == 304
    # un-follow
    response: Response = api_client.delete(url)
    assert response.status_code == 204
    # after un-following
    response: Response = api_client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_users_can_not_follow_themselves(user: User, api_client: APIClient):
    url = reverse(
        "api_v1:following-detail",
        kwargs=dict(follower_username=user.username, username=user.username),
    )
    response: Response = api_client.put(url)
    assert response.status_code == 403
    assert response.json() == {"detail": "You can not follow yourself, unless you are a shadow 🤷"}


@pytest.mark.django_db
def test_only_authenticated_user_can_follow(user: User, api_client: APIClient):
    second_user: User = UserFactory.create()

    url = reverse(
        "api_v1:following-detail",
        kwargs=dict(follower_username=second_user.username, username=user.username),
    )
    response: Response = api_client.put(url)
    assert response.status_code == 403
    assert response.json() == {"detail": "Forbidden"}

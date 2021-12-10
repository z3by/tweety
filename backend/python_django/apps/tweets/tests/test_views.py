from typing import List

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.test import APIClient

from apps.users.tests.factories import UserFactory

from ..models import Tweet
from .factories import TweetFactory

User = get_user_model()


@pytest.mark.django_db
def test_create_tweet(api_client: APIClient, user: User):
    url = reverse("api_v1:tweet-list")
    data = {"text": "Hello there"}
    res: Response = api_client.post(url, data=data)
    assert res.status_code == 201


@pytest.fixture
def tweets(user: User) -> List[Tweet]:
    first_user_tweets = TweetFactory.create_batch(3, author=user)
    second_user = UserFactory.create()
    second_user_tweets = TweetFactory.create_batch(2, author=second_user)
    tweet_objects = first_user_tweets + second_user_tweets
    return tweet_objects


@pytest.mark.django_db
def test_list_tweets(api_client: APIClient, tweets: List[Tweet]):
    url = reverse("api_v1:tweet-list")
    res: Response = api_client.get(url)
    assert res.status_code == 200
    tweets_json = res.json()
    assert len(tweets_json) == len(tweets)
    for tweet_obj, tweet_res in zip(tweets, tweets_json):
        assert tweet_obj.text in tweet_res["text"]


@pytest.mark.django_db
def test_update_tweet(api_client: APIClient, user: User):
    tweet = TweetFactory(author=user)
    old_text = tweet.text
    url = reverse("api_v1:tweet-detail", kwargs={"pk": tweet.pk})
    new_text = "Updated tweet"
    res: Response = api_client.put(url, {"text": new_text})
    assert res.status_code == 200
    assert new_text != old_text
    assert tweet.text == old_text


@pytest.mark.django_db
def test_retreive_single_tweet(api_client: APIClient, tweets: List[Tweet]):
    url = reverse("api_v1:tweet-detail", kwargs={"pk": tweets[0].pk})
    res: Response = api_client.get(url)
    assert res.status_code == 200
    tweet_json = res.json()
    assert tweet_json["text"] == tweets[0].text
    assert tweets[0].author.username in tweet_json["author"]


@pytest.mark.django_db
def test_delete_tweet(api_client: APIClient, tweets: List[Tweet]):
    url = reverse("api_v1:tweet-detail", kwargs={"pk": tweets[0].pk})
    res: Response = api_client.delete(url)
    assert res.status_code == 204


@pytest.mark.django_db
def test_list_user_tweets(api_client: APIClient, tweets: List[Tweet], user: User):
    url = reverse("api_v1:user-tweet-list", kwargs={"author_username": user.username})
    res: Response = api_client.get(url)
    assert res.status_code == 200
    tweets_json = res.json()
    assert len(tweets_json) == 3
    for tweet_obj, tweet_res in zip(tweets, tweets_json):
        assert tweet_obj.text in tweet_res["text"]
        assert tweet_obj.author.username == user.username


@pytest.mark.django_db
def test_retreive_single_user_tweet(api_client: APIClient, tweets: List[Tweet], user: User):
    user_tweet = user.tweets.first()
    url = reverse(
        "api_v1:user-tweet-detail", kwargs={"author_username": user.username, "pk": user_tweet.pk}
    )
    res: Response = api_client.get(url)
    assert res.status_code == 200
    tweet_json = res.json()
    assert tweet_json["text"] == user_tweet.text
    assert user.username in tweet_json["author"]

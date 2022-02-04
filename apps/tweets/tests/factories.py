from factory import Faker
from factory.django import DjangoModelFactory

from ..models import Tweet


class TweetFactory(DjangoModelFactory):
    text = Faker("paragraph")

    class Meta:
        model = Tweet

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Tweet

User = get_user_model()


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = "__all__"
        extra_kwargs = {
            "author": {
                "view_name": "api_v1:user-detail",
                "read_only": True,
                "lookup_field": "username",
            }
        }

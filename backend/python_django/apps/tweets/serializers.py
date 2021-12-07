from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Tweet


User = get_user_model()


class TweetSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        "api_v1:user-detail", queryset=User.objects, lookup_field="username"
    )
    in_reply_to_status = serializers.HyperlinkedRelatedField(
        "api_v1:tweet-detail", queryset=Tweet.objects, lookup_field="pk"
    )

    class Meta:
        model = Tweet
        fields = [
            "id",
            "text",
            "created_date",
            "modified_date",
            "author",
            "in_reply_to_status",
        ]

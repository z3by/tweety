from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    following = serializers.HyperlinkedIdentityField(
        view_name="following-list", lookup_url_kwarg="follower_username", lookup_field="username"
    )
    followers = serializers.HyperlinkedIdentityField(
        view_name="followers-list", lookup_url_kwarg="followed_username", lookup_field="username"
    )
    tweets = serializers.HyperlinkedIdentityField(
        view_name="tweets-list",
        lookup_url_kwarg="author_username",
        lookup_field="username",
        read_only=True,
    )

    class Meta:
        model = User
        fields = [
            "url",
            "username",
            "full_name",
            "short_name",
            "email",
            "bio",
            "location",
            "link",
            "photo",
            "cover",
            "birth_date",
            "date_joined",
            "following",
            "followers",
            "tweets",
        ]
        extra_kwargs = {
            "url": {"view_name": "user-detail", "lookup_field": "username"},
            "date_joined": {"read_only": True},
        }

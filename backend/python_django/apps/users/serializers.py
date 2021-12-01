from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    following_url = serializers.HyperlinkedIdentityField(
        view_name="following-list", lookup_url_kwarg="user_username", lookup_field="username"
    )
    followers_url = serializers.HyperlinkedIdentityField(
        view_name="followers-list", lookup_url_kwarg="user_username", lookup_field="username"
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
            "following_url",
            "followers_url",
        ]
        extra_kwargs = {
            "url": {"view_name": "user-detail", "lookup_field": "username"},
        }

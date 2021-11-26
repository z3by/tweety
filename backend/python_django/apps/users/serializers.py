from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
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
        ]
        extra_kwargs = {
            "url": {"view_name": "user-detail", "lookup_field": "username"},
        }

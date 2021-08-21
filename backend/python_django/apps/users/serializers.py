"""Django Rest Framework Serializers module."""

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """A model serializer for the User Model."""

    class Meta:
        """Override the config of the serializer.

        https://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer
        """

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
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
        ]
        extra_kwargs = {
            "url": {"view_name": "user-detail", "lookup_field": "username"},
        }

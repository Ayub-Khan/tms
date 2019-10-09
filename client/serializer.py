"""Serializers for models."""

from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    """Client model serializer class."""

    class Meta:
        """Specified model for ModelSerializer."""

        model = Client
        fields = [
            'id',
            'name',
            'age',
            'gender',
            'address',
            'phone_number',
            'email'
        ]

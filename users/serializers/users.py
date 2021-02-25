"""users serializers"""

# Django
from django.contrib.auth import authenticate

# Django REST Framework
from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    """User login serializer"""

    email = serializers.EmailField()
    password = serializers.CharField(
        min_length=8,
        max_length=64
    )

    def validate(self, data):
        """check credentials"""

        user = authenticate(username=data['email'], password=data['password'])

        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        return data

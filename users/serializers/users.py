"""users serializers"""

# Django
from django.contrib.auth import authenticate

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token


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
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrive new token"""

        token, created = Token.objects

        return self.context['user'], token.key
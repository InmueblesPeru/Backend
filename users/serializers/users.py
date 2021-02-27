"""Profile serializers"""

# Django
from django.contrib.auth import authenticate

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Models
from users.models.users import Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer"""
    class Meta:
        """Meta class"""

        model = Profile
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number'
        )




class ProfileLoginSerializer(serializers.Serializer):
    """Profile login serializer"""

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
        """generate or retrive a new token"""

        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
